# HomeBanking Web - High Level Design (HLD)

**Versão:** 1.0

**Data:** Janeiro 2026

**Cliente:** Novo Banco

**Elaborado por:** NextReality


---


## Índice

_[Índice será gerado automaticamente no Word]_


---

# 1. Sumário Executivo

## Propósito

Este documento constitui o workbook de arquitetura High Level Design (HLD) para o projeto HomeBanking Web do Novo Banco, definindo as componentes críticas da aplicação e sua implementação em tecnologias 100% Web.

## Conteúdo

### 1.1 Objetivos do Documento

Este documento de arquitetura tem como objetivo:

1. **Definir o cerne do projeto** - Estabelecer as bases tecnológicas, arquitetura de infraestrutura e de software
2. **Documentar processos** - Segurança, desenvolvimento e operações
3. **Servir como baseline** - Referência para auditoria e compliance regulatório
4. **Orientar decisões** - Suportar decisões de Segurança, Casos de Uso e Compliance

O nível de detalhe adotado é **HLD (High Level Design)**, evitando soluções dúbias enquanto permite flexibilidade para detalhamento posterior através de documentos LLD (Low Level Design).

### 1.2 Público-Alvo

| Perfil | Responsabilidade |
|--------|------------------|
| Arquitetos de Software | Definição e validação da arquitetura técnica |
| Desenvolvedores | Implementação seguindo as diretrizes definidas |
| Gestores de Projeto | Gestão e acompanhamento do projeto |

### 1.3 Escopo

#### 1.3.1 In-Scope

O HomeBanking Web incluirá **35 funcionalidades** da aplicação mobile, organizadas nas seguintes categorias:

| Categoria | Funcionalidades |
|-----------|-----------------|
| **Autenticação** | Registo, Login, Recuperação de Acessos |
| **Áreas Principais** | Home, Área Pessoal, Dashboard |
| **Património** | Património, Carteiras, Saldos e Movimentos |
| **Operações** | Ordens Pendentes, Histórico de Operações, Confirmação de Operações |
| **Documentos** | Comprovativos e Extratos |
| **Investimentos** | Warrants, Ações, ETF, Fundos, Obrigações, Índices, Temas Investimento, Depósito a Prazo, Leilões, Ofertas Públicas, Unit Linked, Robot Advisor, BTP |
| **Pagamentos** | Transferências, Pagamentos, Carregamentos, MBWay (componentes não-SDK) |
| **Outros** | Outros Bancos, Eventos Corporativos, Seguros de Proteção, Área do Viajante, Bea, Wishlist, Notícias Externas |

#### 1.3.2 Out-of-Scope

| Funcionalidade | Justificação |
|----------------|--------------|
| MBWay SDK | Componentes nativos do SDK são específicos para aplicações mobile nativas e não compatíveis com ambiente web |

### 1.4 Visão Geral da Arquitetura

![Diagrama 1](diagrams/diagram_01.png)

*Figura: Diagrama 1*

**Princípios Fundamentais:**
- Reutilização da infraestrutura e serviços da aplicação mobile nativa existente
- Tecnologias 100% Web (sem dependências de componentes nativos)
- Conformidade com regulamentações bancárias portuguesas

### 1.5 Princípios Orientadores

| Princípio | Descrição |
|-----------|-----------|
| **Reutilização** | Maximizar uso de APIs e serviços existentes da app mobile |
| **Segurança** | Conformidade com regulamentações bancárias e PSD2 |
| **Paridade Funcional** | Experiência consistente entre canais web e mobile |
| **Auditabilidade** | Suporte a requisitos de compliance e auditoria |
| **Escalabilidade** | Arquitetura preparada para crescimento |

## Diagramas

Ver diagrama conceptual na secção 1.4.




---

# 2. Contexto de Negócio & Requisitos

## Propósito

Descrever o contexto da solução HomeBanking Web, suas partes interessadas, requisitos funcionais e não funcionais, restrições e dependências.

## Conteúdo

### 2.1 Contexto de Negócio

O projeto HomeBanking Web visa disponibilizar aos clientes do Novo Banco uma plataforma web com funcionalidades equivalentes à aplicação mobile nativa existente. A solução reutilizará a infraestrutura e serviços já criados para a app mobile.

**Drivers de Negócio:**
- Oferecer canal alternativo ao mobile para clientes que preferem acesso via browser
- Paridade funcional entre canais para experiência consistente
- Reutilização de investimentos já realizados na infraestrutura mobile

### 2.2 Partes Interessadas (Stakeholders)

| Papel | Responsabilidade | Contacto/Status |
|-------|------------------|-----------------|
| Sponsor | Patrocinador executivo do projeto | Fórum designado pelo Banco Best |
| Product Owner | Definição de requisitos e priorização | A definir no início do projeto |
| Arquiteto NovoBanco | Validação técnica e integração com sistemas existentes | A definir no início do projeto |
| Equipa Segurança | Validação de conformidade e segurança | A definir no início do projeto |
| Equipa Infraestrutura | Suporte Azure e ambientes | A definir no início do projeto |
| Equipa Core Banking | Integração com APIs do Core | A definir no início do projeto |
| Equipa Mobile | Coordenação com app nativa existente | A definir no início do projeto |
| DPO (Data Protection Officer) | Conformidade RGPD | A definir no início do projeto |
| Utilizadores Finais | Clientes do Novo Banco | N/A |

**Notas:**
- O sponsor é o fórum designado pelo Banco Best, podendo ser alterado conforme necessidade
- As equipas técnicas serão definidas no início da execução do projeto
- O projeto não envolve diretamente entidades externas (reguladores, parceiros, fornecedores). As integrações com terceiros são as já existentes na app mobile

### 2.3 Requisitos Funcionais

#### 2.3.1 Funcionalidades por Categoria

| Categoria | Funcionalidades | Quantidade |
|-----------|-----------------|------------|
| **Autenticação** | Registo, Login, Recuperação de Acessos | 3 |
| **Áreas Principais** | Home, Área Pessoal, Dashboard | 3 |
| **Património** | Património, Carteiras, Saldos e Movimentos | 3 |
| **Operações** | Ordens Pendentes, Histórico de Operações, Confirmação de Operações | 3 |
| **Documentos** | Comprovativos e Extratos | 2 |
| **Investimentos** | Warrants, Ações, ETF, Fundos, Obrigações, Índices, Temas Investimento, Depósito a Prazo, Leilões, Ofertas Públicas, Unit Linked, Robot Advisor, BTP | 13 |
| **Pagamentos** | Transferências, Pagamentos, Carregamentos, MBWay (não-SDK) | 4 |
| **Outros** | Outros Bancos, Eventos Corporativos, Seguros de Proteção, Área do Viajante, Bea, Wishlist, Notícias Externas | 7 |
| **TOTAL** | | **35** |

#### 2.3.2 Estratégia de Priorização

- **Critério:** Priorização por dependência entre funcionalidades
- **MVP:** Todas as 35 funcionalidades fazem parte do MVP
- **Funcionalidades Exclusivas Web:** Nenhuma (paridade com mobile)

#### 2.3.3 Suporte Multi-idioma

| Idioma | Prioridade |
|--------|------------|
| Português | Principal |
| Inglês | Secundário |
| Espanhol | Secundário |

#### 2.3.4 Acessibilidade

- **Status:** _A definir_ - Requer aprofundamento
- **Referência:** WCAG 2.1 AA (a considerar)

### 2.4 Requisitos Não Funcionais

#### 2.4.1 Performance

| Métrica | Valor | Observação |
|---------|-------|------------|
| Tempo resposta operações críticas | max 3 segundos | Transações, consultas |
| Throughput | 10 TPS | Transações por segundo |
| Tempo carregamento página inicial | max 10 segundos | First Contentful Paint |

#### 2.4.2 Disponibilidade

| Métrica | Valor | Observação |
|---------|-------|------------|
| SLA Disponibilidade | 99.9% | ~8.76 horas downtime/ano |
| RTO | 30 minutos | Recovery Time Objective |
| RPO | 5 minutos | Recovery Point Objective |
| Janelas Manutenção | Sim | Programadas |

#### 2.4.3 Escalabilidade

| Métrica | Valor | Observação |
|---------|-------|------------|
| Utilizadores concorrentes | 400 | Baseline |
| Crescimento anual | 5% | Projeção 3 anos |
| Picos de utilização | Sim | Fim de mês, períodos fiscais |

#### 2.4.4 Segurança

| Requisito | Status | Observação |
|-----------|--------|------------|
| Certificações | _A definir_ | ISO 27001, PCI-DSS a considerar |
| Encriptação | _A definir_ | TLS 1.3, AES-256 a considerar |
| Retenção de logs | _A definir_ | 7 anos (típico bancário) a validar |

#### 2.4.5 Compatibilidade

| Requisito | Especificação |
|-----------|---------------|
| Browsers | Chrome, Edge, Safari (versões atuais + 2 anteriores) |
| Responsividade | Design responsivo obrigatório |
| Dispositivos móveis | Suporte via design responsivo |

### 2.5 Restrições

| Tipo | Restrição | Impacto |
|------|-----------|---------|
| **Técnica** | Reutilização de APIs e serviços da app mobile | Define integração com backend existente |
| **Técnica** | Tecnologias 100% Web (sem componentes nativos) | MBWay SDK out-of-scope |
| **Regulatória** | Conformidade PSD2 | Autenticação forte (SCA) obrigatória |
| **Regulatória** | Regulamentações Banco de Portugal | Requisitos de segurança e auditoria |

### 2.6 Pressupostos

| ID | Pressuposto | Validado |
|----|-------------|----------|
| P1 | APIs da app mobile estão disponíveis e documentadas | A validar |
| P2 | Infraestrutura existente suporta canal web adicional | A validar |
| P3 | Requisitos de segurança são os mesmos da app mobile | A validar |
| P4 | Não há necessidade de novas integrações com terceiros | Sim |

### 2.7 Dependências

![Diagrama 2](diagrams/diagram_02.png)

*Figura: Diagrama 2*

| Dependência | Tipo | Crítica |
|-------------|------|---------|
| API Gateway | Infraestrutura existente | Sim |
| Backend Services | Serviços existentes | Sim |
| Core Banking | Sistema legado | Sim |
| Serviços Terceiros | Integrações existentes | Sim |




---

# 3. Visão Geral da Solução

## Propósito

Apresentar os princípios de arquitetura, diagrama conceptual e casos de uso principais da solução HomeBanking Web.

## Conteúdo

### 3.1 Princípios de Arquitetura

| Princípio | Decisão | Descrição |
|-----------|---------|-----------|
| **Cloud Strategy** | Containers OpenShift | Arquitetura orientada a containers, compliant com OpenShift |
| **API Strategy** | BFF (Backend for Frontend) | Camada de agregação específica para o canal web, isolando sistemas legados |
| **Build vs Buy** | Preferência Build | Avaliação caso a caso, construir quando soluções de mercado forem caras ou inadequadas |
| **Acoplamento Legados** | Via BFF apenas | Frontend isolado de complexidades dos sistemas legados |
| **Observabilidade** | Stack ELK | Logs de aplicação e métricas centralizados |
| **Segurança** | _A definir_ | Avaliar Zero Trust e Defense in Depth |
| **Resiliência** | _A definir_ | Necessita aprofundamento |
| **Portabilidade** | _A definir_ | Necessita aprofundamento |

