---
id: "SEC-09"
title: "Integracao e Interfaces Externas"
status: "in-progress"
created: "2026-01-04"
updated: "2026-01-04"
depends-on-definitions:
  - "DEF-19"
depends-on-decisions: []
word-count: 0
---

# 9. Integracao & Interfaces Externas

## Definições e Decisões

> **Required definitions:** [DEF-19-integracao-interfaces.md](../definitions/DEF-19-integracao-interfaces.md)
> **Related decisions:**
> - [DEC-007-padrao-bff.md](../decisions/DEC-007-padrao-bff.md) - Status: accepted
> - [DEC-010-stack-tecnologica-backend.md](../decisions/DEC-010-stack-tecnologica-backend.md) - Status: accepted

## Proposito

Definir a arquitetura de integracao do HomeBanking Web com sistemas externos, incluindo Core Banking, servicos de terceiros (KYC/AML, Notificacoes, Cartoes), Open Banking PSD2, e mecanismos de comunicacao assincrona. Esta secao estabelece os padroes, SLAs e catalogo de integracoes necessarios para o funcionamento do canal web.

## Conteudo

### 9.1 Visao Geral de Integracoes

> **Diagrama de Arquitetura:** Ver [Secção 3.2 - Diagrama Conceptual](SEC-03-visao-geral-solucao.md#32-diagrama-conceptual) para a visão completa da arquitetura do sistema.

O HomeBanking Web segue uma arquitetura de integracao em camadas, onde o **BFF (Backend for Frontend)** atua como ponto unico de integracao entre o frontend e todos os sistemas backend. Nao ha acesso direto do frontend a sistemas externos.

**Fluxo de Integracao:**

| Origem | Destino | Protocolo | Autenticacao | Observacao |
|--------|---------|-----------|--------------|------------|
| Frontend → F5 | Omni | Cookie de sessao | HttpOnly, Secure, SameSite=Strict |
| F5 → BFF | Omni | Cookie de sessao (propagado) | - |
| BFF → Redis | - | - | Lookup/Store de sessao e tokens |
| BFF → Microservices | Omni | Token de sessao | Logica de negocio (directo) |
| BFF → API Gateway (IBM) | BEST | ClientID + ClientSecret | **Apenas para Siebel** |
| BFF → Servicos Azure | REST | Direto | Servicos a identificar |
| API Gateway → Siebel | Siebel | Bearer Token | **Siebel valida o token** |
| MS → Siebel | Siebel | - | Logica de negocio |

#### Principios de Integracao

| Principio | Descricao |
|-----------|-----------|
| **BFF como Gateway** | Todas as integracoes passam pelo BFF, nunca acesso direto do frontend |
| **Backend API (Facade)** | Ponto unico de acesso aos sistemas Core Banking |
| **Reutilizacao** | Mesmas APIs utilizadas pela app mobile |
| **Transformacao no BFF** | Adaptacao de dados para necessidades especificas do canal web |


### 9.2 Microservices - Logica de Negocio

Os Microservices sao uma camada de logica de negocio acedida **directamente pelo BFF** via Protocolo Omni.

#### Caracteristicas

| Aspecto | Valor |
|---------|-------|
| **Protocolo** | Omni (padronizacao sobre REST) |
| **Tecnologia** | .NET 8 |
| **Deploy** | Containers OpenShift |
| **Status** | A desenvolver |

#### Responsabilidades

| Responsabilidade | Descricao |
|------------------|-----------|
| Logica de Negocio | Regras de dominio alem do Siebel |
| Processamento | Operacoes que requerem processamento adicional |
| Partilha | Servicos reutilizaveis entre canais (futuramente) |

> **Pendencia:** Identificar quais MS serao desenvolvidos e suas responsabilidades especificas.

### 9.3 Servicos Fora do Middleware BEST

Existem servicos utilizados pela app mobile que nao passam pelo middleware BEST e sao acedidos diretamente. Estes servicos precisam ser identificados e avaliados para o canal web.

> **Nota:** Conforme arquitectura definida, o BFF acede directamente ao Siebel e aos Microservices. O API Gateway IBM e utilizado para routing dos pedidos ao Siebel.

#### Servicos Identificados

| Servico | Tipo | Funcao | Acesso |
|---------|------|--------|--------|
| Servicos Azure | Cloud | _A identificar_ | Directo pelo BFF |

#### Questoes a Resolver

| Questao | Responsavel | Status |
|---------|-------------|--------|
| Lista completa de servicos Azure acedidos diretamente | Cliente | Pendente |


### 9.4 Message Broker

A tecnologia de Message Broker e os eventos a serem publicados/consumidos pelo canal web serao definidos no assessment inicial do projeto.

| Aspecto | Status |
|---------|--------|
| **Tecnologia** | Kafka ou JMS (a definir) |
| Eventos publicados | Necessita aprofundamento |
| Eventos consumidos | Necessita aprofundamento |
| Ordenacao/Exactly-once | Necessita aprofundamento |
| Dead-letter strategy | Necessita aprofundamento |

> **Nota:** RabbitMQ e Azure Service Bus não são opções consideradas.

### 9.5 Tratamento de Erros

#### Circuit Breaker

| Aspecto | Status |
|---------|--------|
| Implementacao | Nao implementado atualmente |
| Biblioteca | A decidir no assessment (Polly sugerido) |
| Thresholds | A definir |
| Tempo de recuperacao | A definir |

#### Fallback

| Aspecto | Status |
|---------|--------|
| Integracoes com fallback | Necessita aprofundamento |
| Comportamento degradado | Necessita aprofundamento |

#### Comunicacao de Erros ao Utilizador

| Erro | Mensagem | Acao |
|------|----------|------|
| Timeout/Indisponibilidade | "Servico temporariamente indisponivel. Por favor aguarde." | Registo de log |
| Rate limiting | "Muitas tentativas. Por favor aguarde alguns segundos." | Registo de log |
| Erro de negocio | Mensagem especifica da operacao | Orientacao ao utilizador |

### 9.6 SLAs de Integracao

_Os SLAs de integracao dependem de informacoes dos sistemas backend e fornecedores terceiros._

| Integracao | Disponibilidade | Latencia P95 | Timeout |
|------------|-----------------|--------------|---------|
| Siebel | Necessita aprofundamento | Necessita aprofundamento | 60s |

**Nota:** Janelas de manutencao programadas que afetam integracoes necessitam aprofundamento.

### 9.7 Catalogo de Integracoes

_O catalogo detalhado de integracoes sera documentado no assessment inicial do projeto._

| Aspecto | Status |
|---------|--------|
| Catalogo documentado | Necessita aprofundamento |
| Ferramenta de documentacao | Necessita aprofundamento |
| Ambiente de sandbox | Necessita aprofundamento |

### 9.8 API Management

#### IBM API Gateway

O **IBM API Gateway** e utilizado como ponto central de gestao de APIs entre o BFF e os Backend Services (Siebel e outros).

> **Nota:** O BFF não tem API Gateway à frente. O API Gateway é utilizado apenas para as chamadas do BFF aos Backend Services.

| Funcionalidade | Status |
|----------------|--------|
| **Gateway** | IBM API Gateway |
| **Autenticacao BFF** | ClientID + ClientSecret |
| **Propagacao Token** | Bearer Token para Siebel |
| **Rate limiting** | Necessita aprofundamento |
| **Throttling diferenciado** | Necessita aprofundamento |
| **Monitoring** | Necessita aprofundamento |


## Entregáveis

- [x] Diagrama de integracao de alto nivel
- [ ] Catalogo de integracoes documentado
- [ ] Especificacao de contratos de API (OpenAPI)
- [ ] Definicao de SLAs por integracao
- [x] Mapeamento de erros e fallbacks
- [ ] Documentacao de fluxos assincronos
- [ ] Matriz de dependencias externas

## Definições Utilizadas

- [x] [DEF-19-integracao-interfaces.md](../definitions/DEF-19-integracao-interfaces.md) - Status: in-progress

## Decisões Referenciadas

- [x] [DEC-007-padrao-bff.md](../decisions/DEC-007-padrao-bff.md) - Status: accepted
- [x] [DEC-010-stack-tecnologica-backend.md](../decisions/DEC-010-stack-tecnologica-backend.md) - Status: accepted
- [x] [DEC-011-diagrama-arquitetura-unico.md](../decisions/DEC-011-diagrama-arquitetura-unico.md) - Status: accepted

## Itens Pendentes

| Item | Responsavel | Prioridade |
|------|-------------|------------|
| **Servicos fora do middleware BEST** | Cliente | **Alta** |
| Tecnologia de Message Broker | Arquitetura | Alta |
| SLAs de integracao com Backend API | Arquitetura + Cliente | Alta |
| Providers de notificacao (SMS, Push, Email) | Assessment | Media |
| Open Banking PSD2 - APIs expostas/consumidas | Assessment | Media |
| Circuit Breaker - biblioteca e configuracao | Assessment | Media |
| Abertura de conta - interacoes com terceiros | Cliente | Media |
| Notificacoes de transferencia na app mobile | Cliente | Baixa |
| Catalogo de APIs documentado | Desenvolvimento | Baixa |
| Ambiente de sandbox | Infraestrutura | Baixa |
