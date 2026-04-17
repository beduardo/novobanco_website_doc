---
id: "SEC-03"
title: "Visao Geral da Solucao"
status: "in-progress"
created: "2026-01-01"
updated: "2026-01-01"
depends-on-definitions:
  - "DEF-05"
  - "DEF-06"
depends-on-decisions:
  - "DEC-016"
word-count: 0
---

# 3. Visão Geral da Solução

## Definições e Decisões

> **Definições requeridas:**
> - [DEF-05-principios-arquitetura.md](../definitions/DEF-05-principios-arquitetura.md) - Status: completed
> - [DEF-06-casos-uso-principais.md](../definitions/DEF-06-casos-uso-principais.md) - Status: completed
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
A representação do canal mobile é meramente ilustrativa para efeitos de clareza em como se ligam os canais na arquitetura proposta.

```plantuml
@startuml
!define RECTANGLE class

skinparam backgroundColor #FEFEFE
skinparam componentStyle rectangle
skinparam linetype ortho

title Arquitetura Conceptual - HomeBanking Web (C4 Level 1)

actor "Cliente" as USER

package "Canal Mobile" as CANAL_MOBILE #LightCyan {
    [App Mobile\n(iOS / Android)] as MOBILE
    note right of MOBILE
      Canal nativo
      Representação ilustrativa
    end note
}

package "Canal Web" as CANAL_WEB #LightBlue {
    [HomeBanking Web\n(SPA React)] as WEB
    note right of WEB
      Container OpenShift
      Design Responsivo
      Multi-idioma (PT/EN/ES)
    end note
}

package "Infraestrutura de Entrada" as INFRAESTRUTURA #LightGreen {
    [F5] as F5
}

package "Camada BFF" as CAMADA_BFF #LightBlue {
    [BFF Web\n(.NET 8)] as BFF
    note right of BFF
      Container OpenShift
      Agregação/Transformação
      Gestão de Sessão (Redis)
      Intermediário APIs
    end note
}

package "Cache Distribuído" as CACHE_DISTRIBUIDO #LightBlue {
    database "Redis Cluster" as REDIS
    note bottom of REDIS
      Sessões de utilizador
      Tokens (apiToken, etc.)
      Chave: token_sessao_spa
    end note
}

package "Serviços Azure" as SERVICOS_AZURE #LightYellow {
    [Serviços Azure\n(a detalhar)] as AZURE
    note bottom of AZURE
      Serviços acedidos
      diretamente pelo BFF
      **PENDENTE: Identificar**
    end note
}

package "MicroService" as MICROSERVICES #LightBlue {
    [MicroService\n(Lógica de Negócio)] as MS
    note right of MS
      Container OpenShift (Pod único)
      Regras de Negócio
      Protocolo Omni
    end note
}

package "Gateway" as GATEWAY #LightGreen {
    [API Gateway\n(IBM)] as APIGW
    note right of APIGW
      Siebel + MicroService
      Autenticação: clientid + secret
      Rate Limiting
    end note
}

package "Backend Services - Core" as BACKEND_SERVICES #LightGreen {
    [Siebel\n(Principal)] as SIEBEL
    note right of SIEBEL
      Validação de Token OAuth 1.1 (HMAC-SHA256)
      Lógica de Negócio Core
      Operações: AUT_004, AUT_001
    end note
}

package "Observabilidade" as OBSERVABILIDADE #LightGray {
    [ELK Stack] as ELK
}

' Fluxo Principal
USER -l-> CANAL_MOBILE : HTTPS
USER -l-> CANAL_WEB : HTTPS
CANAL_MOBILE -d-> CANAL_WEB : Funcionalidades Web\n(WebView)
CANAL_MOBILE -d-> GATEWAY : Serviços Mobile\n(clientid + secret)
CANAL_WEB -d-> INFRAESTRUTURA : Protocolo Omni
INFRAESTRUTURA --> CAMADA_BFF : Protocolo Omni
CAMADA_BFF --> CACHE_DISTRIBUIDO : Lookup/Store\nTokens e Sessão
CAMADA_BFF --> GATEWAY : clientid + secret\n(Siebel + MicroService)
GATEWAY --> MICROSERVICES : Protocolo Omni\n(Lógica de Negócio)
CAMADA_BFF --> SERVICOS_AZURE : Direto
GATEWAY --> BACKEND_SERVICES : Bearer Token
MICROSERVICES --> BACKEND_SERVICES : Protocolo Siebel

' Observabilidade
CANAL_WEB ..> OBSERVABILIDADE : Logs
CAMADA_BFF ..> OBSERVABILIDADE : Logs/Métricas
MICROSERVICES ..> OBSERVABILIDADE : Logs/Métricas

@enduml
```

#### Legenda

| Cor | Significado |
|-----|-------------|
| Azul | Componentes novos (a desenvolver): SPA, BFF, MS, Redis |
| Verde | Componentes existentes (reutilizar): F5, API Gateway, Siebel |
| Amarelo | Componentes a detalhar (pendente): Serviços Azure |
| Cinza | Infraestrutura transversal |

#### Protocolos de Comunicação

> **Nota sobre Protocolos:**
> - **Protocolo Omni:** Padronização sobre REST utilizada para comunicação SPA↔F5↔BFF e BFF→Gateway→MicroService
> - **OAuth + SHA256:** Utilizado para comunicação BFF↔Siebel (autenticação PSD2)
> - **OAuth 1.1 HMAC:** Utilizado para comunicação BFF↔Siebel (APIs bancárias)
> - **BEST:** Protocolo existente para comunicação BFF↔API Gateway
> - **Siebel:** Protocolo existente para comunicação API Gateway/MS↔Siebel

