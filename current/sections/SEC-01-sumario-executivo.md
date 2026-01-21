---
aliases:
  - Sumário Executivo
tags:
  - nextreality-novobanco-website-sections
  - sections
  - executive-summary
approved: true
created: 2026-01-01
hubs:
  - "[[nextreality]]"
para-code: R
reviewed: true
status: in-progress
---

# 1. Sumário Executivo

## Definições e Decisões
> **Definições requeridas:**
> - [DEF-01-objetivos-documento.md](../definitions/DEF-01-objetivos-documento.md) - Status: completed
>
> **Decisões relacionadas:**
> - [DEC-011-diagrama-arquitetura-unico.md](../decisions/DEC-011-diagrama-arquitetura-unico.md) - Status: accepted

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

> **Diagrama:** Ver [Secção 3.2 - Diagrama Conceptual](SEC-03-visao-geral-solucao.md#32-diagrama-conceptual) para a arquitetura completa do sistema.

A arquitetura do HomeBanking Web segue o padrão **BFF (Backend for Frontend)**, onde:

| Componente | Descrição |
|------------|-----------|
| **Frontend Web (SPA)** | Aplicação React executada no browser do cliente |
| **BFF Web (.NET 8)** | Camada de agregação e transformação específica para o canal web |
| **API Gateway (IBM)** | Gateway existente para acesso aos Backend Services |
| **Backend Services (Siebel)** | Serviços de negócio existentes que validam tokens e acedem ao Core Banking |

**Princípios Fundamentais:**
- Reutilização da infraestrutura e serviços existentes através do BFF
- Tecnologias 100% Web (sem dependências de componentes nativos)
- Conformidade com regulamentações bancárias portuguesas
- Isolamento do frontend de complexidades dos sistemas legados via BFF

### 1.5 Princípios Orientadores

| Princípio | Descrição |
|-----------|-----------|
| **Reutilização** | Maximizar uso de APIs e serviços existentes da app mobile |
| **Segurança** | Conformidade com regulamentações bancárias e PSD2 |
| **Paridade Funcional** | Experiência consistente entre canais web e mobile |
| **Auditabilidade** | Suporte a requisitos de compliance e auditoria |
| **Escalabilidade** | Arquitetura preparada para crescimento |

## Diagramas

Ver diagrama de arquitetura de referência na [Secção 3.2](SEC-03-visao-geral-solucao.md#32-diagrama-conceptual).

## Entregáveis

- [x] Declaração clara dos objetivos do documento
- [x] Identificação do público-alvo
- [x] Definição do escopo (in-scope e out-of-scope)
- [x] Referência ao diagrama de arquitetura (secção 3.2)
- [x] Lista de princípios arquiteturais

## Definições Utilizadas

- [x] [DEF-01-objetivos-documento.md](../definitions/DEF-01-objetivos-documento.md) - Status: completed

## Decisões Referenciadas

- [x] [DEC-011-diagrama-arquitetura-unico.md](../decisions/DEC-011-diagrama-arquitetura-unico.md) - Status: accepted (diagrama único de referência)

## Perguntas para o Utilizador

_Todas as perguntas desta secção foram respondidas._
