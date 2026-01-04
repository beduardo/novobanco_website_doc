---
id: SEC-09-integracao-interfaces-externas
aliases:
  - Novo Banco Integracao Interfaces Externas
tags:
  - nextreality-novobanco-website-sections
approved: true
created: 2025-12-22
hubs:
  - "[[nextreality]]"
para-code: R
reviewed: true
---
# 09. Integracao & Interfaces Externas

> **Status:** em-progresso
> **Definicoes necessarias:** DEF-09-regras-transferencias.md, DEF-09-fluxo-transferencia.md

## Proposito

Documentar as integracoes com sistemas externos, incluindo Core Banking, terceiros (KYC, notificacoes, cartoes), Open Banking PSD2 e estrategias de tratamento de erros.

---

## Conteudo

### Integracao Core Banking
_Aguardando informacoes das definicoes_

### Terceiros - KYC/AML
_Aguardando informacoes das definicoes_

### Terceiros - Notificacoes
_Aguardando informacoes das definicoes_

### Terceiros - Cartoes
_Aguardando informacoes das definicoes_

### Open Banking PSD2
_Aguardando informacoes das definicoes_

### Gestao de Consentimentos
_Aguardando informacoes das definicoes_

### Message Broker
_Aguardando informacoes das definicoes_

### Tratamento de Erros
_Aguardando informacoes das definicoes_

### SLAs de Integracao
_Aguardando informacoes das definicoes_

### Catalogo de Integracoes
_Aguardando informacoes das definicoes_

### API Management
_Aguardando informacoes das definicoes_

---

## Entregaveis

- [ ] Diagrama de integracao (integration landscape)
- [ ] Matriz de integracoes (sistema, protocolo, formato, SLA, criticidade)
- [ ] Especificacao de cada interface externa
- [ ] Diagramas de sequencia para integracoes criticas
- [ ] Contratos de integracao (WSDLs, schemas, OpenAPI)
- [ ] Documentacao de APIs PSD2 (endpoints, scopes, autenticacao)
- [ ] Fluxos de consentimento PSD2 (diagramas)
- [ ] Developer portal documentation (para TPPs)
- [ ] Message schemas (XML/JSON/Avro)
- [ ] Configuracao de message broker (queues, topics, DLQ)
- [ ] Estrategia de retry e circuit breaker por integracao
- [ ] Fallback procedures para indisponibilidade
- [ ] SLA agreements com fornecedores externos
- [ ] Error handling specification
- [ ] Integration testing strategy

---

## Definicoes Utilizadas

- [ ] [DEF-09-regras-transferencias.md](../definitions/DEF-09-regras-transferencias.md) - Status: em-progresso
- [ ] [DEF-09-fluxo-transferencia.md](../definitions/DEF-09-fluxo-transferencia.md) - Status: em-progresso

---

## Navegacao

| Anterior | Proximo |
|----------|---------|
| [08. Seguranca & Conformidade](SEC-08-seguranca-conformidade.md) | [10. Arquitetura Operacional](SEC-10-arquitetura-operacional.md) |
