---
id: DEF-06-arquitetura-dados
aliases:
  - Arquitetura de Dados
tags:
  - nextreality-novobanco-website-definitions
  - definitions
  - data
  - storage
  - gdpr
approved: true
created: 2026-01-03
hubs:
  - "[[nextreality]]"
para-code: R
reviewed: true
status: completed
---

# DEF-06: Arquitetura de Dados

> **Secao relacionada:** [6 - Arquitetura de Dados](../sections/SEC-06-arquitetura-dados.md)

## Contexto

Definir a arquitetura de dados do HomeBanking Web, incluindo modelo de dados, armazenamento, encriptacao, retencao e conformidade RGPD. Nota: O canal web reutiliza os servicos backend existentes, logo a maioria dos dados e armazenada nos sistemas existentes.

## Perguntas a Responder

### Modelo de Dados
1. O frontend web tera persistencia local de dados (IndexedDB, localStorage)?
    Sim, localStorage.

2. Quais dados podem ser armazenados temporariamente no browser?
    No momento somente os dados básicos do utilizador. Necessário mais aprofundamento com UI para avaliar se há necessidade de algo a mais. Vamos utilizar uma estratégia de cache para dados públicos, notícias e também para informações muito utilizadas na construção das páginas. As informações sigilosas do usuário ficarão em cache no BFF.

3. Ha dados especificos do canal web que nao existem na app mobile?
    Não

### Armazenamento no BFF
4. O BFF tera base de dados propria ou apenas cache?
    Apenas cache

5. Se houver base de dados, qual tecnologia (SQL Server, PostgreSQL, Redis)?
    Não há

6. Quais dados serao armazenados no BFF (alem de sessoes)?
    No momento somente a sessão. Caso o Frontend utilize SSR e SGA por completo, as informações mais utilizadas estarão disponíveis em cache no BFF.

### Encriptacao
7. Quais dados devem ser encriptados em transito (TLS versao)?
    Ainda não definidos

8. Ha requisitos de encriptacao em repouso para dados no BFF/cache?
    Não há requisitos

9. Como serao geridas as chaves de encriptacao?
    No momento somente SSL está em consideração.

### Retencao de Dados
10. Qual a politica de retencao para logs de acesso web?
    Necessita aprofundamento

11. Qual a politica de retencao para dados de sessao?
    Necessita aprofundamento

12. Ha requisitos especificos de retencao para auditoria?
    Necessita aprofundamento

### Backup & Restore
13. Quais componentes do canal web requerem backup?
    Necessita aprofundamento

14. Qual a frequencia de backup?
    Necessita aprofundamento

15. Qual o RTO/RPO para restauro de dados?
    Necessita aprofundamento


### RGPD - Data Subject Rights
16. Como serao tratados pedidos de acesso a dados (Subject Access Requests)?
    Necessita aprofundamento

17. Como sera implementado o direito ao esquecimento?
    Necessita aprofundamento

18. Ha dados do canal web a incluir nas exportacoes de dados?
    Necessita aprofundamento

### Classificacao de Dados
19. Qual o esquema de classificacao de dados (publico, interno, confidencial, restrito)?
    Necessita aprofundamento

20. Quais dados do canal web sao considerados sensiveis/PII?
    Necessita aprofundamento

### Cache Strategy
21. Quais dados serao cacheados no BFF?
    Necessita aprofundamento

22. Qual o TTL para diferentes tipos de cache?
    Necessita aprofundamento

23. Como sera invalidado o cache?
    Necessita aprofundamento

## Decisoes

### Persistencia Local Frontend
- **Decisao:** _A preencher_
- **Justificacao:**
- **Alternativas consideradas:**

### Armazenamento BFF
- **Decisao:** _A preencher_
- **Justificacao:**
- **Alternativas consideradas:**

### Encriptacao
- **Decisao:** _A preencher_
- **Justificacao:**
- **Alternativas consideradas:**

### Retencao
- **Decisao:** _A preencher_
- **Justificacao:**
- **Alternativas consideradas:**

### RGPD
- **Decisao:** _A preencher_
- **Justificacao:**
- **Alternativas consideradas:**

## Restricoes Conhecidas

- Dados transacionais residem nos backend services existentes
- Conformidade RGPD obrigatoria
- Dados bancarios classificados como sensiveis
- Requisitos de auditoria do Banco de Portugal

## Referencias

- [DEF-02-requisitos-nao-funcionais.md](DEF-02-requisitos-nao-funcionais.md) - RTO/RPO
- [DEF-08-seguranca-conformidade.md](DEF-08-seguranca-conformidade.md) - Requisitos RGPD
- RGPD - Regulamento Geral de Protecao de Dados
