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

package "Infraestrutura de Entrada" #LightGreen {
    [F5] as F5
}

package "Camada BFF" #LightBlue {
    [BFF Web\n(.NET 8)] as BFF
    note right of BFF
      Container OpenShift
      Agregação/Transformação
      Gestão de Sessão (Redis)
      Intermediário APIs
    end note
}

package "Cache Distribuído" #LightBlue {
    database "Redis Cluster" as REDIS
    note bottom of REDIS
      Sessões de utilizador
      Tokens (apiToken, etc.)
      Chave: token_sessao_spa
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

package "Microservices" #LightBlue {
    [Microservices\n(Lógica de Negócio)] as MS
    note right of MS
      Containers OpenShift
      Regras de Negócio
      Protocolo Omni
    end note
}

package "Backend Services - Autenticação" #LightGreen {
    [ApiPsd2\n(Autenticação PSD2)] as APIPSD2
    note right of APIPSD2
      Acesso direto pelo BFF
      OAuth + Assinatura SHA256
      Operações: AUT_004, AUT_001
    end note
}

package "Backend Services - APIs Bancárias" #LightGreen {
    [ApiBBest\n(APIs Principais)] as APIBBEST
    note right of APIBBEST
      Acesso direto pelo BFF
      OAuth 1.1 (HMAC-SHA256)
      APIs de consulta e operações
    end note
}

package "Gateway" #LightGreen {
    [API Gateway\n(IBM)] as APIGW
    note right of APIGW
      **Apenas para Siebel**
      Autenticação: clientid + secret
      Rate Limiting
    end note
}

package "Backend Services - Core" #LightGreen {
    [Siebel\n(Principal)] as SIEBEL
    note right of SIEBEL
      Validação de Token
      Lógica de Negócio Core
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
WEB --> F5 : Protocolo Omni
F5 --> BFF : Protocolo Omni
BFF --> REDIS : Lookup/Store\nTokens e Sessão
BFF --> APIPSD2 : OAuth + SHA256\n(Autenticação)
BFF --> APIBBEST : OAuth 1.1 HMAC\n(APIs Bancárias)
BFF --> MS : Protocolo Omni\n(Lógica de Negócio)
BFF --> APIGW : clientid + secret\n(Apenas Siebel)
BFF --> AZURE : Direto
APIGW --> SIEBEL : Bearer Token
MS --> SIEBEL : Protocolo Siebel
SIEBEL --> CORE
SIEBEL --> DB
SIEBEL --> KYC
SIEBEL --> CARDS
SIEBEL --> NOTIF

' Observabilidade
WEB ..> ELK : Logs
BFF ..> ELK : Logs/Métricas
MS ..> ELK : Logs/Métricas

@enduml
```

#### Legenda

| Cor | Significado |
|-----|-------------|
| Azul | Componentes novos (a desenvolver): SPA, BFF, MS, Redis |
| Verde | Componentes existentes (reutilizar): F5, ApiPsd2, ApiBBest, API Gateway, Siebel |
| Amarelo | Componentes a detalhar (pendente): Serviços Azure |
| Cinza | Infraestrutura transversal |

#### Protocolos de Comunicação

> **Nota sobre Protocolos:**
> - **Protocolo Omni:** Padronização sobre REST utilizada para comunicação SPA↔F5↔BFF e BFF↔MS
> - **OAuth + SHA256:** Utilizado para comunicação BFF↔ApiPsd2 (autenticação)
> - **OAuth 1.1 HMAC:** Utilizado para comunicação BFF↔ApiBBest (APIs bancárias)
> - **BEST:** Protocolo existente para comunicação BFF↔API Gateway
> - **Siebel:** Protocolo existente para comunicação API Gateway/MS↔Siebel

#### Fluxo de Autenticação

| Origem | Destino | Mecanismo | Protocolo |
|--------|---------|-----------|-----------|
| SPA | F5 | Cookie de Sessão (token_sessao_spa, HttpOnly, Secure, SameSite=Strict) | Omni |
| F5 | BFF | Cookie de Sessão (propagado) | Omni |
| BFF | Redis | Lookup por token_sessao_spa → tokens do utilizador | - |
| BFF | ApiPsd2 | OAuth + Assinatura SHA256 | REST |
| BFF | ApiBBest | OAuth 1.1 (HMAC-SHA256) | REST |
| BFF | MS | Token de Sessão | Omni |
| BFF | API Gateway (IBM) | ClientID + ClientSecret | BEST |
| API Gateway | Siebel | Bearer Token (propagado) - **Siebel valida** | Siebel |

> **Esclarecimento API Gateway:** O API Gateway IBM faz **apenas routing** dos pedidos, sem realizar autenticação. Toda a autenticação (validação de clientid+secret do BFF e validação do Bearer Token do utilizador) é realizada pelo **Siebel**.

> **Cenário Secundário - Web na App:** Embora não seja o fluxo primário, está prevista a possibilidade do canal web correr dentro da app mobile nativa (WebView). Este cenário requer integração específica para navegação e biometria. Os detalhes serão definidos em fase posterior.

#### Pendências de Detalhe

| Item | Descrição | Responsável |
|------|-----------|-------------|
| Serviços Azure | Identificar quais serviços Azure são acedidos diretamente pelo BFF | NovoBanco |
| Lista de Microservices | Identificar quais MS serão desenvolvidos e suas responsabilidades | NovoBanco/NextReality |

### 3.3 Componentes Principais

| Componente | Tipo | Responsabilidade | Tecnologia |
|------------|------|------------------|------------|
| **HomeBanking Web** | Frontend SPA | Interface do utilizador, experiência web responsiva | React |
| **F5** | Infraestrutura | Entrada de tráfego web | Existente |
| **BFF Web** | Backend | Lógica de UI, agregação, transformação, orquestração | .NET 8 |
| **Redis Cluster** | Cache | Sessões distribuídas, tokens | Existente |
| **Microservices** | Backend | Lógica de Negócio, regras de domínio | .NET 8 |
| **ApiPsd2** | Backend | Autenticação PSD2 | Existente |
| **ApiBBest** | Backend | APIs bancárias principais | Existente |
| **API Gateway** | Infraestrutura | Roteamento para Siebel | IBM (Existente) |
| **Siebel** | Backend | Lógica de negócio core | Existente |
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
| Microservices (.NET 8) | Novo | Desenvolver | Container OpenShift, Protocolo Omni |
| Redis Cluster | Novo | Desenvolver | Sessões e tokens |
| F5 | Existente | Reutilizar | Entrada de tráfego web |
| ApiPsd2 | Existente | Reutilizar | Autenticação PSD2, OAuth+SHA256 |
| ApiBBest | Existente | Reutilizar | APIs bancárias, OAuth 1.1 HMAC |
| API Gateway (IBM) | Existente | Reutilizar | Apenas para Siebel |
| Siebel | Existente | Reutilizar | Backend principal, lógica core |
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
