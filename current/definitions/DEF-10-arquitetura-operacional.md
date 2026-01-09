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

> **Related section:** [10 - Arquitetura Operacional](../sections/SEC-10-arquitetura-operacional.md)

## Context

Definir a arquitetura operacional do HomeBanking Web, incluindo infraestrutura, ambientes, pipelines CI/CD, estrategia de deploy, gestao de secrets e disaster recovery. O canal web sera deployado em OpenShift, reutilizando a infraestrutura existente.

## Questions to Answer

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
    Rolling Update (com Kubernetes)

17. Qual a janela de deploy para producao?
    Necessita aprofundamento

18. Ha deploys automaticos ou requerem aprovacao manual?
    Necessita aprofundamento

19. Qual o tempo maximo de downtime aceitavel durante deploy?
    Necessita aprofundamento

### Infraestrutura como Codigo (IaC)

20. Qual ferramenta de IaC e utilizada (Terraform, Ansible, Helm)?
    Necessita aprofundamento

21. Como sao geridos os templates/charts?
    Necessita aprofundamento

22. Ha versionamento de infraestrutura?
    Necessita aprofundamento

### Secrets Management

23. Qual ferramenta de gestao de secrets (Vault, Azure Key Vault, OpenShift Secrets)?
    Azure Key Vault

24. Como sao injetados os secrets nos containers?
    Usando Secret Store CSI Driver

25. Qual a politica de rotacao de secrets?
    Necessita aprofundamento

### Container Registry

26. Qual container registry e utilizado?
    Azure Container Registry

27. Ha scanning de vulnerabilidades nas imagens?
    Necessita aprofundamento

28. Qual a politica de retencao de imagens?
    Necessita aprofundamento

### Disaster Recovery

29. Qual o RTO (Recovery Time Objective)?
    Necessita aprofundamento

30. Qual o RPO (Recovery Point Objective)?
    Necessita aprofundamento

31. Ha site de DR? Onde?
    Necessita aprofundamento

32. Qual a estrategia de failover (automatico, manual)?
    Necessita aprofundamento

33. Com que frequencia sao testados os procedimentos de DR?
    Necessita aprofundamento

### Backup Strategy

34. Quais componentes requerem backup?
    Os dados acessados pela aplicação são oriundos dos sistemas backend que já possuem políticas de backup

35. Qual a frequencia de backup?
    Não se aplica

36. Onde sao armazenados os backups?
    Não se aplica

37. Qual o periodo de retencao dos backups?
    Não se aplica

### Runbooks

38. Existem runbooks documentados para operacoes comuns?
    Necessita aprofundamento

39. Ha runbooks para incidentes de seguranca?
    Necessita aprofundamento

40. Como sao mantidos e versionados os runbooks?
    Necessita aprofundamento

## Decisions

### Infrastructure Platform
- **Decision:** _Pending_
- **Justification:** _Pending_
- **Alternatives considered:** _Pending_

### CI/CD Strategy
- **Decision:** _Pending_
- **Justification:** _Pending_
- **Alternatives considered:** _Pending_

### Deployment Strategy
- **Decision:** _Pending_
- **Justification:** _Pending_
- **Alternatives considered:** _Pending_

### Secrets Management
- **Decision:** _Pending_
- **Justification:** _Pending_
- **Alternatives considered:** _Pending_

### Disaster Recovery
- **Decision:** _Pending_
- **Justification:** _Pending_
- **Alternatives considered:** _Pending_

## Known Constraints

- Deploy em OpenShift (decisao ja aceite - DEC-006)
- Stack ELK para observabilidade (decisao ja aceite - DEC-008)
- Disponibilidade 99.9%
- RTO: 30 minutos (referencia DEF-02)
- RPO: 5 minutos (referencia DEF-02)

## Related Decisions

- [DEC-006-estrategia-containers-openshift.md](../decisions/DEC-006-estrategia-containers-openshift.md) - Estrategia de containers
- [DEC-008-stack-observabilidade-elk.md](../decisions/DEC-008-stack-observabilidade-elk.md) - Stack de observabilidade
- [DEC-010-stack-tecnologica-backend.md](../decisions/DEC-010-stack-tecnologica-backend.md) - Stack tecnologica backend

## References

- [DEF-02-requisitos-nao-funcionais.md](DEF-02-requisitos-nao-funcionais.md) - RTO/RPO
- [DEF-03-principios-arquitetura.md](DEF-03-principios-arquitetura.md) - Principios de arquitetura
- OpenShift Documentation
- 12-Factor App Methodology