### 3.2 Diagrama Conceptual

![Arquitetura Conceptual - HomeBanking Web (C4 Level 1)](diagrams/diagram_03.png)

*Figura: Arquitetura Conceptual - HomeBanking Web (C4 Level 1)*

### 3.3 Componentes Principais

| Componente | Tipo | Responsabilidade | Tecnologia |
|------------|------|------------------|------------|
| **HomeBanking Web** | Frontend SPA | Interface do utilizador, experiência web responsiva | _A definir (SEC-04)_ |
| **BFF Web** | Backend | Agregação, transformação, orquestração para canal web | _A definir (SEC-05)_ |
| **API Gateway** | Infraestrutura | Roteamento, rate limiting, autenticação | Existente |
| **Backend Services** | Serviços | Lógica de negócio, integrações | Existente |
| **ELK Stack** | Observabilidade | Logs centralizados, métricas, dashboards | Existente |

### 3.4 Casos de Uso Principais

#### 3.4.1 Atores

| Ator                | Descrição                        | Prioridade |
| ------------------- | -------------------------------- | ---------- |
| Cliente Individual  | Cliente particular do Novo Banco | Principal  |
| Cliente Empresarial | _Futuro_                         | Secundário |

#### 3.4.2 Casos de Uso por Categoria

![Diagrama 4](diagrams/diagram_04.png)

*Figura: Diagrama 4*

#### 3.4.3 Casos de Uso Críticos

| Caso de Uso | Criticidade | Requisitos Especiais |
|-------------|-------------|----------------------|
| **Login** | Alta | SCA obrigatório, ponto de entrada |
| **Transferências** | Alta | SCA obrigatório, operação financeira core |

#### 3.4.4 Requisitos de Autenticação

- **SCA (Strong Customer Authentication):** Obrigatório para todo o acesso à aplicação
- **Conformidade:** PSD2

### 3.5 Integração com Infraestrutura Existente

![Diagrama 5](diagrams/diagram_05.png)

*Figura: Diagrama 5*

| Componente | Origem | Ação |
|------------|--------|------|
| Frontend Web | Novo | Desenvolver |
| BFF Web | Novo | Desenvolver |
| API Gateway | Existente | Reutilizar |
| Backend Services | Existente | Reutilizar |
| Core Banking | Existente | Reutilizar |
| Integrações Terceiros | Existente | Reutilizar |
| Base de Dados | Existente | Reutilizar |




---

# 4. Experiência do Utilizador & Arquitetura Frontend

## Propósito

Definir a arquitetura de informação, diretrizes UI/UX, stack tecnológica frontend, design system, responsividade, segurança e performance do canal web HomeBanking.

## Conteúdo

### 4.1 Arquitetura de Informação

#### 4.1.1 Estrutura de Navegação

![Diagrama 6](diagrams/diagram_06.png)

*Figura: Diagrama 6*

| Elemento | Decisão | Justificação |
|----------|---------|--------------|
| Navegação Principal | SideBar | Padrão para aplicações web complexas |
| Navegação Secundária | Breadcrumbs | Localização rápida, navegação contextual |
| Navegação Contextual | Dependente da origem | Fluxos podem variar conforme ponto de entrada |

### 4.2 Diretrizes UI/UX

#### 4.2.1 Princípios de Design

| Princípio | Descrição |
|-----------|-----------|
| **Paridade Mobile** | Fluxos da app mobile replicados na web |
| **Responsividade** | Design responsivo para todos os dispositivos |
| **Feedback Imediato** | Skeleton screens para perceção de responsividade 100% |
| **Clareza** | Separação clara entre informação e ação requerida |

#### 4.2.2 Padrões de Feedback

| Tipo | Uso | Exemplo |
|------|-----|---------|
| **Toasts** | Avisos não bloqueantes | "Transferência realizada com sucesso" |
| **Modais** | Avisos que requerem resposta | "Confirmar operação?" |
| **Skeleton Screens** | Loading states | Carregamento de listas, dashboards |

### 4.3 Jornadas do Utilizador

#### 4.3.1 Atores

| Ator | Prioridade | Observação |
|------|------------|------------|
| Cliente Individual | Principal | Foco inicial |
| Cliente Empresarial | Futuro | Fase posterior |

#### 4.3.2 Jornadas Prioritárias

As jornadas serão baseadas nos 35 requisitos funcionais definidos, com foco em:

| Categoria | Jornadas | Criticidade |
|-----------|----------|-------------|
| **Autenticação** | Login, Registo, Recuperação | Alta (SCA obrigatório) |
| **Operações Financeiras** | Transferências, Pagamentos | Alta |
| **Consultas** | Dashboard, Saldos, Património | Média |
| **Investimentos** | Ações, ETF, Fundos, Robot Advisor | Média |

### 4.4 Multi-idioma

| Idioma | Prioridade | Cobertura |
|--------|------------|-----------|
| Português | Principal | 100% |
| Inglês | Secundário | 100% |
| Espanhol | Secundário | 100% |

**Implementação:**
- Biblioteca: **i18next** com react-i18next
- Namespaces para lazy loading de traduções
- Deteção automática de idioma do browser
- Persistência de preferência do utilizador

### 4.5 PWA & Offline

| Requisito | Status | Observação |
|-----------|--------|------------|
| PWA Instalável | _A definir_ | Necessita aprofundamento |
| Funcionamento Offline | _A definir_ | Necessita aprofundamento |
| Service Workers | _A definir_ | Para cache de assets |

### 4.6 Stack Frontend

![Diagrama 7](diagrams/diagram_07.png)

*Figura: Diagrama 7*

#### 4.6.1 Stack Tecnológica

| Camada | Tecnologia | Versão |
|--------|------------|--------|
| **Framework** | React | 18+ (mais atual) |
| **Linguagem** | TypeScript | Latest |
| **Build Tool** | Vite | Latest |
| **State Management** | Zustand | Latest |
| **Data Fetching** | TanStack Query | Latest |
| **Styling** | Tailwind CSS | Latest |
| **i18n** | i18next | Latest |
| **Testes Unitários** | Vitest | Latest |
| **Testes E2E** | Playwright | Latest |

#### 4.6.2 Rendering Strategy

| Estratégia | Uso | Exemplo |
|------------|-----|---------|
| **SSG** | Páginas estáticas | Landing, FAQ |
| **SSR** | Dados dinâmicos | Dashboard, Saldos |
| **ISR** | Conteúdo semi-estático | Notícias, Índices |

**Justificação:** Proteção de client_secret no fluxo de login, performance otimizada.

#### 4.6.3 Code Splitting

- **Estratégia:** Code splitting por rotas usando React.Lazy
- **Benefício:** Bundle size otimizado, carregamento sob demanda

### 4.7 Design System

#### 4.7.1 Visão Geral

| Aspeto | Decisão |
|---------|---------|
| **Base** | Criado de raiz para o projeto |
| **Componentes** | Avaliação de bibliotecas existentes, fallback para desenvolvimento interno |
| **Documentação** | Figma (design) + Storybook (desenvolvimento) |
| **Temas** | Suporte a modo escuro |

#### 4.7.2 Tokens de Design

| Token | Status | Observação |
|-------|--------|------------|
| Cores | A definir | Início do desenvolvimento |
| Tipografia | A definir | Início do desenvolvimento |
| Espaçamentos | A definir | Início do desenvolvimento |
| Sombras | A definir | Início do desenvolvimento |

#### 4.7.3 Biblioteca de Componentes

![Diagrama 8](diagrams/diagram_08.png)

*Figura: Diagrama 8*

### 4.8 Responsividade

| Requisito | Especificação |
|-----------|---------------|
| **Design** | Mobile-first responsive |
| **Breakpoints** | sm, md, lg, xl (Tailwind defaults) |
| **Browsers** | Chrome, Edge, Safari (atuais + 2 anteriores) |
| **Dispositivos** | Desktop, Tablet, Mobile |

### 4.9 Segurança Frontend

| Controlo | Implementação |
|----------|---------------|
| **XSS Prevention** | React escaping automático, CSP headers |
| **CSRF** | Tokens CSRF via BFF |
| **Sensitive Data** | Não armazenar em localStorage/sessionStorage |
| **Auth Tokens** | HttpOnly cookies (geridos pelo BFF) |
| **SCA** | Obrigatório para todo o acesso |

#### 4.9.1 Segurança UX

| Aspeto | Decisão |
|---------|---------|
| Comunicação de segurança ao utilizador | _A definir_ |
| Timeout de sessão por inatividade | 10 minutos |
| Aviso prévio de expiração | Popup com temporizador antes de expirar |

### 4.10 Performance Frontend

#### 4.10.1 Métricas Alvo

| Métrica | Target | Observação |
|---------|--------|------------|
| **LCP** (Largest Contentful Paint) | < 2.5s | Core Web Vital |
| **FID** (First Input Delay) | < 100ms | Core Web Vital |
| **CLS** (Cumulative Layout Shift) | < 0.1 | Core Web Vital |
| **Página Inicial** | < 10s | Requisito NFR |

#### 4.10.2 Estratégias de Otimização

| Estratégia | Implementação |
|------------|---------------|
| **Code Splitting** | React.Lazy por rotas |
| **Lazy Loading** | Imagens, componentes pesados |
| **Pre-fetching** | Vite + TanStack Query |
| **Caching** | Service Workers (se PWA), HTTP cache |
| **Bundle Size** | Tree shaking, Tailwind purge |

#### 4.10.3 Bundle Size

| Aspeto | Status |
|---------|--------|
| Limites de bundle | _A definir_ - Necessita consulta ao cliente |

## Diagramas

### Arquitetura Frontend Completa

![Diagrama 9](diagrams/diagram_09.png)

*Figura: Diagrama 9*




---

# 5. Arquitetura Backend & Servicos

## Proposito

Definir a decomposicao de servicos, arquitetura de API, comunicacao, modelo de dominio, rate limiting, resiliencia, versionamento e especificacao de APIs para o HomeBanking Web.

## Conteudo

### 5.1 Decomposicao de Servicos

![Decomposicao de Servicos - HomeBanking Web](diagrams/diagram_10.png)

*Figura: Decomposicao de Servicos - HomeBanking Web*

| Componente | Tipo | Acao | Tecnologia |
|------------|------|------|------------|
| Frontend Web | Novo | Desenvolver | React + TypeScript |
| BFF Web | Novo | Desenvolver | C# .NET 8 |
| API Gateway | Existente | Reutilizar | - |
| Backend Services | Existente | Reutilizar | - |
| Core Banking | Existente | Reutilizar | - |

### 5.2 Arquitetura BFF

#### 5.2.1 Visao Geral

![Diagrama 11](diagrams/diagram_11.png)

*Figura: Diagrama 11*

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

![Diagrama 12](diagrams/diagram_12.png)

