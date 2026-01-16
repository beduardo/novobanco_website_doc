---
id: SEC-11-observabilidade-operacoes
aliases:
  - Observabilidade e Operações
tags:
  - nextreality-novobanco-website-sections
  - sections
  - observability
  - monitoring
  - elk
approved: true
created: 2026-01-08
hubs:
  - "[[nextreality]]"
para-code: R
reviewed: true
status: completed
---

# 11. Observabilidade & Operações

> **Definição:** [DEF-11-observabilidade-operacoes.md](../definitions/DEF-11-observabilidade-operacoes.md)

## Propósito

Definir a estratégia de observabilidade do HomeBanking Web, incluindo stack tecnológica, métricas chave (golden signals), tracing distribuído e abordagem de SLIs/SLOs.

## Conteúdo

### 11.1 Os Três Pilares

| Pilar | Propósito | Ferramenta |
|-------|-----------|------------|
| **Logs** | Eventos e debugging | ELK (Elasticsearch, Logstash, Kibana) |
| **Métricas** | Performance e saúde | Prometheus + Grafana (complemento) |
| **Traces** | Fluxo de requests | Elastic APM |

### 11.2 Stack de Observabilidade

A stack de observabilidade será baseada no **ELK Stack** (Elasticsearch, Logstash, Kibana), reutilizando a infraestrutura existente.

```plantuml
@startuml
skinparam componentStyle rectangle
skinparam backgroundColor white

title Stack de Observabilidade

package "Aplicação" {
  [Frontend SPA] as FE
  [BFF .NET 8] as BFF
}

package "Coleta" {
  [Filebeat] as FB
  [APM Agent] as APM
}

package "ELK Stack" {
  [Logstash] as LS
  [Elasticsearch] as ES
  [Kibana] as KB
}

[ElastAlert] as ALERT

FE --> FB : Logs
BFF --> FB : Logs (Serilog)
BFF --> APM : Traces/Metrics
FB --> LS
APM --> ES
LS --> ES
ES --> KB
ES --> ALERT

@enduml
```

| Componente | Função | Tecnologia |
|------------|--------|------------|
| **Logging** | Logs estruturados JSON | Serilog (.NET), Filebeat |
| **Tracing** | Distributed tracing | Elastic APM |
| **Ingestão** | Coleta e transformação | Logstash |
| **Armazenamento** | Indexação e busca | Elasticsearch |
| **Visualização** | Dashboards | Kibana |
| **Alerting** | Notificações | ElastAlert |

### 11.3 Golden Signals

Os quatro golden signals serão monitorizados conforme melhores práticas SRE:

| Signal | Métrica | Target | Alerta |
|--------|---------|--------|--------|
| **Latency** | P95 response time | < 3s | > 5s |
| **Traffic** | Requests per second | Baseline | > 2x baseline |
| **Errors** | Error rate (5xx) | < 0.1% | > 1% |
| **Saturation** | CPU/Memory usage | < 70% | > 85% |

### 11.4 Logging

Todos os logs serão estruturados em formato JSON com campos padronizados:

#### Campos Obrigatórios

| Campo | Tipo | Descrição |
|-------|------|-----------|
| `timestamp` | ISO8601 | Data/hora UTC do evento |
| `level` | string | DEBUG, INFO, WARN, ERROR, FATAL |
| `service` | string | Nome do componente (frontend-web, bff-web) |
| `correlation_id` | UUID | ID para correlação entre serviços |
| `message` | string | Descrição do evento |
| `environment` | string | dev, qa, prod |

#### Campos Opcionais

| Campo | Tipo | Uso |
|-------|------|-----|
| `user_id` | string | Identificador do utilizador (masked) |
| `session_id` | string | ID da sessão |
| `operation` | string | Tipo de operação |
| `duration_ms` | number | Duração da operação |
| `error_code` | string | Código de erro |

#### Mascaramento de Dados Sensíveis

| Tipo de Dado | Tratamento |
|--------------|------------|
| NIB/IBAN | Mascarar (`PT50****1234`) |
| User ID | Hash ou mascarar |
| Montantes | Mascarar |
| Email | Mascarar (`j***@email.com`) |
| NIF | Mascarar |
| Tokens | Nunca logar |

