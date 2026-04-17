---
id: "DEC-021"
title: "Stack Tecnológica Frontend é Indicativa e Será Validada no Arranque do Projeto"
status: "accepted"
created: 2026-04-17
context: "DEF-08"
affects-definitions:
  - "DEF-08"
affects-sections:
  - "SEC-04"
---

# DEC-021: Stack Tecnológica Frontend é Indicativa e Será Validada no Arranque do Projeto

## Context

A stack tecnológica frontend apresentada na secção 4.6.1 e formalizada em DEC-009 foi definida
durante a fase de proposta/pré-venda com base no conhecimento disponível à data e nas preferências
da equipa Havas. Esta stack representa uma recomendação técnica fundamentada, mas foi elaborada
antes do arranque formal do projeto e sem validação com a equipa técnica do Novo Banco.

O processo de validação no arranque do projeto incluirá sessões técnicas com a equipa NB para
alinhar constrangimentos de infraestrutura, experiência da equipa, políticas de segurança e
restrições contratuais que possam influenciar as escolhas tecnológicas.

## Decision

A stack tecnológica sugerida na secção 4.6.1 (React 18+, TypeScript, Vite, Zustand, TanStack
Query, Tailwind CSS, i18next, Vitest, Playwright) é **meramente indicativa**. As escolhas
definitivas serão validadas e confirmadas no arranque do projeto, em conjunto com a equipa
técnica do Novo Banco.

A DEC-009 mantém-se como referência da stack recomendada, mas as suas escolhas específicas
estão sujeitas a revisão durante a fase de arranque.

## Consequences

- A secção 4.6.1 deve ser lida como uma proposta indicativa, não como uma decisão final e
  irrevogável.
- No arranque do projeto deverá realizar-se uma sessão de validação técnica com a equipa NB
  para confirmar ou ajustar cada componente da stack.
- Se alguma tecnologia for substituída após validação, DEC-009 e SEC-04 deverão ser atualizados
  para refletir as escolhas definitivas.
- Não devem ser adquiridas licenças, configuradas pipelines ou iniciado desenvolvimento com base
  nesta stack antes da sua validação formal.
