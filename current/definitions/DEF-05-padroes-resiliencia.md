---
id: DEF-05-padroes-resiliencia
aliases:
  - Padroes de Resiliencia
tags:
  - nextreality-novobanco-website-definitions
  - definitions
  - resilience
  - patterns
approved: true
created: 2026-01-03
hubs:
  - "[[nextreality]]"
para-code: R
reviewed: true
status: completed
---

# DEF-05: Padroes de Resiliencia

> **Secao relacionada:** [5 - Arquitetura Backend & Servicos](../sections/SEC-05-arquitetura-backend-servicos.md)

## Contexto

Definir os padroes de resiliencia e tolerancia a falhas para o HomeBanking Web, garantindo disponibilidade e experiencia do utilizador mesmo em cenarios de degradacao.

## Perguntas a Responder

> **Nota:** Esta e a definicao principal para padroes de resiliencia do projeto.
> Rate limiting detalhado esta no API Gateway, nao no BFF.

### Circuit Breaker (Consolidado)
1. Sera implementado Circuit Breaker? Qual biblioteca?
    Necessita aprofundamento. Proposta: Polly (.NET)

2. Quais serao os thresholds de abertura do circuito?
    Necessita aprofundamento. Sugestao: 50% de falhas em janela de 10s

3. Qual sera o tempo de recuperacao (half-open)?
    Necessita aprofundamento. Sugestao: 30 segundos

### Retry (Consolidado)
4. Qual sera a politica de retry?
    Exponential backoff

5. Quantas tentativas antes de falhar?
    3 tentativas

6. Quais erros sao elegiveis para retry?
    Timeout, Rate limit (429), erros transientes (5xx)

### Timeout
7. Quais serao os timeouts padrao para chamadas?
    60 segundos

### Fallback
8. Quais operacoes terao fallback?
    Autenticacao (fluxo alternativo OTP se App falhar)

9. Qual sera o comportamento em modo degradado?
    Utilizacao do fluxo mais resiliente disponivel

### Health Checks
10. Quais health checks serao implementados?
    Liveness e Readiness probes (Kubernetes/OpenShift)

11. Qual sera a frequencia de verificacao?
    Necessita aprofundamento. Sugestao: Liveness 10s, Readiness 5s

## Decisoes

### Circuit Breaker
- **Decisao:** Polly (.NET) como biblioteca (a confirmar)
- **Justificacao:** Integracao nativa com .NET, suporte a politicas compostas

### Retry Policy
- **Decisao:** Exponential backoff, 3 tentativas, erros transientes
- **Justificacao:** Recuperacao automatica de falhas transitorias

### Timeout Strategy
- **Decisao:** Timeout padrao de 60 segundos
- **Justificacao:** Valor conservador para operacoes bancarias

### Fallback Strategy
- **Decisao:** Autenticacao com fallback para OTP
- **Justificacao:** Garantir disponibilidade para operacao critica

### Health Checks
- **Decisao:** Liveness e Readiness probes
- **Justificacao:** Integracao nativa com OpenShift/Kubernetes

## Restricoes Conhecidas

- SLA de disponibilidade: 99.9%
- RTO: 30 minutos
- RPO: 5 minutos
- Deploy em OpenShift (suporte a health checks nativo)

## Decisoes Relacionadas

- [DEC-007-padrao-bff.md](../decisions/DEC-007-padrao-bff.md) - Padrao BFF (resiliencia do BFF)
- [DEC-010-stack-tecnologica-backend.md](../decisions/DEC-010-stack-tecnologica-backend.md) - Stack tecnologica backend

## Referencias

- [DEF-02-requisitos-nao-funcionais.md](DEF-02-requisitos-nao-funcionais.md) - SLAs
- [DEF-03-principios-arquitetura.md](DEF-03-principios-arquitetura.md) - Resiliencia (a definir)
- Release It! (Michael Nygard)
- Resilience4j / Polly documentation
