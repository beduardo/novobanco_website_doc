---
id: "SEC-05"
title: "Arquitetura Backend e Servicos"
status: "in-progress"
created: "2026-01-03"
updated: "2026-01-03"
depends-on-definitions:
  - "DEF-07"
  - "DEF-11"
  - "DEF-12"
  - "DEF-15"
  - "DEF-13"
  - "DEF-14"
depends-on-decisions:
  - "DEC-007"
  - "DEC-010"
  - "DEC-016"
word-count: 1377
---

# 5. Arquitetura Backend & Servicos

## Proposito

Definir a decomposicao de servicos, arquitetura de API, comunicacao, modelo de dominio, rate limiting, resiliencia, versionamento e especificacao de APIs para o HomeBanking Web.

## Conteudo

### 5.1 Decomposicao de Servicos

> **Diagrama de Arquitetura:** Ver [Secção 3.2 - Diagrama Conceptual](SEC-03-visao-geral-solucao.md#32-diagrama-conceptual) para a visão geral da arquitetura.

A decomposição de serviços segue a arquitectura de referência definida na secção 3.2:

| Componente | Tipo | Acao | Tecnologia |
|------------|------|------|------------|
| Frontend Web | Novo | Desenvolver | React + TypeScript |
| BFF Web | Novo | Desenvolver | C# .NET 8 |
| API Gateway | Existente | Reutilizar | IBM |
| Siebel (Backend Principal) | Existente | Reutilizar | Valida tokens |
| Outros Backend Services | Existente | Reutilizar | A identificar |
| Serviços Azure | Existente | Reutilizar | Acesso direto pelo BFF |

#### Notas de Integração

| Fluxo | Autenticação | Observação |
|-------|--------------|------------|
| Frontend → BFF | Cookie de sessão | HttpOnly, Secure |
| BFF → API Gateway (IBM) | ClientID + ClientSecret | Para serviços via Siebel |
| BFF → MicroService | Via API Gateway IBM | MicroService acedido via Gateway (Protocolo Omni) |
| BFF → Serviços Azure | Direto | Serviços a identificar |
| API Gateway → Siebel | Bearer Token | **Siebel valida o token** |

> **Nota - Autenticação:** A autenticação é orquestrada pelo MicroService, que interage com o Siebel (AUT_004, AUT_001). O BFF gere a sessão web (cookies, cache de tokens) e propaga o cookie de sessão; a lógica de autenticação reside no MicroService e a validação final no Siebel.

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
| **Container** | Assente em OpenShift |
| **Observabilidade** | ELK Stack |

#### 5.2.3 Responsabilidades

| Responsabilidade | Implementado | Observacao |
|------------------|--------------|------------|
| Agregacao de chamadas | Sim | Combinar multiplas chamadas backend |
| Transformacao de dados | Sim | Adaptar formato para frontend |
| Cache | Sim | Sessao e tokens |
| Autenticacao/Autorizacao | Sim | OAuth 1.1, validacao de sessao |
| Rate Limiting | Nao | Responsabilidade do Gateway |

### 5.3 Arquitetura API

#### 5.3.1 Estilo e Formato

| Aspecto | Decisao |
|---------|---------|
| **Estilo** | REST |
| **Formato** | JSON |
| **Compressao** | gzip |
| **Especificacao** | OpenAPI 3.1 |

#### 5.3.2 Versionamento

| Aspecto | Decisao | Exemplo |
|---------|---------|---------|
| **Estrategia** | URL path | `/web/ocb/bst/` |
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
participant "F5" as F5
participant "BFF" as BFF
participant "MS" as MS
participant "API Gateway\n(IBM)" as GW
participant "Siebel" as SIEBEL

FE -> F5 : REST/HTTPS\n(Cookie sessao)
activate F5

F5 -> BFF : REST/HTTPS\n(Cookie sessao)
activate BFF

BFF -> BFF : Validar sessao\n(Cache lookup)

alt Servicos com acesso direto ao Siebel (sem MS)
    BFF -> GW : REST\n(clientid + secret)
    activate GW
    note right of GW: Routing apenas\n(sem autenticação)

    GW -> SIEBEL : REST\n(Bearer token)
    activate SIEBEL
    note right of SIEBEL: **Valida clientid+secret**\n**e Bearer Token**

    SIEBEL --> GW : JSON
    deactivate SIEBEL

    GW --> BFF : JSON
    deactivate GW

else Servicos delegados ao MicroService (com integracao Siebel)
    BFF -> GW : REST\n(clientid + secret)
    activate GW
    note right of GW: Routing para MicroService

    GW -> MS : REST\n(Omni)
    activate MS

    MS -> GW : REST\n(clientid + secret)
    note right of GW: Routing para Siebel

    GW -> SIEBEL : REST\n(Bearer token)
    activate SIEBEL

    SIEBEL --> GW : JSON
    deactivate SIEBEL

    GW --> MS : JSON

    MS --> GW : JSON
    deactivate MS

    GW --> BFF : JSON
    deactivate GW

else Servicos delegados ao MicroService (autonomo, sem Siebel)
    BFF -> GW : REST\n(clientid + secret)
    activate GW
    note right of GW: Routing para MicroService

    GW -> MS : REST\n(Omni)
    activate MS
    note right of MS: Logica propria\nsem integracao Siebel

    MS --> GW : JSON
    deactivate MS

    GW --> BFF : JSON
    deactivate GW

end

BFF -> BFF : Transformar/Agregar
BFF --> FE : JSON
deactivate BFF

@enduml
```


| Comunicacao | Protocolo | Autenticacao | Observação |
|-------------|-----------|--------------|------------|
| Frontend → BFF | REST/HTTPS | Cookie de sessao (HttpOnly, Secure) | - |
| BFF → API Gateway (IBM) | REST | ClientID + ClientSecret | Ponto de entrada para Siebel e MicroService |
| API Gateway → MicroService | REST (Omni) | Roteado pelo GW | MicroService pode ou não precisar do Siebel |
| MicroService → API Gateway (IBM) | REST | ClientID + ClientSecret | Apenas quando MicroService necessita do Siebel |
| API Gateway → Siebel | REST | Bearer Token (propagado) | **Siebel valida o token** |

> **Nota:** O BFF não tem API Gateway à frente. O API Gateway (IBM) é o ponto de entrada para Siebel **e** MicroService — o BFF roteia ambos via Gateway.
> **Nota:** Não há dados críticos no BFF

> **Nota Importante - Validação de Token:** O API Gateway (IBM) faz **apenas routing**, sem realizar autenticação. Toda a autenticação (validação de clientid+secret e validação do Bearer Token do utilizador) é realizada pelo **Siebel**. Serviços backend que não suportem Bearer Token diretamente são acedidos exclusivamente através do Siebel, que actua como camada de mediação.

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
| **Responsabilidade** | API Gateway IBM (para chamadas aos Backend Services) |
| **No BFF** | Não implementado (BFF não tem APIGW à frente) |
| **Limites** | _A definir_ |
| **Resubmissões** | _A definir_ - Estratégia para pedidos duplicados |
| **Comunicacao** | Mensagem de erro informando necessidade de aguardar |

> **Nota:** O BFF não tem API Gateway à frente, pelo que o rate limiting é aplicado apenas nas chamadas do BFF para os Backend Services através do API Gateway IBM.

### 5.7 Resiliencia

| Padrao | Status | Observacao |
|--------|--------|------------|
| **Retry** | Implementado | Exponential backoff (configuravel) |
| **Timeout** | Implementado | Configuravel por endpoint |
| **Fallback** | Parcial | Apenas autenticacao |
| **Health Checks** | Implementado | Liveness + Readiness probes |
| **Circuit Breaker** | A definir | Proposta: Polly |
| **Bulkhead** | A avaliar | Depende da organização de serviços |

> **Nota - Organização de Serviços:** A arquitectura define um único MicroService Pod (DEC-016). A necessidade de Bulkhead deve ser avaliada internamente ao MicroService, por domínio funcional (ex: separação de threads/pools para operações críticas vs operações de consulta).

### 5.8 Versionamento API

| Aspecto | Decisao |
|---------|---------|
| **Estrategia** | URL path versioning |
| **Formato** | `/api/v{major}/resource` (rever em tempo de projeto) |
| **Politica Deprecacao** | _A definir_ |

### 5.9 Especificacao API

| Aspecto | Decisao |
|---------|---------|
| **Formato** | OpenAPI 3.1 |
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

> **Pendência:** Validar com negócio se degradação graceful sem logs é aceitável ou se é necessário fallback alternativo.

### 5.11 Autenticacao e Sessao

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
- [DEC-011-diagrama-arquitetura-unico.md](../decisions/DEC-011-diagrama-arquitetura-unico.md) - Diagrama de referência único
- [DEC-016-microservice-como-pod-unico.md](../decisions/DEC-016-microservice-como-pod-unico.md) - MicroService como Pod único (via Gateway)
