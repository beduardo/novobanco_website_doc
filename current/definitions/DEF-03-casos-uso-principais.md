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

> **Secao relacionada:** [3 - Visao Geral da Solucao](../sections/SEC-03-visao-geral-solucao.md)

## Contexto

Os casos de uso principais definem as interacoes mais importantes entre os utilizadores e o sistema HomeBanking web. Estes casos de uso serao a base para a definicao da arquitetura e priorizacao do desenvolvimento.

## Perguntas a Responder

1. Quais sao os casos de uso mais frequentes na app mobile atual?
    Todos os listados nos requisitos funcionais
2. Quais casos de uso sao criticos para o negocio?
    Login, Transferencias
3. Ha casos de uso especificos para o canal web?
    Não
4. Quais sao os atores principais (cliente individual, cliente empresarial, etc.)?
    Cliente individual
5. Existem casos de uso que envolvem integracao com terceiros?
    Falta aprofundamento
6. Quais casos de uso requerem autenticacao forte (SCA)?
    Todo o acesso à aplicação
7. Ha casos de uso offline ou com conectividade intermitente?
    Falta aprofundamento

## Decisoes

### Atores do Sistema
- **Decisao:** Cliente Individual como ator principal
- **Justificacao:** Foco inicial no segmento de clientes particulares do banco
- **Alternativas consideradas:** Cliente Empresarial (pode ser incluido em fases futuras)

### Casos de Uso Prioritarios (MVP)
- **Decisao:** Todos os 35 casos de uso listados nos requisitos funcionais fazem parte do MVP
- **Justificacao:** Paridade funcional com app mobile desde o lancamento
- **Alternativas consideradas:** MVP reduzido (descartado - requisito de paridade)

### Casos de Uso Criticos
- **Decisao:** Login e Transferencias identificados como criticos para o negocio
- **Justificacao:**
  - Login: Ponto de entrada obrigatorio, impacta toda a experiencia
  - Transferencias: Operacao financeira core, alto valor de negocio
- **Alternativas consideradas:** N/A

### Casos de Uso Especificos Web
- **Decisao:** Nenhum caso de uso exclusivo para o canal web
- **Justificacao:** Objetivo de paridade funcional com a app mobile
- **Alternativas consideradas:** Funcionalidades adicionais web (descartado)

### Casos de Uso com SCA
- **Decisao:** Todo o acesso a aplicacao requer autenticacao forte (SCA)
- **Justificacao:** Conformidade com PSD2 e politica de seguranca do banco
- **Alternativas consideradas:** SCA apenas para operacoes financeiras (descartado por requisitos de seguranca)

### Casos de Uso com Terceiros
- **Decisao:** _A definir_ - Necessita aprofundamento
- **Justificacao:** Identificar quais casos de uso dependem de integracoes com terceiros
- **Alternativas consideradas:** Reutilizar integracoes existentes da app mobile (baseline)

### Casos de Uso Offline
- **Decisao:** _A definir_ - Necessita aprofundamento
- **Justificacao:** Avaliar se ha requisitos de funcionamento com conectividade intermitente
- **Alternativas consideradas:** Service Workers para cache (a avaliar)

## Restricoes Conhecidas

- Alinhamento com casos de uso da app mobile existente
- Conformidade com PSD2 para operacoes de pagamento

## Referencias

- [CONTEXT.md](../CONTEXT.md) - Contexto geral do projeto
- Documentacao de casos de uso da app mobile (a fornecer)
- Requisitos PSD2 para SCA (a fornecer)
