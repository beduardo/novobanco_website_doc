---
id: DEC-007-padrao-bff
aliases:
  - Padrao BFF Backend for Frontend
tags:
  - nextreality-novobanco-website-decisions
  - decisions
  - bff
  - api
  - architecture
approved: true
created: 2026-01-04
hubs:
  - "[[nextreality]]"
para-code: R
reviewed: true
status: accepted
---

# ADR-007: Padrao BFF (Backend for Frontend)

> **Related sections:** [3 - Visao Geral da Solucao](../sections/SEC-03-visao-geral-solucao.md), [5 - Arquitetura Backend & Servicos](../sections/SEC-05-arquitetura-backend-servicos.md)
> **Related definitions:** [DEF-03-principios-arquitetura.md](../definitions/DEF-03-principios-arquitetura.md), [DEF-05-arquitetura-bff.md](../definitions/DEF-05-arquitetura-bff.md)

## Status

Accepted

## Context

O HomeBanking Web necessita consumir os servicos backend existentes (criados para a app mobile) de forma segura e eficiente. E necessario definir a estrategia de integracao entre o frontend web e os servicos backend.

### Business Goals
- Reutilizacao de servicos backend existentes
- Experiencia otimizada para o canal web
- Isolamento de complexidades do legado

### Technical Constraints
- Servicos backend existentes expostos via API Gateway
- Diferentes requisitos de formato/agregacao entre canais
- Sessao web diferente de sessao mobile

### Non-functional Requirements
- Performance adequada (agregacao reduz latencia percebida)
- Seguranca (tokens nao expostos ao browser)
- Manutencao independente do frontend

## Decision

Adotar o padrao **Backend for Frontend (BFF)** como camada de integracao entre o Frontend Web e os servicos backend existentes.

**Caracteristicas do BFF:**
- Camada dedicada para o canal web
- Responsavel por agregacao e transformacao de dados
- Gestao de sessao e tokens
- Comunicacao exclusiva com API Gateway

**Responsabilidades:**

| Responsabilidade | BFF | API Gateway |
|------------------|-----|-------------|
| Agregacao de chamadas | Sim | Nao |
| Transformacao de dados | Sim | Nao |
| Cache de sessao | Sim | Nao |
| Autenticacao/Sessao | Sim | Nao |
| Rate Limiting | Nao | Sim |
| Roteamento | Nao | Sim |

**Acoplamento com Legados:**
- Frontend **nunca** comunica diretamente com servicos legados
- Todo o acesso e via BFF, que abstrai complexidades

## Alternatives Considered

### Alternative 1: API-First (Frontend direto ao Gateway)
- **Description:** Frontend comunica diretamente com API Gateway sem camada BFF
- **Pros:** Menos componentes, menos latencia
- **Cons:** Expoe complexidade do backend ao frontend, tokens no browser, sem agregacao
- **Why not chosen:** Seguranca insuficiente (tokens expostos), complexidade no frontend para agregar dados

### Alternative 2: GraphQL Gateway
- **Description:** Camada GraphQL para flexibilidade de queries
- **Pros:** Flexibilidade de queries, reduz over-fetching
- **Cons:** Complexidade adicional, curva de aprendizagem, nao alinhado com APIs REST existentes
- **Why not chosen:** APIs backend sao REST, GraphQL adicionaria camada de traducao sem beneficio claro

### Alternative 3: BFF Compartilhado (Web + Mobile)
- **Description:** Unico BFF para ambos os canais
- **Pros:** Menos componentes, reutilizacao
- **Cons:** Conflitos de requisitos entre canais, deploy acoplado
- **Why not chosen:** Canais tem requisitos diferentes, BFF dedicado permite evolucao independente

## Consequences

### Positive
- Frontend isolado de complexidades do backend
- Tokens OAuth nunca expostos ao browser
- Agregacao de dados reduz numero de requests do frontend
- Evolucao independente do canal web
- Transformacao de dados especifica para necessidades web

### Negative
- Componente adicional a desenvolver e manter
- Latencia adicional (hop extra)
- Potencial duplicacao de logica se mal gerido

## Notes

- Stack BFF: C# .NET 8 (conforme DEF-05-arquitetura-bff)
- Comunicacao BFF -> Backend: REST
- Decisoes de resiliencia (retry, timeout) aplicadas no BFF
