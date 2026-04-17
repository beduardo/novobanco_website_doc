---
id: "SEC-09"
title: "Integracao e Interfaces Externas"
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
| BFF → API Gateway (IBM) | Omni / BEST | ClientID + ClientSecret | Siebel e MicroService (via GW) |
| API Gateway → MicroService | Omni | Roteado pelo GW | Logica de negocio (canal web) |
| API Gateway → Siebel | Siebel | Bearer Token | **Siebel valida o token** |
| MicroService → API Gateway (IBM) | BEST | ClientID + ClientSecret | Quando MicroService necessita do Siebel |
| BFF → Backoffice de Configuração | REST/OAuth2 | OAuth2 client credentials (read-only) | Conteudos anonimos e regras de negocio (DEC-020) |
| **App Mobile → API Gateway (IBM)** | Omni | Credenciais App | **Directo ao MicroService — sem BFF (DEC-019)** |

#### Principios de Integracao

| Principio | Descricao |
|-----------|-----------|
| **BFF como Gateway** | Todas as integracoes do canal web passam pelo BFF — excepção: App Mobile acede o MicroService directamente no fluxo QR Code (DEC-019) |
| **Backoffice de Configuração como integração directa** | O BFF acede os servicos Backoffice de Configuracao directamente (sem IBM API Gateway), via REST/OAuth2 client credentials, pois sao servicos anonimos sem contexto de sessao (DEC-020) |
| **Backend API (Facade)** | Ponto unico de acesso aos sistemas Core Banking |
| **Reutilizacao** | Mesmas APIs utilizadas pela app mobile |
| **Transformacao no BFF** | Adaptacao de dados para necessidades especificas do canal web |


### 9.2 MicroService - Logica de Negocio

O MicroService é um único Pod (.NET 8) de logica de negocio acedido pelo BFF **via API Gateway IBM**, usando Protocolo Omni. No fluxo de autenticação QR Code, a App Mobile acede o MicroService **directamente via API Gateway IBM**, sem passar pelo BFF (DEC-019).

#### Caracteristicas

| Aspecto | Valor |
|---------|-------|
| **Protocolo** | Omni (padronizacao sobre REST) |
| **Tecnologia** | .NET 8 |
| **Deploy** | Pod único em OpenShift |
| **Status** | A desenvolver |

#### Responsabilidades

| Responsabilidade | Descricao |
|------------------|-----------|
| Logica de Negocio | Regras de dominio alem do Siebel |
| Processamento | Operacoes que requerem processamento adicional |
| Partilha | Servicos reutilizaveis entre canais (futuramente) |

> **Pendencia:** Identificar as responsabilidades especificas do MicroService.

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

#### Serviços Identificados

| Serviço | Tipo | Função | Acesso |
|---------|------|--------|--------|
| Conteudos (Noticias, Artigos, Overlays, Publicidades) | Backoffice de Configuracao | Conteudos dinamicos para a UI | Directo pelo BFF (OAuth2 client cred.) |
| Regras de negocio (taxas simulacao, permissoes, temas investimento) | Backoffice de Configuracao | Configuracao e regras de negocio | Directo pelo BFF (OAuth2 client cred.) |
| Controlos UX (pedidos de avaliacao da APP) | Backoffice de Configuracao | Logica de apresentacao | Directo pelo BFF (OAuth2 client cred.) |

#### Questões a Resolver

| Questão | Responsável | Status |
|---------|-------------|--------|
| Lista completa de endpoints Backoffice de Configuracao | Cliente | Pendente |


### 9.4 Tratamento de Erros

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

O **IBM API Gateway** é o ponto central de routing entre o BFF e os Backend Services — roteia para o **Siebel** e para o **MicroService**.

> **Nota:** O BFF não tem API Gateway à frente. O API Gateway é utilizado para as chamadas do BFF ao Siebel e ao MicroService (DEC-016).

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
- [x] [DEC-016-microservice-como-pod-unico.md](../decisions/DEC-016-microservice-como-pod-unico.md) - Status: accepted
- [x] [DEC-017-sem-websocket-no-canal-web.md](../decisions/DEC-017-sem-websocket-no-canal-web.md) - Status: accepted
- [x] [DEC-019-app-mobile-acede-microservice-diretamente-na-autenticacao-qr-code.md](../decisions/DEC-019-app-mobile-acede-microservice-diretamente-na-autenticacao-qr-code.md) - Status: accepted
- [x] [DEC-020-backoffice-de-configuracao-acedido-directamente-pelo-bff-via-rest-oauth2.md](../decisions/DEC-020-backoffice-de-configuracao-acedido-directamente-pelo-bff-via-rest-oauth2.md) - Status: accepted

## Itens Pendentes

| Item | Responsavel | Prioridade |
|------|-------------|------------|
| Tecnologia de Message Broker | Arquitetura | Alta |
| SLAs de integracao com Backend API | Arquitetura + Cliente | Alta |
| Providers de notificacao (SMS, Push, Email) | Assessment | Media |
| Open Banking PSD2 - APIs expostas/consumidas | Assessment | Media |
| Circuit Breaker - biblioteca e configuracao | Assessment | Media |
| Abertura de conta - interacoes com terceiros | Cliente | Media |
| Notificacoes de transferencia na app mobile | Cliente | Baixa |
| Catalogo de APIs documentado | Desenvolvimento | Baixa |
| Ambiente de sandbox | Infraestrutura | Baixa |