*Figura: Diagrama 12*

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

![Diagrama 13](diagrams/diagram_13.png)

*Figura: Diagrama 13*

#### Gestao de Sessao

| Aspecto | Decisao |
|---------|---------|
| **Identificador** | Cookie de sessao (HttpOnly, Secure) |
| **Token Storage** | Cache distribuido (chave = Session ID) |
| **Validacao** | App ou OTP (SCA) |
| **Propagacao** | Bearer token para backend services |




---

# 6. Arquitetura de Dados

## Propósito

Definir a arquitetura de dados do HomeBanking Web, incluindo modelo de dados, armazenamento, encriptação, retenção, conformidade RGPD e estratégias de cache. O canal web reutiliza os serviços backend existentes, logo a maioria dos dados transacionais reside nos sistemas existentes.

## Conteúdo

### 6.1 Visão Geral de Dados

![Fluxo de Dados - HomeBanking Web](diagrams/diagram_14.png)

*Figura: Fluxo de Dados - HomeBanking Web*

| Camada | Armazenamento | Dados |
|--------|---------------|-------|
| Frontend | localStorage | Dados básicos utilizador, dados públicos, notícias |
| BFF | Cache (Redis) | Sessão, tokens OAuth |
| Backend | Existente | Dados transacionais, contas, movimentos |

### 6.2 Modelo de Dados

#### 6.2.1 Dados no Frontend

| Tipo | Armazenamento | Exemplo |
|------|---------------|---------|
| Dados básicos utilizador | localStorage | Nome, preferências UI |
| Dados públicos | localStorage | Taxas de câmbio, índices |
| Notícias | localStorage | Comunicações, alertas |
| **Dados sensíveis** | **PROIBIDO** | Saldos, transações, tokens |

#### 6.2.2 Dados no BFF

| Tipo | Armazenamento | TTL |
|------|---------------|-----|
| Session ID | Cache | 30 min (max absoluto) |
| Access Token | Cache | 15 min |
| Refresh Token | Cache | 7 dias |
| Dados SSR/SSG | Cache | _A definir_ |

#### 6.2.3 Dados Específicos do Canal Web

- **Não há dados específicos** do canal web que não existam na app mobile
- Canal web consome os mesmos backend services e modelo de domínio

### 6.3 Armazenamento

![Diagrama 15](diagrams/diagram_15.png)

*Figura: Diagrama 15*

| Decisão | Valor |
|---------|-------|
| **Frontend - Persistência** | localStorage |
| **BFF - Base de dados** | Não (apenas cache) |
| **BFF - Tecnologia cache** | _A definir_ (Redis recomendado) |
| **Backend** | Reutiliza infraestrutura existente |

### 6.4 Encriptação

| Aspeto | Decisão |
|---------|---------|
| **Em trânsito** | TLS (versão a definir) |
| **Em repouso (BFF/cache)** | Sem requisitos específicos |
| **Gestão de chaves** | SSL apenas (no momento) |

### 6.5 Retenção de Dados

| Tipo | Política | Status |
|------|----------|--------|
| Logs de acesso web | _A definir_ | Pendente |
| Dados de sessão | _A definir_ | Pendente |
| Requisitos de auditoria | _A definir_ | Pendente |

### 6.6 Backup & Restore

| Aspeto | Status |
|---------|--------|
| Componentes que requerem backup | _A definir_ |
| Frequência de backup | _A definir_ |
| RTO/RPO para restauro | _A definir_ |

**Nota:** A maioria dos dados reside nos backend services existentes, que já possuem políticas de backup definidas.

### 6.7 RGPD - Data Subject Rights

| Requisito | Status |
|-----------|--------|
| Subject Access Requests (SAR) | _A definir_ |
| Direito ao esquecimento | _A definir_ |
| Dados web nas exportações | _A definir_ |

**Nota:** Processos RGPD existentes da app mobile devem ser estendidos ao canal web.

### 6.8 Classificação de Dados

| Aspeto | Status |
|---------|--------|
| Esquema de classificação | _A definir_ |
| Dados sensíveis/PII | _A definir_ |

### 6.9 Estratégia de Cache

![Diagrama 16](diagrams/diagram_16.png)

*Figura: Diagrama 16*

| Aspeto | Status |
|---------|--------|
| Dados cacheados no BFF | Sessão, tokens; mais se SSR completo |
| TTL por tipo | _A definir_ |
| Invalidação de cache | _A definir_ |




---

# 7. Autenticação & Autorização

## Propósito

Definir a estratégia completa de autenticação e autorização do HomeBanking Web, incluindo fluxos de autenticação, MFA/SCA, gestão de sessões, tokens e políticas de segurança.

## Conteúdo

### 7.1 Visão Geral de Autenticação

![Métodos de Autenticação - HomeBanking Web](diagrams/diagram_17.png)

*Figura: Métodos de Autenticação - HomeBanking Web*

| Método | Suporte | Observação |
|--------|---------|------------|
| QR Code + Biometria | Primário | Validação via app mobile |
| Username/Password | Fallback | Apenas quando QR Code falha |
| SMS OTP | Fallback | Segundo fator no fallback |
| App Push | Fallback | Segundo fator no fallback |
| Certificado Digital | Não | Não suportado |

**Login unificado:** Sim, mesmas credenciais da app mobile.

### 7.2 Fluxos de Autenticação

#### 7.2.1 Fluxo Primário - QR Code

![Diagrama 18](diagrams/diagram_18.png)

*Figura: Diagrama 18*

#### 7.2.2 Fluxo Fallback - Username/Password + 2FA

![Diagrama 19](diagrams/diagram_19.png)

*Figura: Diagrama 19*

### 7.3 MFA/SCA (Strong Customer Authentication)

| Aspeto | Decisão |
|---------|---------|
| **SCA Obrigatório** | Sim, para todos os acessos a áreas restritas |
| **Segundo fator primário** | Biometria via app (validação QR Code) |
| **Segundo fator fallback** | SMS OTP ou App Push |
| **Isenções SCA** | Nenhuma |

**Fluxo de fallback:** Após o utilizador informar falha na leitura do QR Code, a aplicação permite login com SMS OTP ou App Push, dependendo das opções habilitadas para o utilizador.

### 7.4 Gestão de Sessões

![Ciclo de Vida da Sessão](diagrams/diagram_20.png)

*Figura: Ciclo de Vida da Sessão*

| Parâmetro | Valor |
|-----------|-------|
| **Timeout por inatividade** | 10 minutos |
| **Timeout absoluto** | 30 minutos |
| **Sessão exclusiva** | Desejável (pendente aprovação cliente) |
| **Aviso de expiração** | Popup com temporizador |

### 7.5 Estratégia de Tokens

![Arquitetura de Tokens - Dois Níveis](diagrams/diagram_21.png)

*Figura: Arquitetura de Tokens - Dois Níveis*

| Token | Localização | TTL | Uso |
|-------|-------------|-----|-----|
| **Session Cookie** | Browser (cookie) | 30 min | Browser -> BFF |
| **Access Token** | BFF Cache | 15 min | BFF -> Backend |
| **Refresh Token** | BFF Cache | 7 dias | Renovação silenciosa |

**Renovação:** Refresh silencioso conforme atividade do utilizador. BFF renova tokens automaticamente antes de expiração.

### 7.6 Autorização

| Aspeto | Decisão |
|---------|---------|
| **Modelo** | ABAC híbrido com RBAC |
| **Role** | Atributo do sujeito (quando necessário) |
| **Atributos** | Sujeito, Recurso, Ação, Ambiente |
| **Permissões por operação** | Sim (consulta vs transação) |

**Atributos considerados:**

| Categoria | Atributos |
|-----------|-----------|
| **Sujeito** | Utilizador, role, tipo de cliente, segmento |
| **Recurso** | Tipo de conta, produto, limite |
| **Ação** | Consulta, transação, configuração |
| **Ambiente** | Canal (web), horário, localização, dispositivo |

**Nota:** Roles e perfis específicos serão definidos no assessment inicial do projeto.

### 7.7 Políticas de Password

| Aspeto | Decisão |
|---------|---------|
| Requisitos mínimos | Seguirá requisitos da app (a aprofundar) |
| Expiração | _A definir_ |
| Recuperação | _A definir_ |
| Bloqueio por tentativas | _A definir_ |

### 7.8 Anti-automation

| Aspeto | Status |
|---------|--------|
| CAPTCHA | _A definir_ |
| Rate limiting login | _A definir_ |
| Deteção de bots | _A definir_ |

### 7.9 Revogação

| Aspeto | Status |
|---------|--------|
| Revogação por comprometimento | _A definir_ |
| Logout de todos os dispositivos | _A definir_ |
| Revogação ao mudar password | _A definir_ |




---

# 8. Segurança & Conformidade

## Propósito

Definir os requisitos de segurança e conformidade regulatória do HomeBanking Web, incluindo modelo de ameaças, controlos de segurança, e conformidade com PSD2, RGPD, PCI-DSS e regulamentação do Banco de Portugal.

## Conteúdo

### 8.1 Visão Geral de Segurança

![Camadas de Segurança - HomeBanking Web](diagrams/diagram_22.png)

*Figura: Camadas de Segurança - HomeBanking Web*

### 8.2 Modelo de Ameaças

| Aspeto | Status |
|---------|--------|
| **Threat modeling realizado** | Não (ação pendente) |
| **Principais ameaças identificadas** | _A definir_ |
| **Metodologia** | _A definir_ (STRIDE ou PASTA) |

### 8.3 Controlos de Segurança

#### 8.3.1 Security Headers HTTP

| Header | Valor | Justificação |
|--------|-------|--------------|
| **Content-Security-Policy** | `self` (inicial) | Prevenção XSS, expandir conforme necessário |
| **X-Frame-Options** | `SAMEORIGIN` | Prevenção Clickjacking |
| **X-Content-Type-Options** | `nosniff` | Prevenção MIME sniffing |
| **Strict-Transport-Security** | `max-age` a definir | Força HTTPS |

#### 8.3.2 Subresource Integrity (SRI)

| Aspeto | Decisão |
|---------|---------|
| **Estratégia** | Bibliotecas servidas localmente |
| **Atributos** | `integrity` e `crossorigin` em recursos externos |
| **CDN** | Evitar; se necessário, atenção a atualizações de terceiros |

#### 8.3.3 Proteção XSS

![Controlos XSS - Por Camada](diagrams/diagram_23.png)

*Figura: Controlos XSS - Por Camada*

| Camada | Controlo |
|--------|----------|
| **SSR/BFF** | Escape de saída HTML, validação e sanitização de entrada |
| **React** | Escape automático em JSX |
| **Lint/SAST** | `innerHTML` e `eval` proibidos via lint e SonarQube |

#### 8.3.4 Proteção CSRF

| Controlo | Implementação |
|----------|---------------|
| **Tokens CSRF** | Rotacionados por request |
| **Cookie de sessão** | `SameSite=Strict`, `Secure`, `HttpOnly` |
| **CORS** | Configurado restritivamente |
| **Métodos seguros** | GET somente idempotentes |

#### 8.3.5 Controlos Backend/BFF

