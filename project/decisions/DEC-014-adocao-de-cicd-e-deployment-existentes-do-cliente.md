---
id: "DEC-014"
title: "Adocao de CI/CD e Deployment Existentes do Cliente"
status: "accepted"
created: 2026-04-14
context: "DEF-20"
affects-definitions:
  - "DEF-20"
  - "DEF-24"
affects-sections:
  - "SEC-10"
  - "SEC-14"
---

# DEC-014: Adocao de CI/CD e Deployment Existentes do Cliente

> **Related definitions:** [DEF-20-arquitetura-operacional.md](../definitions/DEF-20-arquitetura-operacional.md), [DEF-24-plano-migracao-implementacao.md](../definitions/DEF-24-plano-migracao-implementacao.md)
> **Related sections:** [SEC-10 - Arquitetura Operacional](../sections/SEC-10-arquitetura-operacional.md), [SEC-14 - Plano de Migracao e Implementacao](../sections/SEC-14-plano-migracao-implementacao.md)
> **Complements:** [DEC-006 - Estrategia de Containers OpenShift](./DEC-006-estrategia-containers-openshift.md)

## Context

O cliente (Best) possui infraestrutura de CI/CD, pipelines e estrategias de deployment ja implementadas e em producao, baseadas em Azure DevOps (Azure Repos + Azure Pipelines) com estrategia de deploy Rolling Update em OpenShift/AKS.

A equipa de desenvolvimento do canal web nao tem mandato para redesenhar ou substituir estas praticas. O cliente define e gere a sua propria plataforma de entrega de software.

## Decision

A equipa **adopta a infra de CI/CD e deployment existente do cliente, sem a redesenhar**. A nossa responsabilidade limita-se a:

- Fornecer artefactos de aplicacao compatíveis com a plataforma existente:
  - `Dockerfile` OpenShift-compliant (utilizador nao-root, portas > 1024, base UBI)
  - Configuracoes de pipeline (YAML para Azure Pipelines) adaptadas ao nosso build/test/deploy
  - `ConfigMaps` e `Secrets` alinhados com o Azure Key Vault do cliente
  - Health check endpoints (`/health/live`, `/health/ready`) para liveness/readiness probes
- Adaptar o nosso processo de desenvolvimento ao GitFlow e branch strategy do cliente
- Respeitar os quality gates definidos pelo cliente (SonarQube, SAST, etc.)

**O que NAO e da nossa responsabilidade:**
- Escolha ou substituicao de ferramentas CI/CD
- Definicao da estrategia de deploy (Rolling Update e do cliente)
- Gestao de ambientes (DEV, UAT, PROD) — e responsabilidade do cliente
- Configuracao de clusters OpenShift/AKS

## Consequences

### Positive
- Menor scope de trabalho: sem necessidade de desenhar ou manter infra CI/CD
- Alinhamento automatico com praticas e compliance do cliente
- Reducao de risco: reutilizacao de infra testada e aprovada em producao
- Onboarding mais rapido: aderimos ao que ja existe

### Negative
- Dependencia das decisoes e timings do cliente para evolucoes de pipeline
- Eventuais restricoes da plataforma podem limitar praticas de desenvolvimento preferidas
- Necessidade de coordenacao com a equipa de DevOps do cliente para integracao inicial

## Notes

- Esta decisao complementa DEC-006 (containers OpenShift-compliant): fornecemos imagens conformes, o cliente integra no seu pipeline
- A nota em DEC-006 "Integracao com pipelines CI/CD a detalhar" fica resolvida por esta decisao: nao detalhamos porque nao somos nos a gerir
- DEF-20 descreve o pipeline existente do cliente como referencia — nao como algo que nos implementamos
