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
    **Sim.** Existe fluxo de primeiro acesso/registo específico para o canal web.
    - Validação de identidade: Utiliza a mesma API de Login
    - Registo: Pode ser feito pela Web ou pela APP. São processos semelhantes mas necessários em cada dispositivo (independentes).

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

### Sessão Multi-Canal

11. Como a sessão web se relaciona com a sessão mobile (mesmo utilizador)?
    **Não há relação.** As sessões web e mobile são completamente independentes.

12. Há limite de sessões ativas por utilizador?
    Necessita aprofundamento.

13. O login web deve fazer logout automático de outras sessões?
    Necessita aprofundamento.

### Estratégia de Tokens
14. Qual o tempo de vida do access token?
    15 minutos

15. Qual o tempo de vida do refresh token?
    7 dias

16. Onde serão armazenados os tokens?
    Backend tokens (Access/Refresh): BFF cache
    Session tokens: Cookie HttpOnly Secure

17. Como será tratada a renovação de tokens?
    Refresh silencioso conforme atividade do utilizador

### Autorização
18. Qual o modelo de autorização (RBAC, ABAC)?
    ABAC híbrido com RBAC. Roles como atributo do sujeito.

19. Há permissões específicas por tipo de operação?
    Sim (consulta vs transação)

### Políticas de Password
20. Quais os requisitos mínimos de password?
    **Gerido pela API.** Cliente indicou que toda a lógica de políticas de password é gerida pelo backend/API. Não é responsabilidade do frontend definir estas regras.

21. Há política de expiração de password?
    **Gerido pela API.**

22. Há bloqueio após tentativas falhadas?
    **Gerido pela API.**

23. Como funciona o fluxo de recuperação/reset de password?
    **Gerido pela API.** O frontend apenas apresenta os formulários; a validação e lógica é do backend.

### Anti-automation e Revogação
24. Será implementado CAPTCHA ou rate limiting em login?
    Necessita aprofundamento. Rate limiting no Gateway.

25. Há mecanismo de logout de todos os dispositivos (panic button)?
    Necessita aprofundamento. Essencial para segurança.

26. Como funciona a revogação de tokens em caso de comprometimento?
    Necessita aprofundamento.

### Fallback de MFA
27. A disponibilidade de métodos de fallback depende de configuração por utilizador ou é uniforme?
    **Uniforme.** Todos os utilizadores têm acesso aos mesmos métodos de fallback.

28. Há prioridade entre os métodos de fallback?
    **Não.** Sem prioridade entre métodos.

## Decisões

### Métodos de Autenticação
- **Decisão:** Login unificado (mesmas credenciais web/mobile) com fluxo de registo independente por canal
- **Justificação:** Utilizadores podem registar-se pela Web ou APP separadamente. Validação usa mesma API de Login.
- **Alternativas consideradas:** Registo obrigatório via APP primeiro (descartado pelo cliente)

### MFA/SCA
- **Decisão:** QR Code com biometria como método primário; SMS OTP e App Push como fallback
- **Justificação:** Fallback uniforme para todos os utilizadores, sem prioridade entre métodos
- **Alternativas consideradas:** Configuração por utilizador (descartado - será uniforme)

### Gestão de Sessões
- **Decisão:** Sessões web e mobile completamente independentes
- **Justificação:** Cliente confirmou que não há relação entre sessões dos dois canais
- **Alternativas consideradas:** Sessões sincronizadas (descartado)

### Tokens
- **Decisão:** Access token 15 min, Refresh token 7 dias, armazenados no BFF
- **Justificação:** Segurança com renovação silenciosa conforme atividade
- **Alternativas consideradas:** Tokens mais longos (descartado por segurança)

### Autorização
- **Decisão:** ABAC híbrido com RBAC (roles como atributo)
- **Justificação:** Flexibilidade para permissões por tipo de operação
- **Alternativas consideradas:** RBAC puro (descartado por falta de granularidade)

### Políticas de Password
- **Decisão:** Totalmente gerido pela API/Backend
- **Justificação:** Cliente indicou que requisitos, expiração, bloqueio e recuperação são responsabilidade da API. Frontend apenas apresenta formulários.
- **Alternativas consideradas:** Validação duplicada no frontend (descartado)

### Anti-automation
- **Decisão:** _A definir_ - Necessita aprofundamento
- **Justificação:** CAPTCHA, rate limiting e revogação de tokens ainda pendentes de validação
- **Alternativas consideradas:** N/A

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
