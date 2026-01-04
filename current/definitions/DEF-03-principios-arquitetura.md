---
id: DEF-03-principios-arquitetura
aliases:
  - Principios de Arquitetura
tags:
  - nextreality-novobanco-website-definitions
  - definitions
  - architecture-principles
approved: true
created: 2026-01-01
hubs:
  - "[[nextreality]]"
para-code: R
reviewed: true
status: completed
---

# DEF-03: Principios de Arquitetura

> **Secao relacionada:** [3 - Visao Geral da Solucao](../sections/SEC-03-visao-geral-solucao.md)

## Contexto

Os principios de arquitetura sao diretrizes fundamentais que guiam todas as decisoes tecnicas do projeto. Para o HomeBanking web, estes principios devem considerar a reutilizacao da infraestrutura existente e as melhores praticas para aplicacoes bancarias.

## Perguntas a Responder

1. A arquitetura deve seguir principios cloud-native?
    A aplicação deve ser orientada a containers complaint com OpenShift

2. Qual e a estrategia de API (API-first, BFF)?
    BFF
    
3. Deve-se priorizar build vs buy para componentes?
    Haverá uma avaliação inicial para alguns componentes, mas o cliente pretende construir caso seja muito caro ou não atenda totalmente

4. Qual e o nivel de acoplamento aceitavel com sistemas legados?
    Somente via BFF

5. Ha principios de seguranca especificos a adotar (zero trust, defense in depth)?
    Podemos avaliar Zero Trust e Defense in Depth. Necessário mais informações.

6. Qual e a estrategia de observabilidade?
    Logs de aplicação e captura de métricas na stack ELK

7. Como sera tratada a resiliencia e tolerancia a falhas?
    Necessário aprofundamento.

8. Ha requisitos de portabilidade entre clouds/ambientes?
    Necessário aprofundamento.

## Decisoes

### Cloud Strategy
- **Decisao:** Arquitetura orientada a containers, compliant com OpenShift
- **Justificacao:** Alinhamento com infraestrutura existente e capacidade de orquestracao enterprise
- **Alternativas consideradas:** VMs tradicionais (descartado por falta de flexibilidade), Kubernetes vanilla (OpenShift oferece mais features enterprise)

### API Strategy
- **Decisao:** Backend for Frontend (BFF) como padrao de integracao
- **Justificacao:**
  - Desacoplamento entre frontend web e servicos backend
  - Camada de agregacao e transformacao especifica para o canal web
  - Isolamento de sistemas legados
- **Alternativas consideradas:** API-first direto (descartado por expor complexidade do backend ao frontend)

### Build vs Buy
- **Decisao:** Avaliacao caso a caso com preferencia por Build
- **Justificacao:** Cliente pretende construir componentes quando:
  - Solucoes de mercado forem muito caras
  - Solucoes existentes nao atenderem totalmente aos requisitos
- **Alternativas consideradas:** Buy-first (descartado por potencial custo e limitacoes)

### Acoplamento com Legados
- **Decisao:** Acoplamento exclusivamente via BFF
- **Justificacao:** Isolamento do frontend de complexidades e mudancas nos sistemas legados
- **Alternativas consideradas:** Integracao direta (descartado por criar dependencias frageis)

### Security Principles
- **Decisao:** _A definir_ - Avaliar Zero Trust e Defense in Depth
- **Justificacao:** Necessidade de mais informacoes sobre requisitos especificos de seguranca
- **Alternativas consideradas:** Zero Trust, Defense in Depth (ambos em avaliacao)

### Resilience Strategy
- **Decisao:** _A definir_ - Necessita aprofundamento
- **Justificacao:** Dependente de definicao de SLAs e requisitos de disponibilidade
- **Alternativas consideradas:** Circuit breaker, Retry patterns, Bulkhead (a avaliar)

### Portability Strategy
- **Decisao:** _A definir_ - Necessita aprofundamento
- **Justificacao:** Verificar se ha requisitos de multi-cloud ou migracao futura
- **Alternativas consideradas:** Container-based portability via OpenShift (baseline)

### Observability Strategy
- **Decisao:** Stack ELK para logs de aplicacao e captura de metricas
- **Justificacao:** Centralizacao de logs e metricas para monitorizacao e troubleshooting
- **Alternativas consideradas:** Prometheus/Grafana (pode complementar ELK para metricas)

## Restricoes Conhecidas

- Reutilizacao da infraestrutura e servicos da app mobile nativa
- Alinhamento com standards de arquitetura do Novo Banco (se existirem)

## Referencias

- [CONTEXT.md](../CONTEXT.md) - Contexto geral do projeto
- Standards de arquitetura institucional (a fornecer)
- TOGAF, C4 Model, 12-Factor App (referencias de industria)
