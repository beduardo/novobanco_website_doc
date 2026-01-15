---
id: CONTEXT
aliases: []
tags:
  - nextreality-novobanco-website
approved: true
created: 2026-01-01
hubs:
  - "[[nextreality]]"
para-code: R
reviewed: true
---

# CONTEXT

## 1. Main Objectives

Especificacoes arquiteturais de desenvolvimento de Pagina HomeBanking para banco digital com parte das features equivalentes da aplicacao mobile nativa.

## 2. Project Scope

### 2.1 In Scope

- Desenvolvimento da aplicacao web HomeBanking (React)
- Integracao com APIs existentes do Banco Best
- Integracao com infraestrutura mobile nativa existente
- CMS para gestao de conteudo (.NET)
- Backoffice de administracao
- Conformidade regulatoria (PSD2, RGPD, PCI-DSS, Banco de Portugal)

### 2.2 Out of Scope

- Desenvolvimento de novas APIs no Core Banking
- Modificacoes na aplicacao mobile nativa existente
- Infraestrutura fisica (apenas cloud/Azure)
- [A DEFINIR COM CLIENTE]

## 3. General Information

O documento deve ser um HLD com informacoes para o desenvolvimento do projeto, definindo todas as tecnologias e estruturas necessarias para isso. Ele deve ser completo para que uma equipa consiga preparar um plano de desenvolvimento envolvendo desde o Assessment inicial para a definicao completa das historias de usuario ate a entrega do software.

### 3.1 Deliverables do HLD

- Diagramas arquiteturais (C4 Model)
- Especificacoes de integracao
- Modelo de deployment
- Estrategia de monitorizacao
- Plano de migracao e implementacao

### 3.2 Pontos Tecnicos Relevantes

> **Detalhes:** Ver definicoes especificas de cada secao

- Metodologia de desenvolvimento dos canais Best
- Perfis tecnicos necessarios (React, .NET, iOS, Android)
- Modelo de arquitetura global (canais e aplicacoes conexas)
- Componentes de infraestrutura (cache, GitHub, DevOps, Azure)
- Modelo de trabalho entre equipas

### 3.3 Informacoes Adicionais

- A aplicacao utilizara infraestrutura e servicos criados para a aplicacao mobile nativa ja existente
- O cliente ja possui um APP Mobile com features equivalentes que devem ser replicadas
- Deve definir os requisitos funcionais e nao funcionais, atendendo os padroes internacionais
- Um documento do Word deve ser gerado ao fim do trabalho
- Documento auxiliar de perguntas pendentes para reunioes com cliente

## 4. Premissas e Restricoes

### 4.1 Premissas

- A infraestrutura Azure ja esta disponivel e configurada
- APIs do Core Banking estao documentadas e estaveis
- Equipa de desenvolvimento tem experiencia em React e .NET
- [A VALIDAR COM CLIENTE]

### 4.2 Restricoes

- Conformidade obrigatoria com regulamentacao bancaria portuguesa
- Integracao com sistemas legados existentes
- Utilizacao de infraestrutura Azure do NovoBanco
- [A VALIDAR COM CLIENTE]

## 5. Definicoes de Referencia

| Topico | Definicao | Descricao |
|--------|-----------|-----------|
| Stakeholders | [DEF-02-stakeholders.md](definitions/DEF-02-stakeholders.md) | Partes interessadas e papeis |
| Requisitos Funcionais | [DEF-02-requisitos-funcionais.md](definitions/DEF-02-requisitos-funcionais.md) | Funcionalidades do sistema |
| Requisitos Nao Funcionais | [DEF-02-requisitos-nao-funcionais.md](definitions/DEF-02-requisitos-nao-funcionais.md) | Quality attributes e metricas |
| Dependencias Externas | [DEF-09-integracao-interfaces.md](definitions/DEF-09-integracao-interfaces.md) | Sistemas externos e integracoes |

## 6. List of Sections