| Aspeto | Status |
|---------|--------|
| Input validation | Detalhes no assessment inicial |
| WAF | _A definir_ com equipa de infraestrutura |

### 8.4 OWASP Top 10

| Categoria | Status |
|-----------|--------|
| Controlos específicos | _A definir_ |
| SAST/DAST no pipeline | _A definir_ |
| Frequência de scans | _A definir_ |

### 8.5 Conformidade PSD2

![Conformidade PSD2 - HomeBanking Web](diagrams/diagram_24.png)

*Figura: Conformidade PSD2 - HomeBanking Web*

| Requisito | Decisão |
|-----------|---------|
| **SCA obrigatório** | Sim, todas as operações |
| **Isenções SCA** | Nenhuma |
| **Dynamic Linking** | Estrutura app já segue PSD2 (a aprofundar) |
| **TLS** | 1.2+ (versão específica a definir) |

### 8.6 Conformidade RGPD

| Aspeto | Status |
|---------|--------|
| Base legal para tratamento | _A definir_ |
| Consentimento | _A definir_ |
| DPO designado | _A definir_ |
| ROPA | _A definir_ |

### 8.7 PCI-DSS

| Aspeto | Status |
|---------|--------|
| Processamento de PAN | _A definir_ |
| Nível de conformidade | _A definir_ |
| Tokenização de cartões | _A definir_ |

### 8.8 Banco de Portugal

| Aspeto | Status |
|---------|--------|
| Requisitos regulatórios BdP | _A definir_ |
| Requisitos de reporte | _A definir_ |

### 8.9 Registo de Auditoria

| Aspeto | Status |
|---------|--------|
| Eventos a registar | _A definir_ |
| Formato de logs | _A definir_ |
| Período de retenção | _A definir_ |
| Imutabilidade | _A definir_ |

### 8.10 Resposta a Incidentes

| Aspeto | Status |
|---------|--------|
| Plano de resposta | _A definir_ |
| SLAs de resposta | _A definir_ |
| CSIRT | _A definir_ |

### 8.11 Gestão de Vulnerabilidades

| Aspeto | Status |
|---------|--------|
| Processo de gestão | _A definir_ |
| SLAs de correção | _A definir_ |
| Bug bounty | _A definir_ |

### 8.12 Segregação de Ambientes

| Aspeto | Status |
|---------|--------|
| Segregação (dev/staging/prod) | _A definir_ |
| Segregação de dados | _A definir_ |




---

# 9. Integracao & Interfaces Externas

## Proposito

Definir a arquitetura de integracao do HomeBanking Web com sistemas externos, incluindo Core Banking, servicos de terceiros (KYC/AML, Notificacoes, Cartoes), Open Banking PSD2, e mecanismos de comunicacao assincrona. Esta secao estabelece os padroes, SLAs e catalogo de integracoes necessarios para o funcionamento do canal web.

## Conteudo

### 9.1 Visao Geral de Integracoes

O HomeBanking Web segue uma arquitetura de integracao em camadas, onde o **BFF (Backend for Frontend)** atua como ponto unico de integracao entre o frontend e todos os sistemas backend. Nao ha acesso direto do frontend a sistemas externos.

![Arquitetura de Integracao - HomeBanking Web](diagrams/diagram_25.png)

*Figura: Arquitetura de Integracao - HomeBanking Web*

#### Principios de Integracao

| Principio | Descricao |
|-----------|-----------|
| **BFF como Gateway** | Todas as integracoes passam pelo BFF, nunca acesso direto do frontend |
| **Backend API (Facade)** | Ponto unico de acesso aos sistemas Core Banking |
| **Reutilizacao** | Mesmas APIs utilizadas pela app mobile |
| **Transformacao no BFF** | Adaptacao de dados para necessidades especificas do canal web |

### 9.2 Integracao Core Banking

#### Arquitetura de Acesso

O canal web **nao acede diretamente** ao Core Banking. A integracao e feita atraves de uma camada de Facade denominada **Backend API**, que encapsula a complexidade dos sistemas legados.

![Diagrama 26](diagrams/diagram_26.png)

*Figura: Diagrama 26*

#### Servicos Consumidos

| Categoria | Servicos | Protocolo |
|-----------|----------|-----------|
| **Contas** | Saldos, Movimentos, Extratos | REST/JSON |
| **Transferencias** | Nacionais, SEPA, Internacionais | REST/JSON |
| **Pagamentos** | Servicos, Impostos, Outros | REST/JSON |
| **Cartoes** | Consulta, Bloqueio, Ativacao, Limites | REST/JSON |
| **Autenticacao** | Login, Sessao, MFA | REST/JSON |

#### Protocolo e Formato

| Aspecto | Especificacao |
|---------|---------------|
| **Protocolo** | REST sobre HTTPS |
| **Formato de dados** | JSON |
| **Versionamento** | Via URL path (ex: `/v1/accounts`) |
| **Autenticacao** | Bearer Token (OAuth 2.0) |
| **APIs** | Mesmas utilizadas pela app mobile |
| **Documentacao** | Nao disponivel (a fornecer) |

#### Transformacao de Dados

O BFF e responsavel por transformar os dados do Backend API para o formato otimizado para o canal web:

| Responsabilidade | Descricao |
|------------------|-----------|
| **Agregacao** | Combinar multiplas chamadas em uma unica resposta |
| **Filtragem** | Remover campos nao necessarios para o frontend |
| **Formatacao** | Adaptar formatos de data, moeda, etc. |
| **Enriquecimento** | Adicionar informacoes calculadas ou derivadas |
| **Cache** | Armazenar dados frequentemente acedidos |

### 9.3 Terceiros - KYC/AML

A integracao com servicos de KYC (Know Your Customer) e AML (Anti-Money Laundering) e **gerida inteiramente pelo Backend**, nao havendo requisitos especificos para o canal web.

| Aspecto | Status |
|---------|--------|
| Provider KYC/AML | Implementado no backend |
| Requisitos no canal web | Nenhum requisito especifico |
| Fluxos de onboarding | Necessita aprofundamento |
| Verificacoes AML em tempo real | Necessita aprofundamento |

### 9.4 Terceiros - Notificacoes

O canal web **gera e recebe** notificacoes, integrando com os servicos de notificacao existentes.

#### Capacidades

| Direcao | Descricao |
|---------|-----------|
| **Gera** | O canal web pode acionar envio de notificacoes (ex: confirmacao de transferencia) |
| **Recebe** | O canal web recebe notificacoes para exibir ao utilizador |

#### Canais de Notificacao

| Canal | Provider | Status |
|-------|----------|--------|
| **SMS** | A definir no assessment | Pendente |
| **Push Notifications** | A definir no assessment | Pendente |
| **Email Transacional** | A definir no assessment | Pendente |

#### Fluxo de Notificacoes

![Diagrama 27](diagrams/diagram_27.png)

*Figura: Diagrama 27*

### 9.5 Terceiros - Cartoes

O canal web permite operacoes de gestao de cartoes atraves da integracao com o provider de cartoes.

#### Operacoes Suportadas

| Operacao | Disponivel | Notas |
|----------|------------|-------|
| Consulta de cartoes | Sim | Lista de cartoes do utilizador |
| Bloqueio temporario | Sim | Bloqueio/desbloqueio pelo utilizador |
| Ativacao de cartao | Sim | Ativacao de cartao novo |
| Alteracao de limites | Sim | Ajuste de limites de credito/debito |
| Consulta de movimentos | Sim | Historico de transacoes |
| PIN (alteracao) | Necessita aprofundamento | - |
| 3D Secure | Necessita aprofundamento | - |

#### Provider de Cartoes

| Aspecto | Status |
|---------|--------|
| Provider (emissao/processamento) | Necessita aprofundamento |
| Integracao 3D Secure | Necessita aprofundamento |

### 9.6 Open Banking PSD2

A conformidade PSD2 e tratada a nivel do Backend API. Os detalhes de implementacao para o canal web necessitam aprofundamento.

| Aspecto | Status |
|---------|--------|
| APIs expostas (AISP, PISP) | Necessita aprofundamento |
| APIs consumidas | Necessita aprofundamento |
| Gestao de consentimentos | Necessita aprofundamento |
| Modelo de autorizacao | Necessita aprofundamento |

### 9.7 Gestao de Consentimentos

_Necessita aprofundamento - dependente das decisoes de Open Banking PSD2_

### 9.8 Message Broker

A tecnologia de Message Broker e os eventos a serem publicados/consumidos pelo canal web serao definidos no assessment inicial do projeto.

| Aspecto | Status |
|---------|--------|
| Tecnologia (RabbitMQ, Kafka, Azure Service Bus) | Necessita aprofundamento |
| Eventos publicados | Necessita aprofundamento |
| Eventos consumidos | Necessita aprofundamento |
| Ordenacao/Exactly-once | Necessita aprofundamento |
| Dead-letter strategy | Necessita aprofundamento |

### 9.9 Tratamento de Erros

#### Estrategia de Retry

| Tipo de Erro | Estrategia | Tentativas | Delay |
|--------------|------------|------------|-------|
| **Erros transientes** | Exponential backoff | 3 | 1s, 2s, 4s |
| **Network Timeout** | Immediate retry | 1 | 0s |
| **Rate limiting (429)** | Fixed delay | Ate sucesso | Retry-After header |
| **Erros de negocio (4xx)** | Sem retry | 0 | - |
| **Erros de servidor (5xx)** | Exponential backoff | 3 | 1s, 2s, 4s |

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

### 9.10 SLAs de Integracao

_Os SLAs de integracao dependem de informacoes dos sistemas backend e fornecedores terceiros._

| Integracao | Disponibilidade | Latencia P95 | Timeout |
|------------|-----------------|--------------|---------|
| Backend API (Facade) | Necessita aprofundamento | Necessita aprofundamento | 60s |
| Core Banking | Necessita aprofundamento | Necessita aprofundamento | 60s |
| Notificacoes | Necessita aprofundamento | Necessita aprofundamento | 30s |
| Cartoes | Necessita aprofundamento | Necessita aprofundamento | 60s |
| KYC/AML | N/A (backend) | N/A | N/A |

**Nota:** Janelas de manutencao programadas que afetam integracoes necessitam aprofundamento.

### 9.11 Catalogo de Integracoes

_O catalogo detalhado de integracoes sera documentado no assessment inicial do projeto._

| Aspecto | Status |
|---------|--------|
| Catalogo documentado | Necessita aprofundamento |
| Ferramenta de documentacao | Necessita aprofundamento |
| Ambiente de sandbox | Necessita aprofundamento |

### 9.12 API Management

#### Azure API Gateway

O Azure API Gateway e utilizado como ponto central de gestao de APIs entre o BFF e o Backend API.

![Diagrama 28](diagrams/diagram_28.png)

*Figura: Diagrama 28*

#### Funcionalidades

| Funcionalidade | Status |
|----------------|--------|
| **Gateway** | Azure API Gateway |
| **Rate limiting** | Necessita aprofundamento |
| **Throttling diferenciado** | Necessita aprofundamento |
| **Monitoring** | Necessita aprofundamento |

