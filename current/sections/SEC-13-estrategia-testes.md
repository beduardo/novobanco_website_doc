---
id: SEC-13-estrategia-testes
aliases:
  - Estrategia de Testes
tags:
  - nextreality-novobanco-website-sections
  - sections
  - testing
approved: true
created: 2026-01-08
hubs:
  - "[[nextreality]]"
para-code: R
reviewed: true
status: in-progress
---

# 13. Estrategia de Testes

## Proposito

Definir a estrategia de testes do HomeBanking Web a nivel arquitetural, estabelecendo os tipos de testes, quality gates e integracao com o pipeline CI/CD.

## Conteudo

### 13.1 Abordagem de Testes

A estrategia de testes segue o modelo da **piramide de testes**, priorizando testes automatizados nos niveis inferiores.

```plantuml
@startuml
skinparam backgroundColor white

title Piramide de Testes - HomeBanking Web

rectangle "E2E\n(Fluxos criticos)" as E2E #LightCoral
rectangle "Integracao\n(APIs, componentes)" as INT #LightGoldenRodYellow
rectangle "Unitarios\n(Funcoes, classes)" as UNIT #LightGreen

E2E -[hidden]down- INT
INT -[hidden]down- UNIT

@enduml
```

| Nivel | Escopo | Quantidade | Velocidade |
|-------|--------|------------|------------|
| **Unitarios** | Funcoes, componentes isolados | Muitos | Rapidos |
| **Integracao** | APIs, servicos, base de dados | Moderados | Medios |
| **E2E** | Fluxos completos de utilizador | Poucos | Lentos |

### 13.2 Tipos de Testes

| Tipo | Objetivo | Responsabilidade |
|------|----------|------------------|
| **Unitarios** | Validar logica isolada | Equipa de Desenvolvimento |
| **Integracao** | Validar comunicacao entre componentes | Equipa de Desenvolvimento |
| **E2E** | Validar fluxos criticos de negocio | QA |
| **Performance** | Validar NFRs de carga e tempo de resposta | QA / Arquitetura |
| **Seguranca (SAST/DAST)** | Identificar vulnerabilidades | DevSecOps |
| **Acessibilidade** | Validar conformidade WCAG | QA / UX |

### 13.3 Quality Gates no Pipeline

Os quality gates sao pontos de verificacao automatica no pipeline CI/CD que bloqueiam a promocao de codigo que nao cumpra os criterios minimos.

```plantuml
@startuml
skinparam backgroundColor white

title Quality Gates - Pipeline CI/CD

rectangle "Build" as B #LightBlue {
  rectangle "Unit Tests"
  rectangle "Code Coverage"
  rectangle "SAST Scan"
}

rectangle "Test" as T #LightGreen {
  rectangle "Integration Tests"
  rectangle "E2E (Smoke)"
}

rectangle "Pre-Prod" as P #LightYellow {
  rectangle "DAST Scan"
  rectangle "Performance Test"
}

B --> T : Pass
T --> P : Pass
P --> [Deploy Prod] : Approve

@enduml
```

| Gate | Stage | Criterio | Bloqueante |
|------|-------|----------|------------|
| Unit Tests | Build | 100% a passar | Sim |
| Code Coverage | Build | Minimo a definir | Sim |
| SAST | Build | Sem vulnerabilidades Critical/High | Sim |
| Integration Tests | Test | 100% a passar | Sim |
| E2E Smoke | Test | Fluxos criticos a passar | Sim |
| DAST | Pre-Prod | Sem vulnerabilidades Critical | Sim |

### 13.4 Testes de Seguranca

| Tipo | Descricao | Frequencia |
|------|-----------|------------|
| **SAST** | Analise estatica de codigo | Cada build |
| **DAST** | Analise dinamica em ambiente de teste | Pre-release |
| **Penetration Testing** | Testes manuais de intrusao | Periodico (a definir) |

### 13.5 Ambientes de Teste

| Ambiente | Proposito | Dados |
|----------|-----------|-------|
| **Dev** | Testes unitarios e integracao | Sinteticos |
| **QA** | Testes E2E e aceitacao | Anonimizados |
| **Pre-Prod** | Testes de performance e seguranca | Anonimizados |

## Itens Pendentes

| Item | Responsavel | Prioridade |
|------|-------------|------------|
| Definir cobertura minima de codigo | Arquitetura / QA | Alta |
| Definir ferramentas SAST/DAST | DevSecOps | Alta |
| Definir cenarios E2E criticos | QA / Produto | Alta |
| Definir frequencia de penetration testing | Seguranca | Media |

## Decisoes Referenciadas

- [DEC-009-stack-tecnologica-frontend.md](../decisions/DEC-009-stack-tecnologica-frontend.md) - Stack Frontend
- [DEC-010-stack-tecnologica-backend.md](../decisions/DEC-010-stack-tecnologica-backend.md) - Stack Backend
