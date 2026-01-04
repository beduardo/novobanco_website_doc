---
id: DEC-008-stack-observabilidade-elk
aliases:
  - Stack de Observabilidade ELK
tags:
  - nextreality-novobanco-website-decisions
  - decisions
  - observability
  - elk
  - logging
  - monitoring
approved: true
created: 2026-01-04
hubs:
  - "[[nextreality]]"
para-code: R
reviewed: true
status: accepted
---

# ADR-008: Stack de Observabilidade (ELK)

> **Related sections:** [3 - Visao Geral da Solucao](../sections/SEC-03-visao-geral-solucao.md), [11 - Observabilidade & Operacoes](../sections/SEC-11-observabilidade-operacoes.md)
> **Related definitions:** [DEF-03-principios-arquitetura.md](../definitions/DEF-03-principios-arquitetura.md)

## Status

Accepted

## Context

O HomeBanking Web necessita de capacidades de observabilidade para:
- Monitorizacao de saude da aplicacao
- Troubleshooting e debugging
- Auditoria e compliance
- Analise de performance

### Business Goals
- Visibilidade operacional
- Reducao de tempo de resolucao de incidentes (MTTR)
- Suporte a requisitos de auditoria

### Technical Constraints
- Infraestrutura de observabilidade existente no banco
- Requisitos de retencao de logs (compliance bancario)
- Integracao com ferramentas de alerting existentes

### Non-functional Requirements
- Centralizacao de logs
- Capacidade de correlacao entre componentes
- Dashboards operacionais

## Decision

Adotar a **stack ELK (Elasticsearch, Logstash, Kibana)** para logs de aplicacao e captura de metricas do HomeBanking Web.

**Componentes:**
- **Elasticsearch:** Armazenamento e indexacao de logs
- **Logstash:** Ingestao e transformacao de logs
- **Kibana:** Visualizacao e dashboards

**Dados capturados:**
- Logs de aplicacao (Frontend e BFF)
- Metricas de aplicacao
- Traces de requests (correlacao)

**Integracao:**

```
Frontend Web --> ELK Stack (logs do browser)
BFF Web --> ELK Stack (logs de aplicacao, metricas)
```

## Alternatives Considered

### Alternative 1: Prometheus + Grafana
- **Description:** Prometheus para metricas, Grafana para dashboards
- **Pros:** Excelente para metricas, alerting nativo
- **Cons:** Nao cobre logs centralizados
- **Why not chosen:** Pode complementar ELK para metricas, mas ELK e a base por ser a stack existente

### Alternative 2: Datadog / New Relic (SaaS)
- **Description:** Plataforma de observabilidade SaaS
- **Pros:** Features avancadas, setup rapido, APM integrado
- **Cons:** Custo elevado, dados fora do perimetro do banco
- **Why not chosen:** Custo e requisitos de residencia de dados bancarios

### Alternative 3: Jaeger + Loki + Grafana
- **Description:** Stack moderna de observabilidade cloud-native
- **Pros:** Eficiente para traces, logs estruturados
- **Cons:** Nao alinhado com infraestrutura existente
- **Why not chosen:** ELK ja existe e esta operacional no banco

## Consequences

### Positive
- Reutilizacao de infraestrutura de observabilidade existente
- Centralizacao de logs de todos os componentes
- Dashboards unificados para operacoes
- Suporte a requisitos de auditoria

### Negative
- ELK pode ser resource-intensive
- Curva de aprendizagem para queries complexas (KQL)
- Metricas de aplicacao podem requerer complemento (Prometheus)

## Notes

- Avaliar complemento com Prometheus/Grafana para metricas detalhadas
- Definir politica de retencao de logs conforme requisitos de compliance
- Estrutura de logs a definir para facilitar correlacao
