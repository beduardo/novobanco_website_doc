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

1. Qual e a lista completa de funcionalidades da app mobile?
    A lista de funcionalidade completa não se aplica.
2. Quais funcionalidades serao replicadas no HomeBanking web?
   Registo, Login, Recuperação de Acessos, Home, Área Pessoal, Património, Ordens Pendentes, Histórico de Operações, Outros Bancos, Dashboard, Carteiras, Saldos e Movimentos, Confirmação de Operações, Comprovativos e Extratos, Eventos Corporativos, Seguros de proteção, Área do Viajante, Bea, Warrants, Áções, ETF, Fundos, Obrigações, Caregamentos, MBWay (Somente componentes não SDK), Transferências, Pagamentos, Wishlist, Índices, Notícias eternas, Temas investimento, Depósito a prazo, Leilões, Ofertas públicas, Unit linked, Robot Advisor, BTP
3. Ha funcionalidades exclusivas para o canal web?
    Não
4. Qual e o criterio de priorizacao (MoSCoW, valor de negocio)?
    Por dependendência
5. Quais funcionalidades sao obrigatorias para o MVP?
    Todas fazem parte do MVP.
6. Existem requisitos de acessibilidade especificos (WCAG)?
    Ainda é necessário aprofundar este tema
7. Quais idiomas devem ser suportados?
    Português, Inglês, Espanhol
8. Ha requisitos de integracao com outros sistemas?
    Sim, mas são integrações já existentes no App Mobile

## Decisoes

### Funcionalidades da App Mobile a Replicar
- **Decisao:** 35 funcionalidades serao replicadas no HomeBanking Web:
  - **Autenticacao:** Registo, Login, Recuperacao de Acessos
  - **Areas Principais:** Home, Area Pessoal, Dashboard
  - **Patrimonio:** Patrimonio, Carteiras, Saldos e Movimentos
  - **Operacoes:** Ordens Pendentes, Historico de Operacoes, Confirmacao de Operacoes
  - **Documentos:** Comprovativos e Extratos
  - **Investimentos:** Warrants, Acoes, ETF, Fundos, Obrigacoes, Indices, Temas Investimento, Deposito a Prazo, Leiloes, Ofertas Publicas, Unit Linked, Robot Advisor, BTP
  - **Pagamentos:** Transferencias, Pagamentos, Carregamentos, MBWay (apenas componentes nao-SDK)
  - **Outros:** Outros Bancos, Eventos Corporativos, Seguros de Protecao, Area do Viajante, Bea, Wishlist, Noticias Externas
- **Justificacao:** Paridade funcional com a app mobile para experiencia consistente
- **Alternativas consideradas:** Lista completa de funcionalidades da app mobile (nao se aplica - escopo ja definido)

### Funcionalidades Exclusivas Web
- **Decisao:** Nao ha funcionalidades exclusivas para o canal web
- **Justificacao:** Objetivo e paridade funcional com a app mobile
- **Alternativas consideradas:** Funcionalidades adicionais para web (descartado para manter consistencia)

### MVP - Funcionalidades Obrigatorias
- **Decisao:** Todas as 35 funcionalidades listadas fazem parte do MVP
- **Justificacao:** Lancamento com paridade funcional completa
- **Alternativas consideradas:** MVP reduzido com funcionalidades prioritarias (descartado)

### Priorizacao de Desenvolvimento
- **Decisao:** Priorizacao por dependencia entre funcionalidades
- **Justificacao:** Abordagem tecnica que respeita dependencias arquiteturais
- **Alternativas consideradas:** MoSCoW, Valor de negocio (descartados por nao se aplicarem ao contexto)

### Requisitos de Acessibilidade
- **Decisao:** _A definir_ - Tema requer aprofundamento
- **Justificacao:** Necessidade de avaliar requisitos WCAG aplicaveis
- **Alternativas consideradas:** WCAG 2.1 AA (referencia de industria a considerar)

### Suporte Multi-idioma
- **Decisao:** Suporte a 3 idiomas: Portugues, Ingles e Espanhol
- **Justificacao:** Alinhamento com mercados-alvo do banco
- **Alternativas consideradas:** Apenas Portugues (descartado por limitacao de mercado)

### Integracoes
- **Decisao:** Reutilizacao das integracoes existentes na app mobile
- **Justificacao:** Evitar duplicacao de esforco e garantir consistencia
- **Alternativas consideradas:** Novas integracoes (descartado - nao ha necessidade)

## Restricoes Conhecidas

- Reutilizacao de APIs e servicos da app mobile existente
- Conformidade com regulamentacoes bancarias (PSD2, etc.)

## Referencias

- [CONTEXT.md](../CONTEXT.md) - Contexto geral do projeto
- Documentacao funcional da app mobile (a fornecer)
- Requisitos regulatorios aplicaveis (a fornecer)
