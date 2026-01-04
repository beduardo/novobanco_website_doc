---
id: DEF-05-api-design
aliases:
  - API Design
tags:
  - nextreality-novobanco-website-definitions
  - definitions
  - api
  - rest
approved: true
created: 2026-01-03
hubs:
  - "[[nextreality]]"
para-code: R
reviewed: true
status: completed
---

# DEF-05: API Design

> **Secao relacionada:** [5 - Arquitetura Backend & Servicos](../sections/SEC-05-arquitetura-backend-servicos.md)

## Contexto

Definir os padroes de design de API para o HomeBanking Web, incluindo estilo de API, versionamento, documentacao e padroes de request/response.

## Perguntas a Responder

### Estilo de API
1. As APIs serao REST, GraphQL ou hibrido?
    REST

2. Ha padroes de API existentes no banco a seguir?
    Sim. Já existem contratos a serem seguidos pelas APIs

### Versionamento
3. Qual estrategia de versionamento (URL path, header, query param)?
    Versionamento via url

4. Qual sera a politica de deprecacao de versoes?
    Necessita aprofundamento

### Documentacao
5. Qual formato de especificacao (OpenAPI 3.0, AsyncAPI)?
    OpenApi 3
    
6. Como sera gerada e mantida a documentacao?
    Será utilizada ferramenta automatizada via Pipeline

### Padroes de Request/Response
7. Qual formato de dados (JSON, outro)?
    JSON

8. Ha padroes de paginacao a seguir?
    Sim. Os componentes de lista dependem de um padrão

9. Qual padrao de tratamento de erros?
    Necessita aprofundamento

### Seguranca
10. Qual mecanismo de autenticacao (OAuth 2.0, JWT)?
    Baseado em OAuth 2.0 com implementação mista com com serviço de autenticação existem do banco.

11. Ha requisitos de assinatura de requests?
    Não.

### Performance
12. Quais headers de cache serao utilizados?
    Necessita aprofundamento

13. Ha requisitos de compressao (gzip, brotli)?
    gzip

## Decisoes

### Estilo de API
- **Decisao:** REST
- **Justificacao:** Alinhamento com APIs existentes e contratos ja definidos do banco
- **Alternativas consideradas:** GraphQL (descartado por compatibilidade)

### Padroes Existentes
- **Decisao:** Seguir contratos de API existentes no banco
- **Justificacao:** Consistencia com APIs da app mobile
- **Alternativas consideradas:** Novos contratos (descartado por reutilizacao)

### Versionamento
- **Decisao:** Versionamento via URL path (ex: /api/v1/resource)
- **Justificacao:** Simplicidade, visibilidade, pratica comum
- **Alternativas consideradas:** Header versioning, Query param

### Politica de Deprecacao
- **Decisao:** _A definir_ - Necessita aprofundamento
- **Justificacao:** Definir tempo de suporte a versoes antigas
- **Alternativas consideradas:** N/A

### Especificacao e Documentacao
- **Decisao:** OpenAPI 3.0 com geracao automatizada via Pipeline
- **Justificacao:** Standard de industria, integracao com ferramentas
- **Alternativas consideradas:** AsyncAPI (para eventos), Swagger 2.0

### Formato de Dados
- **Decisao:** JSON
- **Justificacao:** Standard para APIs REST, boa integracao com frontend
- **Alternativas consideradas:** XML (descartado por verbosidade)

### Paginacao
- **Decisao:** Padrao definido para componentes de lista
- **Justificacao:** Consistencia entre endpoints, suporte a UI components
- **Alternativas consideradas:** Cursor-based, Offset-based (a definir em detalhe)

### Tratamento de Erros
- **Decisao:** _A definir_ - Necessita aprofundamento
- **Justificacao:** Definir estrutura de erro padrao (RFC 7807 Problem Details?)
- **Alternativas consideradas:** RFC 7807, Custom error format

### Autenticacao API
- **Decisao:** OAuth 2.0 com implementacao mista com servico de autenticacao existente do banco
- **Justificacao:** Reutilizacao de infraestrutura de autenticacao existente
- **Alternativas consideradas:** JWT puro, SAML (descartados)

### Assinatura de Requests
- **Decisao:** Nao requerida
- **Justificacao:** Autenticacao OAuth suficiente para requisitos atuais
- **Alternativas consideradas:** HMAC signing (pode ser adicionado se necessario)

### Cache Headers
- **Decisao:** _A definir_ - Necessita aprofundamento
- **Justificacao:** Definir politica de cache HTTP
- **Alternativas consideradas:** Cache-Control, ETag, Last-Modified

### Compressao
- **Decisao:** gzip
- **Justificacao:** Suporte universal, boa taxa de compressao
- **Alternativas consideradas:** Brotli (pode ser adicionado)

## Restricoes Conhecidas

- Integracao com APIs existentes da app mobile
- Conformidade PSD2 para operacoes financeiras
- Requisitos de auditoria

## Referencias

- APIs existentes da app mobile (a fornecer)
- OpenAPI Specification 3.0
- REST API Guidelines (Microsoft, Google)