| Section | Title | Description |
|---------|-------|-------------|
| 1 | Sumario Executivo | Objetivos do documento e visao geral da arquitetura |
| 2 | Contexto de Negocio & Requisitos | Contexto da solucao, stakeholders, requisitos funcionais e nao funcionais, restricoes |
| 3 | Visao Geral da Solucao | Principios de Arquitetura, Diagrama Conceptual, Casos de Uso |
| 4 | Experiencia do Utilizador & Arquitetura Frontend | Arquitetura de Informacao, UI/UX, Jornadas, Multi-idioma, PWA, Stack Frontend, Design System |
| 5 | Arquitetura Backend & Servicos | Decomposicao de Servicos, API, Comunicacao, Modelo de Dominio, Resiliencia, Padroes |
| 6 | Arquitetura de Dados | Modelo de Dados, Armazenamento, Encriptacao, Retencao, Backup, RGPD, Classificacao |
| 7 | Autenticacao & Autorizacao | Autenticacao, Autorizacao, Tokens, Sessoes, MFA, SSO, Fluxos, Revogacao |
| 8 | Seguranca & Conformidade | Modelo de Ameacas, OWASP, PSD2, RGPD, PCI-DSS, Auditoria, Incidentes |
| 9 | Integracao & Interfaces Externas | Core Banking, KYC/AML, Notificacoes, Cartoes, Open Banking, Message Broker |
| 10 | Arquitetura Operacional | Infraestrutura, Ambientes, CI/CD, Deploy, IaC, Secrets, DR, Backup |
| 11 | Observabilidade & Operacoes | Observabilidade, Metricas, Tracing, Logging, SLIs, SLOs, SLAs, Alertas |
| 12 | Desempenho & Fiabilidade | Carga, Performance, Caching, Otimizacao, Auto-scaling, Failover |
| 13 | Estrategia de Testes | Unitarios, Integracao, E2E, Performance, Seguranca, Acessibilidade |
| 14 | Plano de Migracao & Implementacao | Roadmap, Cutover, Legado, Migracao, Rollback, Formacao, Hypercare |
| 15 | Governacao & Roadmap | Governacao, Decisoes, Roadmap, Divida Tecnica, KPIs |

## 7. Glossario

| Termo | Definicao |
|-------|-----------|
| HLD | High-Level Design - Documento de arquitetura de alto nivel |
| HomeBanking | Portal web de servicos bancarios para clientes |
| Core Banking | Sistema central de operacoes bancarias |
| PSD2 | Payment Services Directive 2 - Diretiva europeia de servicos de pagamento |
| RGPD | Regulamento Geral de Protecao de Dados |
| PCI-DSS | Payment Card Industry Data Security Standard |
| SLA | Service Level Agreement - Acordo de nivel de servico |
| SLO | Service Level Objective - Objetivo de nivel de servico |
| SLI | Service Level Indicator - Indicador de nivel de servico |
| MFA | Multi-Factor Authentication - Autenticacao multifator |
| SSO | Single Sign-On - Autenticacao unica |
| KYC | Know Your Customer - Processo de identificacao de clientes |
| AML | Anti-Money Laundering - Prevencao de lavagem de dinheiro |
| API | Application Programming Interface |
| CMS | Content Management System - Sistema de gestao de conteudo |
| CI/CD | Continuous Integration / Continuous Deployment |
| PWA | Progressive Web App |
| WCAG | Web Content Accessibility Guidelines |
| OWASP | Open Web Application Security Project |
| BFF | Backend for Frontend - Camada de backend especifica para o frontend |

## 8. Document Control

| Versao | Data | Autor | Alteracoes |
|--------|------|-------|------------|
| 0.1 | 2026-01-01 | NextReality | Versao inicial |
| 0.2 | 2026-01-13 | NextReality | Adicao de escopo, premissas, restricoes, quality attributes e glossario |
| 0.3 | 2026-01-13 | NextReality | Simplificacao - conteudos detalhados movidos para definicoes |

## 9. TO DO
- Criar o documento completo com as informações que temos até o momento. Ele será a unificação  de todas as seções. Faça uma cópia do conteúdo sem frontmatter e marcadores.
