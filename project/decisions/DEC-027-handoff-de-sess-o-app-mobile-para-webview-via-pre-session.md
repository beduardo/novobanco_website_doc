---
id: "DEC-027"
title: "Handoff de Sessão App Mobile para WebView via Pre-Session"
status: "accepted"
created: 2026-04-20
context: "DEF-13"
affects-definitions:
  - "DEF-13"
  - "DEF-17"
affects-sections:
  - "SEC-07"
  - "SEC-16"
---

# DEC-027: Handoff de Sessão App Mobile para WebView via Pre-Session

## Context

A App Mobile nativa precisa de navegar para páginas do HomeBanking Web dentro de uma WebView. Existem dois tipos de destino:

1. **Páginas públicas** — não requerem sessão autenticada; basta redirecionar a WebView para a URL.
2. **Páginas autenticadas** — requerem que o utilizador já tenha uma sessão web válida. A App Mobile já tem o utilizador autenticado, mas essa sessão (app token) não é diretamente utilizável pelo canal web — o canal web usa o seu próprio modelo de sessão gerido pelo BFF.

O mecanismo de QR Code não é adequado para este cenário porque pressupõe uma sessão web pendente iniciada pelo browser; aqui não existe sessão prévia, e o contexto de autenticação já existe na App.

## Decision

A navegação da App Mobile para páginas autenticadas do HomeBanking Web utiliza um mecanismo de **pre-session**: a App cria uma sessão web antecipadamente, antes de abrir a WebView.

**Fluxo:**

1. A App Mobile envia o contexto de autenticação do utilizador atual (`appAccessToken`) a um endpoint dedicado no MicroService, via API Gateway IBM (seguindo o mesmo padrão de DEC-019 — sem BFF).
2. O MicroService valida o token e cria uma **nova sessão web** (independente de qualquer sessão de QR Code), devolvendo um `sessionHandoffId` (GUID).
3. A App Mobile abre a WebView e inclui o `sessionHandoffId` no header HTTP **`x-nb-session-handoff`** no pedido inicial.
4. O BFF lê o header `x-nb-session-handoff`, consulta o MicroService para trocar o `sessionHandoffId` por uma sessão web real, e emite o cookie `token_sessao_spa` normalmente.
5. A partir deste ponto, a WebView opera como qualquer sessão web autenticada.

**Para páginas públicas:** a App Mobile abre a WebView directamente para a URL, sem qualquer header ou pre-session.

**Endpoint de pre-session:**
- `POST /auth/webview-session` — acessível pela App Mobile via API Gateway IBM (channel: `best.app`)
- Devolve: `{ sessionHandoffId: "<guid>", expiresIn: 60 }` (TTL curto — o handoff é one-time-use)

**Header de handoff:**
- Nome: `x-nb-session-handoff`
- Valor: o GUID devolvido pelo endpoint de pre-session
- Enviado apenas no pedido inicial da WebView; após a troca pelo BFF, é descartado

## Consequences

- O MicroService expõe um novo endpoint `/auth/webview-session` acessível pela App Mobile.
- O BFF passa a verificar o header `x-nb-session-handoff` em todos os pedidos recebidos; se presente, troca-o por uma sessão web real antes de processar o pedido.
- O `sessionHandoffId` é **one-time-use** e tem TTL curto (60 segundos) para minimizar o risco de reutilização.
- Este mecanismo é distinto do fluxo de QR Code: não existe estado PENDING/AUTHORIZED em Redis — a sessão é criada directamente pelo MicroService a pedido da App Mobile autenticada.
- O canal web (BFF) não participa na criação da pre-session — apenas na troca final.
- Impacto em SEC-07 (novo fluxo de autenticação) e SEC-16 (navegação App Mobile → WebView).
