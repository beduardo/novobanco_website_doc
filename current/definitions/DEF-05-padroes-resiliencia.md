---
id: DEF-05-padroes-resiliencia
aliases:
  - Padrões de Resiliência
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

# DEF-05: Padrões de Resiliência

> **Secção relacionada:** [5 - Arquitetura Backend & Serviços](../sections/SEC-05-arquitetura-backend-servicos.md)

## Contexto

Definir os padrões de resiliência e tolerância a falhas para o HomeBanking Web, garantindo disponibilidade e experiência do utilizador mesmo em cenários de degradação.

## Perguntas a Responder

> **Nota:** Esta é a definição principal para padrões de resiliência do projeto.
> Rate limiting detalhado está no API Gateway, não no BFF.

### Circuit Breaker (Consolidado)
1. Será implementado Circuit Breaker? Qual biblioteca?
    Necessita aprofundamento. Proposta: Polly (.NET)

2. Quais serão os thresholds de abertura do circuito?
    Necessita aprofundamento. Sugestão: 50% de falhas em janela de 10s

3. Qual será o tempo de recuperação (half-open)?
    Necessita aprofundamento. Sugestão: 30 segundos

### Retry (Consolidado)
4. Qual será a política de retry?
    Exponential backoff

5. Quantas tentativas antes de falhar?
    3 tentativas

6. Quais erros são elegíveis para retry?
    Timeout, Rate limit (429), erros transientes (5xx)

### Timeout
7. Quais serão os timeouts padrão para chamadas?
    60 segundos

### Fallback
8. Quais operações terão fallback?
    Autenticação (fluxo alternativo OTP se App falhar)

9. Qual será o comportamento em modo degradado?
    Utilização do fluxo mais resiliente disponível

### Health Checks
10. Quais health checks serão implementados?
    Liveness e Readiness probes (Kubernetes/OpenShift)

11. Qual será a frequência de verificação?
    Necessita aprofundamento. Sugestão: Liveness 10s, Readiness 5s

## Decisões

### Circuit Breaker
- **Decisão:** Polly (.NET) como biblioteca (a confirmar)
- **Justificação:** Integração nativa com .NET, suporte a políticas compostas

### Retry Policy
- **Decisão:** Exponential backoff, 3 tentativas, erros transientes
- **Justificação:** Recuperação automática de falhas transitórias

### Timeout Strategy
- **Decisão:** Timeout padrão de 60 segundos
- **Justificação:** Valor conservador para operações bancárias

### Fallback Strategy
- **Decisão:** Autenticação com fallback para OTP
- **Justificação:** Garantir disponibilidade para operação crítica

### Health Checks
- **Decisão:** Liveness e Readiness probes
- **Justificação:** Integração nativa com OpenShift/Kubernetes

## Restrições Conhecidas

- SLA de disponibilidade: 99.9%
- RTO: 30 minutos
- RPO: 5 minutos
- Deploy em OpenShift (suporte a health checks nativo)

## Decisões Relacionadas

- [DEC-007-padrao-bff.md](../decisions/DEC-007-padrao-bff.md) - Padrão BFF (resiliência do BFF)
- [DEC-010-stack-tecnologica-backend.md](../decisions/DEC-010-stack-tecnologica-backend.md) - Stack tecnológica backend

## Referências

- [DEF-02-requisitos-nao-funcionais.md](DEF-02-requisitos-nao-funcionais.md) - SLAs
- [DEF-03-principios-arquitetura.md](DEF-03-principios-arquitetura.md) - Resiliência (a definir)
- Release It! (Michael Nygard)
- Resilience4j / Polly documentation
