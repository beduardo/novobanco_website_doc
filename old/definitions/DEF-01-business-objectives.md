---
id: DEF-01-business-objectives
aliases:
  - Novo Banco Business Objectives
tags:
  - nextreality-novobanco-website-definitions
approved: true
created: 2025-12-22
hubs:
  - "[[nextreality]]"
para-code: R
reviewed: true
---
# DEF-01: Objetivos de Negocio

> **Status:** estrutura
> **Secao relacionada:** 01 - Sumario Executivo

## Contexto

Este documento define os objetivos de negocio que motivam a criacao da plataforma web de Homebanking, incluindo os beneficios esperados, metricas de sucesso e value proposition.

## Questoes a Responder

1. Quais sao os principais objetivos de negocio para a criacao do Homebanking web?
R.: O website conterá a maior parte das funcionalidades do App mobile já existente. Inclusive com a autenticação sendo parcialmente feita pelo app.
2. Qual o publico-alvo principal (todos os clientes ou segmento especifico)?
R.: Todos os clientes do banco
3. A plataforma deve ter paridade total com o App Mobile ou apenas funcionalidades selecionadas?
R.: A plataforma web deverá possuir todas as funcionalidades que não dependam do telemóvel para serem utilizadas.

## Decisoes

### Objetivos Primarios
- **Decisao:** Atendimento das necessidades de um cliente do banco, permitindo melhor visão da sua situação financeira.
- **Justificativa:** O sistema atual está defasado com o app mobile existente

### Paridade com App Mobile
- **Decisao:** Parcial.
- **Justificativa:** O cliente precisa ter outro canal além do App Mobile para realizar suas operações. Somente as operações que dependam de recursos exclusivos do telemóvel (como o MBWay) ficarão excluídos da solução.

## Restricoes Conhecidas

- A plataforma deve manter o mesmo processo de autenticacao OAuth do App Mobile
- Infraestrutura atual possui gateway para throttling e segurança

## Referencias

- [architectural_document_structure_novo_banco.md](../architectural_document_structure_novo_banco.md) - Contexto inicial
