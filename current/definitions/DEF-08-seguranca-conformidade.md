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

### OWASP Top 10
10. Quais controlos especificos para cada categoria OWASP Top 10?


11. Ha ferramentas de SAST/DAST integradas no pipeline?


12. Qual a frequencia de scans de vulnerabilidades?


### Conformidade PSD2
13. Como sera implementado o Dynamic Linking (valor + beneficiario)?
    Cliente informa que estrutura app já segue PSD2. Necessita aprofundamento.

14. Quais operacoes requerem SCA obrigatorio?
    Todas as operações

15. Ha operacoes elegiveis para isencoes SCA? Quais?
    Nenhuma

16. Como sera tratada a comunicacao segura (TLS 1.2+)?


### Conformidade RGPD
17. Qual a base legal para tratamento de dados?
    Necessita aprofundamento

18. Como sera obtido o consentimento do utilizador?
    Necessita aprofundamento

19. Ha DPO (Data Protection Officer) designado?
    Necessita aprofundamento

20. Como serao documentadas as atividades de tratamento (ROPA)?
    Necessita aprofundamento

### PCI-DSS
21. O canal web processara dados de cartao (PAN)?
    Necessita aprofundamento

22. Se sim, qual o nivel de conformidade PCI-DSS requerido?
    Necessita aprofundamento

23. Ha tokenizacao de dados de cartao?
    Necessita aprofundamento

### Banco de Portugal
24. Quais requisitos regulatorios especificos do BdP se aplicam?
    Necessita aprofundamento

25. Ha requisitos de reporte ao BdP?
    Necessita aprofundamento

### Registo de Auditoria
26. Quais eventos devem ser registados para auditoria?
    Necessita aprofundamento

27. Qual o formato do log de auditoria?
    Necessita aprofundamento

28. Qual o periodo de retencao dos logs de auditoria?
    Necessita aprofundamento

29. Ha requisitos de imutabilidade dos logs?
    Necessita aprofundamento

### Resposta a Incidentes
30. Existe plano de resposta a incidentes de seguranca?
    Necessita aprofundamento

31. Quais sao os tempos de resposta definidos (SLAs)?
    Necessita aprofundamento

32. Ha equipa de resposta a incidentes (CSIRT)?
    Necessita aprofundamento

### Gestao de Vulnerabilidades
33. Qual o processo de gestao de vulnerabilidades?
    Necessita aprofundamento

34. Quais SLAs para correcao de vulnerabilidades (critica, alta, media, baixa)?
    Necessita aprofundamento

35. Ha programa de bug bounty?
    Necessita aprofundamento

### Segregacao de Ambientes
36. Como serao segregados os ambientes (dev, staging, prod)?
    Necessita aprofundamento

37. Ha requisitos de segregacao de dados entre ambientes?
    Necessita aprofundamento

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

## Referencias

- [DEF-02-requisitos-nao-funcionais.md](DEF-02-requisitos-nao-funcionais.md) - NFRs
- [DEF-07-autenticacao-autorizacao.md](DEF-07-autenticacao-autorizacao.md) - SCA
- PSD2 - Payment Services Directive 2
- RGPD - Regulamento Geral de Protecao de Dados
- PCI-DSS v4.0
- OWASP Top 10 2021
