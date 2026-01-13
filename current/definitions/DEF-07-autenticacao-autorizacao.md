---
id: DEF-07-autenticacao-autorizacao
aliases:
  - Autenticacao e Autorizacao
tags:
  - nextreality-novobanco-website-definitions
  - definitions
  - authentication
  - authorization
  - security
approved: true
created: 2026-01-03
hubs:
  - "[[nextreality]]"
para-code: R
reviewed: true
status: completed
---

# DEF-07: Autenticacao & Autorizacao

> **Secao relacionada:** [7 - Autenticacao & Autorizacao](../sections/SEC-07-autenticacao-autorizacao.md)

## Contexto

Definir a estrategia de autenticacao e autorizacao do HomeBanking Web. Nota: O fluxo basico OAuth ja foi definido em DEF-05-arquitetura-bff.md. Este documento aprofunda os detalhes de sessao, MFA, e politicas de seguranca.

## Perguntas a Responder

### Autenticacao - Fluxos
1. Quais metodos de autenticacao serao suportados?
   - Username/Password? Somente no fluxo de fallback
   - Biometria (WebAuthn/FIDO2)? Requerido pelos fluxos de validação do QR Code de sessão pelo app
   - Certificado digital? Não

2. O login sera unificado com a app mobile (mesmas credenciais)?
    Sim

3. Ha fluxo de primeiro acesso/registo especifico para web?
    Necessita aprofundamento

### MFA/SCA (Strong Customer Authentication)
4. Qual o segundo fator obrigatorio (App push, SMS OTP, TOTP)?
    Nos fluxos de leitura do QR Code, o app deverá requerer a biometria antes de aprovar e vincular a sessão ao utilizador logado na app. E no fluxo de fallback há a possibilidade de se utilizar SMS OTP e App push. A definição de quais dos quatro fluxos realmente serão utilizados ainda necessita de validação.

5. Ha cenarios onde SCA pode ser dispensado (PSD2 exemptions)?
    Até o momento não há cenários públicos. Todos os cenários de acesso à páginas restritas necessita de SCA.

6. Como sera tratado o fallback se o metodo primario falhar?
    Apos a tentativa de leitura do QR Code e informação de falha pelo utilizador, a aplicação deverá permitir o login com a opção via SMS OTP ou App push. Isso dependerá das opções habilitadas para o utilizador.


### Gestao de Sessoes
7. Qual o tempo de vida da sessao (timeout por inatividade)?
    10 minutos

8. Qual o tempo maximo absoluto de sessao?
    30 minutos

9. A sessao e exclusiva (logout de outras sessoes ao fazer login)?
    Desejavel, necessita aprovacao pelo cliente

10. Como sera comunicado ao utilizador que a sessao vai expirar?
    Popup na aplicacao com temporizador

### Sessao Multi-Canal (NOVO)

11. Como a sessao web se relaciona com a sessao mobile (mesmo utilizador)?
    Necessita aprofundamento. Considerar: sessoes independentes ou sincronizadas

12. Ha limite de sessoes ativas por utilizador?
    Necessita aprofundamento. Sugestao: 1 sessao web + 1 sessao mobile

### Estrategia de Tokens
13. Qual o tempo de vida do access token?
    15 minutos

14. Qual o tempo de vida do refresh token?
    7 dias

15. Onde serao armazenados os tokens?
    Backend tokens (Access/Refresh): BFF cache
    Session tokens: Cookie HttpOnly Secure

16. Como sera tratada a renovacao de tokens?
    Refresh silencioso conforme atividade do utilizador

### Autorizacao
17. Qual o modelo de autorizacao (RBAC, ABAC)?
    ABAC hibrido com RBAC. Roles como atributo do sujeito.

18. Ha permissoes especificas por tipo de operacao?
    Sim (consulta vs transacao)

### Politicas de Password
19. Quais os requisitos minimos de password?
    Seguira requisitos preexistentes da App. Necessita aprofundamento

20. Ha bloqueio apos tentativas falhadas?
    Necessita aprofundamento

### Anti-automation e Revogacao (Simplificado)
21. Sera implementado CAPTCHA ou rate limiting em login?
    Necessita aprofundamento. Rate limiting no Gateway.

22. Ha mecanismo de logout de todos os dispositivos?
    Necessita aprofundamento. Essencial para seguranca.

## Decisoes

### Metodos de Autenticacao
- **Decisao:** _A preencher_
- **Justificacao:**
- **Alternativas consideradas:**

### MFA/SCA
- **Decisao:** _A preencher_
- **Justificacao:**
- **Alternativas consideradas:**

### Gestao de Sessoes
- **Decisao:** _A preencher_
- **Justificacao:**
- **Alternativas consideradas:**

### Tokens
- **Decisao:** _A preencher_
- **Justificacao:**
- **Alternativas consideradas:**

### Autorizacao
- **Decisao:** _A preencher_
- **Justificacao:**
- **Alternativas consideradas:**

### Anti-automation
- **Decisao:** _A preencher_
- **Justificacao:**
- **Alternativas consideradas:**

## Restricoes Conhecidas

- SCA obrigatorio conforme PSD2
- Integracao com servico de autenticacao existente do banco
- Cookies HttpOnly para sessao (definido em DEF-05)
- OAuth 2.0 como base (definido em DEF-05)

## Decisoes Relacionadas

- [DEC-001-estrategia-autenticacao-web.md](../decisions/DEC-001-estrategia-autenticacao-web.md) - Estrategia de autenticacao
- [DEC-002-gestao-sessoes-tokens.md](../decisions/DEC-002-gestao-sessoes-tokens.md) - Gestao de sessoes e tokens
- [DEC-003-modelo-autorizacao-abac.md](../decisions/DEC-003-modelo-autorizacao-abac.md) - Modelo de autorizacao ABAC

## Referencias

- [DEF-05-arquitetura-bff.md](DEF-05-arquitetura-bff.md) - Fluxo OAuth basico
- [DEF-08-seguranca-conformidade.md](DEF-08-seguranca-conformidade.md) - PSD2
- PSD2 - Payment Services Directive 2
- OWASP Authentication Cheat Sheet
