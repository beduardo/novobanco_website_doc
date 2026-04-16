---
id: "SEC-02"
title: "Contexto de Negocio e Requisitos"
status: "in-progress"
created: "2026-01-01"
updated: "2026-01-01"
depends-on-definitions:
  - "DEF-02"
  - "DEF-03"
  - "DEF-04"
depends-on-decisions: []
word-count: 0
---

# 2. Contexto de Negócio & Requisitos

## Definições e Decisões

> **Definições requeridas:**
> - [DEF-02-stakeholders.md](../definitions/DEF-02-stakeholders.md) - Status: completed
> - [DEF-03-requisitos-funcionais.md](../definitions/DEF-03-requisitos-funcionais.md) - Status: completed
> - [DEF-04-requisitos-nao-funcionais.md](../definitions/DEF-04-requisitos-nao-funcionais.md) - Status: completed
>
> **Decisões relacionadas:**
> - Nenhuma decisão arquitetural nesta secção (requisitos e contexto de negócio)

## Propósito

Descrever o contexto da solução HomeBanking Web, suas partes interessadas, requisitos funcionais e não funcionais, restrições e dependências.

## Conteúdo

### 2.1 Contexto de Negócio

O projeto HomeBanking Web visa disponibilizar aos clientes do Best uma plataforma web com funcionalidades equivalentes à aplicação mobile nativa existente. A solução reutilizará a infraestrutura e serviços já criados para a app mobile.

**Drivers de Negócio:**
- Oferecer canal alternativo ao mobile para clientes que preferem acesso via browser
- Paridade funcional entre canais para experiência consistente
- Reutilização de investimentos já realizados na infraestrutura mobile

### 2.2 Partes Interessadas (Stakeholders)

| Papel | Responsabilidade | Contacto/Status |
|-------|------------------|-----------------|
| Sponsor | Patrocinador executivo do projeto | Fórum designado pelo Banco Best |
| Product Owner | Definição de requisitos e priorização | A definir no início do projeto |
| Arquiteto Best | Validação técnica e integração com sistemas existentes | A definir no início do projeto |
| Equipa Segurança | Validação de conformidade e segurança | A definir no início do projeto |
| Equipa Infraestrutura | Suporte Azure e ambientes | A definir no início do projeto |
| Equipa Core Banking | Integração com APIs do Core | A definir no início do projeto |
| Equipa Mobile | Coordenação com app nativa existente | A definir no início do projeto |
| DPO (Data Protection Officer) | Conformidade RGPD | A definir no início do projeto |
| Utilizadores Finais | Clientes do Best | N/A |

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

#### 2.3.2 Âmbito e Priorização

- **Âmbito:** Todas as 35 funcionalidades listadas
- **Critério de Priorização:** Por dependência entre funcionalidades
- **Funcionalidades Exclusivas Web:** Nenhuma (paridade com mobile)
- **Faseamento:** Não previsto (lançamento único)

#### 2.3.3 Suporte Multi-idioma

| Idioma | Prioridade |
|--------|------------|
| Português | Principal |
| Inglês | Secundário |
| Francês | Secundário |

#### 2.3.4 Acessibilidade

- **Referência:** WCAG 2.1 AA

### 2.4 Requisitos Não Funcionais

#### 2.4.1 Performance

| Métrica | Valor | Observação |
|---------|-------|------------|
| Tempo resposta operações críticas | max 3 segundos | Transações, consultas |
| Throughput | 10 TPS | Transações por segundo |
| Tempo carregamento página inicial | max 10 segundos | First Contentful Paint |

> **Nota:** Os valores de throughput e utilizadores concorrentes são estimativas iniciais. Devem ser calibrados com métricas reais da app mobile (utilização normal e em pico).

#### 2.4.2 Disponibilidade
Os valores apresentados são recomendações com base em best practices de mercado. Devem ser ajustados aos objetivos do negócio e alinhados com a realidade existente.


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
| Picos de utilização | Sim | Após envio de campanhas |

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
| **Regulatória** | Conformidade PSD2 | Autenticação forte (SCA) obrigatória |
| **Regulatória** | Regulamentações Banco de Portugal | Requisitos de segurança e auditoria |

### 2.6 Estratégia de Lançamento

A estratégia de transição do canal atual para o novo HomeBanking Web necessita de definição.

| Aspeto | Status | Observação |
|--------|--------|------------|
| **Estratégia de Cutover** | _A definir_ | Big bang vs incremental |
| **Coexistência de Canais** | _A definir_ | Período de transição? |
| **Impacto Infraestrutura** | _A definir_ | Dependente da estratégia |

> **Pendência:** Definir estratégia de switch com o cliente, pois pode influenciar o desenho e a infraestrutura.

## Entregáveis

- [x] Descrição do contexto de negócio
- [x] Matriz de stakeholders com papéis e responsabilidades (contactos a definir no início do projeto)
- [x] Lista priorizada de requisitos funcionais
- [x] Lista de requisitos não funcionais com métricas
- [x] Documentação de restrições técnicas e de negócio
- [x] Lista de pressupostos validados
- [x] Mapa de dependências

## Definições Utilizadas

- [x] [DEF-02-stakeholders.md](../definitions/DEF-02-stakeholders.md) - Status: completed (contactos a definir no início do projeto)
- [x] [DEF-03-requisitos-funcionais.md](../definitions/DEF-03-requisitos-funcionais.md) - Status: completed
- [x] [DEF-04-requisitos-nao-funcionais.md](../definitions/DEF-04-requisitos-nao-funcionais.md) - Status: completed

## Decisões Referenciadas

_Nenhuma decisão arquitetural nesta secção. Esta secção documenta contexto de negócio, requisitos funcionais e não funcionais, que são inputs para decisões arquiteturais nas secções seguintes._

## Itens Pendentes

Os seguintes itens requerem informação adicional:

| Item | Documento | Responsável |
|------|-----------|-------------|
| Contactos dos stakeholders | DEF-02-stakeholders | A definir no início do projeto |
| Requisitos de Acessibilidade WCAG | DEF-09-design-system | Equipa UX |
| Certificações de Segurança | DEF-04-requisitos-nao-funcionais | Área de Segurança |
| Requisitos de Encriptação | DEF-04-requisitos-nao-funcionais | Área de Segurança |
| Política de Retenção de Logs | DEF-04-requisitos-nao-funcionais | Compliance |
| **Estratégia de Lançamento/Cutover** | SEC-02 | Produto/Arquitetura |
| **Calibração de métricas de performance** | SEC-02, SEC-12 | Cliente/Infraestrutura |
