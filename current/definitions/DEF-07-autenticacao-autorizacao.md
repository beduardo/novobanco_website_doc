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
    Desejável, mas ainda necessita aprovação pelo cliente.

10. Como sera comunicado ao utilizador que a sessao vai expirar?
    Popup na aplicação com temporizador.

### Estrategia de Tokens
11. Qual o tempo de vida do access token?
    15 min

12. Qual o tempo de vida do refresh token?
    7 dias

13. Onde serao armazenados os tokens (BFF cache, cookies)?
    Tokens do Backend (Access/Refresh) utilizados entre o BFF e o Backend serão armazenados no BFF cache. Tokens de Sessão (Access/Refresh) utilizados entre o browser e o BFF em cookie.

14. Como sera tratada a renovacao de tokens (refresh silencioso)?
    Refresh silencioso conforme atividade

### Autorizacao
15. Qual o modelo de autorizacao (RBAC, ABAC)?
    Modelo de autorização baseado em ABAC híbrido com RBAC, onde role é utilizado apenas como mais um atributo do sujeito quando necessário, e as decisões de acesso são definidas por políticas construídas sobre o conjunto de atributos da operação (sujeito, recurso, ação e ambiente).

16. Quais roles/perfis serao definidos?
    Será especificado no assessment inicial na execução do projeto. O documento atual não aprofundará estes detalhes.

17. Ha permissoes especificas por tipo de operacao (consulta vs transacao)?
    Sim

### Politicas de Password
18. Quais os requisitos minimos de password (comprimento, complexidade)?
    Seguirá os requisitos preexistentes da App. Necessita aprofundamento

19. Ha politica de expiracao de password?
    Necessita aprofundamento

20. Como sera tratado o fluxo de recuperacao de password?
    Necessita aprofundamento

21. Ha bloqueio apos tentativas falhadas? Quantas?
    Necessita aprofundamento

### Anti-automation
22. Sera implementado CAPTCHA? Em quais fluxos?
    Necessita aprofundamento

23. Ha rate limiting especifico para tentativas de login?
    Necessita aprofundamento

24. Como serao detetados e bloqueados bots?
    Necessita aprofundamento

### Revogacao
25. Como serao revogadas sessoes em caso de comprometimento?
    Necessita aprofundamento

26. Ha mecanismo de "logout de todos os dispositivos"?
    Necessita aprofundamento

27. Como sera tratada a revogacao de tokens ao mudar password?
    Necessita aprofundamento

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