## Diagramas

### Diagrama de Contexto de Integracao

![Diagrama de Contexto - Integracoes HomeBanking Web](diagrams/diagram_29.png)

*Figura: Diagrama de Contexto - Integracoes HomeBanking Web*




---

# 10. Arquitetura Operacional

## Propósito

Definir a arquitetura operacional do HomeBanking Web, incluindo infraestrutura de containers, ambientes, pipelines CI/CD, estratégia de deploy, gestão de secrets e disaster recovery.

## Conteúdo

### 10.1 Infraestrutura

A aplicação será deployada em ambiente containerizado, com imagens **compliant com OpenShift** para futura migração.

![Infraestrutura HomeBanking Web](diagrams/diagram_30.png)

*Figura: Infraestrutura HomeBanking Web*

| Aspeto | Especificação |
|---------|---------------|
| **Plataforma atual** | Azure Kubernetes Service (AKS) |
| **Plataforma futura** | OpenShift (em homologação) |
| **Load Balancer** | F5 BIG-IP |
| **Ingress Controller** | NGINX Ingress / OpenShift Routes |
| **Container Registry** | Azure Container Registry (ACR) |

#### Requisitos de Imagens Container (OpenShift-Compliant)

| Requisito | Descrição |
|-----------|-----------|
| Utilizador não-root | Container executa como utilizador arbitrário (UID > 1000) |
| Filesystem read-only | Volumes temporários montados explicitamente |
| Portas > 1024 | Não utilizar portas privilegiadas |
| Base image | Red Hat UBI (Universal Base Image) recomendado |
| Health checks | Liveness e Readiness probes obrigatórios |

### 10.2 Ambientes

A aplicação utiliza três ambientes, segregados por **namespaces** no cluster AKS.

| Ambiente | Propósito | Namespace | Promoção |
|----------|-----------|-----------|----------|
| **dev** | Desenvolvimento e integração | `homebanking-dev` | Automática (CI) |
| **qa** | Testes integrados e UAT | `homebanking-qa` | Automática (após dev OK) |
| **prod** | Produção | `homebanking-prod` | Manual (aprovação) |

#### Segregação de Ambientes

| Tipo | Mecanismo |
|------|-----------|
| Lógica | Namespaces Kubernetes separados |
| Rede | Network Policies por namespace |
| Secrets | Key Vault com políticas por ambiente |
| RBAC | Service accounts distintos por ambiente |

### 10.3 CI/CD Pipeline

#### Stack de CI/CD

| Componente | Ferramenta |
|------------|------------|
| **Repositório** | Azure Repos (Git) |
| **CI/CD Platform** | Azure Pipelines |
| **Container Registry** | Azure Container Registry (ACR) |
| **Secrets** | Azure Key Vault |
| **IaC** | Helm Charts + Terraform |
| **Branching** | GitFlow |

#### Estratégia de Branching (GitFlow)

| Branch | Propósito | Deploy Automático |
|--------|-----------|-------------------|
| `feature/*` | Desenvolvimento de features | Não |
| `develop` | Integração contínua | DEV |
| `release/*` | Preparação de release | QA |
| `main` | Produção | PROD (c/ aprovação) |
| `hotfix/*` | Correções urgentes | PROD (c/ aprovação) |

#### Pipeline Overview

![Pipeline CI/CD](diagrams/diagram_31.png)

*Figura: Pipeline CI/CD*

#### Quality Gates

| Gate | Ferramenta | Threshold | Bloqueante |
|------|------------|-----------|------------|
| Unit Tests | Vitest / xUnit | 100% pass | Sim |
| Code Coverage | Istanbul / Coverlet | >= 80% | Sim |
| SAST | SonarQube / Checkmarx | 0 Critical, 0 High | Sim |
| Lint | ESLint / .NET Analyzers | 0 errors | Sim |
| Build | Azure Pipelines | Success | Sim |

### 10.4 Estratégia de Deploy

| Aspeto | Especificação |
|---------|---------------|
| **Estratégia** | Rolling Update |
| **Zero downtime** | Sim |
| **maxSurge** | 25% |
| **maxUnavailable** | 0 |
| **Réplicas mínimas** | 2 |
| **Health checks** | Readiness + Liveness probes |
| **Rollback** | Automático via Kubernetes |

#### Aprovações por Ambiente

| Ambiente | Aprovação | Aprovadores |
|----------|-----------|-------------|
| DEV | Automática | - |
| QA | Automática | - |
| PROD | Manual | Tech Lead + PO |

### 10.5 Secrets Management

| Aspeto | Especificação |
|---------|---------------|
| **Ferramenta** | Azure Key Vault |
| **Injeção** | Secret Store CSI Driver |
| **Acesso** | Managed Identity por namespace |
| **Rotação** | Suportada (CSI driver faz refresh) |
| **Secrets geridos** | Connection strings, API keys, certificados |

![Injeção de Secrets via CSI Driver](diagrams/diagram_32.png)

*Figura: Injeção de Secrets via CSI Driver*

#### Política de Rotação

| Tipo de Secret | Frequência | Responsável |
|----------------|------------|-------------|
| API Keys | 90 dias | Automático |
| Certificados TLS | Anual | Infra |
| DB Credentials | 180 dias | DBA |

### 10.6 Container Registry

| Aspeto | Configuração |
|---------|--------------|
| Registry | Azure Container Registry (ACR) |
| Autenticação | Managed Identity |
| Scanning | Microsoft Defender for Containers |
| Retenção | 90 dias para tags não-latest |
| Naming | `acr.azurecr.io/homebanking/{component}:{version}` |

#### Tagging Strategy

| Tag | Uso |
|-----|-----|
| `{semver}` | Versão semântica (ex: `1.2.3`) |
| `{branch}-{sha}` | Feature branches (ex: `develop-abc1234`) |
| `latest` | Última versão de produção |

### 10.7 Disaster Recovery

| Aspeto | Configuração |
|---------|--------------|
| **Tipo** | Cluster réplica (standby passivo) |
| **RTO** | 30 minutos |
| **RPO** | 5 minutos |
| **Failover** | Manual (decisão de negócio) |

> **Nota:** Canal web é stateless. Dados estão no backend existente com DR próprio. DR do canal web foca na disponibilidade da aplicação.

### 10.8 Backup

O canal web **não requer backup dedicado**:

| Componente | Backup | Frequência | Retenção |
|------------|--------|------------|----------|
| **Código fonte** | Git | Cada commit | Infinito |
| **Container images** | ACR | Cada build | 90 dias |
| **Secrets** | Azure Key Vault (managed) | Automático | 90 dias |
| **Dados de negócio** | Backend existente | N/A | N/A |
| **Sessões** | Redis (transitório) | N/A | N/A |

### 10.9 Runbooks

| Runbook | Trigger | Responsável |
|---------|---------|-------------|
| Deploy para Produção | Release aprovada | DevOps |
| Rollback de Emergência | Incidente P1 | DevOps |
| Escalação de Pods | Alerta de carga | DevOps / Auto |
| Rotação de Secrets | Schedule / Incidente | SecOps |
| Failover DR | Indisponibilidade > RTO | Infra |




---

# 11. Observabilidade & Operações

## Propósito

Definir a estratégia de observabilidade do HomeBanking Web, incluindo stack tecnológica, métricas chave (golden signals), tracing distribuído e abordagem de SLIs/SLOs.

## Conteúdo

### 11.1 Os Três Pilares

| Pilar | Propósito | Ferramenta |
|-------|-----------|------------|
| **Logs** | Eventos e debugging | ELK (Elasticsearch, Logstash, Kibana) |
| **Métricas** | Performance e saúde | Prometheus + Grafana (complemento) |
| **Traces** | Fluxo de requests | Elastic APM |

### 11.2 Stack de Observabilidade

A stack de observabilidade será baseada no **ELK Stack** (Elasticsearch, Logstash, Kibana), reutilizando a infraestrutura existente.

![Stack de Observabilidade](diagrams/diagram_33.png)

*Figura: Stack de Observabilidade*

| Componente | Função | Tecnologia |
|------------|--------|------------|
| **Logging** | Logs estruturados JSON | Serilog (.NET), Filebeat |
| **Tracing** | Distributed tracing | Elastic APM |
| **Ingestão** | Coleta e transformação | Logstash |
| **Armazenamento** | Indexação e busca | Elasticsearch |
| **Visualização** | Dashboards | Kibana |
| **Alerting** | Notificações | ElastAlert |

### 11.3 Golden Signals

Os quatro golden signals serão monitorizados conforme melhores práticas SRE:

| Signal | Métrica | Target | Alerta |
|--------|---------|--------|--------|
| **Latency** | P95 response time | < 3s | > 5s |
| **Traffic** | Requests per second | Baseline | > 2x baseline |
| **Errors** | Error rate (5xx) | < 0.1% | > 1% |
| **Saturation** | CPU/Memory usage | < 70% | > 85% |

### 11.4 Logging

Todos os logs serão estruturados em formato JSON com campos padronizados:

#### Campos Obrigatórios

| Campo | Tipo | Descrição |
|-------|------|-----------|
| `timestamp` | ISO8601 | Data/hora UTC do evento |
| `level` | string | DEBUG, INFO, WARN, ERROR, FATAL |
| `service` | string | Nome do componente (frontend-web, bff-web) |
| `correlation_id` | UUID | ID para correlação entre serviços |
| `message` | string | Descrição do evento |
| `environment` | string | dev, qa, prod |

#### Campos Opcionais

| Campo | Tipo | Uso |
|-------|------|-----|
| `user_id` | string | Identificador do utilizador (masked) |
| `session_id` | string | ID da sessão |
| `operation` | string | Tipo de operação |
| `duration_ms` | number | Duração da operação |
| `error_code` | string | Código de erro |

#### Mascaramento de Dados Sensíveis

| Tipo de Dado | Tratamento |
|--------------|------------|
| NIB/IBAN | Mascarar (`PT50****1234`) |
| User ID | Hash ou mascarar |
| Montantes | Mascarar |
| Email | Mascarar (`j***@email.com`) |
| NIF | Mascarar |
| Tokens | Nunca logar |

#### Retenção de Logs

| Tipo de Log | Retenção | Requisito |
|-------------|----------|-----------|
| Logs de autenticação | 7 anos | Compliance bancário |
| Logs de transações | 7 anos | Compliance bancário |
| Logs de erro | 1 ano | Operacional |
| Logs gerais | 90 dias | Operacional |

### 11.5 Tracing Distribuído

| Header | Propósito | Gerado por |
|--------|-----------|------------|
| `X-Correlation-ID` | Correlação de logs | Frontend (UUID) |
| `X-Request-ID` | ID único do request | BFF |
| `traceparent` | W3C Trace Context | APM Agent |

| Componente | Instrumentação |
|------------|----------------|
| Frontend | RUM (Real User Monitoring) JS Agent |
| BFF .NET | Elastic APM .NET Agent |

### 11.6 SLIs / SLOs / SLAs

