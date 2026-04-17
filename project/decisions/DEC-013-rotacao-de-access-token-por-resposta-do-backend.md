---
id: "DEC-013"
title: "Access Token Siebel - Sem Rotacao, Header OAuth Dinamico"
status: "accepted"
created: 2026-04-10
updated: 2026-04-17
context: "DEF-13"
affects-definitions:
  - "DEF-13"
affects-sections:
  - "SEC-07"
---

# DEC-013: Access Token Siebel - Sem Rotacao, Header OAuth Dinamico

> **Related definitions:** [DEF-13-autenticacao-oauth.md](../definitions/DEF-13-autenticacao-oauth.md)
> **Related sections:** [SEC-07 - Autenticacao & Autorizacao](../sections/SEC-07-autenticacao-autorizacao.md)
> **Amends:** [DEC-002 - Gestao de Sessoes e Tokens](./DEC-002-gestao-sessoes-tokens.md)

## Context

O `access_token` devolvido pelo Siebel apos autenticacao **nao expira e nunca e rotacionado**. O BFF armazena-o em cache (Redis) e reutiliza-o durante toda a duracao da sessao web.

O que varia em cada chamada ao Siebel e o **conteudo do header Authorization OAuth**, que inclui campos gerados dinamicamente:

- `oauth_timestamp` — unix time no momento da chamada
- `oauth_guid` — GUID unico gerado a cada pedido
- `oauth_signature` — calculada com HMAC-SHA256 sobre todos os campos (incluindo timestamp e GUID), pelo que o seu valor muda em cada interaccao

O `access_token` em si e um dos inputs da assinatura, mas o seu valor permanece constante.

Os TTLs documentados (15 min para Access Token em cache, 30 min para sessao) referem-se exclusivamente a camada **Frontend-BFF** e gerem o ciclo de vida da sessao web — nao ao token do Siebel.

## Decision

O BFF **nao implementa qualquer logica de renovacao ou rotacao do Access Token do Siebel**. Em vez disso:

- O `access_token` e armazenado em cache (Redis) apos o login e reutilizado sem alteracao
- A cada chamada ao Siebel, o BFF gera um novo header Authorization com GUID e timestamp frescos e recalcula a assinatura OAuth
- Nao existe mecanismo de refresh, renovacao proativa, nem expiracao do token Siebel
- A sessao web (e a sua expiracao) e gerida exclusivamente pela camada BFF-Frontend via cookie `token_sessao_spa`

## Consequences

### Positive
- Simplicidade: sem logica de renovacao nem gestao de expiracao do token Siebel no BFF
- Sem necessidade de Refresh Token
- Sem race conditions de renovacao concorrente

### Negative
- O header Authorization deve ser calculado dinamicamente a cada chamada (nao pode ser cacheado)

## Notes

- Esta decisao corrige uma interpretacao anterior que assumia rotacao do access_token a cada resposta do backend — essa interpretacao estava incorrecta
- Os TTLs (15 min / 30 min) sao salvaguardas para a sessao web (BFF-Frontend) e nao tem relacao com o token do Siebel
- O `sasToken` retornado pelo Siebel nao e utilizado no canal web (especifico para app mobile)
