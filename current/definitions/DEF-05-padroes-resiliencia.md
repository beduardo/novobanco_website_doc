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

### Circuit Breaker
1. Sera implementado Circuit Breaker? Qual biblioteca?
2. Quais serao os thresholds de abertura do circuito?
3. Qual sera o tempo de recuperacao?

### Retry
4. Qual sera a politica de retry (exponential backoff)?
    Exponential backoff
5. Quantas tentativas antes de falhar?
    3
6. Quais erros sao elegiceis para retry?
    Error de timeout ou rate limit.

### Timeout
7. Quais serao os timeouts padrao para chamadas?
    60segs.

8. Ha operacoes com timeouts diferenciados?
    Não

### Bulkhead
9. Sera implementado isolamento de recursos (Bulkhead)?
    Não
10. Como serao isolados os diferentes servicos?
    Não haverá bulkhead.

### Fallback
11. Quais operacoes terao fallback?
    Autenticação.

12. Qual sera o comportamento em modo degradado?
    Utilização do fluxo mais resiliente.

### Rate Limiting
13. Quais limites de rate serao aplicados?
    Ainda não definido.

14. Como sera comunicado ao utilizador quando atingir limites?
    Mensagem de erro informando que é necessário aguardar.

### Health Checks
15. Quais health checks serao implementados (liveness, readiness)?
    Ambos.

16. Qual sera a frequencia de verificacao?
    Ainda não definido.

## Decisoes

### Circuit Breaker
- **Decisao:** _A definir_ - Perguntas pendentes (biblioteca, thresholds, tempo de recuperacao)
- **Justificacao:** Necessita definicao de parametros
- **Alternativas consideradas:** Polly (.NET), Resilience4j

### Retry Policy
- **Decisao:**
  - Estrategia: Exponential backoff
  - Tentativas: 3
  - Erros elegiveis: Timeout, Rate limit
- **Justificacao:** Recuperacao automatica de falhas transitorias
- **Alternativas consideradas:** Fixed delay, Linear backoff

### Timeout Strategy
- **Decisao:** Timeout padrao de 60 segundos para todas as chamadas
- **Justificacao:** Valor conservador para operacoes bancarias
- **Alternativas consideradas:** Timeouts diferenciados (descartado por simplicidade)

### Bulkhead
- **Decisao:** Nao sera implementado
- **Justificacao:** Complexidade vs beneficio para escala atual
- **Alternativas consideradas:** Thread pool isolation, Semaphore isolation

### Fallback Strategy
- **Decisao:**
  - Operacoes com fallback: Autenticacao
  - Comportamento degradado: Utilizacao do fluxo mais resiliente
- **Justificacao:** Garantir disponibilidade minima para operacoes criticas
- **Alternativas consideradas:** Fallback para todas operacoes (descartado por complexidade)

### Rate Limiting
- **Decisao:**
  - Limites: _A definir_
  - Comunicacao ao utilizador: Mensagem de erro informando necessidade de aguardar
- **Justificacao:** Rate limiting gerido pelo Gateway, BFF apenas comunica
- **Alternativas consideradas:** Rate limiting no BFF (descartado - responsabilidade do Gateway)

### Health Checks
- **Decisao:**
  - Tipos: Liveness e Readiness
  - Frequencia: _A definir_
- **Justificacao:** Integracao nativa com OpenShift para orquestracao
- **Alternativas consideradas:** Apenas liveness (descartado por funcionalidade limitada)

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
