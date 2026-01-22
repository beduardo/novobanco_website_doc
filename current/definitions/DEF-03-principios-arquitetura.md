---
id: DEF-03-principios-arquitetura
aliases:
  - Princípios de Arquitetura
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

# DEF-03: Princípios de Arquitetura

> **Secção relacionada:** [3 - Visão Geral da Solução](../sections/SEC-03-visao-geral-solucao.md)

## Contexto

Os princípios de arquitetura são diretrizes fundamentais que guiam todas as decisões técnicas do projeto. Para o HomeBanking web, estes princípios devem considerar a reutilização da infraestrutura existente e as melhores práticas para aplicações bancárias.

## Perguntas a Responder

1. A arquitetura deve seguir princípios cloud-native?
    A aplicação deve ser orientada a containers compliant com OpenShift

2. Qual é a estratégia de API (API-first, BFF)?
    BFF

3. Deve-se priorizar build vs buy para componentes?
    Haverá uma avaliação inicial para alguns componentes, mas o cliente pretende construir caso seja muito caro ou não atenda totalmente

4. Qual é o nível de acoplamento aceitável com sistemas legados?
    Somente via BFF

5. Há princípios de segurança específicos a adotar (zero trust, defense in depth)?
    Podemos avaliar Zero Trust e Defense in Depth. Necessário mais informações.

6. Qual é a estratégia de observabilidade?
    Logs de aplicação e captura de métricas na stack ELK

7. Como será tratada a resiliência e tolerância a falhas?
    Necessário aprofundamento.

8. Há requisitos de portabilidade entre clouds/ambientes?
    Necessário aprofundamento.

## Decisões

### Cloud Strategy
- **Decisão:** Arquitetura orientada a containers, compliant com OpenShift
- **Justificação:** Alinhamento com infraestrutura existente e capacidade de orquestração enterprise
- **Alternativas consideradas:** VMs tradicionais (descartado por falta de flexibilidade), Kubernetes vanilla (OpenShift oferece mais features enterprise)

### API Strategy
- **Decisão:** Backend for Frontend (BFF) como padrão de integração
- **Justificação:**
  - Desacoplamento entre frontend web e serviços backend
  - Camada de agregação e transformação específica para o canal web
  - Isolamento de sistemas legados
- **Alternativas consideradas:** API-first direto (descartado por expor complexidade do backend ao frontend)

### Build vs Buy
- **Decisão:** Avaliação caso a caso com preferência por Build
- **Justificação:** Cliente pretende construir componentes quando:
  - Soluções de mercado forem muito caras
  - Soluções existentes não atenderem totalmente aos requisitos
- **Alternativas consideradas:** Buy-first (descartado por potencial custo e limitações)

### Acoplamento com Legados
- **Decisão:** Acoplamento exclusivamente via BFF
- **Justificação:** Isolamento do frontend de complexidades e mudanças nos sistemas legados
- **Alternativas consideradas:** Integração direta (descartado por criar dependências frágeis)

### Security Principles
- **Decisão:** _A definir_ - Avaliar Zero Trust e Defense in Depth
- **Justificação:** Necessidade de mais informações sobre requisitos específicos de segurança
- **Alternativas consideradas:** Zero Trust, Defense in Depth (ambos em avaliação)

### Resilience Strategy
- **Decisão:** _A definir_ - Necessita aprofundamento
- **Justificação:** Dependente de definição de SLAs e requisitos de disponibilidade
- **Alternativas consideradas:** Circuit breaker, Retry patterns, Bulkhead (a avaliar)

### Portability Strategy
- **Decisão:** _A definir_ - Necessita aprofundamento
- **Justificação:** Verificar se há requisitos de multi-cloud ou migração futura
- **Alternativas consideradas:** Container-based portability via OpenShift (baseline)

### Observability Strategy
- **Decisão:** Stack ELK para logs de aplicação e captura de métricas
- **Justificação:** Centralização de logs e métricas para monitorização e troubleshooting
- **Alternativas consideradas:** Prometheus/Grafana (pode complementar ELK para métricas)

## Restrições Conhecidas

- Reutilização da infraestrutura e serviços da app mobile nativa
- Alinhamento com standards de arquitetura do Novo Banco (se existirem)

## Decisões Relacionadas

- [DEC-004-controlos-seguranca-frontend.md](../decisions/DEC-004-controlos-seguranca-frontend.md) - Controlos de segurança frontend
- [DEC-006-estrategia-containers-openshift.md](../decisions/DEC-006-estrategia-containers-openshift.md) - Estratégia de containers
- [DEC-007-padrao-bff.md](../decisions/DEC-007-padrao-bff.md) - Padrão BFF
- [DEC-008-stack-observabilidade-elk.md](../decisions/DEC-008-stack-observabilidade-elk.md) - Stack de observabilidade

## Referências

- [CONTEXT.md](../CONTEXT.md) - Contexto geral do projeto
- Standards de arquitetura institucional (a fornecer)
- TOGAF, C4 Model, 12-Factor App (referências de indústria)
