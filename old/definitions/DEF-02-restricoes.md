---
id: DEF-02-restricoes
aliases:
  - Novo Banco Restricoes
tags:
  - nextreality-novobanco-website-definitions
approved: true
created: 2025-12-22
hubs:
  - "[[nextreality]]"
para-code: R
reviewed: true
---
# DEF-02: Restricoes Tecnicas e de Negocio

> **Status:** em-progresso
> **Secao relacionada:** 02 - Contexto de Negocio & Requisitos

## Contexto

Este documento documenta todas as restricoes tecnicas, de negocio, regulatorias e organizacionais que condicionam as decisoes arquiteturais do projeto.

## Questoes a Responder

1. Quais restricoes de stack tecnologica existem (alem de React + C#)?
R.: Kubernetes (OpenShift compliant mas com deployment em AKS em primeira fase)

2. Existem restricoes de fornecedores/vendors obrigatorios?
R.: Azure

3. Quais restricoes de infraestrutura (on-prem vs cloud)?
R.: Cloud

4. Existem restricoes de integracao com sistemas legados?
R.: Sim. Devemos utilizar Siebel e outras dependências já utilizadas pelo App Mobile.

5. Quais restricoes regulatorias alem de PSD2/RGPD?
R.: Somente PSD2 e RGPD.

6. Existem restricoes de orcamento?
R.: Não.

7. Existem restricoes de prazo/timeline?
R.: Não.

8. Quais restricoes de equipa (skills, dimensao)?
R.: Não.

9. Existem restricoes de seguranca especificas do banco?
R.: Não.

10. Quais restricoes de compatibilidade com App Mobile?
R.: A Autenticacao de ambas as soluções possuem vínculos. O site precisa utilizar o mesmo modelo de token e passar por uma autorização via App/OTP para que se garanta que o cliente que utiliza o site possui app e conta vinculados.

## Restricoes por Categoria

### Restricoes Tecnologicas

| ID | Restricao | Descricao | Impacto | Flexibilidade |
|----|-----------|-----------|---------|---------------|
| RST-TEC-001 | Frontend React | Stack frontend definida como React | Alto | Nenhuma |
| RST-TEC-002 | Backend C# (.NET) | Stack backend definida como C# | Alto | Nenhuma |
| RST-TEC-003 | Padrao BFF | Arquitetura Backend-for-Frontend | Alto | Nenhuma |
| RST-TEC-004 | OAuth compativel | Mesmo modelo de token do App Mobile + autorizacao via App/OTP | Alto | Nenhuma |
| RST-TEC-005 | Kubernetes | OpenShift compliant, deployment inicial em AKS | Alto | Baixa |

### Restricoes de Integracao

| ID | Restricao | Descricao | Impacto | Flexibilidade |
|----|-----------|-----------|---------|---------------|
| RST-INT-001 | Core Banking Oracle | Integracao com BB Core Banking | Alto | Nenhuma |
| RST-INT-002 | Siebel IBM | Utilizacao obrigatoria do Siebel (dependencia do App Mobile) | Alto | Nenhuma |
| RST-INT-003 | Dependencias App Mobile | Reutilizacao de todas as dependencias ja utilizadas pelo App | Alto | Nenhuma |
| RST-INT-004 | API Gateway existente | Reutilizacao do gateway | Medio | Baixa |

### Restricoes de Infraestrutura

| ID | Restricao | Descricao | Impacto | Flexibilidade |
|----|-----------|-----------|---------|---------------|
| RST-INF-001 | Cloud-only | Infraestrutura 100% cloud (sem on-premises) | Alto | Nenhuma |
| RST-INF-002 | Azure | Microsoft Azure como cloud provider obrigatorio | Alto | Nenhuma |
| RST-INF-003 | AKS | Azure Kubernetes Service para orquestracao de containers | Alto | Nenhuma |
| RST-INF-004 | Data residency | Dados em Portugal/UE | Alto | Nenhuma |

### Restricoes Regulatorias

| ID | Restricao | Descricao | Impacto | Flexibilidade |
|----|-----------|-----------|---------|---------------|
| RST-REG-001 | PSD2 SCA | Strong Customer Authentication | Alto | Nenhuma |
| RST-REG-002 | RGPD | Protecao de dados pessoais | Alto | Nenhuma |

### Restricoes de Negocio

| ID | Restricao | Descricao | Impacto | Flexibilidade |
|----|-----------|-----------|---------|---------------|
| RST-BIZ-001 | Paridade App Mobile | Todas funcionalidades do App devem estar no Website | Alto | Nenhuma |
| RST-BIZ-002 | Timeline | Sem restricao de prazo definida | Baixo | Total |
| RST-BIZ-003 | Orcamento | Sem restricao de orcamento definida | Baixo | Total |

### Restricoes Organizacionais

| ID | Restricao | Descricao | Impacto | Flexibilidade |
|----|-----------|-----------|---------|---------------|
| RST-ORG-001 | Equipa | Sem restricao de skills ou dimensao definida | Baixo | Total |

### Restricoes de Compatibilidade

| ID | Restricao | Descricao | Impacto | Flexibilidade |
|----|-----------|-----------|---------|---------------|
| RST-CMP-001 | Autenticacao vinculada | Site utiliza mesmo modelo de token do App + autorizacao via App/OTP | Alto | Nenhuma |
| RST-CMP-002 | Vinculo App obrigatorio | Cliente do site deve possuir App e conta vinculados | Alto | Nenhuma |
| RST-CMP-003 | Dependencias partilhadas | Reutilizacao das dependencias do App Mobile | Alto | Nenhuma |

## Decisoes

### Restricoes Absolutas (Sem Flexibilidade)

| ID | Restricao |
|----|-----------|
| RST-TEC-001 | Frontend React |
| RST-TEC-002 | Backend C# (.NET) |
| RST-TEC-003 | Padrao BFF |
| RST-TEC-004 | OAuth compativel com App Mobile |
| RST-INT-001 | Core Banking Oracle |
| RST-INT-002 | Siebel IBM |
| RST-INT-003 | Dependencias App Mobile |
| RST-INF-001 | Cloud-only |
| RST-INF-002 | Azure |
| RST-INF-003 | AKS |
| RST-INF-004 | Data residency UE |
| RST-REG-001 | PSD2 SCA |
| RST-REG-002 | RGPD |
| RST-BIZ-001 | Paridade App Mobile |
| RST-CMP-001 | Autenticacao vinculada |
| RST-CMP-002 | Vinculo App obrigatorio |
| RST-CMP-003 | Dependencias partilhadas |

### Restricoes com Flexibilidade

| ID | Restricao | Flexibilidade |
|----|-----------|---------------|
| RST-TEC-005 | Kubernetes (OpenShift compliant) | Baixa - AKS em primeira fase |
| RST-BIZ-002 | Timeline | Total |
| RST-BIZ-003 | Orcamento | Total |
| RST-ORG-001 | Equipa | Total |

### Implicacoes Arquiteturais

1. **Autenticacao**: O site NAO pode funcionar de forma independente - requer App Mobile instalado e conta vinculada para autorizacao via App/OTP
2. **Infraestrutura**: Arquitetura cloud-native em Azure/AKS, OpenShift compliant para portabilidade futura
3. **Integracoes**: Reutilizacao obrigatoria de todas as dependencias do App Mobile (Siebel, Core Banking, etc.)
4. **Paridade funcional**: Todas as funcionalidades do mindmap devem ser implementadas

## Analise de Gap

### Sistema Atual vs Futuro

| Area | Sistema Atual | Sistema Futuro | Gap | Acao |
|------|--------------|----------------|-----|------|
| Frontend | _Qual tecnologia atual?_ | React SPA | _Pendente_ | _Pendente_ |
| Backend | _Qual tecnologia atual?_ | C# BFF | _Pendente_ | _Pendente_ |
| Autenticacao | _Como funciona hoje?_ | OAuth compativel | _Pendente_ | _Pendente_ |
| Integracao Core | _Como e hoje?_ | _Pendente_ | _Pendente_ | _Pendente_ |

## Referencias

- [SEC-02-contexto-negocio-requisitos.md](../sections/SEC-02-contexto-negocio-requisitos.md)
- [DEF-01-business-objectives.md](DEF-01-business-objectives.md)
- Documentacao de sistemas legados
