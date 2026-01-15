---
aliases:
  - Arquitetura Backend e Servicos
tags:
  - nextreality-novobanco-website-sections
  - sections
  - backend
  - api
  - services
approved: true
created: 2026-01-03
hubs:
  - "[[nextreality]]"
para-code: R
reviewed: true
status: in-progress
---

# 5. Arquitetura Backend & Servicos

## Proposito

Definir a decomposicao de servicos, arquitetura de API, comunicacao, modelo de dominio, rate limiting, resiliencia, versionamento e especificacao de APIs para o HomeBanking Web.

## Conteudo

### 5.1 Decomposicao de Servicos

```plantuml
@startuml
skinparam backgroundColor #FEFEFE
skinparam componentStyle rectangle

title Decomposicao de Servicos - HomeBanking Web

package "Novos Componentes" #LightBlue {
    [Frontend Web\n(React SPA)] as FE
    [BFF Web\n(.NET 8)] as BFF
}

package "Componentes Existentes" #LightGreen {
    [API Gateway] as APIGW

    package "Backend Services" {
        [Auth Service] as AUTH
        [Account Service] as ACCOUNT
        [Payment Service] as PAYMENT
        [Investment Service] as INVEST
        [Document Service] as DOC
    }

    [Core Banking] as CORE
}

package "Infraestrutura" {
    [ELK Stack] as ELK
    database "Redis Cluster\n(Sessao)" as CACHE
}

FE --> BFF : HTTPS/REST
BFF --> APIGW : REST
BFF --> CACHE : Tokens
APIGW --> AUTH
APIGW --> ACCOUNT
APIGW --> PAYMENT
APIGW --> INVEST
APIGW --> DOC
AUTH --> CORE
ACCOUNT --> CORE
PAYMENT --> CORE

FE ..> ELK : Logs
BFF ..> ELK : Logs/Metricas

@enduml
```

| Componente | Tipo | Acao | Tecnologia |
|------------|------|------|------------|
| Frontend Web | Novo | Desenvolver | React + TypeScript |
| BFF Web | Novo | Desenvolver | C# .NET 8 |
| API Gateway | Existente | Reutilizar | - |
| Backend Services | Existente | Reutilizar | - |
| Core Banking | Existente | Reutilizar | - |

### 5.2 Arquitetura BFF

#### 5.2.1 Visao Geral

```plantuml
@startuml
skinparam backgroundColor #FEFEFE

package "BFF Web (.NET 8)" {
    [Controllers] as CTRL
    [Services] as SVC
    [HTTP Clients] as HTTP

    package "Cross-Cutting" {
        [Auth Middleware] as AUTH
        [Cache Service] as CACHE
        [Logging] as LOG
    }
}

[Frontend] --> CTRL : REST/HTTPS
CTRL --> AUTH : Validacao
AUTH --> CACHE : Session Token
CTRL --> SVC : Business Logic
SVC --> HTTP : Backend Calls
HTTP --> [API Gateway]
SVC --> LOG : ELK

@enduml
```

#### 5.2.2 Stack Tecnologica

| Componente | Tecnologia |
|------------|------------|
| **Runtime** | .NET 8 |
| **Linguagem** | C# |
| **Container** | OpenShift compliant |
| **Observabilidade** | ELK Stack |

#### 5.2.3 Responsabilidades

| Responsabilidade | Implementado | Observacao |
|------------------|--------------|------------|
| Agregacao de chamadas | Sim | Combinar multiplas chamadas backend |
| Transformacao de dados | Sim | Adaptar formato para frontend |
| Cache | Sim | Sessao e tokens |
| Autenticacao/Autorizacao | Sim | OAuth 2.0, validacao de sessao |
| Rate Limiting | Nao | Responsabilidade do Gateway |

### 5.3 Arquitetura API

#### 5.3.1 Estilo e Formato

| Aspecto | Decisao |
|---------|---------|
| **Estilo** | REST |
| **Formato** | JSON |
| **Compressao** | gzip |
| **Especificacao** | OpenAPI 3.0 |

#### 5.3.2 Versionamento

| Aspecto | Decisao | Exemplo |
|---------|---------|---------|
| **Estrategia** | URL path | `/api/v1/accounts` |
| **Deprecacao** | _A definir_ | - |

#### 5.3.3 Estrutura de Endpoints

```
/api/v1/
├── auth/
│   ├── login
│   ├── logout
│   ├── refresh
│   └── validate
├── accounts/
│   ├── {id}
│   ├── {id}/balance
│   └── {id}/movements
├── payments/
│   ├── transfers
│   └── bills
├── investments/
│   ├── portfolio
│   ├── orders
│   └── products
└── documents/
    ├── statements
    └── receipts
```

### 5.4 Comunicacao entre Servicos

