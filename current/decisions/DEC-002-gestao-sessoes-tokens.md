---
id: DEC-002-gestao-sessoes-tokens
aliases:
  - Gestao de Sessoes e Tokens
tags:
  - nextreality-novobanco-website-decisions
  - decisions
  - sessions
  - tokens
  - security
approved: true
created: 2026-01-04
hubs:
  - "[[nextreality]]"
para-code: R
reviewed: true
status: accepted
---

# ADR-002: Gestao de Sessoes e Tokens

> **Related sections:** [7 - Autenticacao & Autorizacao](../sections/SEC-07-autenticacao-autorizacao.md)
> **Related definitions:** [DEF-07-autenticacao-autorizacao.md](../definitions/DEF-07-autenticacao-autorizacao.md), [DEF-05-arquitetura-bff.md](../definitions/DEF-05-arquitetura-bff.md)

## Status

Accepted

## Context

O HomeBanking Web necessita de uma estrategia de gestao de sessoes e tokens que:
- Equilibre seguranca com usabilidade
- Proteja tokens OAuth contra exposicao no browser
- Permita renovacao silenciosa de tokens
- Cumpra requisitos de timeout para aplicacoes bancarias

### Business Goals
- Sessao segura mas conveniente
- Experiencia sem interrupcoes desnecessarias
- Protecao contra ataques de sessao

### Technical Constraints
- BFF como intermediario de autenticacao
- Tokens OAuth do backend nao podem ser expostos ao browser
- Cookies HttpOnly para sessao (definido em DEF-05)

### Non-functional Requirements
- Timeout de sessao conforme boas praticas bancarias
- Conformidade com requisitos de auditoria

## Decision

Implementar **arquitetura de tokens em dois niveis**: tokens de sessao (Browser-BFF) e tokens de backend (BFF-Backend).

**Configuracao de Sessao:**
- Timeout por inatividade: **10 minutos**
- Timeout absoluto: **30 minutos**
- Sessao exclusiva: Desejavel (pendente aprovacao cliente)
- Aviso de expiracao: Popup com temporizador

**Configuracao de Tokens Backend:**
- Access Token TTL: **15 minutos**
- Refresh Token TTL: **7 dias**
- Armazenamento: **BFF cache** (Redis ou similar)

**Configuracao de Sessao Web:**
- Cookie: `token_sessao_spa`
- Atributos: HttpOnly, Secure, SameSite=Strict
- Geracao: GUID no BFF apos autenticacao bem-sucedida
- Funcao: Chave de lookup no Redis

**Armazenamento Redis:**
- Chave: `session:{token_sessao_spa}`
- Valor: JSON com apiToken, contexto de utilizador, flags
- TTL: 30 minutos (timeout absoluto de sessao)
- Tipo: Redis Cluster para alta disponibilidade

**Dados Armazenados por Sessao:**

| Dado | Descricao | Origem |
|------|-----------|--------|
| `apiToken` | Token de acesso a ApiPsd2 | Resposta AUT_004 |
| `mustChangePassword` | Flag de alteracao obrigatoria | Resposta AUT_004 |
| `needStrongAuthentication` | Flag SCA necessario | Resposta AUT_004 |
| `firstLogin` | Flag primeiro acesso | Resposta AUT_004 |
| `user_context` | Dados do utilizador (nao sensiveis) | Resposta login |

**Renovacao:**
- Refresh silencioso conforme atividade do utilizador
- BFF renova tokens backend automaticamente antes de expiracao

**Importante:** O `sasToken` retornado pela ApiPsd2 **nao e utilizado** no canal web. Este token e especifico para a app mobile.

## Alternatives Considered

### Alternative 1: Tokens OAuth diretamente no browser
- **Description:** Access/Refresh tokens armazenados em localStorage ou cookies no browser
- **Pros:** Arquitetura mais simples, menos hops
- **Cons:** Exposicao de tokens sensiveis, risco XSS
- **Why not chosen:** Seguranca insuficiente para aplicacao bancaria

### Alternative 2: Sessao apenas com cookies de sessao (sem tokens)
- **Description:** BFF mantem estado de sessao completo, browser apenas com session ID
- **Pros:** Tokens nunca expostos ao browser
- **Cons:** BFF stateful, complexidade de escalabilidade
- **Why not chosen:** Combinacao de cookies de sessao COM tokens no BFF oferece melhor equilibrio

### Alternative 3: Timeout mais longo (30min inatividade)
- **Description:** Timeout de inatividade mais permissivo
- **Pros:** Melhor UX, menos interrupcoes
- **Cons:** Maior janela de ataque se sessao for comprometida
- **Why not chosen:** 10 minutos e padrao de industria para aplicacoes bancarias

## Consequences

### Positive
- Tokens OAuth nunca expostos ao browser
- Renovacao transparente para o utilizador
- Timeouts adequados para aplicacao bancaria
- Protecao contra XSS (tokens nao acessiveis via JavaScript)

### Negative
- Complexidade de dois niveis de tokens
- BFF precisa gerir cache de tokens
- Sessao exclusiva pode causar inconveniencia se utilizador tiver multiplos tabs

## Notes

- Sessao exclusiva (logout de outras sessoes) necessita aprovacao final do cliente
- Estrategia de comunicacao ao utilizador sobre expiracao via popup com temporizador
