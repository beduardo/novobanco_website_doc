---
id: SEC-13-estrategia-testes
aliases:
  - Estratégia de Testes
tags:
  - nextreality-novobanco-website-sections
  - sections
  - testing
  - quality-assurance
approved: true
created: 2026-01-08
hubs:
  - "[[nextreality]]"
para-code: R
reviewed: true
status: completed
---

# 13. Estratégia de Testes

> **Definição:** [DEF-13-estrategia-testes.md](../definitions/DEF-13-estrategia-testes.md)

## Propósito

Definir a estratégia de testes do HomeBanking Web a nível arquitetural, estabelecendo os tipos de testes, frameworks, quality gates e integração com o pipeline CI/CD.

## Conteúdo

### 13.1 Pirâmide de Testes

A estratégia de testes segue o modelo da **pirâmide de testes**, priorizando testes automatizados nos níveis inferiores.

```plantuml
@startuml
skinparam backgroundColor white

title Pirâmide de Testes - HomeBanking Web

rectangle "E2E Tests" as e2e #lightcoral {
    card "10%"
    card "Playwright"
    card "Critical flows"
}

rectangle "Integration Tests" as int #lightyellow {
    card "20%"
    card "Contract tests"
    card "API integration"
}

rectangle "Unit Tests" as unit #lightgreen {
    card "70%"
    card "Vitest / xUnit"
    card "Component logic"
}

unit -[hidden]-> int
int -[hidden]-> e2e

note right of e2e
Mais lentos
Mais custos
Mais frágeis
end note

note right of unit
Mais rápidos
Mais baratos
Mais estáveis
end note

@enduml
```

| Nível | Distribuição | Frameworks | Escopo |
|-------|--------------|------------|--------|
| **Unit Tests** | 70% | Vitest (FE), xUnit (BFF) | Funções, componentes isolados |
| **Integration** | 20% | WireMock, TestContainers | APIs, serviços, contratos |
| **E2E** | 10% | Playwright | Fluxos críticos de utilizador |

### 13.2 Cobertura de Código

| Tipo de Código | Cobertura Target |
|----------------|------------------|
| Componentes críticos | >= 90% |
| Hooks customizados | >= 90% |
| Utils/helpers | >= 80% |
| Serviços | >= 80% |
| **Código geral** | **>= 80%** |

### 13.3 Frameworks de Teste

#### Frontend (React + TypeScript)

| Aspeto | Especificação |
|---------|---------------|
| Framework | Vitest |
| Assertions | Vitest expect |
| Component Testing | React Testing Library |
| Mocking | Vitest mocks |
| Coverage | Istanbul |

#### BFF (.NET 8)

| Aspeto | Especificação |
|---------|---------------|
| Framework | xUnit |
| Assertions | FluentAssertions |
| Mocking | Moq / NSubstitute |
| Coverage | Coverlet |

#### E2E

| Aspeto | Especificação |
|---------|---------------|
| Framework | Playwright |
| Browsers | Chromium, Firefox, WebKit |
| Execution | CI/CD (headless) |
| Reports | HTML + Screenshots |

### 13.4 Tipos de Testes

| Tipo | Objetivo | Responsabilidade | Frequência |
|------|----------|------------------|------------|
| **Unitários** | Validar lógica isolada | Desenvolvimento | Cada commit |
| **Integração** | Validar comunicação entre componentes | Desenvolvimento | Cada commit |
| **Contrato** | Validar API contracts (Pact) | Desenvolvimento | Cada commit |
| **E2E** | Validar fluxos críticos de negócio | QA + Dev | Cada PR |
| **Performance** | Validar NFRs de carga | QA | Pre-release |
| **Segurança (SAST)** | Análise estática de código | Pipeline | Cada commit |
| **Segurança (DAST)** | Análise dinâmica | SecOps | Pre-release |
| **Acessibilidade** | Validar conformidade WCAG 2.1 AA | QA | Cada PR |
| **Penetration Test** | Testes manuais de intrusão | Externo | Antes go-live |