```plantuml
@startuml
skinparam backgroundColor #FEFEFE

participant "Frontend" as FE
participant "BFF" as BFF
participant "API Gateway" as GW
participant "Backend Services" as BE
participant "Core Banking" as CORE

FE -> BFF : REST/HTTPS\n(Cookie sessao)
activate BFF

BFF -> BFF : Validar sessao\n(Cache lookup)
BFF -> GW : REST\n(Bearer token)
activate GW

GW -> BE : REST
activate BE

BE -> CORE : Protocolo interno
activate CORE
CORE --> BE : Response
deactivate CORE

BE --> GW : JSON
deactivate BE

GW --> BFF : JSON
deactivate GW

BFF -> BFF : Transformar/Agregar
BFF --> FE : JSON
deactivate BFF

@enduml
```

| Comunicacao | Protocolo | Autenticacao |
|-------------|-----------|--------------|
| Frontend -> BFF | REST/HTTPS | Cookie de sessao |
| BFF -> Gateway | REST | Bearer token (OAuth) |
| Gateway -> Services | REST | Token propagado |

#### 5.4.1 Comunicacao Assincrona

| Aspecto | Status |
|---------|--------|
| Message Queues | _A definir_ - Necessita aprofundamento |

### 5.5 Modelo de Dominio

O modelo de dominio segue as entidades ja existentes nos backend services da app mobile:

| Dominio | Entidades Principais |
|---------|---------------------|
| **Autenticacao** | User, Session, Credentials |
| **Contas** | Account, Balance, Movement |
| **Pagamentos** | Transfer, Payment, Beneficiary |
| **Investimentos** | Portfolio, Order, Product, Position |
| **Documentos** | Statement, Receipt |

### 5.6 Rate Limiting

| Aspecto | Decisao |
|---------|---------|
| **Responsabilidade** | API Gateway (nao BFF) |
| **Limites** | _A definir_ |
| **Comunicacao** | Mensagem de erro informando necessidade de aguardar |

### 5.7 Resiliencia

| Padrao | Status | Observacao |
|--------|--------|------------|
| **Retry** | Implementado | Exponential backoff (configuravel) |
| **Timeout** | Implementado | Configuravel por endpoint |
| **Fallback** | Parcial | Apenas autenticacao |
| **Health Checks** | Implementado | Liveness + Readiness probes |
| **Circuit Breaker** | A definir | Proposta: Polly |
| **Bulkhead** | Nao previsto | - |

### 5.8 Versionamento API

| Aspecto | Decisao |
|---------|---------|
| **Estrategia** | URL path versioning |
| **Formato** | `/api/v{major}/resource` |
| **Politica Deprecacao** | _A definir_ |

### 5.9 Especificacao API

| Aspecto | Decisao |
|---------|---------|
| **Formato** | OpenAPI 3.0 |
| **Geracao** | Automatizada via Pipeline |
| **Publicacao** | Swagger UI / ReDoc |

**Nota:** Especificacoes OpenAPI completas serao documentadas separadamente.

### 5.10 Dependencias Criticas

| Dependencia | Tipo | Impacto se Indisponivel |
|-------------|------|------------------------|
| **API Gateway** | Externa | Servico inoperante |
| **Backend Services** | Externa | Servico inoperante |
| **Cache Store** | Externa | Sessoes invalidas |
| **ELK Stack** | Externa | Degradacao graceful (sem logs) |

### 5.11 Autenticacao e Sessao

#### Fluxo de Autenticacao

```plantuml
@startuml
skinparam backgroundColor #FEFEFE

actor "Utilizador" as USER
participant "Frontend" as FE
participant "BFF" as BFF
participant "Auth Service" as AUTH
participant "Cache" as CACHE

USER -> FE : Login
FE -> BFF : POST /auth/login\n(credentials)
BFF -> AUTH : Validar credenciais
AUTH --> BFF : OAuth Token

BFF -> BFF : Gerar Session ID
BFF -> CACHE : Store(SessionID, Token)
BFF --> FE : Set-Cookie: SessionID\n(HttpOnly, Secure)

FE -> BFF : GET /accounts\n(Cookie: SessionID)
BFF -> CACHE : Get(SessionID)
CACHE --> BFF : Token
BFF -> AUTH : Validate Token
BFF --> FE : Account data

@enduml
```

#### Gestao de Sessao

| Aspecto | Decisao |
|---------|---------|
| **Identificador** | Cookie de sessao (HttpOnly, Secure) |
| **Token Storage** | Cache distribuido (chave = Session ID) |
| **Validacao** | App ou OTP (SCA) |
| **Propagacao** | Bearer token para backend services |

## Itens Pendentes

| Item | Responsavel | Prioridade |
|------|-------------|------------|
| Circuit Breaker (biblioteca) | Arquitetura | Media |
| Comunicacao assincrona (se necessario) | Arquitetura | Media |
| Politica deprecacao API | Arquitetura | Baixa |

## Decisoes Referenciadas

- [DEC-007-padrao-bff.md](../decisions/DEC-007-padrao-bff.md) - BFF Pattern
- [DEC-010-stack-tecnologica-backend.md](../decisions/DEC-010-stack-tecnologica-backend.md) - Stack Backend
