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

> **Definicoes requeridas:**
> - [DEF-05-arquitetura-bff.md](../definitions/DEF-05-arquitetura-bff.md) - Status: completed
> - [DEF-05-api-design.md](../definitions/DEF-05-api-design.md) - Status: completed
> - [DEF-05-padroes-resiliencia.md](../definitions/DEF-05-padroes-resiliencia.md) - Status: completed
>
> **Decisoes relacionadas:**
> - [DEC-007-padrao-bff.md](../decisions/DEC-007-padrao-bff.md) - Status: accepted

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
    database "Cache\n(Sessao)" as CACHE
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

#### 5.7.1 Padroes Implementados

```plantuml
@startuml
skinparam backgroundColor #FEFEFE

rectangle "Padroes de Resiliencia" {
    rectangle "Retry" #LightGreen {
        [Exponential Backoff]
        [3 Tentativas]
        [Timeout/Rate Limit]
    }

    rectangle "Timeout" #LightGreen {
        [60 segundos]
    }

    rectangle "Fallback" #LightGreen {
        [Autenticacao]
        [Fluxo Resiliente]
    }

    rectangle "Health Checks" #LightGreen {
        [Liveness]
        [Readiness]
    }

    rectangle "Circuit Breaker" #Yellow {
        [A Definir]
    }

    rectangle "Bulkhead" #LightCoral {
        [Nao Implementado]
    }
}

@enduml
```

#### 5.7.2 Retry Policy

| Parametro | Valor |
|-----------|-------|
| **Estrategia** | Exponential backoff |
| **Tentativas** | 3 |
| **Erros elegiveis** | Timeout, Rate limit |

#### 5.7.3 Timeout

| Parametro | Valor |
|-----------|-------|
| **Timeout padrao** | 60 segundos |
| **Diferenciacao** | Nao (uniforme) |

#### 5.7.4 Fallback

| Operacao | Comportamento |
|----------|---------------|
| **Autenticacao** | Fluxo mais resiliente |
| **Outras** | Nao implementado |

#### 5.7.5 Health Checks

| Tipo | Implementado | Frequencia |
|------|--------------|------------|
| **Liveness** | Sim | _A definir_ |
| **Readiness** | Sim | _A definir_ |

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

#### 5.9.1 Exemplo de Especificacao

```yaml
openapi: 3.0.0
info:
  title: HomeBanking Web BFF API
  version: 1.0.0
paths:
  /api/v1/accounts/{id}/balance:
    get:
      summary: Get account balance
      parameters:
        - name: id
          in: path
          required: true
          schema:
            type: string
      responses:
        '200':
          description: Success
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Balance'
        '401':
          description: Unauthorized
        '404':
          description: Account not found
```

### 5.10 Dependencias

```plantuml
@startuml
skinparam backgroundColor #FEFEFE

package "BFF Dependencies" {
    [BFF Web] as BFF

    package "Runtime" {
        [.NET 8 Runtime]
        [ASP.NET Core]
    }

    package "Libraries" {
        [HttpClient]
        [Polly\n(Resiliencia)]
        [Serilog\n(Logging)]
        [DistributedCache]
    }

    package "External" {
        [API Gateway]
        [ELK Stack]
        [Cache Store]
    }
}

BFF --> [.NET 8 Runtime]
BFF --> [ASP.NET Core]
BFF --> [HttpClient]
BFF --> [Polly\n(Resiliencia)]
BFF --> [Serilog\n(Logging)]
BFF --> [DistributedCache]
BFF --> [API Gateway]
BFF --> [ELK Stack]
BFF --> [Cache Store]

@enduml
```

| Dependencia | Tipo | Critica |
|-------------|------|---------|
| API Gateway | Externa | Sim |
| Backend Services | Externa | Sim |
| Cache Store | Externa | Sim |
| ELK Stack | Externa | Nao (degradacao graceful) |

### 5.11 Padroes de Design

| Padrao | Aplicacao |
|--------|-----------|
| **BFF Pattern** | Camada dedicada para frontend web |
| **API Gateway** | Roteamento, rate limiting (existente) |
| **Repository** | Abstracacao de acesso a dados (se aplicavel) |
| **Circuit Breaker** | Protecao contra falhas em cascata (_a definir_) |
| **Retry with Backoff** | Recuperacao de falhas transitorias |

### 5.12 Autenticacao e Sessao

#### 5.12.1 Fluxo de Autenticacao

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

#### 5.12.2 Gestao de Sessao

| Aspecto | Decisao |
|---------|---------|
| **Identificador** | Cookie de sessao (HttpOnly, Secure) |
| **Token Storage** | Cache distribuido (chave = Session ID) |
| **Validacao** | App ou OTP (SCA) |
| **Propagacao** | Bearer token para backend services |

## Entregaveis

- [x] Diagrama de decomposicao de servicos
- [x] Arquitetura BFF documentada
- [ ] Especificacao de APIs completa (OpenAPI) - Em progresso
- [x] Padroes de comunicacao definidos
- [x] Modelo de dominio documentado (alto nivel)
- [x] Politicas de rate limiting (responsabilidade Gateway)
- [x] Padroes de resiliencia implementados
- [x] Estrategia de versionamento API
- [x] Mapa de dependencias

## Definicoes Utilizadas

- [x] [DEF-05-arquitetura-bff.md](../definitions/DEF-05-arquitetura-bff.md) - Status: completed
- [x] [DEF-05-api-design.md](../definitions/DEF-05-api-design.md) - Status: completed
- [x] [DEF-05-padroes-resiliencia.md](../definitions/DEF-05-padroes-resiliencia.md) - Status: completed

## Decisoes Referenciadas

- [x] [DEC-007-padrao-bff.md](../decisions/DEC-007-padrao-bff.md) - Status: accepted

## Itens Pendentes

| Item | Documento | Responsavel |
|------|-----------|-------------|
| Circuit Breaker (biblioteca, thresholds) | DEF-05-padroes-resiliencia | Arquitetura |
| Rate limiting values | DEF-05-padroes-resiliencia | Arquitetura |
| Health check frequency | DEF-05-padroes-resiliencia | Operacoes |
| Comunicacao assincrona | DEF-05-arquitetura-bff | Arquitetura |
| Escalabilidade BFF | DEF-05-arquitetura-bff | Arquitetura |
| Politica deprecacao API | DEF-05-api-design | Arquitetura |
| Tratamento de erros (estrutura) | DEF-05-api-design | Desenvolvimento |
| Cache headers HTTP | DEF-05-api-design | Desenvolvimento |
