---
id: DEF-05-arquitetura-bff
aliases:
  - Arquitetura BFF
tags:
  - nextreality-novobanco-website-definitions
  - definitions
  - bff
  - backend
approved: true
created: 2026-01-03
hubs:
  - "[[nextreality]]"
para-code: R
reviewed: true
status: completed
---

# DEF-05: Arquitetura BFF

> **Secção relacionada:** [5 - Arquitetura Backend & Serviços](../sections/SEC-05-arquitetura-backend-servicos.md)

## Contexto

Definir a arquitetura do Backend for Frontend (BFF) do HomeBanking Web, que servirá como camada de agregação e transformação entre o frontend web e os serviços backend existentes.

## Perguntas a Responder

### Tecnologia
1. Qual linguagem/framework será utilizado no BFF (Node.js, Java Spring, .NET, Go)?
    C# .NET 8

2. Há preferência por frameworks específicos?
    Não.

3. Há restrições de tecnologia impostas pelo ambiente OpenShift?
    Não.

### Responsabilidades
4. Quais responsabilidades o BFF deve assumir?
   - Agregação de chamadas? Sim
   - Transformação de dados? Sim
   - Cache? Sim
   - Autenticação/Autorização? Sim
   - Rate limiting? Não. Isso ficará a cargo do Gateway.

### Comunicação
5. Como o BFF comunicará com os serviços backend (REST, gRPC, GraphQL)?
    REST

6. Há requisitos de comunicação assíncrona (message queues)?
    Ver [DEF-09-integracao-interfaces.md](DEF-09-integracao-interfaces.md) para detalhes de Message Broker

### Escalabilidade
> **Nota:** Detalhes de auto-scaling em [DEF-12-desempenho-fiabilidade.md](DEF-12-desempenho-fiabilidade.md)

7. Quais são os requisitos de escalabilidade do BFF?
    Suportar 400 utilizadores concorrentes (DEF-02-requisitos-nao-funcionais)

### Sessão Distribuída (NOVO)

8. Como a sessão será compartilhada entre múltiplas instâncias do BFF?
    Redis Cluster como cache de sessão distribuído

9. Qual a estratégia de degradação graciosa em caso de falha de dependências?
    Necessita aprofundamento. Considerar: fallback para operações críticas, circuit breaker

### Segurança
10. Como será tratada a autenticação entre frontend e BFF?
    Fluxo OAuth pré-definido (ver DEF-05-autenticacao-oauth.md). Frontend inicia autenticação, BFF valida via App ou OTP.

11. Como será tratada a autenticação entre BFF e backend services?
    O BFF utilizará o token do utilizador para fazer suas requisições. Este token estará armazenado em um cache de sessão e a chave para este cache será o cookie de sessão (gerado no momento da autenticação) que o utilizador utilizará para acionar o BFF.

## Decisões

### Stack Tecnológica BFF
- **Decisão:** C# .NET 8
- **Justificação:** Stack enterprise, boa performance, suporte a containers
- **Alternativas consideradas:** Node.js, Java Spring, Go (descartados)

### Responsabilidades do BFF
- **Decisão:**
  - Agregação de chamadas: Sim
  - Transformação de dados: Sim
  - Cache: Sim
  - Autenticação/Autorização: Sim
  - Rate limiting: Não (responsabilidade do Gateway)
- **Justificação:** BFF como camada de orquestração e segurança para o canal web
- **Alternativas consideradas:** BFF thin (descartado por necessidade de agregação)

### Protocolo de Comunicação
- **Decisão:** REST para comunicação com backend services
- **Justificação:** Alinhamento com APIs existentes da app mobile
- **Alternativas consideradas:** gRPC (descartado por compatibilidade), GraphQL

### Comunicação Assíncrona
- **Decisão:** _A definir_ - Necessita aprofundamento
- **Justificação:** Avaliar necessidade de message queues
- **Alternativas consideradas:** RabbitMQ, Azure Service Bus, Kafka

### Estratégia de Cache
- **Decisão:** Cache de sessão para tokens de utilizador
- **Justificação:** Token do utilizador armazenado em cache, chave = cookie de sessão
- **Alternativas consideradas:** Cache distribuído (Redis), in-memory

### Escalabilidade
- **Decisão:** _A definir_ - Requisitos ainda não definidos
- **Justificação:** Dependente de definição de carga esperada
- **Alternativas consideradas:** Auto-scaling horizontal em OpenShift

### Autenticação Frontend-BFF
- **Decisão:** Fluxo OAuth pré-definido com validação via App ou OTP
  - Frontend inicia autenticação com BFF
  - BFF valida sessão via sistema de validação (App ou OTP)
  - Cookie de sessão gerado no momento da autenticação
- **Justificação:** Fluxo seguro com SCA, detalhes em documentos dedicados
- **Alternativas consideradas:** JWT stateless (descartado por requisitos de sessão)

### Autenticação BFF-Backend
- **Decisão:** Token do utilizador propagado nas requisições
  - Token armazenado em cache de sessão
  - Chave do cache = cookie de sessão do utilizador
- **Justificação:** Propagação de identidade para backend services
- **Alternativas consideradas:** Service account (descartado por requisitos de auditoria)

## Restrições Conhecidas

- Deploy em containers OpenShift
- Integração com API Gateway existente
- Isolamento de sistemas legados
- Stack ELK para observabilidade

## Decisões Relacionadas

- [DEC-007-padrao-bff.md](../decisions/DEC-007-padrao-bff.md) - Padrão BFF
- [DEC-010-stack-tecnologica-backend.md](../decisions/DEC-010-stack-tecnologica-backend.md) - Stack tecnológica backend

## Referências

- [DEF-03-principios-arquitetura.md](DEF-03-principios-arquitetura.md) - Decisão de BFF
- Documentação API Gateway existente (a fornecer)
- Documentação Backend Services (a fornecer)
