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

> **Secao relacionada:** [5 - Arquitetura Backend & Servicos](../sections/SEC-05-arquitetura-backend-servicos.md)

## Contexto

Definir a arquitetura do Backend for Frontend (BFF) do HomeBanking Web, que servira como camada de agregacao e transformacao entre o frontend web e os servicos backend existentes.

## Perguntas a Responder

### Tecnologia
1. Qual linguagem/framework sera utilizado no BFF (Node.js, Java Spring, .NET, Go)?
    C# .NET 8

2. Ha preferencia por frameworks especificos?
    Não.

3. Ha restricoes de tecnologia impostas pelo ambiente OpenShift?
    Não.

### Responsabilidades
4. Quais responsabilidades o BFF deve assumir?
   - Agregacao de chamadas? Sim
   - Transformacao de dados? Sim
   - Cache? Sim
   - Autenticacao/Autorizacao? Sim
   - Rate limiting? Não. Isso ficará a cargo do Gateway.

### Comunicacao
5. Como o BFF comunicara com os servicos backend (REST, gRPC, GraphQL)?
    REST

6. Ha requisitos de comunicacao assincrona (message queues)?
    Necessita aprofundamento

### Escalabilidade
7. Quais sao os requisitos de escalabilidade do BFF?
    Ainda não definidos

8. Ha requisitos de auto-scaling?
    Ainda não definidos

### Seguranca
9. Como sera tratada a autenticacao entre frontend e BFF?
    Deverá utilizar um fluxo pré definido, especificado em @DEF-05-autenticacao-oauth.md e @DEF-05-authentication-oauth-flow.md.
    Em resumo, o frontend iniciará a autenticação com o BFF que utilizará algum sistema de validação (App ou OTP) para validar a sessão. Ainda há detalhes a serem definidos, mas o fluxo básico já está bem definido.

10. Como sera tratada a autenticacao entre BFF e backend services?
    O BFF utilizará o token do utilizador para fazer suas requisições. Este token estará armazenado em um cache de sessão e a chave para este cache será o cookie de sessão (gerado no momento da auteticação) que o utilizador utilizará para acionar o BFF.

## Decisoes

### Stack Tecnologica BFF
- **Decisao:** C# .NET 8
- **Justificacao:** Stack enterprise, boa performance, suporte a containers
- **Alternativas consideradas:** Node.js, Java Spring, Go (descartados)

### Responsabilidades do BFF
- **Decisao:**
  - Agregacao de chamadas: Sim
  - Transformacao de dados: Sim
  - Cache: Sim
  - Autenticacao/Autorizacao: Sim
  - Rate limiting: Nao (responsabilidade do Gateway)
- **Justificacao:** BFF como camada de orquestracao e seguranca para o canal web
- **Alternativas consideradas:** BFF thin (descartado por necessidade de agregacao)

### Protocolo de Comunicacao
- **Decisao:** REST para comunicacao com backend services
- **Justificacao:** Alinhamento com APIs existentes da app mobile
- **Alternativas consideradas:** gRPC (descartado por compatibilidade), GraphQL

### Comunicacao Assincrona
- **Decisao:** _A definir_ - Necessita aprofundamento
- **Justificacao:** Avaliar necessidade de message queues
- **Alternativas consideradas:** RabbitMQ, Azure Service Bus, Kafka

### Estrategia de Cache
- **Decisao:** Cache de sessao para tokens de utilizador
- **Justificacao:** Token do utilizador armazenado em cache, chave = cookie de sessao
- **Alternativas consideradas:** Cache distribuido (Redis), in-memory

### Escalabilidade
- **Decisao:** _A definir_ - Requisitos ainda nao definidos
- **Justificacao:** Dependente de definicao de carga esperada
- **Alternativas consideradas:** Auto-scaling horizontal em OpenShift

### Autenticacao Frontend-BFF
- **Decisao:** Fluxo OAuth pre-definido com validacao via App ou OTP
  - Frontend inicia autenticacao com BFF
  - BFF valida sessao via sistema de validacao (App ou OTP)
  - Cookie de sessao gerado no momento da autenticacao
- **Justificacao:** Fluxo seguro com SCA, detalhes em documentos dedicados
- **Alternativas consideradas:** JWT stateless (descartado por requisitos de sessao)

### Autenticacao BFF-Backend
- **Decisao:** Token do utilizador propagado nas requisicoes
  - Token armazenado em cache de sessao
  - Chave do cache = cookie de sessao do utilizador
- **Justificacao:** Propagacao de identidade para backend services
- **Alternativas consideradas:** Service account (descartado por requisitos de auditoria)

## Restricoes Conhecidas

- Deploy em containers OpenShift
- Integracao com API Gateway existente
- Isolamento de sistemas legados
- Stack ELK para observabilidade

## Decisoes Relacionadas

- [DEC-007-padrao-bff.md](../decisions/DEC-007-padrao-bff.md) - Padrao BFF
- [DEC-010-stack-tecnologica-backend.md](../decisions/DEC-010-stack-tecnologica-backend.md) - Stack tecnologica backend

## Referencias

- [DEF-03-principios-arquitetura.md](DEF-03-principios-arquitetura.md) - Decisao de BFF
- Documentacao API Gateway existente (a fornecer)
- Documentacao Backend Services (a fornecer)
