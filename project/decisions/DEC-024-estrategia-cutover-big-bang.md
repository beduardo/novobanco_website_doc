---
id: "DEC-024"
title: "Estrategia de Cutover Big Bang"
status: "accepted"
created: 2026-04-18
context: "DEF-24"
affects-definitions:
  - "DEF-24"
affects-sections:
  - "SEC-14"
---

# DEC-024: Estratégia de Cutover Big Bang

## Context

O plano de migração (DEF-24) definia inicialmente uma estratégia de lançamento gradual (phased rollout) com feature flags, para mitigar riscos através de activação progressiva por segmentos de utilizadores. Após análise do contexto operacional do Novo Banco, o cliente determinou a adopção de uma estratégia Big Bang, motivada por exigência explícita do cliente, simplicidade operacional e limitações técnicas que inviabilizam o rollout faseado.

## Decision

A estratégia de cutover será **Big Bang**: o HomeBanking Web será activado simultaneamente para todos os utilizadores no momento do go-live, substituindo a abordagem de lançamento gradual (phased rollout) anteriormente prevista em DEF-24.

## Consequences

- O critério de go/no-go torna-se crítico e não-negociável — não existe possibilidade de regressão gradual por segmento de utilizadores após o go-live
- O programa de beta testing (Alpha, Beta fechado, Beta aberto) mantém-se e ganha maior importância como única janela de validação real antes do lançamento geral
- O rollback, caso necessário, é aplicado a todos os utilizadores em simultâneo (via feature flag `enable_web_banking` ou deployment rollback)
- A lógica de feature flags para rollout faseado (percentagens de utilizadores) deixa de se aplicar; as flags mantêm-se exclusivamente para rollback de emergência
- Simplifica o processo de lançamento: elimina a gestão de percentagens de rollout e os critérios de progressão entre fases
- SEC-14 deve ser actualizada para reflectir esta estratégia e remover referências ao phased rollout
- DEF-24 deve ser actualizada para alinhar a secção "Estratégia de Cutover" com esta decisão
