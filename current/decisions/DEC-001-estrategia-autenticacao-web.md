---
id: DEC-001-estrategia-autenticacao-web
aliases:
  - Estrategia de Autenticacao Web
tags:
  - nextreality-novobanco-website-decisions
  - decisions
  - authentication
  - sca
  - security
approved: true
created: 2026-01-04
hubs:
  - "[[nextreality]]"
para-code: R
reviewed: true
status: accepted
---

# ADR-001: Estrategia de Autenticacao Web

> **Related sections:** [7 - Autenticacao & Autorizacao](../sections/SEC-07-autenticacao-autorizacao.md)
> **Related definitions:** [DEF-07-autenticacao-autorizacao.md](../definitions/DEF-07-autenticacao-autorizacao.md)

## Status

Accepted

## Context

O HomeBanking Web necessita de uma estrategia de autenticacao que:
- Cumpra os requisitos PSD2 de Strong Customer Authentication (SCA)
- Reutilize a infraestrutura de autenticacao existente da app mobile
- Proporcione boa experiencia de utilizador no canal web
- Suporte multiplos metodos de segundo fator

### Business Goals
- Paridade funcional com app mobile
- Seguranca robusta para operacoes bancarias
- Experiencia de utilizador fluida

### Technical Constraints
- Integracao com servico de autenticacao existente
- SCA obrigatorio para todas as operacoes
- Sessao web diferente de sessao mobile

### Non-functional Requirements
- Disponibilidade 99.9%
- Conformidade PSD2

## Decision

Implementar autenticacao baseada em **QR Code com validacao biometrica na app mobile** como metodo primario, com **fallback para SMS OTP ou App Push**.

**Fluxo Primario (QR Code):**
1. Frontend web apresenta QR Code gerado pelo BFF
2. Utilizador escaneia QR Code com app mobile
3. App mobile requer biometria para aprovar
4. Sessao web e vinculada ao utilizador autenticado na app

**Fluxo Fallback:**
- Apos falha na leitura do QR Code, utilizador pode optar por:
  - SMS OTP
  - App Push notification
- Opcoes dependem das configuracoes do utilizador

**Metodos de Autenticacao:**
- Username/Password: Somente no fluxo de fallback
- Biometria (WebAuthn/FIDO2): Requerido na validacao do QR Code pela app
- Certificado digital: Nao suportado

## Alternatives Considered

### Alternative 1: Username/Password + SMS OTP
- **Description:** Autenticacao tradicional com segundo fator SMS
- **Pros:** Simples de implementar, familiaridade do utilizador
- **Cons:** Menos seguro (SIM swap), UX mais lenta
- **Why not chosen:** Menor seguranca e UX inferior ao QR Code

### Alternative 2: WebAuthn/FIDO2 nativo no browser
- **Description:** Autenticacao sem password usando chaves biometricas do dispositivo
- **Pros:** Alta seguranca, sem dependencia da app mobile
- **Cons:** Requer registo previo de dispositivo, nao reutiliza infra existente
- **Why not chosen:** Nao aproveita a app mobile ja instalada pelos utilizadores

### Alternative 3: Magic Link por email
- **Description:** Link de autenticacao enviado por email
- **Pros:** Simples, sem necessidade de app
- **Cons:** Seguranca dependente do email, latencia
- **Why not chosen:** Nao cumpre requisitos SCA adequadamente

## Consequences

### Positive
- Reutilizacao da app mobile como segundo fator
- Experiencia de utilizador rapida (scan + biometria)
- Alta seguranca (biometria + dispositivo registado)
- Cumprimento PSD2 SCA

### Negative
- Dependencia da app mobile para autenticacao primaria
- Necessita fluxo fallback para utilizadores sem app
- Complexidade adicional na gestao de sessoes cross-device

## Notes

- Fluxos especificos de fallback a validar: quais combinacoes SMS OTP / App Push serao realmente disponibilizadas
- Fluxo de primeiro acesso/registo web necessita aprofundamento
