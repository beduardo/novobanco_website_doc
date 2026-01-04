---
id: DEC-009-stack-tecnologica-frontend
aliases:
  - Stack Tecnologica Frontend
tags:
  - nextreality-novobanco-website-decisions
  - decisions
  - frontend
  - react
  - typescript
approved: true
created: 2026-01-04
hubs:
  - "[[nextreality]]"
para-code: R
reviewed: true
status: accepted
---

# ADR-009: Stack Tecnologica Frontend

> **Related sections:** [4 - Experiencia do Utilizador & Arquitetura Frontend](../sections/SEC-04-experiencia-utilizador-frontend.md)
> **Related definitions:** [DEF-04-stack-frontend.md](../definitions/DEF-04-stack-frontend.md)

## Status

Accepted

## Context

O HomeBanking Web necessita de uma stack frontend moderna que:
- Suporte aplicacao SPA complexa com multiplas funcionalidades
- Permita desenvolvimento eficiente e manutencao a longo prazo
- Oferca boa performance e experiencia de utilizador
- Suporte multi-idioma e responsividade

### Business Goals
- Desenvolvimento rapido de 35 funcionalidades
- Experiencia de utilizador de alta qualidade
- Facilidade de contratacao de desenvolvedores

### Technical Constraints
- Deploy em containers OpenShift
- Compatibilidade com Chrome, Edge, Safari
- Suporte a 3 idiomas (PT, EN, ES)
- Design responsivo obrigatorio

### Non-functional Requirements
- LCP < 2.5s, FID < 100ms, CLS < 0.1
- Pagina inicial < 10s
- Suporte offline (a definir)

## Decision

Adotar a seguinte stack tecnologica para o frontend:

| Camada | Tecnologia | Versao |
|--------|------------|--------|
| **Framework** | React | 18+ (mais atual) |
| **Linguagem** | TypeScript | Latest |
| **Build Tool** | Vite | Latest |
| **State Management** | Zustand | Latest |
| **Data Fetching** | TanStack Query | Latest |
| **Styling** | Tailwind CSS | Latest |
| **i18n** | i18next | Latest |
| **Testes Unitarios** | Vitest | Latest |
| **Testes E2E** | Playwright | Latest |

**Rendering Strategy:**
- **SSG:** Paginas estaticas (landing, FAQ)
- **SSR:** Paginas com dados dinamicos (dashboard, saldos)
- **ISR:** Conteudo semi-estatico (noticias, indices)

**Justificacao da estrategia de rendering:** Protecao de `client_secret` no fluxo de login, performance otimizada, SEO quando aplicavel.

**Code Splitting:**
- Por rotas usando React.Lazy
- Bundle size otimizado com carregamento sob demanda

## Alternatives Considered

### Alternative 1: Angular + RxJS
- **Description:** Framework Angular com programacao reativa
- **Pros:** Framework completo, opinativo, bom para grandes equipas
- **Cons:** Curva de aprendizagem, mais verbose, menor pool de candidatos
- **Why not chosen:** React tem maior ecossistema e facilidade de contratacao

### Alternative 2: Vue 3 + Pinia
- **Description:** Vue.js 3 com Composition API e Pinia para state
- **Pros:** Sintaxe simples, boa documentacao, performance
- **Cons:** Ecossistema menor que React, menos candidatos no mercado
- **Why not chosen:** React oferece maior maturidade e ecossistema

### Alternative 3: Next.js (React)
- **Description:** Framework React com SSR/SSG built-in
- **Pros:** SSR/SSG integrado, routing automatico, API routes
- **Cons:** Opinativo, pode conflitar com BFF existente
- **Why not chosen:** Vite oferece mais flexibilidade; BFF dedicado ja existe para server-side logic

### Alternative 4: Redux para State Management
- **Description:** Redux Toolkit para gestao de estado global
- **Pros:** Previsibilidade, DevTools, grande adocao
- **Cons:** Boilerplate, complexidade para estados simples
- **Why not chosen:** Zustand oferece API mais simples sem sacrificar funcionalidade

### Alternative 5: Webpack para Build
- **Description:** Webpack 5 para bundling
- **Pros:** Maduro, muitos plugins, flexivel
- **Cons:** Configuracao complexa, builds mais lentos
- **Why not chosen:** Vite oferece builds significativamente mais rapidos e configuracao mais simples

## Consequences

### Positive
- Stack moderna e bem suportada
- Desenvolvimento rapido com hot module replacement (Vite)
- Type safety com TypeScript
- Styling eficiente com Tailwind (utility-first)
- Cache e prefetching inteligente (TanStack Query)
- Testes robustos (Vitest + Playwright)

### Negative
- Curva de aprendizagem para desenvolvedores nao familiarizados
- SSR/SSG hibrido adiciona complexidade
- Multiplas bibliotecas a manter atualizadas

## Notes

- Versoes especificas a fixar no inicio do desenvolvimento
- Bundle size limits a definir com cliente
- Design System a avaliar: biblioteca existente vs desenvolvimento interno
