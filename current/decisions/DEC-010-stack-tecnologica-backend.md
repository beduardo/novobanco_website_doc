---
id: DEC-010-stack-tecnologica-backend
aliases:
  - Stack Tecnologica Backend
tags:
  - nextreality-novobanco-website-decisions
  - decisions
  - backend
  - bff
  - dotnet
approved: true
created: 2026-01-04
hubs:
  - "[[nextreality]]"
para-code: R
reviewed: true
status: accepted
---

# ADR-010: Stack Tecnologica Backend (BFF)

> **Related sections:** [5 - Arquitetura Backend & Servicos](../sections/SEC-05-arquitetura-backend-servicos.md), [9 - Integracao & Interfaces Externas](../sections/SEC-09-integracao-interfaces-externas.md)
> **Related definitions:** [DEF-05-arquitetura-bff.md](../definitions/DEF-05-arquitetura-bff.md), [DEF-05-api-design.md](../definitions/DEF-05-api-design.md)

## Status

Accepted

## Context

O HomeBanking Web necessita de um Backend for Frontend (BFF) que:
- Sirva como ponto unico de integracao entre frontend e sistemas backend
- Realize agregacao e transformacao de dados especifica para o canal web
- Gira sessoes e cache de tokens de utilizador
- Suporte integracao com Backend API (Facade) via REST
- Opere em ambiente containerizado OpenShift

### Business Goals
- Desacoplamento do frontend de complexidades dos sistemas backend
- Performance otimizada para o canal web
- Seguranca reforçada (tokens nao expostos ao browser)

### Technical Constraints
- Deploy em containers OpenShift
- Integracao com Azure API Gateway
- Stack ELK para observabilidade
- Backend API existente como unico ponto de acesso ao Core Banking

### Non-functional Requirements
- Disponibilidade: 99.9%
- RTO: 30 minutos
- RPO: 5 minutos
- Latencia: < 60s timeout padrao

## Decision

Adotar a seguinte stack tecnologica para o BFF:

| Camada | Tecnologia | Versao |
|--------|------------|--------|
| **Runtime** | .NET | 8 (LTS) |
| **Linguagem** | C# | 12 |
| **Framework Web** | ASP.NET Core | 8 |
| **Cache** | Redis | Latest |
| **HTTP Client** | HttpClientFactory | Built-in |
| **Serialization** | System.Text.Json | Built-in |
| **Logging** | Serilog | Latest |
| **Health Checks** | ASP.NET Core Health Checks | Built-in |

**Comunicacao:**
- **Frontend -> BFF:** REST/HTTPS com cookies HttpOnly para sessao
- **BFF -> Backend API:** REST/HTTPS com token do utilizador

**Cache Strategy:**
- Tokens de utilizador em Redis (chave = session cookie)
- Cache de dados publicos/semi-estaticos para SSG/ISR

**Resiliencia:**
- Retry: Exponential backoff (3 retries) para erros transientes
- Timeout: 60s padrao para todas as chamadas
- Circuit Breaker: A definir no assessment (Polly sugerido)

## Alternatives Considered

### Alternative 1: Node.js + Express/Fastify
- **Description:** Runtime Node.js com framework Express ou Fastify
- **Pros:** Mesmo ecossistema JavaScript do frontend, leve, rapido para I/O
- **Cons:** Menor performance para CPU-bound, tipagem dinamica
- **Why not chosen:** .NET oferece melhor performance e e stack enterprise consolidada

### Alternative 2: Java Spring Boot
- **Description:** Framework Spring Boot com Java 21
- **Pros:** Maduro, grande ecossistema enterprise, muitos developers
- **Cons:** Maior footprint de memoria, startup mais lento
- **Why not chosen:** .NET 8 oferece melhor performance em containers e startup mais rapido

### Alternative 3: Go (Golang)
- **Description:** Linguagem Go com frameworks como Gin ou Echo
- **Pros:** Excelente performance, binarios estaticos pequenos
- **Cons:** Ecossistema menor, menos developers no mercado portugues
- **Why not chosen:** Pool de desenvolvedores mais limitado para o mercado alvo

### Alternative 4: In-memory cache em vez de Redis
- **Description:** Cache de sessao em memoria do processo BFF
- **Pros:** Simplicidade, sem dependencia externa
- **Cons:** Nao suporta horizontal scaling, perda de sessoes em restart
- **Why not chosen:** Redis necessario para suportar multiplas instancias do BFF

## Consequences

### Positive
- Stack enterprise consolidada e bem suportada
- Excelente performance em containers
- Type safety com C#
- Integracao nativa com Azure (API Gateway, Redis Cache)
- Logging estruturado com Serilog
- Health checks nativos para OpenShift

### Negative
- Requer developers com experiencia .NET
- Compilacao mais lenta que linguagens interpretadas
- Curva de aprendizagem para equipas sem experiencia .NET

## Notes

- Versao .NET 8 LTS garante suporte ate Nov 2026
- Polly recomendado para circuit breaker (a confirmar no assessment)
- Serilog configurado para output compativel com ELK
- Redis pode ser Azure Cache for Redis ou instancia dedicada
