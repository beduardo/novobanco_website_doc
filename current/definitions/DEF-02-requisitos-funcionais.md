---
id: DEF-02-requisitos-funcionais
aliases:
  - Requisitos Funcionais
tags:
  - nextreality-novobanco-website-definitions
  - definitions
  - functional-requirements
approved: true
created: 2026-01-01
hubs:
  - "[[nextreality]]"
para-code: R
reviewed: true
status: completed
---

# DEF-02: Requisitos Funcionais

> **Secao relacionada:** [2 - Contexto de Negocio & Requisitos](../sections/SEC-02-contexto-negocio-requisitos.md)

## Contexto

Definir os requisitos funcionais do HomeBanking web, considerando que parte das features serao equivalentes a aplicacao mobile nativa existente. E necessario identificar quais funcionalidades serao incluidas e sua priorizacao.

## Perguntas a Responder

> **Nota:** Funcionalidades in-scope/out-of-scope estao definidas em [DEF-01-objetivos-documento.md](DEF-01-objetivos-documento.md)
> **Nota:** Requisitos de acessibilidade (WCAG) estao definidos em [DEF-04-design-system.md](DEF-04-design-system.md)
> **Nota:** Requisitos de PWA/Offline estao definidos em [DEF-04-ux-guidelines.md](DEF-04-ux-guidelines.md)

1. Qual e o criterio de priorizacao (MoSCoW, valor de negocio)?
    Por dependencia entre funcionalidades

2. Quais funcionalidades sao obrigatorias para o MVP?
    Todas as 35 funcionalidades fazem parte do MVP.

3. Quais idiomas devem ser suportados?
    Portugues, Ingles, Espanhol

4. Ha requisitos de integracao com outros sistemas alem dos existentes?
    Nao. Todas as integracoes necessarias ja existem no App Mobile.

## Decisoes

### Funcionalidades e Escopo
- **Decisao:** Ver [DEF-01-objetivos-documento.md](DEF-01-objetivos-documento.md) para lista completa de funcionalidades in-scope e out-of-scope
- **Justificacao:** Consolidacao em documento unico para evitar duplicacao

### Priorizacao de Desenvolvimento
- **Decisao:** Priorizacao por dependencia entre funcionalidades
- **Justificacao:** Abordagem tecnica que respeita dependencias arquiteturais

### Suporte Multi-idioma
- **Decisao:** Suporte a 3 idiomas: Portugues, Ingles e Espanhol
- **Justificacao:** Alinhamento com mercados-alvo do banco

### Acessibilidade
- **Decisao:** Ver [DEF-04-design-system.md](DEF-04-design-system.md)
- **Justificacao:** Consolidacao em documento de design system

## Restricoes Conhecidas

- Reutilizacao de APIs e servicos da app mobile existente
- Conformidade com regulamentacoes bancarias (PSD2, etc.)

## Referencias

- [CONTEXT.md](../CONTEXT.md) - Contexto geral do projeto
- Documentacao funcional da app mobile (a fornecer)
- Requisitos regulatorios aplicaveis (a fornecer)
