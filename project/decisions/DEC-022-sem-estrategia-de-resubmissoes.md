---
id: "DEC-022"
title: "Sem Estratégia de Resubmissões"
status: "accepted"
created: 2026-04-17
context: "DEF-15"
affects-definitions: []
affects-sections:
  - "SEC-05"
---

# DEC-022: Sem Estratégia de Resubmissões

## Contexto

O Rate Limiting documentado em SEC-05 (secção 5.6) incluía uma linha "_A definir_" para Resubmissões ("Estratégia para pedidos duplicados"). Esta entrada foi introduzida como placeholder mas nunca foi concretizada, uma vez que o canal web HomeBanking não prevê resubmissão automática de pedidos duplicados. A responsabilidade de rate limiting e controlo de pedidos recai no API Gateway IBM.

## Decisão

O canal HomeBanking Web **não implementa estratégia de resubmissões** (idempotency/deduplicação de pedidos). A entrada correspondente em SEC-05 (§5.6) é removida. O BFF não implementa retry automático — erros transientes são propagados ao utilizador com mensagem de erro adequada (ver DEF-15).

## Consequências

- A linha "Resubmissões" é removida da tabela de Rate Limiting em SEC-05 (§5.6)
- O API Gateway IBM é responsável por rate limiting e controlo de pedidos duplicados ao nível de infraestrutura
- O BFF não implementa idempotency keys nem deduplicação de pedidos
