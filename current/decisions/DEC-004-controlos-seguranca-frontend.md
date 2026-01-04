---
id: DEC-004-controlos-seguranca-frontend
aliases:
  - Controlos de Seguranca Frontend
tags:
  - nextreality-novobanco-website-decisions
  - decisions
  - security
  - headers
  - xss
  - csrf
approved: true
created: 2026-01-04
hubs:
  - "[[nextreality]]"
para-code: R
reviewed: true
status: accepted
---

# ADR-004: Controlos de Seguranca Frontend

> **Related sections:** [8 - Seguranca & Conformidade](../sections/SEC-08-seguranca-conformidade.md)
> **Related definitions:** [DEF-08-seguranca-conformidade.md](../definitions/DEF-08-seguranca-conformidade.md)

## Status

Accepted

## Context

O HomeBanking Web necessita de controlos de seguranca robustos no frontend para:
- Proteger contra ataques comuns (XSS, CSRF, Clickjacking)
- Cumprir boas praticas OWASP
- Garantir integridade de recursos carregados
- Estabelecer comunicacao segura

### Business Goals
- Protecao de dados dos utilizadores
- Conformidade com regulamentacao bancaria
- Confianca dos utilizadores no canal web

### Technical Constraints
- Stack frontend: React + TypeScript
- Rendering: SSR (Server-Side Rendering) via BFF
- Bibliotecas de terceiros necessarias

### Non-functional Requirements
- Seguranca sem degradacao significativa de performance
- Compatibilidade com browsers modernos

## Decision

Implementar os seguintes controlos de seguranca:

### Security Headers HTTP

| Header | Valor | Justificacao |
|--------|-------|--------------|
| **Content-Security-Policy** | `self` inicial, expandir conforme necessidade | Prevencao XSS, controlo de recursos |
| **X-Frame-Options** | `SAMEORIGIN` | Prevencao Clickjacking |
| **X-Content-Type-Options** | `nosniff` | Prevencao MIME sniffing |
| **Strict-Transport-Security** | `max-age` a definir no assessment | Forcas HTTPS |

### Subresource Integrity (SRI)

- **Estrategia:** Bibliotecas servidas localmente (evitar CDN externas)
- **Atributos:** `integrity` e `crossorigin` em todos os recursos externos
- **Gestao de dependencias:** Atencao a atualizacoes que possam quebrar hash

### Protecao XSS

**SSR/BFF:**
- Escape de saida do HTML gerado pelo SSR
- Validacao e sanitizacao de entrada

**Frontend React:**
- React faz escape automatico de variaveis em JSX
- `innerHTML` e `eval` **proibidos** via lint rules e SonarQube

### Protecao CSRF

- Tokens CSRF rotacionados por request
- Cookie de sessao: `SameSite=Strict`, `Secure`, `HttpOnly`
- CORS configurado restritivamente
- Operacoes GET somente idempotentes (sem efeitos colaterais)

## Alternatives Considered

### Alternative 1: CSP permissivo (unsafe-inline, unsafe-eval)
- **Description:** CSP mais flexivel para facilitar desenvolvimento
- **Pros:** Menos restricoes, desenvolvimento mais rapido
- **Cons:** Seguranca significativamente reduzida
- **Why not chosen:** Inaceitavel para aplicacao bancaria

### Alternative 2: Bibliotecas via CDN com SRI
- **Description:** Usar CDNs publicas com verificacao de integridade
- **Pros:** Melhor cache, menor carga no servidor
- **Cons:** Dependencia de terceiros, risco de alteracoes inesperadas
- **Why not chosen:** Preferencia por controlo total dos recursos

### Alternative 3: CSRF via header customizado (X-CSRF-Token apenas)
- **Description:** Apenas header customizado sem rotacao
- **Pros:** Implementacao mais simples
- **Cons:** Menor protecao, tokens estaticos
- **Why not chosen:** Rotacao de tokens oferece protecao superior

## Consequences

### Positive
- Protecao robusta contra XSS, CSRF, Clickjacking
- Controlos verificaveis e auditaveis
- Alinhamento com OWASP Top 10
- Recursos sob controlo total (sem CDN)

### Negative
- CSP restritivo pode requerer ajustes durante desenvolvimento
- SRI local requer gestao de atualizacoes de bibliotecas
- Overhead de rotacao de tokens CSRF

## Notes

- Valor de `max-age` para HSTS a definir no assessment inicial
- Politica CSP inicial `self`, expandir conforme necessidades identificadas
- Regras de lint e SonarQube a configurar para bloquear `innerHTML`/`eval`