### 13.5 Cenários E2E Críticos

| Fluxo | Prioridade | Criticidade |
|-------|------------|-------------|
| Login via QR Code | Alta | Crítico |
| Login tradicional (fallback) | Alta | Crítico |
| Consulta de saldos | Alta | Crítico |
| Transferência nacional | Alta | Crítico |
| Pagamento de serviços | Alta | Crítico |
| Logout | Média | Alto |
| Alteração de dados | Média | Alto |

### 13.6 Testes de Segurança

| Tipo | Ferramenta | Quando |
|------|------------|--------|
| SAST | SonarQube / Checkmarx | Cada commit |
| DAST | OWASP ZAP | Pre-release |
| Dependency Scan | Snyk / Dependabot | Diário |
| Penetration Test | Manual (externo) | Antes go-live |

### 13.7 Testes de Acessibilidade

| Aspeto | Especificação |
|---------|---------------|
| Standard | WCAG 2.1 AA |
| Tool | axe-core |
| Integration | Playwright + axe |
| Reports | HTML |

### 13.8 Quality Gates no Pipeline

```plantuml
@startuml
skinparam backgroundColor white

title Quality Gates no Pipeline

start
:Commit;
:Build;
:Unit Tests;
if (Pass?) then (sim)
    :Coverage Check;
    if (>= 80%?) then (sim)
        :SAST Scan;
        if (0 Critical?) then (sim)
            :E2E Tests;
            if (Critical pass?) then (sim)
                :Deploy to DEV;
            else (não)
                :BLOCK;
                stop
            endif
        else (não)
            :BLOCK;
            stop
        endif
    else (não)
        :BLOCK;
        stop
    endif
else (não)
    :BLOCK;
    stop
endif

stop

@enduml
```

| Gate | Threshold | Bloqueante |
|------|-----------|------------|
| Unit Tests | 100% pass | Sim |
| Code Coverage | >= 80% | Sim |
| SAST | 0 Critical, 0 High | Sim |
| Lint | 0 errors | Sim |
| E2E Critical | 100% pass | Sim |
| E2E Non-critical | >= 95% pass | Não |
| Accessibility | 0 Critical | Sim |

### 13.9 Test Data Management

| Ambiente | Dados | Fonte |
|----------|-------|-------|
| **dev** | Dados sintéticos (fixtures) | Gerados |
| **qa** | Dados anonimizados de produção | DB anonimizado |
| **prod** | N/A (não testar em prod) | - |

### 13.10 Matriz de Responsabilidades

| Tipo de Teste | Quem Escreve | Quem Executa | Quando |
|---------------|--------------|--------------|--------|
| Unit Tests | Developers | CI Pipeline | Cada commit |
| Integration | Developers | CI Pipeline | Cada commit |
| Contract | Developers | CI Pipeline | Cada commit |
| E2E | QA + Developers | CI Pipeline | Cada PR |
| Performance | QA | Manual + CI | Pre-release |
| Security (SAST) | Automated | CI Pipeline | Cada commit |
| Security (DAST) | SecOps | Manual | Pre-release |
| Accessibility | QA | CI Pipeline | Cada PR |
| UAT | QA + PO | Manual | Pre-release |

## Decisões Referenciadas

- [DEC-009-stack-tecnologica-frontend.md](../decisions/DEC-009-stack-tecnologica-frontend.md) - Stack Frontend (Vitest)
- [DEC-010-stack-tecnologica-backend.md](../decisions/DEC-010-stack-tecnologica-backend.md) - Stack Backend (xUnit)

## Definições Utilizadas

- [DEF-13-estrategia-testes.md](../definitions/DEF-13-estrategia-testes.md) - Detalhes completos
- [DEF-08-seguranca-conformidade.md](../definitions/DEF-08-seguranca-conformidade.md) - Requisitos de segurança
- [DEF-04-design-system.md](../definitions/DEF-04-design-system.md) - WCAG requirements
