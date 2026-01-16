---
aliases:
  - Visão Geral da Solução
tags:
  - nextreality-novobanco-website-sections
  - sections
  - solution-overview
  - architecture
approved: true
created: 2026-01-01
hubs:
  - "[[nextreality]]"
para-code: R
reviewed: true
status: in-progress
---

# 3. Visão Geral da Solução

> **Definições requeridas:**
> - [DEF-03-principios-arquitetura.md](../definitions/DEF-03-principios-arquitetura.md) - Status: completed
> - [DEF-03-casos-uso-principais.md](../definitions/DEF-03-casos-uso-principais.md) - Status: completed
>
> **Decisões relacionadas:**
> - [DEC-006-estrategia-containers-openshift.md](../decisions/DEC-006-estrategia-containers-openshift.md) - Status: accepted
> - [DEC-007-padrao-bff.md](../decisions/DEC-007-padrao-bff.md) - Status: accepted
> - [DEC-008-stack-observabilidade-elk.md](../decisions/DEC-008-stack-observabilidade-elk.md) - Status: accepted

## Propósito

Apresentar os princípios de arquitetura, diagrama conceptual e casos de uso principais da solução HomeBanking Web.

## Conteúdo

### 3.1 Princípios de Arquitetura

| Princípio | Decisão | Descrição |
|-----------|---------|-----------|
| **Cloud Strategy** | Containers OpenShift | Arquitetura orientada a containers, compliant com OpenShift |
| **API Strategy** | BFF (Backend for Frontend) | Camada de agregação específica para o canal web, isolando sistemas legados |
| **Build vs Buy** | Preferência Build | Avaliação caso a caso, construir quando soluções de mercado forem caras ou inadequadas |
| **Acoplamento Legados** | Via BFF apenas | Frontend isolado de complexidades dos sistemas legados |
| **Observabilidade** | Stack ELK | Logs de aplicação e métricas centralizados |
| **Segurança** | _A definir_ | Avaliar Zero Trust e Defense in Depth |
| **Resiliência** | _A definir_ | Necessita aprofundamento |
| **Portabilidade** | _A definir_ | Necessita aprofundamento |

### 3.2 Diagrama Conceptual

```plantuml
@startuml
!define RECTANGLE class

skinparam backgroundColor #FEFEFE
skinparam componentStyle rectangle
skinparam linetype ortho

title Arquitetura Conceptual - HomeBanking Web (C4 Level 1)

actor "Cliente Individual" as USER

package "Canal Web" {
    [HomeBanking Web\n(SPA)] as WEB
    note right of WEB
      Container OpenShift
      Design Responsivo
      Multi-idioma (PT/EN/ES)
    end note
}

package "Camada BFF" {
    [BFF Web\n(Backend for Frontend)] as BFF
    note right of BFF
      Container OpenShift
      Agregação/Transformação
      Isolamento de Legados
    end note
}

package "Serviços Existentes" {
    [API Gateway] as APIGW
    [Backend Services] as BE
}

package "Infraestrutura Existente" {
    [Core Banking] as CORE
    database "Base de Dados" as DB
}

package "Terceiros" {
    [KYC/AML] as KYC
    [Cartões] as CARDS
    [Notificações] as NOTIF
}

package "Observabilidade" {
    [ELK Stack] as ELK
}

USER --> WEB : HTTPS
WEB --> BFF : HTTPS/REST
BFF --> APIGW : Integração
APIGW --> BE
BE --> CORE
BE --> DB
BE --> KYC
BE --> CARDS
BE --> NOTIF

WEB ..> ELK : Logs/Métricas
BFF ..> ELK : Logs/Métricas

@enduml
```

### 3.3 Componentes Principais

| Componente | Tipo | Responsabilidade | Tecnologia |
|------------|------|------------------|------------|
| **HomeBanking Web** | Frontend SPA | Interface do utilizador, experiência web responsiva | _A definir (SEC-04)_ |
| **BFF Web** | Backend | Agregação, transformação, orquestração para canal web | _A definir (SEC-05)_ |
| **API Gateway** | Infraestrutura | Roteamento, rate limiting, autenticação | Existente |
| **Backend Services** | Serviços | Lógica de negócio, integrações | Existente |
| **ELK Stack** | Observabilidade | Logs centralizados, métricas, dashboards | Existente |

### 3.4 Casos de Uso Principais

#### 3.4.1 Atores

| Ator                | Descrição                        | Prioridade |
| ------------------- | -------------------------------- | ---------- |
| Cliente Individual  | Cliente particular do Novo Banco | Principal  |
| Cliente Empresarial | _Futuro_                         | Secundário |

