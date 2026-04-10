---
id: "DEC-013"
title: "Rotacao de Access Token por Resposta do Backend"
status: "accepted"
created: 2026-04-10
context: "DEF-13"
affects-definitions:
  - "DEF-13"
affects-sections:
  - "SEC-07"
---

# DEC-013: Rotacao de Access Token por Resposta do Backend

> **Related definitions:** [DEF-13-autenticacao-oauth.md](../definitions/DEF-13-autenticacao-oauth.md)
> **Related sections:** [SEC-07 - Autenticacao & Autorizacao](../sections/SEC-07-autenticacao-autorizacao.md)
> **Amends:** [DEC-002 - Gestao de Sessoes e Tokens](./DEC-002-gestao-sessoes-tokens.md)

## Context

O backend (Siebel) implementa um mecanismo de rotacao de Access Token: cada resposta a um pedido autenticado devolve um novo Access Token, que substitui o anterior. Este comportamento e inerente ao protocolo OAuth 1.1 utilizado pelo Siebel.

Esta caracteristica elimina a necessidade de logica de renovacao proativa de tokens no BFF, uma vez que o token e automaticamente actualizado a cada interaccao com o backend.

## Decision

O BFF **nao implementa logica de renovacao proativa de Access Token**. Em vez disso:

- Cada resposta do backend inclui um novo Access Token rotacionado
- O BFF actualiza o Access Token em cache (Redis) apos cada resposta do backend
- O Access Token armazenado em cache e sempre o mais recente recebido
- Nao existe temporizador de renovacao nem mecanismo de refresh separado

## Consequences

### Positive
- Simplicidade: sem logica de renovacao no BFF
- Token sempre actualizado apos cada uso — menor janela de ataque
- Eliminacao de race conditions de renovacao concorrente
- Sem necessidade de Refresh Token (confirmado tambem em DEC-002)

### Negative
- O BFF deve sempre persistir o novo token recebido antes de responder ao Frontend
- Se uma resposta do backend nao incluir o novo token (erro, timeout), o BFF deve tratar este caso sem invalidar a sessao
- Requer atencao na implementacao para garantir atomicidade: receber resposta → guardar novo token → responder ao Frontend

## Notes

- Esta decisao amenda a seccao "Renovacao" de DEC-002, que mencionava renovacao proativa pelo BFF
- O TTL do Access Token em cache (15 min) permanece valido como salvaguarda, mas na pratica o token e substituido a cada pedido
