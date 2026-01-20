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

> **Secção relacionada:** [4 - Experiência do Utilizador & Arquitetura Frontend](../sections/SEC-04-experiencia-utilizador-frontend.md)

## Contexto

Definir o design system a ser utilizado no HomeBanking Web, garantindo consistência visual e de experiência com a marca do Novo Banco e a app mobile existente.

## Perguntas a Responder

### Design System Existente
1. Existe um design system corporativo do Novo Banco?
    Não. O Design será criado para a aplicação nas primeiras sprints após a criação deste documento.
2. A app mobile tem um design system documentado?
    Não
3. Há um style guide ou brand guidelines a seguir?
    Será criado na execução deste projeto.

### Componentes
4. Será utilizada uma biblioteca de componentes existente (Material UI, Ant Design, etc.) ou será desenvolvida internamente?
    Serão avaliadas bibliotecas existentes e caso se adequem serão usadas. Caso contrário, será desenvolvida.

5. Há componentes específicos do setor bancário a considerar?
    Necessário aprofundamento.

### Tokens de Design
6. Há definição de cores, tipografia e espaçamentos corporativos?
    Serão definidos no início do desenvolvimento do projeto.

7. Será necessário suporte a temas (ex: modo escuro)?
    Sim

### Documentação
8. Como será documentado o design system (Storybook, outro)?
    Figma + Storybook

### Acessibilidade (Consolidado)

> **Nota:** Esta é a definição principal para requisitos de acessibilidade do projeto.

9. Quais níveis de WCAG devem ser atingidos?
    **WCAG 2.1 AA** - Confirmado pelo cliente.

10. Há requisitos específicos de contraste ou tamanho de fonte?
    Necessita aprofundamento. Seguir WCAG 2.1 AA como baseline até esclarecimento.

11. Será utilizada ferramenta automatizada de verificação de acessibilidade?
    Necessita aprofundamento (ex: axe-core, Lighthouse)

12. Será necessária auditoria de acessibilidade externa?
    Necessita aprofundamento.

## Decisões

### Base do Design System
- **Decisão:** Design System criado de raiz para o projeto (primeiras sprints)
- **Justificação:** Não existe design system corporativo nem da app mobile documentado
- **Alternativas consideradas:** Adaptar design system existente (não disponível)

### Biblioteca de Componentes
- **Decisão:** Avaliação de bibliotecas existentes (Material UI, Ant Design, etc.) com fallback para desenvolvimento interno
- **Justificação:** Pragmatismo - usar existente se adequado, desenvolver se necessário
- **Alternativas consideradas:** 100% custom (descartado por tempo), 100% biblioteca (descartado por limitações)

### Componentes Bancários
- **Decisão:** _A definir_ - Necessita aprofundamento
- **Justificação:** Identificar componentes específicos do setor bancário
- **Alternativas consideradas:** N/A

### Tokens de Design
- **Decisão:** Cores, tipografia e espaçamentos definidos no início do desenvolvimento
- **Justificação:** Style guide será criado durante execução do projeto
- **Alternativas consideradas:** N/A

### Suporte a Temas
- **Decisão:** Sim, incluindo modo escuro
- **Justificação:** Requisito de acessibilidade e preferência do utilizador
- **Alternativas consideradas:** Tema único (descartado)

### Documentação
- **Decisão:** Figma (design) + Storybook (componentes)
- **Justificação:** Figma para designers, Storybook para developers, ambos integrados
- **Alternativas consideradas:** Apenas Figma, apenas Storybook

### Acessibilidade
- **Decisão:** WCAG 2.1 AA obrigatório
- **Justificação:** Confirmado pelo cliente. Nível AA é o padrão de indústria para aplicações bancárias.
- **Alternativas consideradas:** WCAG 2.1 AAA (descartado por requisitos excessivos)

## Restrições Conhecidas

- Alinhamento com identidade visual do Novo Banco
- Consistência com experiência da app mobile
- Requisitos de acessibilidade a definir

## Decisões Relacionadas

- [DEC-009-stack-tecnologica-frontend.md](../decisions/DEC-009-stack-tecnologica-frontend.md) - Stack tecnológica frontend

## Referências

- Brand guidelines do Novo Banco (a fornecer)
- Design system da app mobile (a fornecer)
- WCAG 2.1 Guidelines
