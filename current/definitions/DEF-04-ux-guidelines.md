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

> **Secção relacionada:** [4 - Experiência do Utilizador & Arquitetura Frontend](../sections/SEC-04-experiencia-utilizador-frontend.md)

## Contexto

Definir as diretrizes de experiência do utilizador para o HomeBanking Web, garantindo uma experiência consistente, intuitiva e alinhada com as melhores práticas do setor bancário.

## Perguntas a Responder

### Jornadas do Utilizador
1. Quais são as jornadas de utilizador prioritárias?
    Jornadas ainda a validar, mas serão baseadas nos requisitos funcionais.

2. Existem fluxos documentados da app mobile que devem ser replicados?
    Sim. Os fluxos da app mobile devem ser replicados na web

3. Há pontos de dor conhecidos na app mobile a evitar?
    Necessita aprofundamento

### Navegação
4. Qual será a estrutura de navegação (sidebar, top nav, bottom nav)?
    SideBar.

5. Há requisitos de breadcrumbs ou navegação contextual?
    Sim. O utilizador precisa se localizar rapidamente e haverá momentos que a navegação dependerá da origem.

### Feedback ao Utilizador
6. Quais padrões de feedback serão utilizados (toasts, modais, inline)?
    Toasts para avisos não bloqueantes e modais para avisos que necessitem de uma resposta do utilizador.

7. Há requisitos específicos para mensagens de erro?
    Não

### Performance Percebida
8. Há requisitos de skeleton screens ou loading states?
    Sim. O utilizador deve sentir que a aplicação está responsiva 100% do tempo.

9. Qual é a estratégia de pre-fetching de dados?
    Pre-fetch com Vite + dados com TanStack

### PWA e Offline (Consolidado)

> **Nota:** Esta é a definição principal para requisitos de PWA/Offline do projeto.

10. Há requisitos de funcionamento offline?
    **Não.** O cliente confirmou que não há requisitos de funcionamento offline.

11. Será implementado como PWA instalável?
    **Não.** A aplicação não será uma PWA instalável.

12. Quais funcionalidades devem estar disponíveis offline (se aplicável)?
    **N/A.** Sem requisitos de offline.

13. Qual o comportamento esperado em conectividade intermitente?
    Necessita aprofundamento. Apresentar opções ao cliente (retry automático, mensagem de erro, etc.)

### Segurança UX

14. Como será comunicada a segurança ao utilizador?
    Necessita aprofundamento (indicadores visuais, certificado, etc.)

15. Há requisitos de timeout de sessão com aviso prévio?
    Sim. Popup na aplicação com temporizador antes de expirar.
    Timeout por inatividade: 10 minutos (ver DEF-07)

## Decisões

### Jornadas Prioritárias
- **Decisão:** Jornadas baseadas nos requisitos funcionais, a validar em detalhe
- **Justificação:** Paridade com fluxos da app mobile
- **Alternativas consideradas:** N/A

### Replicação de Fluxos Mobile
- **Decisão:** Fluxos da app mobile devem ser replicados na web
- **Justificação:** Consistência de experiência entre canais
- **Alternativas consideradas:** Fluxos otimizados para web (descartado por requisito de paridade)

### Pontos de Dor Mobile
- **Decisão:** _A definir_ - Necessita aprofundamento
- **Justificação:** Identificar e evitar problemas conhecidos da app mobile
- **Alternativas consideradas:** N/A

### Estrutura de Navegação
- **Decisão:** SideBar com breadcrumbs e navegação contextual
- **Justificação:** Utilizador precisa se localizar rapidamente; navegação pode depender da origem
- **Alternativas consideradas:** Top nav, Bottom nav (descartados)

### Padrões de Feedback
- **Decisão:**
  - Toasts: Avisos não bloqueantes
  - Modais: Avisos que requerem resposta do utilizador
- **Justificação:** Separação clara entre informação e ação requerida
- **Alternativas consideradas:** Inline feedback, Notificações push

### Loading States
- **Decisão:** Skeleton screens obrigatórios para perceção de responsividade 100%
- **Justificação:** Experiência de utilizador fluida, redução de perceção de lentidão
- **Alternativas consideradas:** Spinners simples (descartado por UX inferior)

### Pre-fetching
- **Decisão:** Pre-fetch com Vite + cache de dados com TanStack Query
- **Justificação:** Carregamento antecipado de dados para navegação fluida
- **Alternativas consideradas:** Fetch on demand apenas

### PWA/Offline
- **Decisão:** Não será PWA instalável e não haverá funcionamento offline
- **Justificação:** Cliente confirmou que não há requisitos de PWA nem offline. Aplicação web tradicional.
- **Alternativas consideradas:** PWA instalável, Service Workers para cache (descartados por requisito do cliente)

### Segurança UX
- **Decisão:** _A definir_ - Necessita aprofundamento
- **Justificação:** Definir comunicação de segurança e timeout de sessão
- **Alternativas consideradas:** N/A

## Restrições Conhecidas

- Paridade funcional com app mobile
- SCA obrigatório para todo o acesso
- Design responsivo
- Suporte multi-idioma (PT, EN, ES)

## Decisões Relacionadas

- [DEC-009-stack-tecnologica-frontend.md](../decisions/DEC-009-stack-tecnologica-frontend.md) - Stack tecnológica frontend

## Referências

- Fluxos da app mobile (a fornecer)
- Best practices UX bancário
- Nielsen Norman Group guidelines
