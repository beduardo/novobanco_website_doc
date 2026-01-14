---
id: DEF-11-observabilidade-operacoes
aliases:
  - Observabilidade e Operacoes
tags:
  - nextreality-novobanco-website-definitions
  - definitions
  - observability
  - monitoring
  - logging
  - alerting
approved: true
created: 2026-01-08
hubs:
  - "[[nextreality]]"
para-code: R
reviewed: true
status: structure
---

# DEF-11: Observabilidade & Operacoes

> **Secção relacionada:** [11 - Observabilidade & Operacoes](../sections/SEC-11-observabilidade-operacoes.md)

## Contexto

Definir a estrategia de observabilidade do HomeBanking Web, incluindo logging centralizado, metricas, tracing distribuido, alertas e dashboards operacionais. A stack ELK ja foi definida como base (DEC-008).

## Perguntas a Responder

### Stack de Observabilidade

1. A stack ELK existente sera reutilizada ou ha instancia dedicada?
    Necessita aprofundamento

2. Ha complemento com Prometheus/Grafana para metricas?
    Necessita aprofundamento

### Golden Signals

3. Quais metricas golden signals serao monitorizadas?
    Minimo: Latency (P95, P99), Traffic (RPS), Errors (%), Saturation (CPU/Mem)

4. Quais sao os thresholds aceitaveis?
    Baseados em DEF-02-requisitos-nao-funcionais (3s operacoes, 99.9% disponibilidade)

### Metricas de Negocio

5. Quais metricas de negocio devem ser capturadas?
    Necessita aprofundamento. Sugestao: logins/hora, transacoes/tipo, erros auth

### Distributed Tracing

6. Sera implementado tracing distribuido?
    Necessita aprofundamento. Essencial para debugging em arquitetura distribuida.

7. Como sera feita a correlacao entre Frontend e BFF?
    Necessita aprofundamento. Sugestao: correlation-id em headers

### Logging Centralizado (Consolidado)

> **Nota:** Esta e a definicao principal para politica de logs do projeto.

8. Qual o formato de logs?
    JSON estruturado. Facilita parsing e queries.

9. Quais campos sao obrigatorios em cada log entry?
    Necessita aprofundamento. Sugestao: timestamp, level, correlation-id, service, message

10. Qual a politica de retencao de logs?
    Necessita aprofundamento. Sugestao: 30 dias hot, 1 ano cold, 7 anos auditoria

11. Ha requisitos de mascaramento de dados sensiveis?
    Sim. PII e dados bancarios devem ser mascarados.

### SLIs/SLOs (Simplificado)

> **Nota:** SLAs de negocio em [DEF-02-requisitos-nao-funcionais.md](DEF-02-requisitos-nao-funcionais.md)

12. Quais SLOs target para o canal web?
    Disponibilidade: 99.9%, Latencia P95: < 3s, Taxa erro: < 0.1%

### Alertas e Dashboards (Simplificado)

13. Qual a ferramenta de alerting?
    Necessita aprofundamento

14. Quais dashboards operacionais sao necessarios?
    Necessita aprofundamento. Minimo: health overview, performance, errors

## Decisões

### Stack de Observabilidade
- **Decisão:** ELK Stack (DEC-008 aceite)
- **Justificação:** Reutilizacao de infraestrutura existente
- **Alternativas consideradas:** Prometheus/Grafana, Datadog, Jaeger+Loki

### Tracing Distribuido
- **Decisão:** _Pendente_
- **Justificação:** _Pendente_
- **Alternativas consideradas:** _Pendente_

### Alerting
- **Decisão:** _Pendente_
- **Justificação:** _Pendente_
- **Alternativas consideradas:** _Pendente_

### SLOs
- **Decisão:** _Pendente_
- **Justificação:** _Pendente_
- **Alternativas consideradas:** _Pendente_

## Restrições Conhecidas

- Stack ELK como base (DEC-008)
- Requisitos de auditoria bancaria
- Retenção de logs conforme compliance
- Mascaramento de dados sensiveis (PII)

## Decisões Relacionadas

- [DEC-008-stack-observabilidade-elk.md](../decisions/DEC-008-stack-observabilidade-elk.md) - Stack de observabilidade

## Referências

- [DEF-02-requisitos-nao-funcionais.md](DEF-02-requisitos-nao-funcionais.md) - SLAs
- [DEF-10-arquitetura-operacional.md](DEF-10-arquitetura-operacional.md) - Infraestrutura
- Google SRE Book - SLIs/SLOs
- OpenTelemetry Specification
