---
id: DEF-10-arquitetura-operacional
aliases:
  - Arquitetura Operacional
tags:
  - nextreality-novobanco-website-definitions
  - definitions
  - infrastructure
  - devops
  - cicd
approved: true
created: 2026-01-04
hubs:
  - "[[nextreality]]"
para-code: R
reviewed: true
status: structure
---

# DEF-10: Arquitetura Operacional

> **Secção relacionada:** [10 - Arquitetura Operacional](../sections/SEC-10-arquitetura-operacional.md)

## Contexto

Definir a arquitetura operacional do HomeBanking Web, incluindo infraestrutura, ambientes, pipelines CI/CD, estrategia de deploy, gestao de secrets e disaster recovery. O canal web sera deployado em OpenShift, reutilizando a infraestrutura existente.

## Perguntas a Responder

### Infraestrutura

1. Qual a versao do OpenShift utilizada?
   O Openshit ainda está em homologação por não temos essa informação. O cliente ainda utiliza o AKS mas precisamos já deixar as imagens complaint.

2. Quantos clusters OpenShift existem (producao, DR)?
    Necessita aprofundamento

3. Qual a topologia de rede (DMZ, zonas de seguranca)?
    Necessita aprofundamento

4. Ha load balancer externo? Qual?
    Sim. F5 BIP-IP

### Ambientes

5. Quais ambientes serao provisionados (dev, test, staging, prod)?
    dev, qa, prod

6. Ha ambiente de DR (Disaster Recovery)?
    Não

7. Qual a estrategia de promocao entre ambientes?
    Necessita aprofundamento

8. Ha ambientes efemeros para feature branches?
   Não

### Segregacao

9. Como sao segregados os ambientes (namespaces, clusters)?
   Namespaces

10. Ha segregacao de rede entre ambientes?
    Necessita aprofundamento

11. Quais controlos de acesso existem por ambiente?
    Necessita aprofundamento

### CI/CD Pipelines

12. Qual ferramenta de CI/CD e utilizada (Jenkins, GitLab CI, Azure DevOps)?
    Azure DevOps

13. Onde esta alojado o repositorio de codigo (GitLab, GitHub, Azure Repos)?
    Azure Repos

14. Qual a estrategia de branching (GitFlow, trunk-based)?
    GitFlow

15. Ha quality gates definidos (cobertura, SAST, DAST)?
    Cobertura e SAST

### Estrategia de Deploy

16. Qual a estrategia de deploy (rolling update, blue-green, canary)?
    Rolling Update (com Kubernetes). Zero downtime.

17. Ha deploys automaticos ou requerem aprovacao manual?
    Necessita aprofundamento. Dev/QA automatico, Prod com aprovacao.

18. Sera utilizado sistema de feature flags para rollout gradual?
    Necessita aprofundamento. Beneficios: rollout gradual, kill switch

### Infraestrutura como Codigo (IaC)

19. Qual ferramenta de IaC e utilizada (Terraform, Ansible, Helm)?
    Necessita aprofundamento. Helm para Kubernetes e provavelmente Terraform para Azure.

### Secrets Management

20. Qual ferramenta de gestao de secrets?
    Azure Key Vault

21. Como sao injetados os secrets nos containers?
    Secret Store CSI Driver

22. Qual a politica de rotacao de secrets?
    Necessita aprofundamento

### Container Registry

23. Qual container registry e utilizado?
    Azure Container Registry

24. Ha scanning de vulnerabilidades nas imagens?
    Necessita aprofundamento

### Disaster Recovery (Simplificado)

> **Nota:** RTO/RPO definidos em [DEF-02-requisitos-nao-funcionais.md](DEF-02-requisitos-nao-funcionais.md)

25. Ha site de DR? Onde?
    Necessita aprofundamento

26. Qual a estrategia de failover?
    Necessita aprofundamento

### Backup Strategy

27. Quais componentes do canal web requerem backup?
    Nenhum. Dados sao oriundos do backend com politicas proprias.

### Runbooks (Simplificado)

28. Existem runbooks documentados para operacoes criticas?
    Necessita aprofundamento. Minimo: deploy, rollback, incident response

## Decisões

### Plataforma de Infraestrutura
- **Decisão:** _Pendente_
- **Justificação:** _Pendente_
- **Alternativas consideradas:** _Pendente_

### Estrategia CI/CD
- **Decisão:** _Pendente_
- **Justificação:** _Pendente_
- **Alternativas consideradas:** _Pendente_

### Estrategia de Deploy
- **Decisão:** _Pendente_
- **Justificação:** _Pendente_
- **Alternativas consideradas:** _Pendente_

### Gestão de Secrets
- **Decisão:** _Pendente_
- **Justificação:** _Pendente_
- **Alternativas consideradas:** _Pendente_

### Disaster Recovery
- **Decisão:** _Pendente_
- **Justificação:** _Pendente_
- **Alternativas consideradas:** _Pendente_

## Restrições Conhecidas

- Deploy em OpenShift (decisao ja aceite - DEC-006)
- Stack ELK para observabilidade (decisao ja aceite - DEC-008)
- Disponibilidade 99.9%
- RTO: 30 minutos (referencia DEF-02)
- RPO: 5 minutos (referencia DEF-02)

## Decisões Relacionadas

- [DEC-006-estrategia-containers-openshift.md](../decisions/DEC-006-estrategia-containers-openshift.md) - Estrategia de containers
- [DEC-008-stack-observabilidade-elk.md](../decisions/DEC-008-stack-observabilidade-elk.md) - Stack de observabilidade
- [DEC-010-stack-tecnologica-backend.md](../decisions/DEC-010-stack-tecnologica-backend.md) - Stack tecnologica backend

## Referências

- [DEF-02-requisitos-nao-funcionais.md](DEF-02-requisitos-nao-funcionais.md) - RTO/RPO
- [DEF-03-principios-arquitetura.md](DEF-03-principios-arquitetura.md) - Principios de arquitetura
- OpenShift Documentation
- 12-Factor App Methodology