#### Retenção de Logs

| Tipo de Log | Retenção | Requisito |
|-------------|----------|-----------|
| Logs de autenticação | 7 anos | Compliance bancário |
| Logs de transações | 7 anos | Compliance bancário |
| Logs de erro | 1 ano | Operacional |
| Logs gerais | 90 dias | Operacional |

### 11.5 Tracing Distribuído

| Header | Propósito | Gerado por |
|--------|-----------|------------|
| `X-Correlation-ID` | Correlação de logs | Frontend (UUID) |
| `X-Request-ID` | ID único do request | BFF |
| `traceparent` | W3C Trace Context | APM Agent |

| Componente | Instrumentação |
|------------|----------------|
| Frontend | RUM (Real User Monitoring) JS Agent |
| BFF .NET | Elastic APM .NET Agent |

### 11.6 SLIs / SLOs / SLAs

| Conceito | Definição | Responsável |
|----------|-----------|-------------|
| **SLI** (Indicator) | Métrica que mede o nível de serviço | Engenharia |
| **SLO** (Objective) | Target interno para o SLI | Engenharia |
| **SLA** (Agreement) | Compromisso contratual externo | Negócio |

#### SLOs do Canal Web

| SLI | SLO Target | Janela | Cálculo |
|-----|------------|--------|---------|
| Disponibilidade | 99.9% | Mensal | Uptime / Tempo total |
| Latência P95 | < 3s | Mensal | Percentil 95 dos requests |
| Taxa de Erro | < 0.1% | Mensal | Erros 5xx / Total requests |
| TTFB | < 800ms | Mensal | Time to First Byte P95 |

#### Error Budget

| SLO | Error Budget Mensal |
|-----|---------------------|
| 99.9% | 43.2 minutos |
| 99.95% | 21.6 minutos |
| 99.99% | 4.3 minutos |

### 11.7 Alertas

| Severidade | Critério | Tempo Resposta | Notificação |
|------------|----------|----------------|-------------|
| **P1 - Critical** | Serviço indisponível, impacto total | < 15 min | On-call + SMS |
| **P2 - High** | Degradação significativa | < 30 min | Email + Teams |
| **P3 - Medium** | Degradação parcial | < 4 horas | Email |
| **P4 - Low** | Anomalia sem impacto | Próximo dia útil | Ticket |

#### Alertas Configurados

| Alerta | Condição | Severidade |
|--------|----------|------------|
| Serviço DOWN | Health check falha > 2 min | P1 |
| Error Rate Alto | > 5% erros 5xx | P1 |
| Latência Degradada | P95 > 5s por 5 min | P2 |
| CPU Saturado | > 90% por 10 min | P2 |
| Memory Alto | > 85% por 10 min | P2 |
| Auth Failures Spike | > 10x baseline | P2 |
| Circuit Breaker Open | Estado OPEN | P3 |
| Error Rate Elevado | > 1% erros | P3 |

### 11.8 Dashboards

| Dashboard | Audiência | Conteúdo |
|-----------|-----------|----------|
| **Health Overview** | NOC / On-call | Status geral, alertas ativos, SLO status |
| **Performance** | Engenharia | Latência, throughput, errors por endpoint |
| **Business** | Produto | Logins, transações, conversion rates |
| **Security** | SecOps | Auth failures, suspicious activity |
| **Infrastructure** | DevOps | CPU, memory, pods, network |

### 11.9 Métricas de Negócio

| Métrica | Descrição | Dashboard |
|---------|-----------|-----------|
| Logins/hora | Taxa de autenticações | Business |
| Transações/tipo | Transferências, pagamentos | Business |
| Taxa abandono login | % que não completa login | Business |
| Erros auth | Falhas de autenticação | Security |
| Sessões ativas | Utilizadores online | Operations |

## Decisões Referenciadas

- [DEC-008-stack-observabilidade-elk.md](../decisions/DEC-008-stack-observabilidade-elk.md) - ELK Stack

## Definições Utilizadas

- [DEF-11-observabilidade-operacoes.md](../definitions/DEF-11-observabilidade-operacoes.md) - Detalhes completos
- [DEF-02-requisitos-nao-funcionais.md](../definitions/DEF-02-requisitos-nao-funcionais.md) - SLAs
