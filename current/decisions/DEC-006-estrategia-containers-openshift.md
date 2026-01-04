---
id: DEC-006-estrategia-containers-openshift
aliases:
  - Estrategia de Containers OpenShift
tags:
  - nextreality-novobanco-website-decisions
  - decisions
  - containers
  - openshift
  - infrastructure
approved: true
created: 2026-01-04
hubs:
  - "[[nextreality]]"
para-code: R
reviewed: true
status: accepted
---

# ADR-006: Estrategia de Containers (OpenShift)

> **Related sections:** [3 - Visao Geral da Solucao](../sections/SEC-03-visao-geral-solucao.md)
> **Related definitions:** [DEF-03-principios-arquitetura.md](../definitions/DEF-03-principios-arquitetura.md)

## Status

Accepted

## Context

O HomeBanking Web necessita de uma estrategia de deploy e runtime que:
- Se integre com a infraestrutura existente do banco
- Suporte escalabilidade e alta disponibilidade
- Permita deploy e gestao enterprise-grade
- Facilite a operacao e monitorizacao

### Business Goals
- Reutilizacao de infraestrutura existente
- Operacoes simplificadas
- Suporte a SLA 99.9%

### Technical Constraints
- Infraestrutura existente baseada em OpenShift
- Requisitos de seguranca bancaria
- Integracao com pipelines CI/CD existentes

### Non-functional Requirements
- Alta disponibilidade (99.9%)
- Escalabilidade horizontal
- Recuperacao de desastres

## Decision

Adotar **arquitetura orientada a containers, compliant com OpenShift** para todos os componentes do HomeBanking Web (Frontend e BFF).

**Componentes containerizados:**
- HomeBanking Web (SPA) - servido via container
- BFF Web (.NET 8) - container

**Caracteristicas:**
- Imagens container otimizadas
- Health checks (liveness/readiness)
- Resource limits e requests definidos
- Configuracao via ConfigMaps/Secrets

## Alternatives Considered

### Alternative 1: VMs Tradicionais
- **Description:** Deploy em maquinas virtuais tradicionais
- **Pros:** Modelo conhecido, menor curva de aprendizagem
- **Cons:** Menor flexibilidade, escalabilidade manual, mais recursos
- **Why not chosen:** Nao alinhado com estrategia de modernizacao, falta de flexibilidade

### Alternative 2: Kubernetes Vanilla
- **Description:** Kubernetes sem a camada OpenShift
- **Pros:** Mais leve, sem custos de licenciamento Red Hat
- **Cons:** Menos features enterprise, menos integracao com ferramentas existentes
- **Why not chosen:** OpenShift ja e o padrao do banco, oferece mais features enterprise (RBAC, Routes, ImageStreams)

### Alternative 3: Serverless/FaaS
- **Description:** Funcoes serverless para o BFF
- **Pros:** Escalabilidade automatica, pago por uso
- **Cons:** Cold starts, complexidade de gestao de estado, vendor lock-in
- **Why not chosen:** Nao adequado para BFF com gestao de sessao, latencia de cold start inaceitavel

## Consequences

### Positive
- Alinhamento com infraestrutura existente do banco
- Capacidades enterprise (RBAC, auditing, routes)
- Escalabilidade horizontal nativa
- Integracao com CI/CD existente
- Health checks e self-healing

### Negative
- Dependencia de Red Hat/OpenShift
- Curva de aprendizagem para equipas nao familiarizadas
- Overhead de orquestracao para aplicacao relativamente simples

## Notes

- Versao OpenShift a confirmar com equipa de infraestrutura
- Estrategia de resource limits a definir no assessment
- Integracao com pipelines CI/CD a detalhar
