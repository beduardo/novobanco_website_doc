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

Especificações arquiteturais de desenvolvimento de Página HomeBanking para banco digital com parte das features equivalentes da aplicação mobile nativa.

## 2. Project Scope

### 2.1 In Scope

- Desenvolvimento da aplicação web HomeBanking (React)
- Integração com APIs existentes do Banco Best
- Integração com infraestrutura mobile nativa existente
- CMS para gestão de conteúdo (.NET)
- Backoffice de administração
- Conformidade regulatória (PSD2, RGPD, PCI-DSS, Banco de Portugal)

### 2.2 Out of Scope

- Desenvolvimento de novas APIs no Core Banking
- Modificações na aplicação mobile nativa existente
- Infraestrutura física (apenas cloud/Azure)
- [A DEFINIR COM CLIENTE]

## 3. General Information

O documento deve ser um HLD com informações para o desenvolvimento do projeto, definindo todas as tecnologias e estruturas necessárias para isso. Ele deve ser completo para que uma equipa consiga preparar um plano de desenvolvimento envolvendo desde o Assessment inicial para a definição completa das histórias de utilizador até à entrega do software.

### 3.1 Deliverables do HLD

- Diagramas arquiteturais (C4 Model)
- Especificações de integração
- Modelo de deployment
- Estratégia de monitorização
- Plano de migração e implementação

### 3.2 Pontos Técnicos Relevantes

> **Detalhes:** Ver definições específicas de cada secção

- Metodologia de desenvolvimento dos canais Best
- Perfis técnicos necessários (React, .NET, iOS, Android)
- Modelo de arquitetura global (canais e aplicações conexas)
- Componentes de infraestrutura (cache, GitHub, DevOps, Azure)
- Modelo de trabalho entre equipas

### 3.3 Informações Adicionais

- A aplicação utilizará infraestrutura e serviços criados para a aplicação mobile nativa já existente
- O cliente já possui um APP Mobile com features equivalentes que devem ser replicadas
- Deve definir os requisitos funcionais e não funcionais, atendendo os padrões internacionais
- Um documento do Word deve ser gerado ao fim do trabalho, sem frontmatter e nem referências aos documentos Markdown auxiliares como Definições e Decisões. Todos os seus diagramas PlantUML e MermaidJS precisam ser convertidos para imagens.
- Documento auxiliar de perguntas pendentes para reuniões com cliente
- Tudo deve ser escrito em Português Europeu, utilizando acentuação correta.

## 4. Premissas e Restrições

### 4.1 Premissas

- A infraestrutura Azure já está disponível e configurada
- APIs do Core Banking estão documentadas e estáveis
- Equipa de desenvolvimento tem experiência em React e .NET
- [A VALIDAR COM CLIENTE]

### 4.2 Restrições

- Conformidade obrigatória com regulamentação bancária portuguesa
- Integração com sistemas legados existentes
- Utilização de infraestrutura Azure do NovoBanco
- [A VALIDAR COM CLIENTE]

## 5. Definições de Referência

| Tópico | Definição | Descrição |
|--------|-----------|-----------|
| Stakeholders | [DEF-02-stakeholders.md](definitions/DEF-02-stakeholders.md) | Partes interessadas e papéis |
| Requisitos Funcionais | [DEF-02-requisitos-funcionais.md](definitions/DEF-02-requisitos-funcionais.md) | Funcionalidades do sistema |
| Requisitos Não Funcionais | [DEF-02-requisitos-nao-funcionais.md](definitions/DEF-02-requisitos-nao-funcionais.md) | Quality attributes e métricas |
| Dependências Externas | [DEF-09-integracao-interfaces.md](definitions/DEF-09-integracao-interfaces.md) | Sistemas externos e integrações |

## 6. List of Sections

| Section | Title | Description |
|---------|-------|-------------|
| 1 | Sumário Executivo | Objetivos do documento e visão geral da arquitetura |
| 2 | Contexto de Negócio & Requisitos | Contexto da solução, stakeholders, requisitos funcionais e não funcionais, restrições |
| 3 | Visão Geral da Solução | Princípios de Arquitetura, Diagrama Conceptual, Casos de Uso |
| 4 | Experiência do Utilizador & Arquitetura Frontend | Arquitetura de Informação, UI/UX, Jornadas, Multi-idioma, PWA, Stack Frontend, Design System |
| 5 | Arquitetura Backend & Serviços | Decomposição de Serviços, API, Comunicação, Modelo de Domínio, Resiliência, Padrões |
| 6 | Arquitetura de Dados | Modelo de Dados, Armazenamento, Encriptação, Retenção, Backup, RGPD, Classificação |
| 7 | Autenticação & Autorização | Autenticação, Autorização, Tokens, Sessões, MFA, SSO, Fluxos, Revogação |
| 8 | Segurança & Conformidade | Modelo de Ameaças, OWASP, PSD2, RGPD, PCI-DSS, Auditoria, Incidentes |
| 9 | Integração & Interfaces Externas | Core Banking, KYC/AML, Notificações, Cartões, Open Banking, Message Broker |
| 10 | Arquitetura Operacional | Infraestrutura, Ambientes, CI/CD, Deploy, IaC, Secrets, DR, Backup |
| 11 | Observabilidade & Operações | Observabilidade, Métricas, Tracing, Logging, SLIs, SLOs, SLAs, Alertas |
| 12 | Desempenho & Fiabilidade | Carga, Performance, Caching, Otimização, Auto-scaling, Failover |
| 13 | Estratégia de Testes | Unitários, Integração, E2E, Performance, Segurança, Acessibilidade |
| 14 | Plano de Migração & Implementação | Roadmap, Cutover, Legado, Migração, Rollback, Formação, Hypercare |
| 15 | Governação & Roadmap | Governação, Decisões, Roadmap, Dívida Técnica, KPIs |

## 7. Glossário

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

## 8. Document Control

| Versão | Data | Autor | Alterações |
|--------|------|-------|------------|
| 0.1 | 2026-01-01 | NextReality | Versão inicial |
| 0.2 | 2026-01-13 | NextReality | Adição de escopo, premissas, restrições, quality attributes e glossário |
| 0.3 | 2026-01-13 | NextReality | Simplificação - conteúdos detalhados movidos para definições |
| 0.4 | 2026-01-15 | NextReality | Correção de acentuação em português europeu |

