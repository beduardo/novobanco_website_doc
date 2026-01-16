---
id: DEF-07-autenticacao-autorizacao
aliases:
  - Autenticação e Autorização
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

# DEF-07: Autenticação & Autorização

> **Secção relacionada:** [7 - Autenticação & Autorização](../sections/SEC-07-autenticacao-autorizacao.md)

## Contexto

Definir a estratégia de autenticação e autorização do HomeBanking Web. Nota: O fluxo básico OAuth já foi definido em DEF-05-arquitetura-bff.md. Este documento aprofunda os detalhes de sessão, MFA, e políticas de segurança.

## Perguntas a Responder

### Autenticação - Fluxos
1. Quais métodos de autenticação serão suportados?
   - Username/Password? Somente no fluxo de fallback
   - Biometria (WebAuthn/FIDO2)? Requerido pelos fluxos de validação do QR Code de sessão pelo app
   - Certificado digital? Não

2. O login será unificado com a app mobile (mesmas credenciais)?
    Sim

3. Há fluxo de primeiro acesso/registo específico para web?
    Necessita aprofundamento

### MFA/SCA (Strong Customer Authentication)
4. Qual o segundo fator obrigatório (App push, SMS OTP, TOTP)?
    Nos fluxos de leitura do QR Code, o app deverá requerer a biometria antes de aprovar e vincular a sessão ao utilizador logado na app. E no fluxo de fallback há a possibilidade de se utilizar SMS OTP e App push. A definição de quais dos quatro fluxos realmente serão utilizados ainda necessita de validação.

5. Há cenários onde SCA pode ser dispensado (PSD2 exemptions)?
    Até o momento não há cenários públicos. Todos os cenários de acesso a páginas restritas necessitam de SCA.

6. Como será tratado o fallback se o método primário falhar?
    Após a tentativa de leitura do QR Code e informação de falha pelo utilizador, a aplicação deverá permitir o login com a opção via SMS OTP ou App push. Isso dependerá das opções habilitadas para o utilizador.


### Gestão de Sessões
7. Qual o tempo de vida da sessão (timeout por inatividade)?
    10 minutos

8. Qual o tempo máximo absoluto de sessão?
    30 minutos

9. A sessão é exclusiva (logout de outras sessões ao fazer login)?
    Desejável, necessita aprovação pelo cliente

10. Como será comunicado ao utilizador que a sessão vai expirar?
    Popup na aplicação com temporizador

### Sessão Multi-Canal (NOVO)

11. Como a sessão web se relaciona com a sessão mobile (mesmo utilizador)?
    Necessita aprofundamento. Considerar: sessões independentes ou sincronizadas

12. Há limite de sessões ativas por utilizador?
    Necessita aprofundamento. Sugestão: 1 sessão web + 1 sessão mobile

### Estratégia de Tokens
13. Qual o tempo de vida do access token?
    15 minutos

14. Qual o tempo de vida do refresh token?
    7 dias

15. Onde serão armazenados os tokens?
    Backend tokens (Access/Refresh): BFF cache
    Session tokens: Cookie HttpOnly Secure

16. Como será tratada a renovação de tokens?
    Refresh silencioso conforme atividade do utilizador

### Autorização
17. Qual o modelo de autorização (RBAC, ABAC)?
    ABAC híbrido com RBAC. Roles como atributo do sujeito.

18. Há permissões específicas por tipo de operação?
    Sim (consulta vs transação)

### Políticas de Password
19. Quais os requisitos mínimos de password?
    Seguirá requisitos preexistentes da App. Necessita aprofundamento

20. Há bloqueio após tentativas falhadas?
    Necessita aprofundamento

### Anti-automation e Revogação (Simplificado)
21. Será implementado CAPTCHA ou rate limiting em login?
    Necessita aprofundamento. Rate limiting no Gateway.

22. Há mecanismo de logout de todos os dispositivos?
    Necessita aprofundamento. Essencial para segurança.

## Decisões

### Métodos de Autenticação
- **Decisão:** _A preencher_
- **Justificação:**
- **Alternativas consideradas:**

### MFA/SCA
- **Decisão:** _A preencher_
- **Justificação:**
- **Alternativas consideradas:**

### Gestão de Sessões
- **Decisão:** _A preencher_
- **Justificação:**
- **Alternativas consideradas:**

### Tokens
- **Decisão:** _A preencher_
- **Justificação:**
- **Alternativas consideradas:**

### Autorização
- **Decisão:** _A preencher_
- **Justificação:**
- **Alternativas consideradas:**

### Anti-automation
- **Decisão:** _A preencher_
- **Justificação:**
- **Alternativas consideradas:**

## Restrições Conhecidas

- SCA obrigatório conforme PSD2
- Integração com serviço de autenticação existente do banco
- Cookies HttpOnly para sessão (definido em DEF-05)
- OAuth 2.0 como base (definido em DEF-05)

## Decisões Relacionadas

- [DEC-001-estrategia-autenticacao-web.md](../decisions/DEC-001-estrategia-autenticacao-web.md) - Estratégia de autenticação
- [DEC-002-gestao-sessoes-tokens.md](../decisions/DEC-002-gestao-sessoes-tokens.md) - Gestão de sessões e tokens
- [DEC-003-modelo-autorizacao-abac.md](../decisions/DEC-003-modelo-autorizacao-abac.md) - Modelo de autorização ABAC

## Referências

- [DEF-05-arquitetura-bff.md](DEF-05-arquitetura-bff.md) - Fluxo OAuth básico
- [DEF-08-seguranca-conformidade.md](DEF-08-seguranca-conformidade.md) - PSD2
- PSD2 - Payment Services Directive 2
- OWASP Authentication Cheat Sheet
