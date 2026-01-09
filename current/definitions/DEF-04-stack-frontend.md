---
id: DEF-04-stack-frontend
aliases:
  - Stack Frontend
tags:
  - nextreality-novobanco-website-definitions
  - definitions
  - frontend
  - technology-stack
approved: true
created: 2026-01-03
hubs:
  - "[[nextreality]]"
para-code: R
reviewed: true
status: completed
---

# DEF-04: Stack Frontend

> **Secao relacionada:** [4 - Experiencia do Utilizador & Arquitetura Frontend](../sections/SEC-04-experiencia-utilizador-frontend.md)

## Contexto

Definir a stack tecnologica do frontend do HomeBanking Web, considerando os requisitos de performance, seguranca, multi-idioma e compatibilidade com browsers.

## Perguntas a Responder

### Framework e Linguagem
1. Qual framework JavaScript sera utilizado (React, Angular, Vue, outro)?
    React

2. Sera utilizado TypeScript?
    Sim

3. Ha preferencia por alguma versao especifica do framework?
    A mais atual

### Build e Bundling
4. Qual ferramenta de build sera utilizada (Webpack, Vite, outro)?
    Vite

5. Ha requisitos de code splitting e lazy loading?
    Code Splitting por rotas usando React.Lazy.

### State Management
6. Qual solucao de state management (Redux, MobX, Zustand, Context API)?
    Zustand

### Styling
7. Qual abordagem de styling (CSS-in-JS, SASS, CSS Modules, Tailwind)?
    Tailwind CSS

### Testes
8. Qual framework de testes unitarios (Jest, Vitest)?
    Vitest

9. Qual ferramenta de testes E2E (Cypress, Playwright)?
    Playwright

### Multi-idioma
10. Qual biblioteca de i18n sera utilizada?
    i18next

### Performance
11. Ha requisitos especificos de bundle size?
    Necessita consulta ao cliente
    
12. Sera implementado SSR (Server Side Rendering) ou SSG?
    Sim, SSG no que for possível, SSR nas páginas com acesso dados que mudem constantemente e SSG + ISR no que for possível. Isso será usado inclusive para permitir um fluxo de login mais seguro protegendo o client_secret. Teremos um BFF disponível para o SSR se tecnicamente possível e necessário.

## Decisoes

### Framework Principal
- **Decisao:** React (versao mais atual)
- **Justificacao:** Framework maduro, grande ecossistema, facilidade de contratacao
- **Alternativas consideradas:** Angular, Vue (descartados)

### Linguagem
- **Decisao:** TypeScript
- **Justificacao:** Type safety, melhor DX, reducao de bugs em runtime
- **Alternativas consideradas:** JavaScript vanilla (descartado por falta de tipagem)

### Build Tool
- **Decisao:** Vite
- **Justificacao:** Build rapido, HMR eficiente, configuracao simples, suporte nativo a ESM
- **Alternativas consideradas:** Webpack (descartado por complexidade e velocidade)

### Code Splitting
- **Decisao:** Code Splitting por rotas usando React.Lazy
- **Justificacao:** Otimizacao de bundle size, carregamento sob demanda
- **Alternativas consideradas:** Manual splitting (descartado por complexidade)

### State Management
- **Decisao:** Zustand
- **Justificacao:** API simples, performance, sem boilerplate, integracao com React
- **Alternativas consideradas:** Redux (descartado por boilerplate), MobX, Context API

### Data Fetching
- **Decisao:** TanStack Query (React Query) para pre-fetching e cache de dados
- **Justificacao:** Cache inteligente, deduplicacao, prefetching, estados de loading/error
- **Alternativas consideradas:** SWR, fetch manual

### Styling
- **Decisao:** Tailwind CSS
- **Justificacao:** Utility-first, rapido desenvolvimento, bundle size otimizado com purge
- **Alternativas consideradas:** CSS-in-JS, SASS, CSS Modules

### Testes
- **Decisao:**
  - Unitarios: Vitest
  - E2E: Playwright
- **Justificacao:** Vitest integra com Vite, Playwright suporta multiplos browsers
- **Alternativas consideradas:** Jest (descartado por integracao), Cypress

### Internacionalizacao
- **Decisao:** i18next com react-i18next
- **Justificacao:** Biblioteca madura, suporte a namespaces, lazy loading de traducoes
- **Alternativas consideradas:** react-intl, linguiJS

### Rendering Strategy
- **Decisao:** Hibrido SSG + SSR + ISR
  - SSG: Paginas estaticas onde possivel
  - SSR: Paginas com dados dinamicos
  - ISR: Revalidacao incremental onde aplicavel
- **Justificacao:** Performance otimizada, SEO, protecao de client_secret no fluxo de login
- **Alternativas consideradas:** CSR puro (descartado por SEO e seguranca)

### Bundle Size
- **Decisao:** _A definir_ - Necessita consulta ao cliente
- **Justificacao:** Definir limites de bundle para garantir performance
- **Alternativas consideradas:** N/A

## Restricoes Conhecidas

- Compatibilidade com Chrome, Edge e Safari
- Design responsivo obrigatorio
- Suporte a 3 idiomas (PT, EN, ES)
- Deploy em containers OpenShift

## Decisoes Relacionadas

- [DEC-009-stack-tecnologica-frontend.md](../decisions/DEC-009-stack-tecnologica-frontend.md) - Stack tecnologica frontend

## Referencias

- [DEF-02-requisitos-nao-funcionais.md](DEF-02-requisitos-nao-funcionais.md) - Requisitos de compatibilidade
- [DEF-03-principios-arquitetura.md](DEF-03-principios-arquitetura.md) - Principios de arquitetura