| Conceito | Definição | Responsável |
|----------|-----------|-------------|
| **SLI** (Indicator) | Métrica que mede o nível de serviço | Engenharia |
| **SLO** (Objective) | Target interno para o SLI | Engenharia |
| **SLA** (Agreement) | Compromisso contratual externo | Negócio |

#### SLOs do Canal Web

| SLI | SLO Target | Janela | Cálculo |
|-----|------------|--------|---------|
| Disponibilidade | 99.9% | Mensal | Uptime / Tempo total |
| Latência P95 | < 3s | Mensal | Percentil 95 dos requests |
| Taxa de Erro | < 0.1% | Mensal | Erros 5xx / Total requests |
| TTFB | < 800ms | Mensal | Time to First Byte P95 |

#### Error Budget

| SLO | Error Budget Mensal |
|-----|---------------------|
| 99.9% | 43.2 minutos |
| 99.95% | 21.6 minutos |
| 99.99% | 4.3 minutos |

### 11.7 Alertas

| Severidade | Critério | Tempo Resposta | Notificação |
|------------|----------|----------------|-------------|
| **P1 - Critical** | Serviço indisponível, impacto total | < 15 min | On-call + SMS |
| **P2 - High** | Degradação significativa | < 30 min | Email + Teams |
| **P3 - Medium** | Degradação parcial | < 4 horas | Email |
| **P4 - Low** | Anomalia sem impacto | Próximo dia útil | Ticket |

#### Alertas Configurados

| Alerta | Condição | Severidade |
|--------|----------|------------|
| Serviço DOWN | Health check falha > 2 min | P1 |
| Error Rate Alto | > 5% erros 5xx | P1 |
| Latência Degradada | P95 > 5s por 5 min | P2 |
| CPU Saturado | > 90% por 10 min | P2 |
| Memory Alto | > 85% por 10 min | P2 |
| Auth Failures Spike | > 10x baseline | P2 |
| Circuit Breaker Open | Estado OPEN | P3 |
| Error Rate Elevado | > 1% erros | P3 |

### 11.8 Dashboards

| Dashboard | Audiência | Conteúdo |
|-----------|-----------|----------|
| **Health Overview** | NOC / On-call | Status geral, alertas ativos, SLO status |
| **Performance** | Engenharia | Latência, throughput, errors por endpoint |
| **Business** | Produto | Logins, transações, conversion rates |
| **Security** | SecOps | Auth failures, suspicious activity |
| **Infrastructure** | DevOps | CPU, memory, pods, network |

### 11.9 Métricas de Negócio

| Métrica | Descrição | Dashboard |
|---------|-----------|-----------|
| Logins/hora | Taxa de autenticações | Business |
| Transações/tipo | Transferências, pagamentos | Business |
| Taxa abandono login | % que não completa login | Business |
| Erros auth | Falhas de autenticação | Security |
| Sessões ativas | Utilizadores online | Operations |




---

# 12. Desempenho & Fiabilidade

## Propósito

Definir os objetivos de desempenho e a estratégia de fiabilidade do HomeBanking Web, incluindo targets de performance, caching, auto-scaling e testes de carga.

## Conteúdo

### 12.1 Objetivos de Desempenho

Os targets são baseados nos requisitos não funcionais (DEF-02):

| Métrica | Target | Fonte |
|---------|--------|-------|
| **Utilizadores Concorrentes** | 400 | DEF-02 |
| **Throughput** | 10 TPS | DEF-02 |
| **Tempo de Resposta (P95)** | < 3 segundos | DEF-02 |
| **Tempo de Carregamento Inicial** | < 10 segundos | DEF-02 |
| **Disponibilidade** | 99.9% | DEF-02 |
| **Crescimento Anual** | 5% | DEF-02 |

### 12.2 Core Web Vitals

| Métrica | Target | Classificação |
|---------|--------|---------------|
| **LCP** (Largest Contentful Paint) | < 2.5s | Good |
| **FID** (First Input Delay) | < 100ms | Good |
| **CLS** (Cumulative Layout Shift) | < 0.1 | Good |
| **TTFB** (Time to First Byte) | < 800ms | Good |
| **FCP** (First Contentful Paint) | < 1.8s | Good |

### 12.3 Perfil de Carga

![Perfil de Carga - HomeBanking Web](diagrams/diagram_34.png)

*Figura: Perfil de Carga - HomeBanking Web*

### 12.4 Estratégia de Cache

![Camadas de Cache](diagrams/diagram_35.png)

*Figura: Camadas de Cache*

#### Níveis de Cache

| Nível | Dados | TTL |
|-------|-------|-----|
| **Browser** | Assets estáticos (JS, CSS, imagens) | Longo (com cache busting) |
| **Browser** | Local Storage (sessão, prefs) | Sessão |
| **CDN** | JS, CSS, imagens, fontes | 24 horas |
| **BFF (Redis)** | Sessões, tokens, dados partilhados | Variável |

#### TTL por Tipo de Dado (Redis)

| Dado | TTL | Justificação |
|------|-----|--------------|
| Sessão do utilizador | 10 min | Inatividade timeout |
| Tokens OAuth | Variável | Alinhado com expiração |
| Configurações do sistema | 5 min | Baixa frequência de mudança |
| Dados de referência (países, bancos) | 1 hora | Dados estáticos |
| Cotações/Taxas | 1 min | Dados voláteis |

**Princípio:** Dados sensíveis (contas, transações) NÃO são cacheados.

#### Cache Invalidation

| Evento | Ação |
|--------|------|
| Logout | Invalidar sessão no Redis |
| Transação executada | Invalidar cache de saldos (se aplicável) |
| Deploy | Versionar assets (cache busting) |
| Configuração alterada | Invalidar cache de config |

### 12.5 Otimização Frontend

#### Bundle Optimization

| Técnica | Implementação | Impacto |
|---------|---------------|---------|
| Code Splitting | React.lazy() + Suspense | Reduz initial bundle |
| Tree Shaking | Webpack/Vite config | Remove código não utilizado |
| Lazy Loading | Componentes e rotas | Carrega sob demanda |
| Minification | Terser (JS), CSSNano | Reduz tamanho |
| Compression | gzip/Brotli | 70-90% redução |

#### Budget de Bundle

| Métrica | Limite | Ação se exceder |
|---------|--------|-----------------|
| Initial JS | < 200KB (gzipped) | Code split |
| Initial CSS | < 50KB (gzipped) | Purge CSS |
| Largest chunk | < 100KB | Split ou lazy load |
| Total assets | < 1MB | Review dependencies |

#### Otimização de Assets

| Asset | Estratégia |
|-------|------------|
| Imagens | WebP format, lazy loading, srcset |
| Fontes | WOFF2, font-display: swap, subset |
| Icons | SVG sprite ou icon font |
| CSS | Critical CSS inline, defer restante |

### 12.6 Otimização Backend (BFF)

#### Connection Pooling

| Conexão | Pool Size | Timeout |
|---------|-----------|---------|
| Redis | 10-20 | 5s |
| HTTP Client (Backend) | 100 | 30s |

#### Compressão

| Tipo | Configuração |
|------|--------------|
| Response | gzip (nível 6) |
| Threshold | > 1KB |
| Content-Types | application/json, text/html |

#### Async/Non-blocking

![Pattern: Async Processing](diagrams/diagram_36.png)

*Figura: Pattern: Async Processing*

### 12.7 Auto-Scaling

| Aspeto | Abordagem |
|---------|-----------|
| **Mecanismo** | Horizontal Pod Autoscaler (HPA) |
| **Métricas** | CPU, Memory |
| **CPU Target** | 70% |
| **Memory Target** | 80% |

#### Configuração por Componente

| Componente | Min Replicas | Max Replicas | CPU Target | Memory Target |
|------------|--------------|--------------|------------|---------------|
| Frontend | 2 | 6 | 70% | 80% |
| BFF | 2 | 10 | 70% | 80% |

#### Scale-up vs Scale-down

| Evento | Tempo | Ação |
|--------|-------|------|
| Scale-up | 60s estabilização | Duplicar réplicas |
| Scale-down | 300s estabilização | Reduzir 50% |

> **Nota:** Scale-down mais conservador para evitar oscilações.

### 12.8 Capacity Planning

#### Resource Requests/Limits

| Componente | CPU Request | CPU Limit | Memory Request | Memory Limit |
|------------|-------------|-----------|----------------|--------------|
| Frontend | 100m | 500m | 128Mi | 256Mi |
| BFF | 250m | 1000m | 256Mi | 512Mi |

#### Estimativa de Recursos (400 users)

| Componente | Pods | CPU Total | Memory Total |
|------------|------|-----------|--------------|
| Frontend | 2 | 1 vCPU | 512Mi |
| BFF | 4 | 4 vCPU | 2Gi |
| **Total** | 6 | **5 vCPU** | **2.5Gi** |

### 12.9 Resiliência

| Padrão | Implementação |
|--------|---------------|
| **Circuit Breaker** | Polly (.NET) |
| **Retry** | Exponential backoff (3 tentativas) |
| **Timeout** | Configurável por endpoint |
| **Bulkhead** | Limite de conexões |
| **Health Checks** | Liveness + Readiness probes |

#### Pod Disruption Budget

| Aspeto | Configuração |
|---------|--------------|
| minAvailable | 50% |
| Propósito | Garantir disponibilidade durante manutenção |

### 12.10 Load Testing

#### Ferramenta

| Ferramenta | Uso | Justificação |
|------------|-----|--------------|
| **k6** | Load testing principal | Scripting em JS, integração CI/CD |

#### Cenários de Teste

| Cenário | Users | Duração | Objetivo |
|---------|-------|---------|----------|
| Smoke | 10 | 5 min | Validar ambiente |
| Load | 400 | 30 min | Validar capacidade nominal |
| Stress | 600 | 15 min | Identificar limites |
| Soak | 200 | 4 horas | Identificar memory leaks |

#### Critérios de Aceitação

| Métrica | Critério | Fail |
|---------|----------|------|
| Response Time P95 | < 3s | > 5s |
| Error Rate | < 0.1% | > 1% |
| Throughput | >= 10 TPS | < 8 TPS |
| CPU (peak) | < 80% | > 90% |
| Memory (peak) | < 80% | > 90% |




---

# 13. Estratégia de Testes

## Propósito

Definir a estratégia de testes do HomeBanking Web a nível arquitetural, estabelecendo os tipos de testes, frameworks, quality gates e integração com o pipeline CI/CD.

## Conteúdo

### 13.1 Pirâmide de Testes

A estratégia de testes segue o modelo da **pirâmide de testes**, priorizando testes automatizados nos níveis inferiores.

![Pirâmide de Testes - HomeBanking Web](diagrams/diagram_37.png)

*Figura: Pirâmide de Testes - HomeBanking Web*

| Nível | Distribuição | Frameworks | Escopo |
|-------|--------------|------------|--------|
| **Unit Tests** | 70% | Vitest (FE), xUnit (BFF) | Funções, componentes isolados |
| **Integration** | 20% | WireMock, TestContainers | APIs, serviços, contratos |
| **E2E** | 10% | Playwright | Fluxos críticos de utilizador |

### 13.2 Cobertura de Código

