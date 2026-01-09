---
id: DEF-04-ux-guidelines
aliases:
  - UX Guidelines
tags:
  - nextreality-novobanco-website-definitions
  - definitions
  - ux
  - user-experience
approved: true
created: 2026-01-03
hubs:
  - "[[nextreality]]"
para-code: R
reviewed: true
status: completed
---

# DEF-04: UX Guidelines

> **Secao relacionada:** [4 - Experiencia do Utilizador & Arquitetura Frontend](../sections/SEC-04-experiencia-utilizador-frontend.md)

## Contexto

Definir as diretrizes de experiencia do utilizador para o HomeBanking Web, garantindo uma experiencia consistente, intuitiva e alinhada com as melhores praticas do sector bancario.

## Perguntas a Responder

### Jornadas do Utilizador
1. Quais sao as jornadas de utilizador prioritarias?
    Jornadas ainda a validar, mas serão baseadas nos requisitos funcionais.

2. Existem fluxos documentados da app mobile que devem ser replicados?
    Sim. Os fluxos da app mobible devem ser replicados na web

3. Ha pontos de dor conhecidos na app mobile a evitar?
    Necessita aprofundamento

### Navegacao
4. Qual sera a estrutura de navegacao (sidebar, top nav, bottom nav)?
    SideBar.

5. Ha requisitos de breadcrumbs ou navegacao contextual?
    Sim. O utilizador precisa se localizar rapidamente e haverá momentos que a navegação dependerá da origem.

### Feedback ao Utilizador
6. Quais padroes de feedback serao utilizados (toasts, modais, inline)?
    Toasts para avisos não bloqueantes e modais para avisos que necessitem de uma resposta do utilizador.

7. Ha requisitos especificos para mensagens de erro?
    Não

### Performance Percebida
8. Ha requisitos de skeleton screens ou loading states?
    Sim. O utilizador deve sentir que a aplicação está responsiva 100% do tempo.

9. Qual e a estrategia de pre-fetching de dados?
    Pre-fetch com Vite + dados com TanStack

### PWA e Offline
10. Ha requisitos de funcionamento offline?
    Necessita de aprofundamento

11. Sera implementado como PWA instalavel?
    Necessita de aprofundamento

### Seguranca UX
12. Como sera comunicada a seguranca ao utilizador?
    Necessita aprofundamento

13. Ha requisitos de timeout de sessao com aviso previo?
    Necessita aprofundamento

## Decisoes

### Jornadas Prioritarias
- **Decisao:** Jornadas baseadas nos requisitos funcionais, a validar em detalhe
- **Justificacao:** Paridade com fluxos da app mobile
- **Alternativas consideradas:** N/A

### Replicacao de Fluxos Mobile
- **Decisao:** Fluxos da app mobile devem ser replicados na web
- **Justificacao:** Consistencia de experiencia entre canais
- **Alternativas consideradas:** Fluxos otimizados para web (descartado por requisito de paridade)

### Pontos de Dor Mobile
- **Decisao:** _A definir_ - Necessita aprofundamento
- **Justificacao:** Identificar e evitar problemas conhecidos da app mobile
- **Alternativas consideradas:** N/A

### Estrutura de Navegacao
- **Decisao:** SideBar com breadcrumbs e navegacao contextual
- **Justificacao:** Utilizador precisa se localizar rapidamente; navegacao pode depender da origem
- **Alternativas consideradas:** Top nav, Bottom nav (descartados)

### Padroes de Feedback
- **Decisao:**
  - Toasts: Avisos nao bloqueantes
  - Modais: Avisos que requerem resposta do utilizador
- **Justificacao:** Separacao clara entre informacao e acao requerida
- **Alternativas consideradas:** Inline feedback, Notificacoes push

### Loading States
- **Decisao:** Skeleton screens obrigatorios para percepcao de responsividade 100%
- **Justificacao:** Experiencia de utilizador fluida, reducao de percepcao de lentidao
- **Alternativas consideradas:** Spinners simples (descartado por UX inferior)

### Pre-fetching
- **Decisao:** Pre-fetch com Vite + cache de dados com TanStack Query
- **Justificacao:** Carregamento antecipado de dados para navegacao fluida
- **Alternativas consideradas:** Fetch on demand apenas

### PWA/Offline
- **Decisao:** _A definir_ - Necessita aprofundamento
- **Justificacao:** Avaliar requisitos de instalacao e funcionamento offline
- **Alternativas consideradas:** PWA instalavel, Service Workers para cache

### Seguranca UX
- **Decisao:** _A definir_ - Necessita aprofundamento
- **Justificacao:** Definir comunicacao de seguranca e timeout de sessao
- **Alternativas consideradas:** N/A

## Restricoes Conhecidas

- Paridade funcional com app mobile
- SCA obrigatorio para todo o acesso
- Design responsivo
- Suporte multi-idioma (PT, EN, ES)

## Decisoes Relacionadas

- [DEC-009-stack-tecnologica-frontend.md](../decisions/DEC-009-stack-tecnologica-frontend.md) - Stack tecnologica frontend

## Referencias

- Fluxos da app mobile (a fornecer)
- Best practices UX bancario
- Nielsen Norman Group guidelines
