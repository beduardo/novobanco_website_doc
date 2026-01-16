---
id: DEF-03-casos-uso-principais
aliases:
  - Casos de Uso Principais
tags:
  - nextreality-novobanco-website-definitions
  - definitions
  - use-cases
approved: true
created: 2026-01-01
hubs:
  - "[[nextreality]]"
para-code: R
reviewed: true
status: completed
---

# DEF-03: Casos de Uso Principais

> **Secção relacionada:** [3 - Visão Geral da Solução](../sections/SEC-03-visao-geral-solucao.md)

## Contexto

Os casos de uso principais definem as interações mais importantes entre os utilizadores e o sistema HomeBanking web. Estes casos de uso serão a base para a definição da arquitetura e priorização do desenvolvimento.

## Perguntas a Responder

> **Nota:** Requisitos de PWA/Offline estão definidos em [DEF-04-ux-guidelines.md](DEF-04-ux-guidelines.md)
> **Nota:** Detalhes de SCA estão definidos em [DEF-07-autenticacao-autorizacao.md](DEF-07-autenticacao-autorizacao.md)

1. Quais casos de uso são críticos para o negócio?
    Login, Transferências

2. Quais são os atores principais (cliente individual, cliente empresarial, etc.)?
    Cliente individual

3. Existem casos de uso que envolvem integração com terceiros?
    Necessita aprofundamento - verificar integrações KYC/AML, Pagamentos

4. Quais casos de uso requerem autenticação forte (SCA)?
    Todo o acesso à aplicação (áreas restritas)

## Decisões

### Atores do Sistema
- **Decisão:** Cliente Individual como ator principal
- **Justificação:** Foco inicial no segmento de clientes particulares do banco
- **Alternativas consideradas:** Cliente Empresarial (pode ser incluído em fases futuras)

### Casos de Uso Críticos
- **Decisão:** Login e Transferências identificados como críticos para o negócio
- **Justificação:**
  - Login: Ponto de entrada obrigatório, impacta toda a experiência
  - Transferências: Operação financeira core, alto valor de negócio

### Casos de Uso com SCA
- **Decisão:** Todo o acesso à aplicação requer autenticação forte (SCA)
- **Justificação:** Conformidade com PSD2 e política de segurança do banco
- **Nota:** Detalhes de implementação em [DEF-07-autenticacao-autorizacao.md](DEF-07-autenticacao-autorizacao.md)

### PWA e Offline
- **Decisão:** Ver [DEF-04-ux-guidelines.md](DEF-04-ux-guidelines.md)
- **Justificação:** Consolidação em documento de UX

## Restrições Conhecidas

- Alinhamento com casos de uso da app mobile existente
- Conformidade com PSD2 para operações de pagamento

## Referências

- [CONTEXT.md](../CONTEXT.md) - Contexto geral do projeto
- Documentação de casos de uso da app mobile (a fornecer)
- Requisitos PSD2 para SCA (a fornecer)
