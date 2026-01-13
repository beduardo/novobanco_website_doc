---
id: DEF-04-design-system
aliases:
  - Design System
tags:
  - nextreality-novobanco-website-definitions
  - definitions
  - design-system
  - ui
approved: true
created: 2026-01-03
hubs:
  - "[[nextreality]]"
para-code: R
reviewed: true
status: completed
---

# DEF-04: Design System

> **Secao relacionada:** [4 - Experiencia do Utilizador & Arquitetura Frontend](../sections/SEC-04-experiencia-utilizador-frontend.md)

## Contexto

Definir o design system a ser utilizado no HomeBanking Web, garantindo consistencia visual e de experiencia com a marca do Novo Banco e a app mobile existente.

## Perguntas a Responder

### Design System Existente
1. Existe um design system corporativo do Novo Banco?
    Não. O Design será criado para a aplicação nas primeiras sprints após a criação deste documento.
2. A app mobile tem um design system documentado?
    Não
3. Ha um style guide ou brand guidelines a seguir?
    Será criado na execução deste projeto.

### Componentes
4. Sera utilizada uma biblioteca de componentes existente (Material UI, Ant Design, etc.) ou sera desenvolvida internamente?
    Serão avaliadas bibliotecas existentes e caso se adequem serão usadas. Caso contrário, será desenvolvida.

5. Ha componentes especificos do sector bancario a considerar?
    Necessário aprofundamento.

### Tokens de Design
6. Ha definicao de cores, tipografia e espacamentos corporativos?
    Serão definidos no início do desenvolvimento do projeto.

7. Sera necessario suporte a temas (ex: modo escuro)?
    Sim

### Documentacao
8. Como sera documentado o design system (Storybook, outro)?
    Figma + Storykbook

### Acessibilidade (Consolidado)

> **Nota:** Esta e a definicao principal para requisitos de acessibilidade do projeto.

9. Quais niveis de WCAG devem ser atingidos?
    Necessita aprofundamento. Referencia de industria: WCAG 2.1 AA

10. Ha requisitos especificos de contraste ou tamanho de fonte?
    Ainda nao definidos - seguir WCAG 2.1 AA como baseline

11. Sera utilizada ferramenta automatizada de verificacao de acessibilidade?
    Necessita aprofundamento (ex: axe-core, Lighthouse)

## Decisoes

### Base do Design System
- **Decisao:** Design System criado de raiz para o projeto (primeiras sprints)
- **Justificacao:** Nao existe design system corporativo nem da app mobile documentado
- **Alternativas consideradas:** Adaptar design system existente (nao disponivel)

### Biblioteca de Componentes
- **Decisao:** Avaliacao de bibliotecas existentes (Material UI, Ant Design, etc.) com fallback para desenvolvimento interno
- **Justificacao:** Pragmatismo - usar existente se adequado, desenvolver se necessario
- **Alternativas consideradas:** 100% custom (descartado por tempo), 100% biblioteca (descartado por limitacoes)

### Componentes Bancarios
- **Decisao:** _A definir_ - Necessita aprofundamento
- **Justificacao:** Identificar componentes especificos do sector bancario
- **Alternativas consideradas:** N/A

### Tokens de Design
- **Decisao:** Cores, tipografia e espacamentos definidos no inicio do desenvolvimento
- **Justificacao:** Style guide sera criado durante execucao do projeto
- **Alternativas consideradas:** N/A

### Suporte a Temas
- **Decisao:** Sim, incluindo modo escuro
- **Justificacao:** Requisito de acessibilidade e preferencia do utilizador
- **Alternativas consideradas:** Tema unico (descartado)

### Documentacao
- **Decisao:** Figma (design) + Storybook (componentes)
- **Justificacao:** Figma para designers, Storybook para developers, ambos integrados
- **Alternativas consideradas:** Apenas Figma, apenas Storybook

### Acessibilidade
- **Decisao:** _A definir_ - Nivel WCAG a determinar
- **Justificacao:** Necessita aprofundamento com stakeholders
- **Alternativas consideradas:** WCAG 2.1 AA (referencia de industria)

## Restricoes Conhecidas

- Alinhamento com identidade visual do Novo Banco
- Consistencia com experiencia da app mobile
- Requisitos de acessibilidade a definir

## Decisoes Relacionadas

- [DEC-009-stack-tecnologica-frontend.md](../decisions/DEC-009-stack-tecnologica-frontend.md) - Stack tecnologica frontend

## Referencias

- Brand guidelines do Novo Banco (a fornecer)
- Design system da app mobile (a fornecer)
- WCAG 2.1 Guidelines
