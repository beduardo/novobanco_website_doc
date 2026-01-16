---
id: DEF-02-requisitos-nao-funcionais
aliases:
  - Requisitos Não Funcionais
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

# DEF-02: Requisitos Não Funcionais

> **Secção relacionada:** [2 - Contexto de Negócio & Requisitos](../sections/SEC-02-contexto-negocio-requisitos.md)

## Contexto

Os requisitos não funcionais definem os atributos de qualidade da solução HomeBanking web, incluindo performance, segurança, disponibilidade e escalabilidade. Estes requisitos são críticos para um sistema bancário.

## Perguntas a Responder

### Performance
1. Qual é o tempo de resposta máximo aceitável para operações críticas?
    3 segs
2. Qual é o throughput esperado (transações por segundo)?
    10
3. Qual é o tempo máximo de carregamento da página inicial?
    10 segs

### Disponibilidade
4. Qual é o SLA de disponibilidade esperado (ex: 99.9%)?
    99.9%
5. Há janelas de manutenção programadas?
    sim
6. Qual é o RTO (Recovery Time Objective)?
    30min
7. Qual é o RPO (Recovery Point Objective)?
    5 min

### Escalabilidade
8. Qual é o número esperado de utilizadores concorrentes?
    400
9. Qual é a projeção de crescimento para os próximos 3 anos?
    5%
10. Há picos de utilização previstos (ex: fim do mês)?
    Sim

### Segurança
11. Quais certificações de segurança são requeridas?
    Falta aprofundamento
12. Há requisitos específicos de encriptação?
    Falta aprofundamento
13. Qual é a política de retenção de logs?
    Falta aprofundamento

### Compatibilidade
14. Quais browsers devem ser suportados?
    Chrome, Edge e Safari
15. Quais resoluções de ecrã devem ser suportadas?
    Deve ser responsivo
16. Há requisitos de suporte a dispositivos móveis (responsive)?
    Sim

## Decisões

### Performance - Tempos de Resposta
- **Decisão:**
  - Operações críticas: máx 3 segundos
  - Throughput: 10 transações por segundo
  - Carregamento página inicial: máx 10 segundos
- **Justificação:** Valores alinhados com expectativas de utilizadores de serviços bancários online
- **Alternativas consideradas:** Tempos mais agressivos (descartados por viabilidade técnica)

### Disponibilidade - SLAs
- **Decisão:**
  - SLA de disponibilidade: 99.9%
  - RTO (Recovery Time Objective): 30 minutos
  - RPO (Recovery Point Objective): 5 minutos
  - Janelas de manutenção: Sim (programadas)
- **Justificação:** SLAs alinhados com padrões de indústria bancária
- **Alternativas consideradas:** 99.99% (descartado por custo vs benefício)

### Escalabilidade - Capacidade
- **Decisão:**
  - Utilizadores concorrentes: 400
  - Projeção de crescimento: 5% ao ano (3 anos)
  - Picos de utilização: Sim (considerar fim de mês, períodos fiscais)
- **Justificação:** Baseado em projeções de utilização do canal web
- **Alternativas consideradas:** Capacidade superior (pode ser revista conforme demanda)

### Segurança - Certificações
- **Decisão:** _A definir_ - Requer aprofundamento
- **Justificação:** Necessidade de levantar requisitos específicos junto à área de segurança
- **Alternativas consideradas:** ISO 27001, PCI-DSS (referências a considerar)

### Segurança - Encriptação
- **Decisão:** _A definir_ - Requer aprofundamento
- **Justificação:** Necessidade de alinhar com políticas de segurança do banco
- **Alternativas consideradas:** TLS 1.3, AES-256 (referências de indústria)

### Segurança - Retenção de Logs
- **Decisão:** _A definir_ - Requer aprofundamento
- **Justificação:** Necessidade de alinhar com requisitos regulatórios e políticas internas
- **Alternativas consideradas:** 7 anos (requisito típico bancário a validar)

### Compatibilidade - Browsers
- **Decisão:** Suporte a Chrome, Edge e Safari (versões atuais e 2 anteriores)
- **Justificação:** Cobertura dos browsers mais utilizados no mercado português
- **Alternativas consideradas:** Firefox (pode ser adicionado se necessário)

### Compatibilidade - Responsividade
- **Decisão:** Design responsivo com suporte a dispositivos móveis
- **Justificação:** Garantir experiência consistente em diferentes dispositivos e resoluções
- **Alternativas consideradas:** Versão mobile separada (descartado por custo de manutenção)

## Restrições Conhecidas

- Alinhamento com SLAs da infraestrutura existente da app mobile
- Requisitos regulatórios de segurança bancária

## Referências

- [CONTEXT.md](../CONTEXT.md) - Contexto geral do projeto
- SLAs da infraestrutura atual (a fornecer)
- Políticas de segurança do Novo Banco (a fornecer)
