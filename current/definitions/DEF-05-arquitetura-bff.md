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

## Dependências de Backend

O BFF comunica directamente com múltiplos backends, cada um com o seu protocolo específico:

| Backend | Protocolo | Propósito | Via Gateway |
|---------|-----------|-----------|-------------|
| **ApiPsd2** | OAuth + SHA256 | Autenticação PSD2 | Não (directo) |
| **ApiBBest** | OAuth 1.1 HMAC | APIs bancárias principais | Não (directo) |
| **Microservices** | Protocolo Omni | Lógica de Negócio | Não (directo) |
| **Siebel** | BEST | Lógica de negócio core | **Sim** (API Gateway IBM) |
| **Serviços Azure** | REST | Serviços cloud | Não (directo) |

> **Nota:** O API Gateway IBM é utilizado **apenas** para comunicação com o Siebel.

### ApiPsd2 como Dependência

O BFF atua como intermediário para todas as chamadas à ApiPsd2:

| Aspeto | Decisão |
|--------|---------|
| **Acesso** | Directo (sem API Gateway) |
| **Protocolo** | REST com OAuth |
| **Autenticação** | Assinatura SHA256 |
| **Responsabilidade** | BFF encapsula toda a complexidade |

**Componentes da Assinatura OAuth:**

| Componente | Descrição | Armazenamento |
|------------|-----------|---------------|
| `consumer_key` | Identificador do cliente OAuth | Secrets/Config |
| `secret_key` | Chave secreta para assinatura | Secrets |
| `access_token_anonimo` | Token para operações pré-login | Secrets/Config |
| `GUID` | Identificador único por request | Gerado em runtime |
| `timestamp` | Timestamp do request | Gerado em runtime |
| `version` | Versão do protocolo (1.1) | Config |

**Cálculo da Assinatura:**
```
assinatura = SHA256(consumer_key & GUID & timestamp & version & secret_key)
```

**Header de Identificação de Canal:**
```
x-nb-channel: best.spa
```

### Separação de Responsabilidades: BFF vs Microservices

| Componente | Responsabilidades |
|------------|-------------------|
| **BFF** | Lógica de UI/Apresentação, Agregação de dados, Transformação de formatos, Gestão de sessão web, Orquestração de chamadas |
| **Microservices** | Lógica de Negócio, Regras de domínio, Operações que requerem processamento além do Siebel, Serviços partilháveis entre canais |

> **Nota:** O BFF é inicialmente monolítico mas a arquitectura deve permitir evolução para microserviços.

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

- **Decisão:** Múltiplos protocolos conforme o destino
- **Justificação:** Alinhamento com APIs existentes e padronização de canais

| Origem | Destino | Protocolo |
|--------|---------|-----------|
| SPA | F5 | Protocolo Omni |
| F5 | BFF | Protocolo Omni |
| BFF | Microservices | Protocolo Omni |
| BFF | ApiPsd2 | OAuth + SHA256 |
| BFF | ApiBBest | OAuth 1.1 HMAC |
| BFF | API Gateway | BEST |
| API Gateway | Siebel | Siebel |

**Protocolo Omni:**
O Protocolo Omni é uma padronização sobre REST utilizada para comunicação entre o canal web (SPA) e o BFF, e entre BFF e Microservices. Esta abstração permite:
- Uniformização de contratos entre canais
- Evolução controlada das interfaces
- Separação clara entre protocolo de canal (Omni) e protocolo de backend (BEST)

### Comunicação Assíncrona
- **Decisão:** _A definir_ - Necessita aprofundamento
- **Justificação:** Avaliar necessidade de message queues
- **Alternativas consideradas:** RabbitMQ, Azure Service Bus, Kafka

### Estratégia de Cache e Sessão

- **Decisão:** Redis Cluster para gestão de sessões distribuídas
- **Justificação:** Alta disponibilidade, suporte a TTL, estruturas de dados flexíveis
- **Alternativas consideradas:** In-memory (descartado por não suportar múltiplas instâncias)

**Configuração de Sessão Web:**

| Aspeto | Decisão |
|--------|---------|
| **Tecnologia** | Redis Cluster |
| **Chave** | `token_sessao_spa` (cookie enviado pelo browser) |
| **Dados armazenados** | apiToken, refresh info, dados de sessão |
| **TTL** | Alinhado com timeout de sessão (30 min absoluto) |

**Dados Armazenados por Sessão:**

| Dado | Descrição | Origem |
|------|-----------|--------|
| `apiToken` | Token de acesso à ApiPsd2 | Resposta AUT_004 |
| `mustChangePassword` | Flag de alteração obrigatória | Resposta AUT_004 |
| `needStrongAuthentication` | Flag SCA necessário | Resposta AUT_004 |
| `firstLogin` | Flag primeiro acesso | Resposta AUT_004 |
| `user_context` | Dados do utilizador (não sensíveis) | Resposta login |

**Importante:** O `sasToken` retornado pela ApiPsd2 **não é utilizado** no canal web. Este token é específico para a app mobile.

### Cache de Dados Transitórios

O BFF implementa o padrão "Cache or API" para dados frequentemente acedidos:

| Dados | TTL Sugerido | Invalidação |
|-------|--------------|-------------|
| Dados do cliente (nome, contactos) | 30 min | Login, alteração de dados |
| Lista de contas | 5 min | Operação de conta |
| Lista de beneficiários | 15 min | Adição/remoção |
| Saldos | 1 min | Qualquer operação |
| Movimentos | 2 min | Operação de conta |
| Dados de home (agregados) | 5 min | Login |

**Configuração Redis:**

| Parâmetro | Valor |
|-----------|-------|
| Tipo | Redis Cluster (HA) |
| Serialização | JSON |
| Compressão | Opcional para payloads grandes |
| Política de evicção | LRU |

> **Nota:** TTLs são sugestões e devem ser ajustados conforme requisitos de negócio e carga.

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
- API Gateway IBM utilizado **apenas** para Siebel
- Acesso directo a ApiPsd2, ApiBBest e Microservices
- Isolamento de sistemas legados via BFF
- Stack ELK para observabilidade
- Redis Cluster para sessões distribuídas

## Decisões Relacionadas

- [DEC-007-padrao-bff.md](../decisions/DEC-007-padrao-bff.md) - Padrão BFF
- [DEC-010-stack-tecnologica-backend.md](../decisions/DEC-010-stack-tecnologica-backend.md) - Stack tecnológica backend

## Referências

- [DEF-03-principios-arquitetura.md](DEF-03-principios-arquitetura.md) - Decisão de BFF
- Documentação API Gateway existente (a fornecer)
- Documentação Backend Services (a fornecer)
