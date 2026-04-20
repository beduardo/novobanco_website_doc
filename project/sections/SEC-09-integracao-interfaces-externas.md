---
id: "SEC-09"
title: "Integração e Interfaces Externas"
status: "in-progress"
created: "2026-01-04"
updated: "2026-01-04"
depends-on-definitions:
  - "DEF-19"
depends-on-decisions:
  - "DEC-016"
  - "DEC-017"
  - "DEC-019"
  - "DEC-020"
  - "DEC-026"
word-count: 0
---

# 9. Integração & Interfaces Externas

## Definições e Decisões

> **Required definitions:** [DEF-19-integracao-interfaces.md](../definitions/DEF-19-integracao-interfaces.md)
> **Related decisions:**
> - [DEC-007-padrao-bff.md](../decisions/DEC-007-padrao-bff.md) - Status: accepted
> - [DEC-010-stack-tecnologica-backend.md](../decisions/DEC-010-stack-tecnologica-backend.md) - Status: accepted

## Propósito

Definir a arquitetura de integração do HomeBanking Web com sistemas externos, incluindo Core Banking, serviços de terceiros (KYC/AML, Notificações, Cartões), Open Banking PSD2, e mecanismos de comunicação assíncrona. Esta secção estabelece os padrões, SLAs e catálogo de integrações necessários para o funcionamento do canal web.

## Conteúdo

### 9.1 Visão Geral de Integrações

