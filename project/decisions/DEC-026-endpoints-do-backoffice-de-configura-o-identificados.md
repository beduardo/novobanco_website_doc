---
id: "DEC-026"
title: "Endpoints do Backoffice de Configuração identificados"
status: "accepted"
created: 2026-04-20
context: "DEF-19"
affects-definitions:
  - "DEF-19"
affects-sections:
  - "SEC-09"
---

# DEC-026: Endpoints do Backoffice de Configuração identificados

## Context

O Backoffice de Configuração foi reconhecido como ponto de integração externo distinto na arquitectura (DEC-020), com acesso directo pelo BFF via REST/OAuth2 client credentials. No entanto, a lista concreta dos seus endpoints permanecia pendente (SEC-09 §9.3, "Questões a Resolver"). O cliente forneceu a lista completa dos endpoints disponíveis.

## Decision

Os endpoints do **Backoffice de Configuração** são os seguintes:

### Conteúdos Dinâmicos

| Endpoint | Função |
|----------|--------|
| `advertising` | Publicidades / cards promocionais |
| `article` | Artigos de conteúdo |
| `overlay` | Overlays informativos |
| `externallink` | Links de informação externa |
| `opvs` | Operações públicas de venda |
| `investmentThemes` | Temas de investimento |

### Regras de Negócio e Dados de Suporte

| Endpoint | Função |
|----------|--------|
| `accountRestriction` | Permissões de acesso e visualização de áreas por perfil/tipo de conta |
| `deposits` | Taxas de simulação de depósitos a prazo |
| `availableoptions` | Lista de produtos activos / opções disponíveis |
| `retirement` | Dados de produtos de reforma |
| `retirementSimulator` | Taxas de simulação de rendimentos para produtos de reforma |
| `marginAccounts` | Taxas de simulação para contas margem |
| `servicePaymentEntity` | Entidades para pagamentos de serviços |

### Controlos de UX

| Endpoint | Função |
|----------|--------|
| `EvaluationFeedbackByArea` | Pedidos de avaliação da app por área |

Todos os endpoints são acedidos directamente pelo BFF via REST/JSON, com autenticação OAuth2 client credentials (read-only), conforme DEC-020.

## Consequences

- SEC-09 §9.3: remover a questão pendente "Lista completa de endpoints" e actualizar a tabela "Serviços Identificados" com os endpoints acima
- DEF-19: actualizar a tabela "APIs de Backoffice (CMS)" com os nomes reais dos endpoints
- Os endpoints são todos anónimos (sem contexto de sessão de cliente), consistente com DEC-020
- Qualquer endpoint adicional identificado no futuro requer actualização desta decisão
