---
id: DEF-02-requisitos-nao-funcionais
aliases:
  - Requisitos Nao Funcionais
tags:
  - nextreality-novobanco-website-definitions
  - definitions
  - non-functional-requirements
  - nfr
approved: true
created: 2026-01-01
hubs:
  - "[[nextreality]]"
para-code: R
reviewed: true
status: completed
---

# DEF-02: Requisitos Nao Funcionais

> **Secao relacionada:** [2 - Contexto de Negocio & Requisitos](../sections/SEC-02-contexto-negocio-requisitos.md)

## Contexto

Os requisitos nao funcionais definem os atributos de qualidade da solucao HomeBanking web, incluindo performance, seguranca, disponibilidade e escalabilidade. Estes requisitos sao criticos para um sistema bancario.

## Perguntas a Responder

### Performance
1. Qual e o tempo de resposta maximo aceitavel para operacoes criticas?
    3 segs
2. Qual e o throughput esperado (transacoes por segundo)?
    10
3. Qual e o tempo maximo de carregamento da pagina inicial?
    10 segs

### Disponibilidade
4. Qual e o SLA de disponibilidade esperado (ex: 99.9%)?
    99.9%
5. Ha janelas de manutencao programadas?
    sim
6. Qual e o RTO (Recovery Time Objective)?
    30min
7. Qual e o RPO (Recovery Point Objective)?
    5 min

### Escalabilidade
8. Qual e o numero esperado de utilizadores concorrentes?
    400
9. Qual e a projecao de crescimento para os proximos 3 anos?
    5%
10. Ha picos de utilizacao previstos (ex: fim do mes)?
    Sim

### Seguranca
11. Quais certificacoes de seguranca sao requeridas?
    Falta aprofundamento
12. Ha requisitos especificos de encriptacao?
    Falta aprofundamento
13. Qual e a politica de retencao de logs?
    Falta aprofundamento

### Compatibilidade
14. Quais browsers devem ser suportados?
    Chrome, Edge e Safari
15. Quais resolucoes de ecra devem ser suportadas?
    Deve ser responsivo
16. Ha requisitos de suporte a dispositivos moveis (responsive)?
    Sim

## Decisoes

### Performance - Tempos de Resposta
- **Decisao:**
  - Operacoes criticas: max 3 segundos
  - Throughput: 10 transacoes por segundo
  - Carregamento pagina inicial: max 10 segundos
- **Justificacao:** Valores alinhados com expectativas de utilizadores de servicos bancarios online
- **Alternativas consideradas:** Tempos mais agressivos (descartados por viabilidade tecnica)

### Disponibilidade - SLAs
- **Decisao:**
  - SLA de disponibilidade: 99.9%
  - RTO (Recovery Time Objective): 30 minutos
  - RPO (Recovery Point Objective): 5 minutos
  - Janelas de manutencao: Sim (programadas)
- **Justificacao:** SLAs alinhados com padroes de industria bancaria
- **Alternativas consideradas:** 99.99% (descartado por custo vs beneficio)

### Escalabilidade - Capacidade
- **Decisao:**
  - Utilizadores concorrentes: 400
  - Projecao de crescimento: 5% ao ano (3 anos)
  - Picos de utilizacao: Sim (considerar fim de mes, periodos fiscais)
- **Justificacao:** Baseado em projecoes de utilizacao do canal web
- **Alternativas consideradas:** Capacidade superior (pode ser revista conforme demanda)

### Seguranca - Certificacoes
- **Decisao:** _A definir_ - Requer aprofundamento
- **Justificacao:** Necessidade de levantar requisitos especificos junto a area de seguranca
- **Alternativas consideradas:** ISO 27001, PCI-DSS (referencias a considerar)

### Seguranca - Encriptacao
- **Decisao:** _A definir_ - Requer aprofundamento
- **Justificacao:** Necessidade de alinhar com politicas de seguranca do banco
- **Alternativas consideradas:** TLS 1.3, AES-256 (referencias de industria)

### Seguranca - Retencao de Logs
- **Decisao:** _A definir_ - Requer aprofundamento
- **Justificacao:** Necessidade de alinhar com requisitos regulatorios e politicas internas
- **Alternativas consideradas:** 7 anos (requisito tipico bancario a validar)

### Compatibilidade - Browsers
- **Decisao:** Suporte a Chrome, Edge e Safari (versoes atuais e 2 anteriores)
- **Justificacao:** Cobertura dos browsers mais utilizados no mercado portugues
- **Alternativas consideradas:** Firefox (pode ser adicionado se necessario)

### Compatibilidade - Responsividade
- **Decisao:** Design responsivo com suporte a dispositivos moveis
- **Justificacao:** Garantir experiencia consistente em diferentes dispositivos e resolucoes
- **Alternativas consideradas:** Versao mobile separada (descartado por custo de manutencao)

## Restricoes Conhecidas

- Alinhamento com SLAs da infraestrutura existente da app mobile
- Requisitos regulatorios de seguranca bancaria

## Referencias

- [CONTEXT.md](../CONTEXT.md) - Contexto geral do projeto
- SLAs da infraestrutura atual (a fornecer)
- Politicas de seguranca do Novo Banco (a fornecer)
