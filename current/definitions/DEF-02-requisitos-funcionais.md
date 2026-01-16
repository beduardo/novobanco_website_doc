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

> **Secção relacionada:** [2 - Contexto de Negócio & Requisitos](../sections/SEC-02-contexto-negocio-requisitos.md)

## Contexto

Definir os requisitos funcionais do HomeBanking web, considerando que parte das features serão equivalentes à aplicação mobile nativa existente. É necessário identificar quais funcionalidades serão incluídas e a sua priorização.

## Perguntas a Responder

> **Nota:** Funcionalidades in-scope/out-of-scope estão definidas em [DEF-01-objetivos-documento.md](DEF-01-objetivos-documento.md)
> **Nota:** Requisitos de acessibilidade (WCAG) estão definidos em [DEF-04-design-system.md](DEF-04-design-system.md)
> **Nota:** Requisitos de PWA/Offline estão definidos em [DEF-04-ux-guidelines.md](DEF-04-ux-guidelines.md)

1. Qual é o critério de priorização (MoSCoW, valor de negócio)?
    Por dependência entre funcionalidades

2. Quais funcionalidades são obrigatórias para o MVP?
    Todas as 35 funcionalidades fazem parte do MVP.

3. Quais idiomas devem ser suportados?
    Português, Inglês, Espanhol

4. Há requisitos de integração com outros sistemas além dos existentes?
    Não. Todas as integrações necessárias já existem no App Mobile.

## Decisões

### Funcionalidades e Escopo
- **Decisão:** Ver [DEF-01-objetivos-documento.md](DEF-01-objetivos-documento.md) para lista completa de funcionalidades in-scope e out-of-scope
- **Justificação:** Consolidação em documento único para evitar duplicação

### Priorização de Desenvolvimento
- **Decisão:** Priorização por dependência entre funcionalidades
- **Justificação:** Abordagem técnica que respeita dependências arquiteturais

### Suporte Multi-idioma
- **Decisão:** Suporte a 3 idiomas: Português, Inglês e Espanhol
- **Justificação:** Alinhamento com mercados-alvo do banco

### Acessibilidade
- **Decisão:** Ver [DEF-04-design-system.md](DEF-04-design-system.md)
- **Justificação:** Consolidação em documento de design system

## Restrições Conhecidas

- Reutilização de APIs e serviços da app mobile existente
- Conformidade com regulamentações bancárias (PSD2, etc.)

## Referências

- [CONTEXT.md](../CONTEXT.md) - Contexto geral do projeto
- Documentação funcional da app mobile (a fornecer)
- Requisitos regulatórios aplicáveis (a fornecer)
