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

> **Definições requeridas:**
> - [DEF-01-objetivos-documento.md](../definitions/DEF-01-objetivos-documento.md) - Status: completed
>
> **Decisões relacionadas:**
> - Nenhuma decisão arquitetural nesta secção (decisões de documento/escopo)

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

```plantuml
@startuml
!define RECTANGLE class

skinparam backgroundColor #FEFEFE
skinparam componentStyle rectangle

package "Canal Web" {
    [HomeBanking Web\n(SPA)] as WEB
}

package "Canal Mobile" {
    [App Mobile Nativa\n(Existente)] as MOBILE
}

package "Camada de Serviços" {
    [API Gateway] as APIGW
    [Backend Services\n(Reutilizados)] as BACKEND
}

package "Infraestrutura Existente" {
    [Core Banking] as CORE
    [Serviços Terceiros] as THIRD
    database "Base de Dados" as DB
}

WEB --> APIGW : HTTPS
MOBILE --> APIGW : HTTPS
APIGW --> BACKEND
BACKEND --> CORE
BACKEND --> THIRD
BACKEND --> DB

note right of WEB
  Tecnologias 100% Web
  Reutilização de APIs existentes
end note
@enduml
```

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

## Entregáveis

- [x] Declaração clara dos objetivos do documento
- [x] Identificação do público-alvo
- [x] Definição do escopo (in-scope e out-of-scope)
- [x] Diagrama conceptual de alto nível
- [x] Lista de princípios arquiteturais

## Definições Utilizadas

- [x] [DEF-01-objetivos-documento.md](../definitions/DEF-01-objetivos-documento.md) - Status: completed

## Decisões Referenciadas

_Nenhuma decisão arquitetural nesta secção. As decisões documentadas em DEF-01 são decisões de documento (objetivo, público-alvo, nível de detalhe) e escopo, não decisões arquiteturais que requeiram ADRs._

## Perguntas para o Utilizador

_Todas as perguntas desta secção foram respondidas._
