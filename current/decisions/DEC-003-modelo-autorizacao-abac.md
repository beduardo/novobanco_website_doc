---
id: DEC-003-modelo-autorizacao-abac
aliases:
  - Modelo de Autorizacao ABAC
tags:
  - nextreality-novobanco-website-decisions
  - decisions
  - authorization
  - abac
  - rbac
approved: true
created: 2026-01-04
hubs:
  - "[[nextreality]]"
para-code: R
reviewed: true
status: accepted
---

# ADR-003: Modelo de Autorizacao ABAC Hibrido

> **Related sections:** [7 - Autenticacao & Autorizacao](../sections/SEC-07-autenticacao-autorizacao.md)
> **Related definitions:** [DEF-07-autenticacao-autorizacao.md](../definitions/DEF-07-autenticacao-autorizacao.md)

## Status

Accepted

## Context

O HomeBanking Web necessita de um modelo de autorizacao que:
- Suporte diferentes tipos de operacoes (consulta vs transacao)
- Seja flexivel para regras de negocio complexas
- Reutilize modelo existente da app mobile
- Permita evolucao sem alteracoes estruturais

### Business Goals
- Controlo granular de acessos
- Diferentes permissoes por tipo de operacao
- Suporte a evolucao de produtos e funcionalidades

### Technical Constraints
- Integracao com sistema de autorizacao existente
- Paridade com app mobile
- Performance adequada para validacao em tempo real

### Non-functional Requirements
- Auditabilidade de decisoes de acesso
- Flexibilidade para novos atributos

## Decision

Implementar modelo de autorizacao **ABAC (Attribute-Based Access Control) hibrido com RBAC**, onde:

- **Role** e utilizado apenas como mais um atributo do sujeito (quando necessario)
- **Decisoes de acesso** sao definidas por politicas construidas sobre o conjunto de atributos
- **Atributos considerados:**
  - **Sujeito**: utilizador, role (opcional), tipo de cliente, segmento
  - **Recurso**: tipo de conta, produto, limite
  - **Acao**: consulta, transacao, configuracao
  - **Ambiente**: canal (web), horario, localizacao, dispositivo

**Permissoes por tipo de operacao:**
- Ha permissoes especificas diferenciando consulta vs transacao
- Detalhes de roles/perfis serao especificados no assessment inicial

## Alternatives Considered

### Alternative 1: RBAC puro (Role-Based Access Control)
- **Description:** Controlo de acesso baseado apenas em roles/perfis
- **Pros:** Simplicidade, facil de entender e auditar
- **Cons:** Rigido, explosao de roles para regras complexas
- **Why not chosen:** Insuficiente para regras de negocio bancarias que dependem de multiplos atributos

### Alternative 2: ACL (Access Control Lists)
- **Description:** Listas de acesso por recurso
- **Pros:** Controlo granular por recurso
- **Cons:** Dificil de gerir em escala, nao considera contexto
- **Why not chosen:** Nao escala bem e nao suporta decisoes baseadas em contexto

### Alternative 3: ABAC puro (sem roles)
- **Description:** Todas as decisoes baseadas apenas em atributos, sem conceito de role
- **Pros:** Maxima flexibilidade
- **Cons:** Complexidade de gestao, perda de abstracoes uteis
- **Why not chosen:** Roles ainda sao uteis como abstracoes, modelo hibrido oferece melhor equilibrio

## Consequences

### Positive
- Flexibilidade para regras de negocio complexas
- Reutilizacao de roles como atributo quando conveniente
- Suporte a contexto (canal, horario, etc.) nas decisoes
- Facilidade de adicionar novos atributos sem reestruturacao

### Negative
- Maior complexidade que RBAC puro
- Necessita motor de politicas ou logica de avaliacao
- Documentacao de politicas requer mais detalhe

## Notes

- Roles e perfis especificos serao definidos no assessment inicial do projeto
- O documento atual nao aprofunda estes detalhes operacionais