#### 3.4.2 Casos de Uso por Categoria

```plantuml
@startuml
skinparam backgroundColor #FEFEFE

left to right direction

actor "Cliente Individual" as USER

rectangle "HomeBanking Web" {
    package "Autenticação" {
        usecase "Login" as UC_LOGIN
        usecase "Registo" as UC_REG
        usecase "Recuperação Acessos" as UC_REC
    }

    package "Consultas" {
        usecase "Dashboard" as UC_DASH
        usecase "Saldos e Movimentos" as UC_SALDOS
        usecase "Património" as UC_PAT
    }

    package "Operações" {
        usecase "Transferências" as UC_TRANSF
        usecase "Pagamentos" as UC_PAG
    }

    package "Investimentos" {
        usecase "Ações/ETF/Fundos" as UC_INV
        usecase "Robot Advisor" as UC_ROBOT
    }
}

USER --> UC_LOGIN
USER --> UC_REG
USER --> UC_REC
USER --> UC_DASH
USER --> UC_SALDOS
USER --> UC_PAT
USER --> UC_TRANSF
USER --> UC_PAG
USER --> UC_INV
USER --> UC_ROBOT

note right of UC_LOGIN
  **Crítico**
  SCA obrigatório
end note

note right of UC_TRANSF
  **Crítico**
  SCA obrigatório
end note

@enduml
```

#### 3.4.3 Casos de Uso Críticos

| Caso de Uso | Criticidade | Requisitos Especiais |
|-------------|-------------|----------------------|
| **Login** | Alta | SCA obrigatório, ponto de entrada |
| **Transferências** | Alta | SCA obrigatório, operação financeira core |

#### 3.4.4 Requisitos de Autenticação

- **SCA (Strong Customer Authentication):** Obrigatório para todo o acesso à aplicação
- **Conformidade:** PSD2

### 3.5 Integração com Infraestrutura Existente

```plantuml
@startuml
skinparam backgroundColor #FEFEFE

package "Novo (HomeBanking Web)" #LightBlue {
    [Frontend Web] as FE
    [BFF Web] as BFF
}

package "Existente (App Mobile)" #LightGreen {
    [API Gateway] as APIGW
    [Backend Services] as BE
    [Core Banking] as CORE
    [Integrações Terceiros] as THIRD
    database "Base de Dados" as DB
}

FE --> BFF : Novo
BFF --> APIGW : Reutiliza
APIGW --> BE : Existente
BE --> CORE : Existente
BE --> THIRD : Existente
BE --> DB : Existente

note bottom of FE
  Componentes novos
  a desenvolver
end note

note bottom of APIGW
  Componentes existentes
  reutilizados
end note

@enduml
```

| Componente | Origem | Ação |
|------------|--------|------|
| Frontend Web | Novo | Desenvolver |
| BFF Web | Novo | Desenvolver |
| API Gateway | Existente | Reutilizar |
| Backend Services | Existente | Reutilizar |
| Core Banking | Existente | Reutilizar |
| Integrações Terceiros | Existente | Reutilizar |
| Base de Dados | Existente | Reutilizar |

## Entregáveis

- [x] Lista de princípios arquiteturais documentados
- [x] Diagrama conceptual de alto nível (C4 Level 1)
- [x] Descrição dos componentes principais
- [x] Diagrama de casos de uso
- [x] Mapeamento de integração com sistemas existentes

## Definições Utilizadas

- [x] [DEF-03-principios-arquitetura.md](../definitions/DEF-03-principios-arquitetura.md) - Status: completed
- [x] [DEF-03-casos-uso-principais.md](../definitions/DEF-03-casos-uso-principais.md) - Status: completed

## Decisões Referenciadas

- [x] [DEC-006-estrategia-containers-openshift.md](../decisions/DEC-006-estrategia-containers-openshift.md) - Status: accepted
- [x] [DEC-007-padrao-bff.md](../decisions/DEC-007-padrao-bff.md) - Status: accepted
- [x] [DEC-008-stack-observabilidade-elk.md](../decisions/DEC-008-stack-observabilidade-elk.md) - Status: accepted

## Itens Pendentes

| Item | Documento | Responsável |
|------|-----------|-------------|
| Princípios de Segurança (Zero Trust, Defense in Depth) | DEF-03-principios-arquitetura | Área de Segurança |
| Estratégia de Resiliência | DEF-03-principios-arquitetura | Arquitetura |
| Requisitos de Portabilidade | DEF-03-principios-arquitetura | Arquitetura |
| Casos de Uso com Terceiros | DEF-03-casos-uso-principais | Integração |
| Requisitos Offline | DEF-03-casos-uso-principais | Arquitetura |
