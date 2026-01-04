---
id: DEF-03-principios-arquiteturais
aliases:
  - Novo Banco Principios Arquiteturais
tags:
  - nextreality-novobanco-website-definitions
approved: true
created: 2025-12-22
hubs:
  - "[[nextreality]]"
para-code: R
reviewed: true
---
# DEF-03: Principios Arquiteturais

> **Status:** em-progresso
> **Secao relacionada:** 03 - Visao Geral da Solucao

## Contexto

Este documento define os principios arquiteturais que guiam todas as decisoes de design e implementacao da plataforma web de Homebanking.

## Questoes a Responder

1. Quais principios de design de software devem ser seguidos?
R.: SOLID

2. Quais principios de arquitetura cloud-native devem ser aplicados?
R.: 12-Factor App

3. Existem outros principios ou padroes obrigatorios?
R.: CQRS usando MediatR no BFF

4. Como garantir consistencia entre equipas no uso destes principios?
R.: _Pendente_

## Principios Definidos

### SOLID

Os principios SOLID devem ser aplicados em todo o codigo da solucao:

| Principio | Descricao | Aplicacao |
|-----------|-----------|-----------|
| **S** - Single Responsibility | Uma classe deve ter apenas uma razao para mudar | Cada componente/servico com responsabilidade unica |
| **O** - Open/Closed | Aberto para extensao, fechado para modificacao | Uso de interfaces e abstracoes |
| **L** - Liskov Substitution | Subtipos devem ser substituiveis pelos tipos base | Contratos de interface respeitados |
| **I** - Interface Segregation | Interfaces especificas em vez de interfaces genericas | APIs granulares e focadas |
| **D** - Dependency Inversion | Depender de abstracoes, nao de implementacoes | Injecao de dependencias |

### 12-Factor App

A aplicacao deve seguir os 12 fatores para aplicacoes cloud-native:

| Fator | Descricao | Implementacao |
|-------|-----------|---------------|
| **I. Codebase** | Uma codebase, multiplos deploys | Git com branches por ambiente |
| **II. Dependencies** | Declarar e isolar dependencias | NuGet (C#), npm (React) |
| **III. Config** | Configuracao no ambiente | Azure App Configuration / Environment Variables |
| **IV. Backing Services** | Tratar servicos como recursos anexados | Connection strings configuraveis |
| **V. Build, Release, Run** | Separar build, release e execucao | CI/CD pipelines |
| **VI. Processes** | Executar como processos stateless | Containers sem estado local |
| **VII. Port Binding** | Exportar servicos via port binding | Kestrel/containers com portas expostas |
| **VIII. Concurrency** | Escalar via modelo de processos | Horizontal pod autoscaling (AKS) |
| **IX. Disposability** | Maximizar robustez com startup rapido e shutdown gracioso | Health checks, graceful shutdown |
| **X. Dev/Prod Parity** | Manter ambientes similares | Containers identicos em todos os ambientes |
| **XI. Logs** | Tratar logs como event streams | Structured logging para Azure Monitor |
| **XII. Admin Processes** | Executar tarefas admin como processos one-off | Kubernetes Jobs |

## Padroes Arquiteturais Adicionais

### Padroes a Confirmar

| Padrao | Aplicacao | Status |
|--------|-----------|--------|
| CQRS | Separacao de comandos e queries | _Pendente_ |
| Event Sourcing | Persistencia baseada em eventos | _Pendente_ |
| Domain-Driven Design | Modelagem por dominios | _Pendente_ |
| Microservices vs Modular Monolith | Granularidade dos servicos | _Pendente_ |

## Decisoes

### Principios Obrigatorios

- SOLID em todo o codigo
- 12-Factor App para arquitetura cloud-native

### Principios Pendentes de Decisao

- _Lista de padroes a validar com a equipa_

## Referencias

- [SEC-03-visao-geral-solucao.md](../sections/SEC-03-visao-geral-solucao.md)
- [DEF-02-restricoes.md](DEF-02-restricoes.md)
- https://12factor.net/
