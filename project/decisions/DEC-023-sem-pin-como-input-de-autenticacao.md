---
id: "DEC-023"
title: "Sem PIN como Input de Autenticação"
status: "accepted"
created: 2026-04-17
context: "DEF-13"
affects-definitions: ["DEF-13"]
affects-sections: ["SEC-07", "SEC-08"]
---

# DEC-023: Sem PIN como Input de Autenticação

## Context

Durante a revisão da documentação de autenticação (DEF-13), identificaram-se múltiplas referências a PIN como método de input de autenticação, tanto na app mobile como no canal web. Esta assunção foi transportada de análises anteriores, mas não reflete o comportamento real das plataformas.

## Decision

Nem a app mobile nem o website do Novo Banco utilizam PIN como input de autenticação. O único input de conhecimento suportado é a **password**. A confirmação de segundo fator na app é feita exclusivamente por **biometria** (fingerprint ou face ID), não por PIN.

Toda a documentação deve ser atualizada para remover referências a PIN como método de autenticação em qualquer canal.

## Consequences

- As tabelas de fatores SCA (PSD2) devem listar apenas Password (conhecimento) e Biometria (inerência), sem PIN.
- Os diagramas de fluxo da app devem referenciar apenas biometria, não "biometria/PIN".
- As pendências de segurança relativas a "cifra de PIN" e "teclado virtual para PIN" são removidas por não aplicáveis.
- A row "PIN/Password" na tabela de transmissão de credenciais passa a ser apenas "Password".
- "Certificate pinning" (pinning de certificados TLS) não é afetado por esta decisão — é um conceito distinto.
