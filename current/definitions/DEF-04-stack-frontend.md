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

> **Secção relacionada:** [4 - Experiência do Utilizador & Arquitetura Frontend](../sections/SEC-04-experiencia-utilizador-frontend.md)

## Contexto

Definir a stack tecnológica do frontend do HomeBanking Web, considerando os requisitos de performance, segurança, multi-idioma e compatibilidade com browsers.

## Perguntas a Responder

### Framework e Linguagem
1. Qual framework JavaScript será utilizado (React, Angular, Vue, outro)?
    React

2. Será utilizado TypeScript?
    Sim

3. Há preferência por alguma versão específica do framework?
    A mais atual

### Build e Bundling
4. Qual ferramenta de build será utilizada (Webpack, Vite, outro)?
    Vite

5. Há requisitos de code splitting e lazy loading?
    Code Splitting por rotas usando React.Lazy.

### State Management
6. Qual solução de state management (Redux, MobX, Zustand, Context API)?
    Zustand

### Styling
7. Qual abordagem de styling (CSS-in-JS, SASS, CSS Modules, Tailwind)?
    Tailwind CSS

### Testes
8. Qual framework de testes unitários (Jest, Vitest)?
    Vitest

9. Qual ferramenta de testes E2E (Cypress, Playwright)?
    Playwright

### Multi-idioma
10. Qual biblioteca de i18n será utilizada?
    i18next

### Performance
11. Há requisitos específicos de bundle size?
    Necessita consulta ao cliente. Sugestão: < 200KB inicial (gzipped)

12. Será implementado SSR (Server Side Rendering) ou SSG?
    Híbrido: SSG para páginas estáticas, SSR para dados dinâmicos, ISR onde aplicável.
    BFF disponível para SSR protegendo client_secret no fluxo de login.

13. Será utilizado CDN para assets estáticos?
    **Sim.** Cliente delegou a decisão. Recomendação: Azure CDN (integração nativa com infraestrutura existente).

    **Justificação técnica:**
    - Redução de latência para utilizadores geograficamente distribuídos
    - Offload de tráfego dos servidores de aplicação
    - Cache de assets estáticos (JS, CSS, imagens)
    - Compressão automática (gzip/brotli)
    - Proteção contra picos de tráfego

    **Provider recomendado:** Azure CDN
    - Integração nativa com Azure (infraestrutura já existente)
    - Configuração via IaC (Terraform/Bicep)
    - Regras de cache granulares
    - Suporte a custom domains e HTTPS

## Decisões

### Framework Principal
- **Decisão:** React (versão mais atual)
- **Justificação:** Framework maduro, grande ecossistema, facilidade de contratação
- **Alternativas consideradas:** Angular, Vue (descartados)

### Linguagem
- **Decisão:** TypeScript
- **Justificação:** Type safety, melhor DX, redução de bugs em runtime
- **Alternativas consideradas:** JavaScript vanilla (descartado por falta de tipagem)

### Build Tool
- **Decisão:** Vite
- **Justificação:** Build rápido, HMR eficiente, configuração simples, suporte nativo a ESM
- **Alternativas consideradas:** Webpack (descartado por complexidade e velocidade)

### Code Splitting
- **Decisão:** Code Splitting por rotas usando React.Lazy
- **Justificação:** Otimização de bundle size, carregamento sob demanda
- **Alternativas consideradas:** Manual splitting (descartado por complexidade)

### State Management
- **Decisão:** Zustand
- **Justificação:** API simples, performance, sem boilerplate, integração com React
- **Alternativas consideradas:** Redux (descartado por boilerplate), MobX, Context API

### Data Fetching
- **Decisão:** TanStack Query (React Query) para pre-fetching e cache de dados
- **Justificação:** Cache inteligente, deduplicação, prefetching, estados de loading/error
- **Alternativas consideradas:** SWR, fetch manual

### Styling
- **Decisão:** Tailwind CSS
- **Justificação:** Utility-first, rápido desenvolvimento, bundle size otimizado com purge
- **Alternativas consideradas:** CSS-in-JS, SASS, CSS Modules

### Testes
- **Decisão:**
  - Unitários: Vitest
  - E2E: Playwright
- **Justificação:** Vitest integra com Vite, Playwright suporta múltiplos browsers
- **Alternativas consideradas:** Jest (descartado por integração), Cypress

### Internacionalização
- **Decisão:** i18next com react-i18next
- **Justificação:** Biblioteca madura, suporte a namespaces, lazy loading de traduções
- **Alternativas consideradas:** react-intl, linguiJS

### Rendering Strategy
- **Decisão:** Híbrido SSG + SSR + ISR
  - SSG: Páginas estáticas onde possível
  - SSR: Páginas com dados dinâmicos
  - ISR: Revalidação incremental onde aplicável
- **Justificação:** Performance otimizada, SEO, proteção de client_secret no fluxo de login
- **Alternativas consideradas:** CSR puro (descartado por SEO e segurança)

### Bundle Size
- **Decisão:** _A definir_ - Necessita consulta ao cliente
- **Justificação:** Definir limites de bundle para garantir performance
- **Alternativas consideradas:** N/A

### CDN para Assets Estáticos
- **Decisão:** Azure CDN para distribuição de assets estáticos
- **Justificação:** Cliente delegou decisão. Azure CDN oferece integração nativa com infraestrutura existente, redução de latência, offload de servidores e cache eficiente.
- **Alternativas consideradas:** Cloudflare (descartado por preferência de ecossistema Azure), sem CDN (descartado por impacto em performance)

## Restrições Conhecidas

- Compatibilidade com Chrome, Edge e Safari
- Design responsivo obrigatório
- Suporte a 3 idiomas (PT, EN, ES)
- Deploy em containers OpenShift

## Decisões Relacionadas

- [DEC-009-stack-tecnologica-frontend.md](../decisions/DEC-009-stack-tecnologica-frontend.md) - Stack tecnológica frontend

## Referências

- [DEF-02-requisitos-nao-funcionais.md](DEF-02-requisitos-nao-funcionais.md) - Requisitos de compatibilidade
- [DEF-03-principios-arquitetura.md](DEF-03-principios-arquitetura.md) - Princípios de arquitetura
