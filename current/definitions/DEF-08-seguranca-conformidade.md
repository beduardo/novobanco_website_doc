---
id: DEF-08-seguranca-conformidade
aliases:
  - Segurança e Conformidade
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

# DEF-08: Segurança & Conformidade

> **Secção relacionada:** [8 - Segurança & Conformidade](../sections/SEC-08-seguranca-conformidade.md)

## Contexto

Definir os requisitos de segurança e conformidade regulatória do HomeBanking Web, incluindo modelo de ameaças, controlos de segurança, e conformidade com PSD2, RGPD, PCI-DSS e regulamentação do Banco de Portugal.

## Perguntas a Responder

### Modelo de Ameaças
1. Foi realizada análise de ameaças (threat modeling) para o canal web?
    Não. Ação ainda pendente.

2. Quais são as principais ameaças identificadas?
    Necessita aprofundamento

3. Qual metodologia será usada para threat modeling (STRIDE, PASTA)?
    Necessita aprofundamento

### Controlos de Segurança - Frontend
4. Quais headers de segurança HTTP serão implementados?
   - Content-Security-Policy (CSP)? Sim. Iniciaremos com `self` e adicionamos o necessário durante o desenvolvimento.
   - X-Frame-Options? Sim. Com valor `SAMEORIGIN`
   - X-Content-Type-Options? Sim. Valor `nosniff`
   - Strict-Transport-Security (HSTS)? Sim. Avaliar o melhor valor para `max-age` no início do assessment.

5. Há requisitos de Subresource Integrity (SRI)?
    Sim. Traremos o máximo de bibliotecas para o servidor local para evitar mudanças de Hash inesperadas e utilizaremos `integrity` e `crossorigin`. Caso haja necessidade de utilização de bibliotecas CDN externas, necessário atenção com atualizações dos terceiros que possam quebrar o site.

6. Como será tratada a proteção contra XSS?
    SSR / BFF
        - Escape de saída do html gerado pelo SSR
        - Validação e Sanitização de Entrada
    Frontend
        - React faz o escape automaticamente.
        - `innerHTML` e `eval` proibidos via lint e SonarQube

### Controlos de Segurança - Backend/BFF
7. Quais controlos de input validation serão implementados?
    Detalhes técnicos serão especificados no assessment inicial durante a execução do projeto

8. Há WAF (Web Application Firewall)? Qual?
    Necessita aprofundamento junto à equipa de infraestrutura.

9. Como será tratada a proteção contra CSRF?
     - Utilização de tokens rotacionados por request (Tokens CSRF)
     - Cookie de sessão configurado com Strict, Secure e HttpOnly
     - CORS bem configurado
     - GET somente idempotentes e sem efeitos colaterais

### OWASP Top 10 (Simplificado)
10. Há ferramentas de SAST/DAST integradas no pipeline?
    SAST: Sim (ver DEF-10). DAST: Necessita aprofundamento

11. Será realizado penetration testing antes do go-live?
    Necessita aprofundamento


### Conformidade PSD2
12. Como será implementado o Dynamic Linking (valor + beneficiário)?
    App mobile já segue PSD2. Canal web reutiliza mesma implementação.

13. Quais operações requerem SCA obrigatório?
    Todas as operações (sem isenções)

14. Qual a versão mínima de TLS?
    TLS 1.2+ obrigatório

### Conformidade RGPD (Consolidado)
15. Qual a base legal para tratamento de dados?
    Necessita aprofundamento junto a DPO

16. Há DPO (Data Protection Officer) designado?
    Necessita aprofundamento

### PCI-DSS
17. O canal web processará dados de cartão (PAN)?
    Necessita aprofundamento. Se sim, definir nível de conformidade.

18. Há tokenização de dados de cartão?
    Necessita aprofundamento

### Banco de Portugal
19. Quais requisitos regulatórios específicos do BdP se aplicam?
    Necessita aprofundamento

### Registo de Auditoria (Consolidado)
> **Nota:** Retenção de logs em [DEF-11-observabilidade-operacoes.md](DEF-11-observabilidade-operacoes.md)

20. Quais eventos devem ser registados para auditoria?
    Necessita aprofundamento. Mínimo: logins, transações, alterações de dados

21. Há requisitos de imutabilidade dos logs?
    Necessita aprofundamento

### Resposta a Incidentes e Vulnerabilidades (Simplificado)
22. Existe plano de resposta a incidentes de segurança?
    Necessita aprofundamento

23. Quais SLAs para correção de vulnerabilidades críticas?
    Necessita aprofundamento. Sugestão: Críticas < 24h, Altas < 7 dias

### Segregação de Ambientes
> **Nota:** Ver [DEF-10-arquitetura-operacional.md](DEF-10-arquitetura-operacional.md) para detalhes de ambientes

24. Há requisitos de segregação de dados entre ambientes?
    Necessita aprofundamento. Produção nunca deve usar dados reais em dev/qa.

## Decisões

### Threat Modeling
- **Decisão:** _A preencher_
- **Justificação:**
- **Alternativas consideradas:**

### Security Headers
- **Decisão:** _A preencher_
- **Justificação:**
- **Alternativas consideradas:**

### OWASP Compliance
- **Decisão:** _A preencher_
- **Justificação:**
- **Alternativas consideradas:**

### PSD2 Compliance
- **Decisão:** _A preencher_
- **Justificação:**
- **Alternativas consideradas:**

### RGPD Compliance
- **Decisão:** _A preencher_
- **Justificação:**
- **Alternativas consideradas:**

### Audit Logging
- **Decisão:** _A preencher_
- **Justificação:**
- **Alternativas consideradas:**

### Vulnerability Management
- **Decisão:** _A preencher_
- **Justificação:**
- **Alternativas consideradas:**

## Restrições Conhecidas

- Conformidade PSD2 obrigatória para operações de pagamento
- Conformidade RGPD obrigatória para dados pessoais
- Regulamentação Banco de Portugal para instituições de crédito
- Auditoria externa regular
- SLA de disponibilidade 99.9%

## Decisões Relacionadas

- [DEC-004-controlos-seguranca-frontend.md](../decisions/DEC-004-controlos-seguranca-frontend.md) - Controlos de segurança frontend

## Referências

- [DEF-02-requisitos-nao-funcionais.md](DEF-02-requisitos-nao-funcionais.md) - NFRs
- [DEF-07-autenticacao-autorizacao.md](DEF-07-autenticacao-autorizacao.md) - SCA
- PSD2 - Payment Services Directive 2
- RGPD - Regulamento Geral de Proteção de Dados
- PCI-DSS v4.0
- OWASP Top 10 2021
