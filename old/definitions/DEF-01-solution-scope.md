---
id: DEF-01-solution-scope
aliases:
  - Novo Banco Solution Scope
tags:
  - nextreality-novobanco-website-definitions
approved: true
created: 2025-12-22
hubs:
  - "[[nextreality]]"
para-code: R
reviewed: true
---
# DEF-01: Escopo da Solucao

> **Status:** estrutura
> **Secao relacionada:** 01 - Sumario Executivo

## Contexto

Este documento define o escopo da solucao, identificando quais sistemas e funcionalidades estao incluidos ou excluidos do projeto de Homebanking web.

## Questoes a Responder

1. Quais funcionalidades do App Mobile devem estar presentes no MVP?
2. Quais funcionalidades ficam para fases posteriores (Fase 1, Fase 2)?
3. Existem funcionalidades do App que NAO serao replicadas no web? Quais e porque?
R.: MBWay, pois depende de SMS e Push do Telemóvel para funcionar
4. O Backoffice de Gestao faz parte deste escopo ou e um projeto separado?
R.: O Backoffice de Gestão já existe e já está desenvolvido.
5. Quais integracoes com sistemas externos sao obrigatorias no MVP?
6. Qual o papel do Siebel na nova arquitetura?
R.: É o backend onde está toda a informação de negócio/cliente. Tem também regras de negócio e validações.
7. Qual a relacao com o Core Banking (BI Core Banking)?
8. Quais "Sistemas Externos" (Financeiros, Seguradoras, Parceiros) sao prioritarios?

## Decisoes

### Funcionalidades MVP
- **Decisao:** _Pendente_
- **Lista de funcionalidades:** _Pendente_

### Funcionalidades Fase 1
- **Decisao:** _Pendente_
- **Lista de funcionalidades:** _Pendente_

### Funcionalidades Fase 2+
- **Decisao:** _Pendente_
- **Lista de funcionalidades:** _Pendente_

### Funcionalidades Excluidas
- **Decisao:** _Pendente_
- **Justificativa:** _Pendente_

### Integracao com Siebel
- **Decisao:** Integrar - Siebel é o backend principal
- **Papel:** Backend centralizado com toda a informação de negócio e dados do cliente
- **Responsabilidades:** Regras de negócio e validações
- **Justificativa:** O Siebel permanece como fonte de verdade para dados e lógica de negócio; o novo Website consome via APIs

### Backoffice de Gestao
- **Decisao:** Projeto separado (já existente e desenvolvido)
- **Interacao:** Entrega conteúdos e regras por API ao Website e APP
- **Justificativa:** Sistema independente que fornece dados de configuração e regras de negócio via APIs

## Restricoes Conhecidas

- Upgrade do Siebel e o trigger para este projeto
- Deve ser o mais semelhante possivel a APP movel
- Stack definida: React (Frontend) + C# (Backend BFF)

## Referencias

- [architectural_document_structure_novo_banco.md](../architectural_document_structure_novo_banco.md) - Contexto inicial
- Diagrama de contexto inicial adicionado em SEC-01