#### Fluxo de Autenticação

| Origem | Destino | Mecanismo | Protocolo |
|--------|---------|-----------|-----------|
| SPA | F5 | Cookie de Sessão (token_sessao_spa, HttpOnly, Secure, SameSite=Strict) | Omni |
| F5 | BFF | Cookie de Sessão (propagado) | Omni |
| BFF | Redis | Lookup por token_sessao_spa → tokens do utilizador | - |
| BFF | API Gateway (IBM) | ClientID + ClientSecret | Omni / BEST |
| API Gateway | MicroService | Protocolo Omni (roteado pelo GW) | Omni |
| API Gateway | Siebel | Bearer Token (propagado) - **Siebel valida** | Siebel |

> **Esclarecimento API Gateway:** O API Gateway IBM faz **apenas routing** dos pedidos para Siebel e MicroService, sem realizar autenticação. Toda a autenticação (validação de clientid+secret do BFF e validação do Bearer Token do utilizador) é realizada pelo **Siebel**.

> **Cenário Secundário - Web na App:** Embora não seja o fluxo primário, está prevista a possibilidade de haver funcionalidade web a correr dentro da app mobile nativa (WebView). Este cenário requer integração específica para navegação e biometria. Os detalhes serão definidos em fase posterior.

#### Pendências de Detalhe

| Item | Descrição | Responsável |
|------|-----------|-------------|
| Serviços Azure | Identificar quais serviços Azure são acedidos diretamente pelo BFF | Banco Best |
| Responsabilidades do MicroService | Identificar as responsabilidades específicas do MicroService | Banco Best/NextReality |

### 3.3 Componentes Principais

| Componente | Tipo | Responsabilidade | Tecnologia |
|------------|------|------------------|------------|
| **HomeBanking Web** | Frontend SPA | Interface do utilizador, experiência web responsiva | React |
| **F5** | Infraestrutura | Entrada de tráfego web | Existente |
| **BFF Web** | Backend | Lógica de UI, agregação, transformação, orquestração | .NET 8 |
| **Redis Cluster** | Cache | Sessões distribuídas, tokens | Existente |
| **MicroService** | Backend | Lógica de Negócio, regras de domínio (Pod único) | .NET 8 |
| **API Gateway** | Infraestrutura | Roteamento para Siebel e MicroService | IBM (Existente) |
| **Siebel** | Backend | Lógica de negócio core | Existente |
| **ELK Stack** | Observabilidade | Logs centralizados, métricas, dashboards | Existente |

### 3.4 Casos de Uso Principais

#### 3.4.1 Atores

| Ator                | Descrição                        | Prioridade |
| ------------------- | -------------------------------- | ---------- |
| Cliente Individual  | Cliente particular do Best | Principal  |
| Cliente Empresarial | _Futuro_                         | Secundário |

#### 3.4.2 Casos de Uso por Categoria

```plantuml
@startuml
skinparam backgroundColor #FEFEFE

left to right direction

actor "Cliente Individual" as USER

rectangle "HomeBanking Web" as web {
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

note right of web
  **Crítico**
  SCA obrigatório conforme retorno da API
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
| MicroService (.NET 8) | Novo | Desenvolver | Pod único OpenShift, Protocolo Omni |
| Redis Cluster | Novo | Desenvolver | Sessões e tokens |
| F5 | Existente | Reutilizar | Entrada de tráfego web |
| API Gateway (IBM) | Existente | Reutilizar | Para Siebel e MicroService |
| Siebel | Existente | Reutilizar | Backend principal, lógica core |
| Serviços Azure | Existente | Reutilizar | Acesso direto pelo BFF |
| ELK Stack | Existente | Reutilizar | Logs e métricas |

## Entregáveis

- [x] Lista de princípios arquiteturais documentados
- [x] Diagrama conceptual de alto nível (C4 Level 1)
- [x] Descrição dos componentes principais
- [x] Diagrama de casos de uso
- [x] Mapeamento de integração com sistemas existentes

## Definições Utilizadas

- [x] [DEF-05-principios-arquitetura.md](../definitions/DEF-05-principios-arquitetura.md) - Status: completed
- [x] [DEF-06-casos-uso-principais.md](../definitions/DEF-06-casos-uso-principais.md) - Status: completed

## Decisões Referenciadas

- [x] [DEC-006-estrategia-containers-openshift.md](../decisions/DEC-006-estrategia-containers-openshift.md) - Status: accepted
- [x] [DEC-007-padrao-bff.md](../decisions/DEC-007-padrao-bff.md) - Status: accepted
- [x] [DEC-008-stack-observabilidade-elk.md](../decisions/DEC-008-stack-observabilidade-elk.md) - Status: accepted
- [x] [DEC-016-microservice-como-pod-unico.md](../decisions/DEC-016-microservice-como-pod-unico.md) - Status: accepted

## Itens Pendentes

| Item | Documento | Responsável |
|------|-----------|-------------|
| Princípios de Segurança (Zero Trust, Defense in Depth) | DEF-05-principios-arquitetura | Área de Segurança |
| Estratégia de Resiliência | DEF-05-principios-arquitetura | Arquitetura |
| Requisitos de Portabilidade | DEF-05-principios-arquitetura | Arquitetura |
| Casos de Uso com Terceiros | DEF-06-casos-uso-principais | Integração |
| Requisitos Offline | DEF-06-casos-uso-principais | Arquitetura |
