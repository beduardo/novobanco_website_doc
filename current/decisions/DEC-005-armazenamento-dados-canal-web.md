---
id: DEC-005-armazenamento-dados-canal-web
aliases:
  - Armazenamento de Dados Canal Web
tags:
  - nextreality-novobanco-website-decisions
  - decisions
  - data
  - storage
  - cache
approved: true
created: 2026-01-04
hubs:
  - "[[nextreality]]"
para-code: R
reviewed: true
status: accepted
---

# ADR-005: Armazenamento de Dados no Canal Web

> **Related sections:** [6 - Arquitetura de Dados](../sections/SEC-06-arquitetura-dados.md)
> **Related definitions:** [DEF-06-arquitetura-dados.md](../definitions/DEF-06-arquitetura-dados.md)

## Status

Accepted

## Context

O HomeBanking Web necessita definir onde e como os dados serao armazenados:
- Dados no browser (frontend)
- Dados no BFF
- Estrategia de cache

### Business Goals
- Performance adequada
- Seguranca de dados sensiveis
- Reutilizacao de dados entre paginas

### Technical Constraints
- Canal web reutiliza backend services existentes (dados transacionais la residem)
- BFF stateless preferencial
- Dados bancarios sao sensiveis

### Non-functional Requirements
- Conformidade RGPD
- Protecao de dados pessoais
- Performance de carregamento

## Decision

### Frontend (Browser)

**Persistencia Local:**
- **Tecnologia:** localStorage
- **Dados permitidos:** Apenas dados basicos do utilizador (nao sensiveis)
- **Estrategia de cache:** Dados publicos, noticias, informacoes frequentemente utilizadas na construcao de paginas
- **Dados proibidos:** Informacoes sigilosas do utilizador

### BFF

**Armazenamento:**
- **Base de dados propria:** Nao (apenas cache)
- **Cache:** Sim
- **Dados em cache:**
  - Sessao do utilizador
  - Tokens OAuth (Access e Refresh)
  - Informacoes frequentes se SSR/SSG completo for utilizado

### Dados Especificos do Canal Web

- Nao ha dados especificos do canal web que nao existam na app mobile
- Canal web consome os mesmos backend services

## Alternatives Considered

### Alternative 1: IndexedDB no frontend para dados offline
- **Description:** Base de dados local para funcionamento offline
- **Pros:** Suporte offline, melhor performance
- **Cons:** Complexidade, risco de dados sensiveis no browser
- **Why not chosen:** Requisitos PWA/Offline ainda nao definidos; localStorage suficiente para dados basicos

### Alternative 2: BFF com base de dados propria
- **Description:** PostgreSQL ou SQL Server no BFF para dados do canal web
- **Pros:** Independencia de backend services, cache persistente
- **Cons:** Duplicacao de dados, complexidade operacional, sincronizacao
- **Why not chosen:** Dados transacionais ja existem nos backend services; cache suficiente

### Alternative 3: Nenhum armazenamento no browser
- **Description:** Todo estado gerido pelo BFF, browser stateless
- **Pros:** Maxima seguranca, controlo total no servidor
- **Cons:** Performance degradada, mais requests ao servidor
- **Why not chosen:** localStorage para dados nao sensiveis oferece melhor UX

## Consequences

### Positive
- Simplicidade arquitetural (BFF apenas cache)
- Dados sensiveis nunca no browser
- Reutilizacao de backend services existentes
- Performance adequada com cache em dois niveis

### Negative
- Funcionalidade offline limitada
- Dependencia de conectividade para dados alem do basico
- Cache invalidation a definir

## Notes

- Estrategia de cache (TTL, invalidacao) necessita aprofundamento
- Se SSR/SSG completo for implementado, mais dados poderao residir em cache no BFF
- Necessario aprofundamento com UI para avaliar necessidades adicionais de dados no browser
