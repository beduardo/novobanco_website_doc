---
id: "DEC-025"
title: "Parâmetros Operacionais de Plataforma Definidos pelo Banco"
status: "accepted"
created: 2026-04-18
context: "DEF-22"
affects-definitions:
  - "DEF-22"
affects-sections:
  - "SEC-12"
---

# DEC-025: Parâmetros Operacionais de Plataforma Definidos pelo Banco

## Context

A plataforma OpenShift do Novo Banco (DEC-006, DEC-015) tem configurações e políticas próprias para a operação de workloads: limites de recursos por pod, parâmetros de auto-scaling, budgets de disrupção e ferramentas de load testing aprovadas. Definir estes parâmetros unilateralmente no documento de arquitectura sem validação com a equipa de infraestrutura resultaria em configurações que podem não ser compatíveis com as políticas da plataforma existente.

## Decision

Os parâmetros operacionais de plataforma abaixo **são definidos e validados pela equipa de infraestrutura do Novo Banco**, não pela equipa de desenvolvimento:

- **Auto-scaling (HPA):** min/max réplicas, targets de CPU e memória, janelas de estabilização de scale-up e scale-down por componente.
- **Capacity Planning:** resource requests e limits (CPU e memória) por container/pod.
- **Pod Disruption Budget (PDB):** política de `minAvailable` por deployment.
- **Load Testing:** ferramentas aprovadas, cenários obrigatórios, critérios de aceitação e integração com pipeline.

A equipa de desenvolvimento adapta os artefactos da aplicação (Deployment YAML, health checks, endpoints de métricas) para conformidade com os parâmetros definidos pelo banco, mas não define esses parâmetros.

## Consequences

### Positive
- Conformidade garantida com políticas de quota, RBAC e SLAs da plataforma OpenShift do banco.
- Eliminação de risco de incompatibilidade entre os parâmetros propostos e os limites de namespace reais.
- Scope da equipa de desenvolvimento claramente delimitado: implementar a aplicação, não configurar a plataforma.

### Negative
- A equipa depende dos timings da equipa de infraestrutura para obter os parâmetros finais.
- O documento não pode especificar valores concretos nestas áreas até validação com o banco.
- Sessão de onboarding técnico com a equipa de infraestrutura é necessária antes do primeiro deploy.