> **Diagrama de Arquitetura:** Ver [Secção 3.2 - Diagrama Conceptual](SEC-03-visao-geral-solucao.md#32-diagrama-conceptual) para a visão completa da arquitetura do sistema.

O HomeBanking Web segue uma arquitetura de integração em camadas, onde o **BFF (Backend for Frontend)** atua como ponto único de integração entre o frontend e todos os sistemas backend. Não há acesso directo do frontend a sistemas externos.

**Fluxo de Integração:**

| Origem | Destino | Protocolo | Autenticação | Observação |
|--------|---------|-----------|--------------|------------|
| Frontend → F5 | Omni | Cookie de sessão | HttpOnly, Secure, SameSite=Strict |
| F5 → BFF | Omni | Cookie de sessão (propagado) | - |
| BFF → Redis | - | - | Lookup/Store de sessão e tokens |
| BFF → API Gateway (IBM) | Omni / BEST | ClientID + ClientSecret | Siebel e MicroService (via GW) |
| API Gateway → MicroService | Omni | Roteado pelo GW | Lógica de negócio (canal web) |
| API Gateway → Siebel | Siebel | Bearer Token | **Siebel valida o token** |
| MicroService → API Gateway (IBM) | BEST | ClientID + ClientSecret | Quando MicroService necessita do Siebel |
| BFF → Backoffice de Configuração | REST/OAuth2 | OAuth2 client credentials (read-only) | Conteúdos anónimos e regras de negócio (DEC-020) |
| **App Mobile → API Gateway (IBM)** | Omni | Credenciais App | **Directo ao MicroService — sem BFF (DEC-019)** |

#### Princípios de Integração

| Princípio | Descrição |
|-----------|-----------|
| **BFF como Gateway** | Todas as integrações do canal web passam pelo BFF — excepção: App Mobile acede o MicroService directamente no fluxo QR Code (DEC-019) |
| **Backoffice de Configuração como integração directa** | O BFF acede os serviços Backoffice de Configuração directamente (sem IBM API Gateway), via REST/OAuth2 client credentials, pois são serviços anónimos sem contexto de sessão (DEC-020) |
| **Backend API (Facade)** | Ponto único de acesso aos sistemas Core Banking |
| **Reutilização** | Mesmas APIs utilizadas pela app mobile |
| **Transformação no BFF** | Adaptação de dados para necessidades específicas do canal web |


### 9.2 MicroService - Lógica de Negócio

O MicroService é um único Pod (.NET 8) de lógica de negócio acedido pelo BFF **via API Gateway IBM**, usando Protocolo Omni. No fluxo de autenticação QR Code, a App Mobile acede o MicroService **directamente via API Gateway IBM**, sem passar pelo BFF (DEC-019).

#### Características

| Aspecto | Valor |
|---------|-------|
| **Protocolo** | Omni (padronização sobre REST) |
| **Tecnologia** | .NET 8 |
| **Deploy** | Pod único em OpenShift |
| **Status** | A desenvolver |

#### Responsabilidades

| Responsabilidade | Descrição |
|------------------|-----------|
| Lógica de Negócio | Regras de domínio além do Siebel |
| Processamento | Operações que requerem processamento adicional |
| Partilha | Serviços reutilizáveis entre canais (futuramente) |

> **Pendência:** Identificar as responsabilidades específicas do MicroService.

### 9.3 Backoffice de Configuração

O **Backoffice de Configuração** constitui um ponto de integração externo distinto na arquitectura.
Os seus serviços são acedidos directamente pelo BFF — sem passar pelo IBM API Gateway ou middleware
BEST (DEC-020). São serviços anónimos: não registam qualquer informação de cliente.

#### Categorias de Serviços

**Conteúdos Dinâmicos**
Devolvem conteúdos para alimentar áreas dinâmicas da interface:
- Notícias, Artigos, Overlays, imagens associadas e publicidades
- Entidades para pagamentos, reminders e links de informação externa
- Temas de investimento, operações públicas de venda e lista de produtos activos

**Regras de Negócio e Dados de Suporte**
Devolvem regras e dados necessários à lógica de negócio no cliente:
- Taxas de simulação de rendimentos (produtos de reforma, contas margem e depósitos a prazo)
- Permissões de acesso e visualização de áreas, baseadas no perfil ou tipo de conta

**Controlos de UX**
Controlam como e quando surgem os pedidos de avaliação da app.

#### Características Técnicas

| Aspecto | Detalhe |
|---------|---------|
| **Tecnologia** | REST/JSON |
| **Infraestrutura** | Azure |
| **Autenticação** | OAuth2 client credentials (client_id + client_secret) |
| **Scope** | Read-only |
| **Anonimato** | Não registam informação de cliente |
| **Acesso** | Directo pelo BFF — sem IBM API Gateway (DEC-020) |

#### Serviços Identificados (DEC-026)

**Conteúdos Dinâmicos**

| Endpoint | Função | Acesso |
|----------|--------|--------|
| `advertising` | Publicidades / cards promocionais | Directo pelo BFF (OAuth2 client cred.) |
| `article` | Artigos de conteúdo | Directo pelo BFF (OAuth2 client cred.) |
| `overlay` | Overlays informativos | Directo pelo BFF (OAuth2 client cred.) |
| `externallink` | Links de informação externa | Directo pelo BFF (OAuth2 client cred.) |
| `opvs` | Operações públicas de venda | Directo pelo BFF (OAuth2 client cred.) |
| `investmentThemes` | Temas de investimento | Directo pelo BFF (OAuth2 client cred.) |

**Regras de Negócio e Dados de Suporte**

| Endpoint | Função | Acesso |
|----------|--------|--------|
| `accountRestriction` | Permissões de acesso e visualização de áreas por perfil/tipo de conta | Directo pelo BFF (OAuth2 client cred.) |
| `deposits` | Taxas de simulação de depósitos a prazo | Directo pelo BFF (OAuth2 client cred.) |
| `availableoptions` | Lista de produtos activos / opções disponíveis | Directo pelo BFF (OAuth2 client cred.) |
| `retirement` | Dados de produtos de reforma | Directo pelo BFF (OAuth2 client cred.) |
| `retirementSimulator` | Taxas de simulação de rendimentos para produtos de reforma | Directo pelo BFF (OAuth2 client cred.) |
| `marginAccounts` | Taxas de simulação para contas margem | Directo pelo BFF (OAuth2 client cred.) |
| `servicePaymentEntity` | Entidades para pagamentos de serviços | Directo pelo BFF (OAuth2 client cred.) |

**Controlos de UX**

| Endpoint | Função | Acesso |
|----------|--------|--------|
| `EvaluationFeedbackByArea` | Pedidos de avaliação da app por área | Directo pelo BFF (OAuth2 client cred.) |


### 9.4 Tratamento de Erros

#### Circuit Breaker

| Aspecto | Status |
|---------|--------|
| Implementação | Não implementado atualmente |
| Biblioteca | A decidir no assessment (Polly sugerido) |
| Thresholds | A definir |
| Tempo de recuperação | A definir |

#### Fallback

| Aspecto | Status |
|---------|--------|
| Integrações com fallback | Necessita aprofundamento |
| Comportamento degradado | Necessita aprofundamento |

#### Comunicação de Erros ao Utilizador

| Erro | Mensagem | Ação |
|------|----------|------|
| Timeout/Indisponibilidade | "Serviço temporariamente indisponível. Por favor aguarde." | Registo de log |
| Rate limiting | "Muitas tentativas. Por favor aguarde alguns segundos." | Registo de log |
| Erro de negócio | Mensagem específica da operação | Orientação ao utilizador |

### 9.6 SLAs de Integração

_Os SLAs de integração dependem de informações dos sistemas backend e fornecedores terceiros._

| Integração | Disponibilidade | Latência P95 | Timeout |
|------------|-----------------|--------------|---------|
| Siebel | Necessita aprofundamento | Necessita aprofundamento | 60s |

**Nota:** Janelas de manutenção programadas que afetam integrações necessitam aprofundamento.

### 9.7 Catálogo de Integrações

_O catálogo detalhado de integrações será documentado no assessment inicial do projeto._

| Aspecto | Status |
|---------|--------|
| Catálogo documentado | Necessita aprofundamento |
| Ferramenta de documentação | Necessita aprofundamento |
| Ambiente de sandbox | Necessita aprofundamento |

### 9.8 API Management

#### IBM API Gateway

O **IBM API Gateway** é o ponto central de routing entre o BFF e os Backend Services — roteia para o **Siebel** e para o **MicroService**.

> **Nota:** O BFF não tem API Gateway à frente. O API Gateway é utilizado para as chamadas do BFF ao Siebel e ao MicroService (DEC-016).

| Funcionalidade | Status |
|----------------|--------|
| **Gateway** | IBM API Gateway |
| **Autenticação BFF** | ClientID + ClientSecret |
| **Propagação Token** | Bearer Token para Siebel |
| **Rate limiting** | Necessita aprofundamento |
| **Throttling diferenciado** | Necessita aprofundamento |
| **Monitoring** | Necessita aprofundamento |


## Entregáveis

- [x] Diagrama de integração de alto nível
- [ ] Catálogo de integrações documentado
- [ ] Especificação de contratos de API (OpenAPI)
- [ ] Definição de SLAs por integração
- [x] Mapeamento de erros e fallbacks
- [ ] Documentação de fluxos assíncronos
- [ ] Matriz de dependências externas

## Definições Utilizadas

- [x] [DEF-19-integracao-interfaces.md](../definitions/DEF-19-integracao-interfaces.md) - Status: in-progress

## Decisões Referenciadas

- [x] [DEC-007-padrao-bff.md](../decisions/DEC-007-padrao-bff.md) - Status: accepted
- [x] [DEC-010-stack-tecnologica-backend.md](../decisions/DEC-010-stack-tecnologica-backend.md) - Status: accepted
- [x] [DEC-011-diagrama-arquitetura-unico.md](../decisions/DEC-011-diagrama-arquitetura-unico.md) - Status: accepted
- [x] [DEC-016-microservice-como-pod-unico.md](../decisions/DEC-016-microservice-como-pod-unico.md) - Status: accepted
- [x] [DEC-017-sem-websocket-no-canal-web.md](../decisions/DEC-017-sem-websocket-no-canal-web.md) - Status: accepted
- [x] [DEC-019-app-mobile-acede-microservice-diretamente-na-autenticacao-qr-code.md](../decisions/DEC-019-app-mobile-acede-microservice-diretamente-na-autenticacao-qr-code.md) - Status: accepted
- [x] [DEC-020-backoffice-de-configuracao-acedido-directamente-pelo-bff-via-rest-oauth2.md](../decisions/DEC-020-backoffice-de-configuracao-acedido-directamente-pelo-bff-via-rest-oauth2.md) - Status: accepted
- [x] [DEC-026-endpoints-do-backoffice-de-configura-o-identificados.md](../decisions/DEC-026-endpoints-do-backoffice-de-configura-o-identificados.md) - Status: accepted

