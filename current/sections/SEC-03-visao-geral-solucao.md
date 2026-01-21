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

## Definições e Decisões

> **Definições requeridas:**
> - [DEF-03-principios-arquitetura.md](../definitions/DEF-03-principios-arquitetura.md) - Status: completed
> - [DEF-03-casos-uso-principais.md](../definitions/DEF-03-casos-uso-principais.md) - Status: completed
>
> **Decisões relacionadas:**
> - [DEC-006-estrategia-containers-openshift.md](../decisions/DEC-006-estrategia-containers-openshift.md) - Status: accepted
> - [DEC-007-padrao-bff.md](../decisions/DEC-007-padrao-bff.md) - Status: accepted
> - [DEC-008-stack-observabilidade-elk.md](../decisions/DEC-008-stack-observabilidade-elk.md) - Status: accepted
> - [DEC-011-diagrama-arquitetura-unico.md](../decisions/DEC-011-diagrama-arquitetura-unico.md) - Status: accepted

## Propósito

Apresentar os princípios de arquitetura, diagrama conceptual e casos de uso principais da solução HomeBanking Web.

## Conteúdo

### 3.1 Princípios de Arquitetura

| Princípio | Decisão | Descrição |
|-----------|---------|-----------|
| **Cloud Strategy** | Containers OpenShift | Arquitetura orientada a containers, assente em OpenShift |
| **API Strategy** | BFF (Backend for Frontend) | Camada de agregação específica para o canal web, isolando sistemas legados |
| **Build vs Buy** | Preferência Build | Avaliação caso a caso, construir quando soluções de mercado forem caras ou inadequadas |
| **Acoplamento Legados** | Via BFF apenas | Frontend isolado de complexidades dos sistemas legados |
| **Observabilidade** | Stack ELK | Logs de aplicação e métricas centralizados |
| **Segurança** | _A definir_ | Avaliar Zero Trust e Defense in Depth |
| **Resiliência** | _A definir_ | Necessita aprofundamento |
| **Portabilidade** | _A definir_ | Necessita aprofundamento |

### 3.2 Diagrama Conceptual

> **Nota:** Este é o diagrama de referência principal da arquitetura. Todas as outras secções devem referenciar este diagrama em vez de duplicá-lo (ver [DEC-011](../decisions/DEC-011-diagrama-arquitetura-unico.md)).

```plantuml
@startuml
!define RECTANGLE class

skinparam backgroundColor #FEFEFE
skinparam componentStyle rectangle
skinparam linetype ortho

title Arquitetura Conceptual - HomeBanking Web (C4 Level 1)

actor "Cliente" as USER

package "Canal Web" #LightBlue {
    [HomeBanking Web\n(SPA React)] as WEB
    note right of WEB
      Container OpenShift
      Design Responsivo
      Multi-idioma (PT/EN/ES)
    end note
}

package "Camada BFF" #LightBlue {
    [BFF Web\n(.NET 8)] as BFF
    note right of BFF
      Container OpenShift
      Agregação/Transformação
      Gestão de Sessão
    end note
}

package "Serviços Azure" #LightYellow {
    [Serviços Azure\n(a detalhar)] as AZURE
    note bottom of AZURE
      Serviços acedidos
      diretamente pelo BFF
      **PENDENTE: Identificar**
    end note
}

package "Gateway" #LightGreen {
    [API Gateway\n(IBM)] as APIGW
    note right of APIGW
      Autenticação: clientid + secret
      Rate Limiting
      Routing
    end note
}

package "Backend Services" #LightGreen {
    [Siebel\n(Principal)] as SIEBEL
    note right of SIEBEL
      Validação de Token
      Lógica de Negócio
    end note
    [Outros Serviços\n(a detalhar)] as OUTROS
    note bottom of OUTROS
      **PENDENTE: Identificar**
    end note
}

package "Core Banking" #LightGreen {
    [Core Banking] as CORE
    database "Base de Dados" as DB
}

package "Terceiros" #LightGreen {
    [KYC/AML] as KYC
    [Cartões] as CARDS
    [Notificações] as NOTIF
}

package "Observabilidade" #LightGray {
    [ELK Stack] as ELK
}

' Fluxo Principal
USER --> WEB : HTTPS
WEB --> BFF : Cookie Sessão\n(HTTPS/REST)
BFF --> APIGW : clientid + secret
BFF --> AZURE : Direto
APIGW --> SIEBEL : Bearer Token
APIGW --> OUTROS : Bearer Token
SIEBEL --> CORE
SIEBEL --> DB
SIEBEL --> KYC
SIEBEL --> CARDS
SIEBEL --> NOTIF
OUTROS --> CORE

' Observabilidade
WEB ..> ELK : Logs
BFF ..> ELK : Logs/Métricas

@enduml
```

#### Legenda

| Cor | Significado |
|-----|-------------|
| Azul | Componentes novos (a desenvolver) |
| Verde | Componentes existentes (reutilizar) |
| Amarelo | Componentes a detalhar (pendente) |
| Cinza | Infraestrutura transversal |

#### Fluxo de Autenticação

| Origem | Destino | Mecanismo |
|--------|---------|-----------|
| Frontend Web | BFF | Cookie de Sessão (HttpOnly, Secure) |
| BFF | API Gateway | ClientID + ClientSecret |
| API Gateway | Backend Services | Bearer Token (propagado) |
| Siebel | - | **Validação do Token** |

#### Pendências de Detalhe

| Item | Descrição | Responsável |
|------|-----------|-------------|
| Serviços Azure | Identificar quais serviços Azure são acedidos diretamente pelo BFF | NovoBanco |
| Outros Backend Services | Identificar serviços além do Siebel | NovoBanco |

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

> **Diagrama:** Ver secção 3.2 (Diagrama Conceptual) para a visão completa da arquitetura.

A integração segue o modelo definido no diagrama de referência (secção 3.2), com clara separação entre componentes novos e existentes:

| Componente | Origem | Ação | Observação |
|------------|--------|------|------------|
| Frontend Web (SPA React) | Novo | Desenvolver | Container OpenShift |
| BFF Web (.NET 8) | Novo | Desenvolver | Container OpenShift |
| API Gateway (IBM) | Existente | Reutilizar | Autenticação clientid+secret |
| Siebel | Existente | Reutilizar | Backend principal, valida token |
| Outros Backend Services | Existente | Reutilizar | A identificar |
| Core Banking | Existente | Reutilizar | Via Siebel |
| Serviços Azure | Existente | Reutilizar | Acesso direto pelo BFF |
| Integrações Terceiros | Existente | Reutilizar | KYC/AML, Cartões, Notificações |
| Base de Dados | Existente | Reutilizar | Via Backend Services |
| ELK Stack | Existente | Reutilizar | Logs e métricas |

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
