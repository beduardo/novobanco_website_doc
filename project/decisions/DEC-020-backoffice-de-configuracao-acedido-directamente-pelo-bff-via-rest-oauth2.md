---
id: "DEC-020"
title: "Backoffice de Configuração acedido directamente pelo BFF via REST OAuth2"
status: "accepted"
created: 2026-04-17
context: "DEF-19"
affects-definitions:
  - "DEF-12"
  - "DEF-19"
affects-sections:
  - "SEC-03"
  - "SEC-09"
---

# DEC-020: Backoffice de Configuração acedido directamente pelo BFF via REST OAuth2

## Context

O canal web (via BFF) necessita de acesso a serviços de conteúdo e configuração de negócio alojados no Azure. Estes serviços — denominados **Backoffice de Configuração** — disponibilizam conteúdos dinâmicos (notícias, artigos, overlays, imagens, publicidades, temas de investimento, operações públicas de venda, lista de produtos activos), regras de negócio (taxas de simulação de rendimentos para produtos de reforma, contas margem e depósitos a prazo, permissões de acesso e visualização de áreas baseado no perfil ou tipo de conta) e controlos de UX (pedidos de avaliação da APP).

Anteriormente estes serviços estavam referenciados de forma genérica como "Serviços Azure" na arquitectura, sem identificação precisa do seu papel como ponto de integração externo distinto.

## Decision

Os serviços **Backoffice de Configuração** constituem um ponto de integração externo distinto na arquitectura. O BFF acede-lhes **directamente** (sem passar pelo IBM API Gateway ou middleware BEST), via REST/JSON, autenticando com **OAuth2 client credentials** (client_id + client_secret, scope read-only). Todos os serviços são anónimos — não registam qualquer informação de cliente. Os serviços estão alojados no Azure.

## Consequences

- O Backoffice de Configuração é tratado como componente de integração distinto nos diagramas e tabelas de arquitectura (em vez do genérico "Serviços Azure pendente de identificar")
- O BFF é o único ponto de acesso no canal web — acesso directo, sem IBM API Gateway
- A autenticação usa OAuth2 client credentials (não Bearer Token de utilizador), dado que os dados são anónimos e não requerem contexto de sessão
- SEC-03: substituir o package `Serviços Azure (PENDENTE)` por `Backoffice de Configuração` e remover da lista de itens pendentes
- SEC-09: tabela de fluxo de integração (9.1), princípios de integração, e "Decisões Referenciadas" devem referenciar DEC-020
- DEF-12: actualizar tabela de backends do BFF com linha específica para Backoffice de Configuração
- DEF-19: registar Backoffice de Configuração como dependência externa distinta no catálogo de dependências
