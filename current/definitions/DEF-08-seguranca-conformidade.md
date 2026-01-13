---
id: DEF-08-seguranca-conformidade
aliases:
  - Seguranca e Conformidade
tags:
  - nextreality-novobanco-website-definitions
  - definitions
  - security
  - compliance
  - psd2
  - gdpr
approved: true
created: 2026-01-03
hubs:
  - "[[nextreality]]"
para-code: R
reviewed: true
status: completed
---

# DEF-08: Seguranca & Conformidade

> **Secao relacionada:** [8 - Seguranca & Conformidade](../sections/SEC-08-seguranca-conformidade.md)

## Contexto

Definir os requisitos de seguranca e conformidade regulatoria do HomeBanking Web, incluindo modelo de ameacas, controlos de seguranca, e conformidade com PSD2, RGPD, PCI-DSS e regulamentacao do Banco de Portugal.

## Perguntas a Responder

### Modelo de Ameacas
1. Foi realizada analise de ameacas (threat modeling) para o canal web?
    Não. Ação ainda pendente.

2. Quais sao as principais ameacas identificadas?
    Necessita aprofundamento

3. Qual metodologia sera usada para threat modeling (STRIDE, PASTA)?
    Necessita aprofundamento

### Controlos de Seguranca - Frontend
4. Quais headers de seguranca HTTP serao implementados?
   - Content-Security-Policy (CSP)? Sim. Iniciaremos com `self` e adicionamos o necessário durante o desenvolvimento.
   - X-Frame-Options? Sim. Com valor `SAMEORIGIN`
   - X-Content-Type-Options? Sim. Valor `nosniff`
   - Strict-Transport-Security (HSTS)? Sim. Avaliar o melhor valor para `max-age` no início do assessment.

5. Ha requisitos de Subresource Integrity (SRI)?
    Sim. Traremos o máximo de bibliotecas para o servidor local para evitar mudanças de Hash inesperadas e utilizaremos `integrity` e `crossorigin`. Caso haja necessidade de utilização de bibliotecas CDN externas, necessário atenção com atualizações dos terceiros que possam quebrar o site.

6. Como sera tratada a protecao contra XSS?
    SSR / BFF
        - Escape de saída do html gerado pelo SSR
        - Validação e Sanitização de Entrada
    Frontend
        - React faz o escape automaticamente.
        - `innerHTML` e `eval` proibidos via lint e SonarQube

### Controlos de Seguranca - Backend/BFF
7. Quais controlos de input validation serao implementados?
    Detalhes técnicos serão especificados no assessment inicial durante a execução do projeto

8. Ha WAF (Web Application Firewall)? Qual?
    Necessita aprofundamento junto à equipa de infraestrutura.

9. Como sera tratada a protecao contra CSRF?
     - Utilização de tokens rotacionados por request (Tokens CSRF)
     - Cookie de sessão configurado com Strict, Secure e HttpOnly
     - CORS bem configurado
     - GET somente idempotentes e sem efeitos colaterais

### OWASP Top 10 (Simplificado)
10. Ha ferramentas de SAST/DAST integradas no pipeline?
    SAST: Sim (ver DEF-10). DAST: Necessita aprofundamento

11. Sera realizado penetration testing antes do go-live?
    Necessita aprofundamento


### Conformidade PSD2
12. Como sera implementado o Dynamic Linking (valor + beneficiario)?
    App mobile ja segue PSD2. Canal web reutiliza mesma implementacao.

13. Quais operacoes requerem SCA obrigatorio?
    Todas as operacoes (sem isencoes)

14. Qual a versao minima de TLS?
    TLS 1.2+ obrigatorio

### Conformidade RGPD (Consolidado)
15. Qual a base legal para tratamento de dados?
    Necessita aprofundamento junto a DPO

16. Ha DPO (Data Protection Officer) designado?
    Necessita aprofundamento

### PCI-DSS
17. O canal web processara dados de cartao (PAN)?
    Necessita aprofundamento. Se sim, definir nivel de conformidade.

18. Ha tokenizacao de dados de cartao?
    Necessita aprofundamento

### Banco de Portugal
19. Quais requisitos regulatorios especificos do BdP se aplicam?
    Necessita aprofundamento

### Registo de Auditoria (Consolidado)
> **Nota:** Retencao de logs em [DEF-11-observabilidade-operacoes.md](DEF-11-observabilidade-operacoes.md)

20. Quais eventos devem ser registados para auditoria?
    Necessita aprofundamento. Minimo: logins, transacoes, alteracoes de dados

21. Ha requisitos de imutabilidade dos logs?
    Necessita aprofundamento

### Resposta a Incidentes e Vulnerabilidades (Simplificado)
22. Existe plano de resposta a incidentes de seguranca?
    Necessita aprofundamento

23. Quais SLAs para correcao de vulnerabilidades criticas?
    Necessita aprofundamento. Sugestao: Criticas < 24h, Altas < 7 dias

### Segregacao de Ambientes
> **Nota:** Ver [DEF-10-arquitetura-operacional.md](DEF-10-arquitetura-operacional.md) para detalhes de ambientes

24. Ha requisitos de segregacao de dados entre ambientes?
    Necessita aprofundamento. Producao nunca deve usar dados reais em dev/qa.

## Decisoes

### Threat Modeling
- **Decisao:** _A preencher_
- **Justificacao:**
- **Alternativas consideradas:**

### Security Headers
- **Decisao:** _A preencher_
- **Justificacao:**
- **Alternativas consideradas:**

### OWASP Compliance
- **Decisao:** _A preencher_
- **Justificacao:**
- **Alternativas consideradas:**

### PSD2 Compliance
- **Decisao:** _A preencher_
- **Justificacao:**
- **Alternativas consideradas:**

### RGPD Compliance
- **Decisao:** _A preencher_
- **Justificacao:**
- **Alternativas consideradas:**

### Audit Logging
- **Decisao:** _A preencher_
- **Justificacao:**
- **Alternativas consideradas:**

### Vulnerability Management
- **Decisao:** _A preencher_
- **Justificacao:**
- **Alternativas consideradas:**

## Restricoes Conhecidas

- Conformidade PSD2 obrigatoria para operacoes de pagamento
- Conformidade RGPD obrigatoria para dados pessoais
- Regulamentacao Banco de Portugal para instituicoes de credito
- Auditoria externa regular
- SLA de disponibilidade 99.9%

## Decisoes Relacionadas

- [DEC-004-controlos-seguranca-frontend.md](../decisions/DEC-004-controlos-seguranca-frontend.md) - Controlos de seguranca frontend

## Referencias

- [DEF-02-requisitos-nao-funcionais.md](DEF-02-requisitos-nao-funcionais.md) - NFRs
- [DEF-07-autenticacao-autorizacao.md](DEF-07-autenticacao-autorizacao.md) - SCA
- PSD2 - Payment Services Directive 2
- RGPD - Regulamento Geral de Protecao de Dados
- PCI-DSS v4.0
- OWASP Top 10 2021
