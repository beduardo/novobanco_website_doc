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

> **Secção relacionada:** [6 - Arquitetura de Dados](../sections/SEC-06-arquitetura-dados.md)

## Contexto

Definir a arquitetura de dados do HomeBanking Web, incluindo modelo de dados, armazenamento, encriptação, retenção e conformidade RGPD. Nota: O canal web reutiliza os serviços backend existentes, logo a maioria dos dados é armazenada nos sistemas existentes.

## Perguntas a Responder

### Modelo de Dados
1. O frontend web terá persistência local de dados (IndexedDB, localStorage)?
    Sim, localStorage.

2. Quais dados podem ser armazenados temporariamente no browser?
    No momento somente os dados básicos do utilizador. Necessário mais aprofundamento com UI para avaliar se há necessidade de algo a mais. Vamos utilizar uma estratégia de cache para dados públicos, notícias e também para informações muito utilizadas na construção das páginas. As informações sigilosas do utilizador ficarão em cache no BFF.

3. Há dados específicos do canal web que não existem na app mobile?
    Não

### Armazenamento no BFF
4. O BFF terá base de dados própria ou apenas cache?
    Apenas cache

5. Se houver base de dados, qual tecnologia (SQL Server, PostgreSQL, Redis)?
    Não há

6. Quais dados serão armazenados no BFF (além de sessões)?
    No momento somente a sessão. Caso o Frontend utilize SSR e SGA por completo, as informações mais utilizadas estarão disponíveis em cache no BFF.

### Encriptação
7. Quais dados devem ser encriptados em trânsito (TLS versão)?
    Ainda não definidos

8. Há requisitos de encriptação em repouso para dados no BFF/cache?
    Não há requisitos

9. Como serão geridas as chaves de encriptação?
    No momento somente SSL está em consideração.

### Retenção de Dados
10. Qual a política de retenção para logs de acesso web?
    Necessita aprofundamento

11. Qual a política de retenção para dados de sessão?
    Necessita aprofundamento

12. Há requisitos específicos de retenção para auditoria?
    Necessita aprofundamento

### Backup & Restore
13. Quais componentes do canal web requerem backup?
    Necessita aprofundamento

14. Qual a frequência de backup?
    Necessita aprofundamento

15. Qual o RTO/RPO para restauro de dados?
    Necessita aprofundamento


### RGPD (Simplificado)

> **Nota:** Detalhes de conformidade RGPD em [DEF-08-seguranca-conformidade.md](DEF-08-seguranca-conformidade.md)

16. Há dados específicos do canal web sujeitos a RGPD?
    Logs de sessão, preferências de utilizador. Dados transacionais são do Core Banking.

17. Quais dados do canal web são considerados PII?
    Session ID, IP, User-Agent, preferências. Dados bancários são do backend.

### Cache Strategy (Consolidado)

18. Quais dados serão cacheados no BFF?
    - Tokens de sessão (chave: session cookie)
    - Dados públicos (notícias, taxas)
    - Dados frequentes do utilizador (com TTL curto)

19. Qual a estrutura de chaves do cache Redis?
    Necessita aprofundamento. Sugestão: `session:{id}`, `user:{id}:data`, `public:{type}`

20. Qual o TTL para diferentes tipos de cache?
    Necessita aprofundamento. Sugestão: sessão 30min, público 1h, utilizador 5min

21. Como será invalidado o cache?
    Necessita aprofundamento. Considerar: TTL expiry, invalidação explícita em logout

## Decisões

### Persistência Local Frontend
- **Decisão:** localStorage para dados não sensíveis (DEC-005)
- **Justificação:** Dados básicos do utilizador, dados públicos, notícias e informações frequentes para construção de páginas. Informações sigilosas ficam em cache no BFF.
- **Alternativas consideradas:** IndexedDB (descartado - requisitos PWA/Offline não definidos), nenhum armazenamento (descartado - impacto em performance)

### Armazenamento BFF
- **Decisão:** Apenas cache - Redis Cluster (DEC-005)
- **Justificação:** BFF não possui base de dados própria. Dados transacionais residem nos backend services existentes. Cache para sessões e tokens.
- **Alternativas consideradas:** BFF com base de dados própria (descartado - duplicação de dados, complexidade operacional)

### Encriptação
- **Decisão:** TLS em trânsito; encriptação em repouso em definição durante projeto
- **Justificação:** SSL/TLS como base. Requisitos de encriptação em repouso e gestão de chaves a detalhar em âmbito de implementação.
- **Alternativas consideradas:** N/A

### Retenção
- **Decisão:** _A definir_ - Necessita aprofundamento
- **Justificação:** Políticas de retenção para logs de acesso, dados de sessão e requisitos de auditoria ainda pendentes.
- **Alternativas consideradas:** N/A

### RGPD
- **Decisão:** Conformidade RGPD gerida integralmente pela API/Backend
- **Justificação:** Dados transacionais são do Core Banking. Logs de sessão e preferências do utilizador seguem processos RGPD existentes.
- **Alternativas consideradas:** Gestão parcial no frontend (descartado por requisito do cliente)

## Restrições Conhecidas

- Dados transacionais residem nos backend services existentes
- Conformidade RGPD obrigatória
- Dados bancários classificados como sensíveis
- Requisitos de auditoria do Banco de Portugal

## Decisões Relacionadas

- [DEC-005-armazenamento-dados-canal-web.md](../decisions/DEC-005-armazenamento-dados-canal-web.md) - Armazenamento de dados no canal web

## Referências

- [DEF-02-requisitos-nao-funcionais.md](DEF-02-requisitos-nao-funcionais.md) - RTO/RPO
- [DEF-08-seguranca-conformidade.md](DEF-08-seguranca-conformidade.md) - Requisitos RGPD
- RGPD - Regulamento Geral de Proteção de Dados
