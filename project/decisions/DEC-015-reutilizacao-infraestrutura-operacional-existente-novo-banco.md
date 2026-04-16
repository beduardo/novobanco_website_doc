---
id: "DEC-015"
title: "Reutilizacao de Infraestrutura Operacional Existente do Novo Banco"
status: "accepted"
created: 2026-04-16
context: "DEF-20"
affects-definitions:
  - "DEF-20"
  - "DEF-18"
  - "DEF-21"
  - "DEF-22"
affects-sections:
  - "SEC-10"
  - "SEC-11"
  - "SEC-08"
  - "SEC-12"
---

# DEC-015: Reutilizacao de Infraestrutura Operacional Existente do Novo Banco

> **Related definitions:** [DEF-20 - Arquitetura Operacional](../definitions/DEF-20-arquitetura-operacional.md), [DEF-18 - Seguranca e Conformidade](../definitions/DEF-18-seguranca-conformidade.md), [DEF-21 - Observabilidade e Operacoes](../definitions/DEF-21-observabilidade-operacoes.md), [DEF-22 - Desempenho e Fiabilidade](../definitions/DEF-22-desempenho-fiabilidade.md)
> **Related sections:** [SEC-10 - Arquitetura Operacional](../sections/SEC-10-arquitetura-operacional.md), [SEC-11 - Observabilidade e Operacoes](../sections/SEC-11-observabilidade-operacoes.md), [SEC-08 - Seguranca e Conformidade](../sections/SEC-08-seguranca-conformidade.md), [SEC-12 - Desempenho e Fiabilidade](../sections/SEC-12-desempenho-fiabilidade.md)
> **Complements:** [DEC-006 - Estrategia de Containers OpenShift](./DEC-006-estrategia-containers-openshift.md), [DEC-008 - Stack de Observabilidade ELK](./DEC-008-stack-observabilidade-elk.md), [DEC-014 - Adocao de CI/CD e Deployment Existentes do Cliente](./DEC-014-adocao-de-cicd-e-deployment-existentes-do-cliente.md)

## Context

O Novo Banco possui infraestrutura operacional consolidada e em producao, cobrindo as seguintes areas:

- **Deployment e pipelines CI/CD:** Azure DevOps (Azure Repos + Azure Pipelines), com estrategia GitFlow e deploy Rolling Update em OpenShift/AKS (coberto em detalhe por DEC-014)
- **Observabilidade:** Stack ELK (Elasticsearch, Logstash, Kibana) para logs, metricas e auditoria (coberto em detalhe por DEC-008)
- **Seguranca de infraestrutura:** WAF, firewalls, network policies, scanning de vulnerabilidades (Microsoft Defender for Containers), SIEM e controlos de conformidade bancaria
- **Disaster Recovery e continuidade de negocio:** Estrategia de DR, politicas de backup, RTO/RPO e procedimentos de failover definidos e operados pela equipa de infraestrutura do banco

A equipa de desenvolvimento do canal HomeBanking Web nao tem mandato para redesenhar, substituir ou questionar estas plataformas. O Novo Banco define e opera a sua propria infraestrutura operacional.

## Decision

**Toda a infraestrutura de deployment, pipelines, observabilidade e seguranca existente no Novo Banco sera reutilizada pela solucao HomeBanking Web, sem redesenho.**

A responsabilidade da equipa de desenvolvimento limita-se a **adaptar os artefactos do projeto** para conformidade com o que ja esta definido:

### Deployment e CI/CD
- Fornecer `Dockerfile` OpenShift-compliant e configuracoes de pipeline YAML para Azure Pipelines
- Respeitar GitFlow, quality gates e processo de aprovacao para PROD
- (Ver DEC-014 para detalhe)

### Observabilidade
- Instrumentar a aplicacao para emitir logs estruturados consumiveis pelo ELK existente
- Expor metricas e health check endpoints no formato esperado pela plataforma
- Nao instalar ou gerir infraestrutura de observabilidade propria
- (Ver DEC-008 para detalhe)

### Seguranca de Infraestrutura
- Conformar imagens e configuracoes aos requisitos de seguranca do banco (scanning, politicas de rede, RBAC)
- Nao gerir WAF, firewalls, SIEM ou controlos de rede — sao responsabilidade da equipa de seguranca do banco
- Coordenar com SecOps do banco para validacao de conformidade antes de cada deploy em PROD

### Disaster Recovery e Backup
- Adoptar a estrategia de DR e politicas de backup definidas pelo Novo Banco (RTO/RPO documentados em DEF-04/DEF-22)
- Garantir que a aplicacao e stateless, delegando recuperacao de estado ao backend existente com DR proprio
- Adaptar configuracoes de deployment (replicas, health checks, rollback) para estar alinhado com os procedimentos de DR do banco
- Nao definir nem operar infraestrutura de DR propria

**O que NAO e da responsabilidade da equipa:**
- Escolha ou configuracao de solucoes de seguranca de infraestrutura
- Definicao de estrategias de DR ou politicas de backup
- Configuracao de clusters, namespaces ou network policies
- Gestao de ferramentas de observabilidade (ELK, alerting, dashboards operacionais)

## Consequences

### Positive
- Scope claramente delimitado: a equipa foca no desenvolvimento da aplicacao, nao em infraestrutura
- Conformidade automatica com politicas de seguranca e compliance bancario ja aprovadas
- Reutilizacao de infraestrutura testada e em producao, reduzindo risco operacional
- Menor custo e tempo de setup: sem necessidade de provisionar ou manter infraestrutura adicional
- DR e backups garantidos pela plataforma do banco, sem esforco adicional da equipa

### Negative
- Dependencia dos timings e decisoes da equipa de infraestrutura do banco para evolucoes ou ajustes
- Eventuais constrangimentos da plataforma podem limitar praticas de desenvolvimento preferidas
- Necessidade de coordenacao com equipas de Infra, DevOps e SecOps do banco para integracao e validacao

## Notes

- Esta decisao e um principio transversal que enquadra DEC-006, DEC-008 e DEC-014 numa logica de reutilizacao global
- Qualquer necessidade de infraestrutura adicional ou ajuste deve ser negociada com as equipas responsaveis do banco, nao implementada autonomamente
- DEF-20 documenta a infraestrutura existente como referencia — nao como algo que a equipa implementa ou gere
