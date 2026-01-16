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

> **Secção relacionada:** [5 - Arquitetura Backend & Serviços](../sections/SEC-05-arquitetura-backend-servicos.md)

## Contexto

Definir os padrões de design de API para o HomeBanking Web, incluindo estilo de API, versionamento, documentação e padrões de request/response.

## Perguntas a Responder

### Estilo de API
1. As APIs serão REST, GraphQL ou híbrido?
    REST

2. Há padrões de API existentes no banco a seguir?
    Sim. Já existem contratos a serem seguidos pelas APIs

### Versionamento
3. Qual estratégia de versionamento (URL path, header, query param)?
    Versionamento via URL path (ex: /api/v1/resource)

4. Qual será a política de deprecação de versões?
    Necessita aprofundamento. Sugestão: 6 meses de suporte após nova versão

5. Qual a estratégia para breaking changes nos contratos API?
    Necessita aprofundamento. Considerar: feature flags, versões paralelas

### Documentação
6. Qual formato de especificação (OpenAPI 3.0, AsyncAPI)?
    OpenAPI 3.0

7. Como será gerada e mantida a documentação?
    Ferramenta automatizada via Pipeline (Swagger/NSwag)

### Padrões de Request/Response
8. Qual formato de dados (JSON, outro)?
    JSON

9. Há padrões de paginação a seguir?
    Sim. Os componentes de lista dependem de um padrão definido

10. Qual padrão de tratamento de erros?
    Necessita aprofundamento. Considerar: RFC 7807 (Problem Details)

### Segurança
11. Qual mecanismo de autenticação (OAuth 2.0, JWT)?
    OAuth 2.0 com serviço de autenticação existente do banco

12. Há requisitos de assinatura de requests?
    Não

### Performance
13. Quais headers de cache serão utilizados?
    Necessita aprofundamento. Considerar: Cache-Control, ETag

14. Há requisitos de compressão (gzip, brotli)?
    gzip

## Decisões

### Estilo de API
- **Decisão:** REST
- **Justificação:** Alinhamento com APIs existentes e contratos já definidos do banco
- **Alternativas consideradas:** GraphQL (descartado por compatibilidade)

### Padrões Existentes
- **Decisão:** Seguir contratos de API existentes no banco
- **Justificação:** Consistência com APIs da app mobile
- **Alternativas consideradas:** Novos contratos (descartado por reutilização)

### Versionamento
- **Decisão:** Versionamento via URL path (ex: /api/v1/resource)
- **Justificação:** Simplicidade, visibilidade, prática comum
- **Alternativas consideradas:** Header versioning, Query param

### Política de Deprecação
- **Decisão:** _A definir_ - Necessita aprofundamento
- **Justificação:** Definir tempo de suporte a versões antigas
- **Alternativas consideradas:** N/A

### Especificação e Documentação
- **Decisão:** OpenAPI 3.0 com geração automatizada via Pipeline
- **Justificação:** Standard de indústria, integração com ferramentas
- **Alternativas consideradas:** AsyncAPI (para eventos), Swagger 2.0

### Formato de Dados
- **Decisão:** JSON
- **Justificação:** Standard para APIs REST, boa integração com frontend
- **Alternativas consideradas:** XML (descartado por verbosidade)

### Paginação
- **Decisão:** Padrão definido para componentes de lista
- **Justificação:** Consistência entre endpoints, suporte a UI components
- **Alternativas consideradas:** Cursor-based, Offset-based (a definir em detalhe)

### Tratamento de Erros
- **Decisão:** _A definir_ - Necessita aprofundamento
- **Justificação:** Definir estrutura de erro padrão (RFC 7807 Problem Details?)
- **Alternativas consideradas:** RFC 7807, Custom error format

### Autenticação API
- **Decisão:** OAuth 2.0 com implementação mista com serviço de autenticação existente do banco
- **Justificação:** Reutilização de infraestrutura de autenticação existente
- **Alternativas consideradas:** JWT puro, SAML (descartados)

### Assinatura de Requests
- **Decisão:** Não requerida
- **Justificação:** Autenticação OAuth suficiente para requisitos atuais
- **Alternativas consideradas:** HMAC signing (pode ser adicionado se necessário)

### Cache Headers
- **Decisão:** _A definir_ - Necessita aprofundamento
- **Justificação:** Definir política de cache HTTP
- **Alternativas consideradas:** Cache-Control, ETag, Last-Modified

### Compressão
- **Decisão:** gzip
- **Justificação:** Suporte universal, boa taxa de compressão
- **Alternativas consideradas:** Brotli (pode ser adicionado)

## Restrições Conhecidas

- Integração com APIs existentes da app mobile
- Conformidade PSD2 para operações financeiras
- Requisitos de auditoria

## Decisões Relacionadas

- [DEC-007-padrao-bff.md](../decisions/DEC-007-padrao-bff.md) - Padrão BFF
- [DEC-010-stack-tecnologica-backend.md](../decisions/DEC-010-stack-tecnologica-backend.md) - Stack tecnológica backend

## Referências

- APIs existentes da app mobile (a fornecer)
- OpenAPI Specification 3.0
- REST API Guidelines (Microsoft, Google)