| Tipo de Código | Cobertura Target |
|----------------|------------------|
| Componentes críticos | >= 90% |
| Hooks customizados | >= 90% |
| Utils/helpers | >= 80% |
| Serviços | >= 80% |
| **Código geral** | **>= 80%** |

### 13.3 Frameworks de Teste

#### Frontend (React + TypeScript)

| Aspeto | Especificação |
|---------|---------------|
| Framework | Vitest |
| Assertions | Vitest expect |
| Component Testing | React Testing Library |
| Mocking | Vitest mocks |
| Coverage | Istanbul |

#### BFF (.NET 8)

| Aspeto | Especificação |
|---------|---------------|
| Framework | xUnit |
| Assertions | FluentAssertions |
| Mocking | Moq / NSubstitute |
| Coverage | Coverlet |

#### E2E

| Aspeto | Especificação |
|---------|---------------|
| Framework | Playwright |
| Browsers | Chromium, Firefox, WebKit |
| Execution | CI/CD (headless) |
| Reports | HTML + Screenshots |

### 13.4 Tipos de Testes

| Tipo | Objetivo | Responsabilidade | Frequência |
|------|----------|------------------|------------|
| **Unitários** | Validar lógica isolada | Desenvolvimento | Cada commit |
| **Integração** | Validar comunicação entre componentes | Desenvolvimento | Cada commit |
| **Contrato** | Validar API contracts (Pact) | Desenvolvimento | Cada commit |
| **E2E** | Validar fluxos críticos de negócio | QA + Dev | Cada PR |
| **Performance** | Validar NFRs de carga | QA | Pre-release |
| **Segurança (SAST)** | Análise estática de código | Pipeline | Cada commit |
| **Segurança (DAST)** | Análise dinâmica | SecOps | Pre-release |
| **Acessibilidade** | Validar conformidade WCAG 2.1 AA | QA | Cada PR |
| **Penetration Test** | Testes manuais de intrusão | Externo | Antes go-live |

### 13.5 Cenários E2E Críticos

| Fluxo | Prioridade | Criticidade |
|-------|------------|-------------|
| Login via QR Code | Alta | Crítico |
| Login tradicional (fallback) | Alta | Crítico |
| Consulta de saldos | Alta | Crítico |
| Transferência nacional | Alta | Crítico |
| Pagamento de serviços | Alta | Crítico |
| Logout | Média | Alto |
| Alteração de dados | Média | Alto |

### 13.6 Testes de Segurança

| Tipo | Ferramenta | Quando |
|------|------------|--------|
| SAST | SonarQube / Checkmarx | Cada commit |
| DAST | OWASP ZAP | Pre-release |
| Dependency Scan | Snyk / Dependabot | Diário |
| Penetration Test | Manual (externo) | Antes go-live |

### 13.7 Testes de Acessibilidade

| Aspeto | Especificação |
|---------|---------------|
| Standard | WCAG 2.1 AA |
| Tool | axe-core |
| Integration | Playwright + axe |
| Reports | HTML |

### 13.8 Quality Gates no Pipeline

![Quality Gates no Pipeline](diagrams/diagram_38.png)

*Figura: Quality Gates no Pipeline*

| Gate | Threshold | Bloqueante |
|------|-----------|------------|
| Unit Tests | 100% pass | Sim |
| Code Coverage | >= 80% | Sim |
| SAST | 0 Critical, 0 High | Sim |
| Lint | 0 errors | Sim |
| E2E Critical | 100% pass | Sim |
| E2E Non-critical | >= 95% pass | Não |
| Accessibility | 0 Critical | Sim |

### 13.9 Test Data Management

| Ambiente | Dados | Fonte |
|----------|-------|-------|
| **dev** | Dados sintéticos (fixtures) | Gerados |
| **qa** | Dados anonimizados de produção | DB anonimizado |
| **prod** | N/A (não testar em prod) | - |

### 13.10 Matriz de Responsabilidades

| Tipo de Teste | Quem Escreve | Quem Executa | Quando |
|---------------|--------------|--------------|--------|
| Unit Tests | Developers | CI Pipeline | Cada commit |
| Integration | Developers | CI Pipeline | Cada commit |
| Contract | Developers | CI Pipeline | Cada commit |
| E2E | QA + Developers | CI Pipeline | Cada PR |
| Performance | QA | Manual + CI | Pre-release |
| Security (SAST) | Automated | CI Pipeline | Cada commit |
| Security (DAST) | SecOps | Manual | Pre-release |
| Accessibility | QA | CI Pipeline | Cada PR |
| UAT | QA + PO | Manual | Pre-release |




---

# 14. Plano de Migracao & Implementacao

> **Definicao:** 

## Proposito

Definir o plano de migracao e implementacao do HomeBanking Web, incluindo roadmap, estrategia de cutover, coexistencia com app mobile, criterios go/no-go, procedimentos de rollback, beta testing e periodo de hypercare.

## Conteudo

### 14.1 Roadmap de Implementacao

![Roadmap de Implementacao - HomeBanking Web](diagrams/diagram_39.png)

*Figura: Roadmap de Implementacao - HomeBanking Web*

| Fase | Duracao | Entregas |
|------|---------|----------|
| **0: Setup** | 4 semanas | Infraestrutura, pipelines CI/CD, ambientes, design system base |
| **1: MVP Core** | 12 semanas | Login (4 fluxos), Dashboard, Contas, Saldos, Transferencias |
| **2: Features** | 8 semanas | Restantes 35 funcionalidades (paridade mobile) |
| **3: Beta/UAT** | 4 semanas | Testes UAT, correcoes, pentest |
| **4: Go-Live** | 2 semanas | Cutover, lancamento controlado |
| **5: Hypercare** | 4 semanas | Suporte intensivo, monitorizacao, ajustes |

### 14.2 MVP - Funcionalidades Core

| Funcionalidade | Prioridade | Complexidade |
|----------------|------------|--------------|
| Login QR Code (principal) | P1 | Alta |
| Login tradicional (fallback) | P1 | Media |
| Dashboard / Home | P1 | Media |
| Consulta de contas | P1 | Baixa |
| Consulta de saldos | P1 | Baixa |
| Transferencias nacionais | P1 | Alta |
| Pagamentos de servicos | P1 | Alta |
| Logout | P1 | Baixa |

### 14.3 Estrategia de Cutover

**Abordagem:** Lancamento Gradual (Phased Rollout) com Feature Flags

![Estrategia de Lancamento Gradual](diagrams/diagram_40.png)

*Figura: Estrategia de Lancamento Gradual*

#### Criterios de Progressao

| Etapa | Condicao para Avancar |
|-------|----------------------|
| Beta -> Lancamento Parcial | 0 bugs criticos, taxa de erro < 1% |
| Parcial -> Geral | SLOs cumpridos, feedback positivo, 0 P1 abertos |

#### Feature Flags para Rollout

| Flag | Descricao | Default |
|------|-----------|---------|
| `enable_web_banking` | Habilita acesso ao canal web | false |
| `enable_qr_login` | Habilita login via QR Code | true |
| `enable_transfers` | Habilita transferencias | true |
| `maintenance_mode` | Modo manutencao (bloqueia acessos) | false |

### 14.4 Coexistencia com App Mobile

![Coexistencia Web + Mobile](diagrams/diagram_41.png)

*Figura: Coexistencia Web + Mobile*

| Aspecto | Comportamento |
|---------|---------------|
| Sessoes simultaneas | Permitidas (Web + Mobile) |
| Logout | Independente por canal |
| Tokens | Separados (App vs Web BFF) |

### 14.5 Migracao de Dados

> **Conclusao:** O canal web e **stateless** e nao requer migracao de dados. Todos os dados de negocio estao no backend existente que ja serve a App Mobile.

| Tipo de Dado | Migracao Necessaria? | Notas |
|--------------|---------------------|-------|
| Dados de utilizadores | Nao | Backend existente |
| Contas e saldos | Nao | Backend existente |
| Historico de transacoes | Nao | Backend existente |
| Preferencias de utilizador | Nao | Geridas no backend |
| Configuracoes do sistema | Nao | Novas configs para Web |

### 14.6 Criterios Go/No-Go

#### Checklist Pre-Go-Live

| Categoria | Criterio | Bloqueante |
|-----------|----------|------------|
| **Funcional** | 100% dos testes E2E criticos passam | Sim |
| **Funcional** | UAT aprovado pelo PO | Sim |
| **Performance** | Load test 400 users OK | Sim |
| **Performance** | SLOs validados (99.9%, < 3s) | Sim |
| **Seguranca** | Pentest concluido | Sim |
| **Seguranca** | 0 vulnerabilidades criticas/altas | Sim |
| **Seguranca** | SAST/DAST sem findings criticos | Sim |
| **Operacional** | Runbooks documentados | Sim |
| **Operacional** | Alertas configurados | Sim |
| **Operacional** | Dashboards operacionais prontos | Sim |
| **Operacional** | Equipa de suporte treinada | Sim |
| **Legal** | Aprovacao compliance | Sim |

#### Comite de Aprovacao

| Papel | Responsabilidade |
|-------|------------------|
| Tech Lead | Validacao tecnica |
| PO / Product Manager | Validacao funcional |
| Security Officer | Validacao de seguranca |
| Operations Lead | Validacao operacional |
| Sponsor | Aprovacao final |

### 14.7 Procedimentos de Rollback

![Procedimento de Rollback](diagrams/diagram_42.png)

*Figura: Procedimento de Rollback*

#### Tipos de Rollback

| Tipo | Tempo | Quando Usar |
|------|-------|-------------|
| Feature Flag | Instantaneo | Problema em feature especifica |
| Deployment | 2-5 min | Problema geral na versao |
| Full Rollback | 15-30 min | Problema sistemico |

### 14.8 Beta Testing

| Fase | Duracao | Participantes | Objetivo |
|------|---------|---------------|----------|
| Alpha | 1 semana | Equipa interna (50) | Smoke testing |
| Beta fechado | 2 semanas | Colaboradores selecionados (500) | Funcional completo |
| Beta aberto | 1 semana | Early adopters (2000) | Stress real |

#### Criterios de Selecao Beta

| Criterio | Justificacao |
|----------|--------------|
| Utilizadores ativos da App | Familiarizados com fluxos |
| Diferentes perfis | Standard, Premium, Empresas |
| Diferentes regioes | Testar latencia |
| Tech-savvy | Feedback qualitativo |

#### Feedback Collection

| Canal | Tipo de Feedback |
|-------|------------------|
| In-app widget | Bugs e sugestoes |
| Formulario dedicado | Feedback estruturado |
| Analytics | Comportamento (heatmaps, funnels) |
| Entrevistas | Qualitativo (amostra) |

### 14.9 Hypercare Period

| Aspecto | Especificacao |
|---------|---------------|
| **Duracao** | 4 semanas apos go-live |
| **Cobertura** | 24/7 na primeira semana, 8-20h restantes |
| **Equipa** | Dev + Ops + Suporte dedicados |

#### Actividades por Semana

| Semana | Foco |
|--------|------|
| 1 | Monitorizacao intensiva, resolucao imediata de bugs |
| 2 | Estabilizacao, ajustes de performance |
| 3 | Optimizacao, resolucao de feedback |
| 4 | Transicao para operacao normal |

#### Criterios de Saida do Hypercare

| Criterio | Threshold |
|----------|-----------|
| Bugs P1/P2 abertos | 0 |
| SLOs cumpridos | 3 dias consecutivos |
| Taxa de erro | < 0.1% |
| Feedback negativo | < 5% |

### 14.10 Comunicacao e Formacao

#### Plano de Comunicacao

| Audiencia | Canal | Mensagem | Timing |
|-----------|-------|----------|--------|
| Utilizadores | Email + App | Lancamento do novo canal | 2 semanas antes |
| Utilizadores | Landing page | Features e beneficios | Go-live |
| Suporte | Training | Novos fluxos e FAQs | 1 semana antes |
| Internos | Intranet | Anuncio de lancamento | Go-live |

#### Formacao

| Grupo | Conteudo | Formato |
|-------|----------|---------|
| Equipa de Suporte | Fluxos, troubleshooting, FAQs | Workshop presencial |
| Gestores de Conta | Demo, beneficios | Video + Demo |
| Equipa Tecnica | Arquitetura, runbooks | Documentacao + Sessao |




---

# 15. Governação & Roadmap

## Propósito

Definir o modelo de governação e roadmap do HomeBanking Web, incluindo modelo de governação, gestão de decisões arquiteturais, roadmap de produto, gestão de dívida técnica, processo de gestão de mudança, KPIs de sucesso e continuous improvement.

## Conteúdo

### 15.1 Modelo de Governação

![Estrutura de Governança - HomeBanking Web](diagrams/diagram_43.png)

*Figura: Estrutura de Governança - HomeBanking Web*

#### Modelo de Trabalho

| Aspeto | Especificação |
|---------|---------------|
| **Metodologia** | Scrum (2-week sprints) |
| **Cerimónias** | Daily, Planning, Review, Retro |
| **Ferramentas** | Azure DevOps (boards), Teams |
| **Reporting** | Sprint Review + Monthly Report |

#### Papéis e Responsabilidades

| Papel | Responsabilidades |
|-------|-------------------|
| **Sponsor** | Aprovação estratégica, budget, escalação |
| **Product Owner** | Backlog, priorização, aceitação |
| **Tech Lead** | Decisões técnicas, arquitetura, quality |
| **Scrum Master** | Processo, impedimentos, cerimónias |
| **Frontend Lead** | Arquitetura frontend, code review |
| **Backend Lead** | Arquitetura BFF, code review |
| **QA Lead** | Estratégia de testes, qualidade |
| **DevOps** | Infraestrutura, CI/CD, operações |
| **Security** | Validação de segurança, compliance |

### 15.2 Gestão de Decisões Arquiteturais

#### Processo de Decisão

![Processo de Decisão Arquitetural (ADR)](diagrams/diagram_44.png)

*Figura: Processo de Decisão Arquitetural (ADR)*

#### Tipos de Decisão

| Tipo | Aprovador | Exemplos |
|------|-----------|----------|
| **Estratégica** | Steering Committee | Stack tecnológica, arquitetura global |
| **Tática** | Tech Lead | Padrões de código, bibliotecas |
| **Operacional** | Lead da área | Configurações, tooling |

#### ADRs do Projeto

| ID | Decisão | Status | Data |
|----|---------|--------|------|
| DEC-001 | Estratégia de autenticação web | Accepted | 2026-01-04 |
| DEC-002 | Gestão de sessões e tokens | Accepted | 2026-01-04 |
| DEC-003 | Modelo de autorização ABAC | Accepted | 2026-01-04 |
| DEC-004 | Controlos de segurança frontend | Accepted | 2026-01-04 |
| DEC-005 | Armazenamento de dados canal web | Accepted | 2026-01-04 |
| DEC-006 | Estratégia de containers OpenShift | Accepted | 2026-01-04 |
| DEC-007 | Padrão BFF | Accepted | 2026-01-04 |
| DEC-008 | Stack de observabilidade ELK | Accepted | 2026-01-04 |
| DEC-009 | Stack tecnológica frontend | Accepted | 2026-01-04 |
| DEC-010 | Stack tecnológica backend | Accepted | 2026-01-04 |

### 15.3 Roadmap de Produto

![Roadmap - Visão de Longo Prazo](diagrams/diagram_45.png)

*Figura: Roadmap - Visão de Longo Prazo*

#### Backlog de Features Pós-MVP

| Feature | Prioridade | Estimativa |
|---------|------------|------------|
| Dashboard personalizável | P2 | M |
| Notificações web push | P2 | S |
| Modo escuro | P3 | S |
| Exportação de extratos PDF | P2 | M |
| Comparador de produtos | P3 | L |
| Chat com assistente | P3 | XL |

#### Release Cadence

| Tipo | Frequência | Conteúdo |
|------|------------|----------|
| **Major** | Trimestral | Novas features significativas |
| **Minor** | Mensal | Melhorias e features pequenas |
| **Patch** | Semanal (se necessário) | Bug fixes, segurança |

### 15.4 Gestão de Dívida Técnica

![Gestão de Dívida Técnica](diagrams/diagram_46.png)

*Figura: Gestão de Dívida Técnica*

#### Categorias de Dívida Técnica

| Categoria | Exemplos | Prioridade |
|-----------|----------|------------|
| **Segurança** | Vulnerabilidades, outdated dependencies | Crítica |
| **Performance** | Queries lentas, memory leaks | Alta |
| **Arquitetura** | Code smells, tight coupling | Média |
| **Código** | Duplicação, complexidade ciclomática | Média |
| **Testes** | Baixa cobertura, testes frágeis | Média |
| **Documentação** | APIs não documentadas | Baixa |

#### Alocação de Capacidade

| Sprint | Features | Dívida Técnica | Bugs |
|--------|----------|----------------|------|
| Normal | 70% | **20%** | 10% |
| Pre-release | 50% | 30% | 20% |
| Pós-release | 40% | 20% | 40% |

#### Métricas de Dívida Técnica

| Métrica | Ferramenta | Target |
|---------|------------|--------|
| Code Coverage | Istanbul/Coverlet | >= 80% |
| Cyclomatic Complexity | SonarQube | < 15 por método |
| Duplicated Lines | SonarQube | < 3% |
| Technical Debt Ratio | SonarQube | < 5% |
| Outdated Dependencies | Dependabot | 0 critical |

### 15.5 Processo de Gestão de Mudança

#### Change Advisory Board (CAB)

| Tipo de Mudança | Aprovação | Lead Time |
|-----------------|-----------|-----------|
| **Standard** | Automática (CI/CD) | Imediato |
| **Normal** | Tech Lead | 1 dia |
| **Emergency** | On-call + Tech Lead | Imediato |
| **Major** | CAB | 1 semana |

#### Janelas de Mudança

| Ambiente | Janela | Restrições |
|----------|--------|------------|
| dev | 24/7 | Nenhuma |
| qa | 24/7 | Nenhuma |
| prod (standard) | 9h-18h dias úteis | Evitar sextas |
| prod (major) | Sábados 6h-10h | Comunicação prévia |

![Processo de Change Management](diagrams/diagram_47.png)

*Figura: Processo de Change Management*

### 15.6 KPIs de Sucesso

#### KPIs Técnicos (DORA Metrics)

| KPI | Métrica | Target |
|-----|---------|--------|
| **Disponibilidade** | Uptime % | 99.9% |
| **Latência** | Response time P95 | < 3s |
| **Taxa de Erro** | Error rate | < 0.1% |
| **MTTR** | Mean Time To Recover | < 30 min |
| **Deploy Frequency** | Deploys/semana | >= 2 |
| **Lead Time** | Commit to prod | < 1 dia |
| **Change Failure Rate** | Deploys com rollback | < 5% |

#### KPIs de Produto

| KPI | Métrica | Target |
|-----|---------|--------|
| **Adoção** | Utilizadores ativos | +20% Q/Q |
| **Engagement** | Sessões/utilizador | >= 5/mês |
| **Satisfação** | NPS | >= 40 |
| **Task Success** | Taxa de conclusão de fluxos | >= 95% |
| **Time on Task** | Tempo médio por operação | Baseline -10% |

### 15.7 Continuous Improvement

#### Cerimónias de Melhoria

| Cerimónia | Frequência | Participantes | Output |
|-----------|------------|---------------|--------|
| Sprint Retro | 2 semanas | Equipa | Action items |
| Tech Retro | Mensal | Tech team | Tech improvements |
| Post-mortem | Por incidente | Envolvidos | Lessons learned |
| Architecture Review | Trimestral | Leads + Arquiteto | ADRs, Roadmap |

#### Feedback Loops

![Ciclo de Melhoria Contínua](diagrams/diagram_48.png)

*Figura: Ciclo de Melhoria Contínua*

#### Métricas de Maturidade

| Área | Nível Atual | Target | Ações |
|------|-------------|--------|-------|
| CI/CD | 3 | 4 | Automação de testes |
| Observability | 3 | 4 | Tracing distribuído |
| Security | 3 | 4 | DAST automatizado |
| Documentation | 2 | 3 | API docs automáticas |




---


## Glossário


| Termo | Definição |
|-------|-----------|
| HLD | High-Level Design - Documento de arquitetura de alto nível |
| HomeBanking | Portal web de serviços bancários para clientes |
| Core Banking | Sistema central de operações bancárias |
| PSD2 | Payment Services Directive 2 - Diretiva europeia de serviços de pagamento |
| RGPD | Regulamento Geral de Proteção de Dados |
| PCI-DSS | Payment Card Industry Data Security Standard |
| SLA | Service Level Agreement - Acordo de nível de serviço |
| SLO | Service Level Objective - Objetivo de nível de serviço |
| SLI | Service Level Indicator - Indicador de nível de serviço |
| MFA | Multi-Factor Authentication - Autenticação multifator |
| SSO | Single Sign-On - Autenticação única |
| KYC | Know Your Customer - Processo de identificação de clientes |
| AML | Anti-Money Laundering - Prevenção de lavagem de dinheiro |
| API | Application Programming Interface |
| CMS | Content Management System - Sistema de gestão de conteúdo |
| CI/CD | Continuous Integration / Continuous Deployment |
| PWA | Progressive Web App |
| WCAG | Web Content Accessibility Guidelines |
| OWASP | Open Web Application Security Project |
| BFF | Backend for Frontend - Camada de backend específica para o frontend |


---


## Controlo de Documento


| Versão | Data | Autor | Alterações |
|--------|------|-------|------------|
| 0.1 | 2026-01-01 | NextReality | Versão inicial |
| 0.2 | 2026-01-13 | NextReality | Adição de escopo, premissas, restrições |
| 0.3 | 2026-01-13 | NextReality | Simplificação - conteúdos movidos para definições |
| 0.4 | 2026-01-15 | NextReality | Correção de acentuação em português europeu |
| 1.0 | 2026-01-15 | NextReality | Documento HLD compilado para entrega |
