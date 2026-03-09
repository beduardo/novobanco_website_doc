# Questoes para Reuniao com Cliente

**Data:** 2026-01-13
**Projeto:** HomeBanking Web - HLD
**Objetivo:** Esclarecer questoes pendentes nas definicoes do HLD
**Versão:** 2.3 (consolidação de itens pendentes das definições)

---

## Prioridade Alta - Decisoes Arquiteturais

### 1. PWA e Funcionamento Offline (DEF-04-ux-guidelines)

- O HomeBanking Web deve funcionar como PWA instalavel?
    Não
- Ha requisitos de funcionamento offline? Se sim, quais funcionalidades?
    Não
- Qual o comportamento esperado em conectividade intermitente?
    (Quais as opções?)

### 2. Sessao Multi-Canal (DEF-07-autenticacao-autorizacao)

- Como a sessao web se relaciona com a sessao mobile (mesmo utilizador)?
    Não há relação
- Ha limite de sessoes ativas por utilizador?
    (A questionar)
- O login web deve fazer logout automatico de outras sessoes?
    (A questionar)

### 3. Fluxos de Autenticacao Fallback (DEF-07-autenticacao-autorizacao)

- Quais combinacoes de segundo fator estarao disponiveis no fallback (SMS OTP, App Push, ambos)?
    (O cliente não entendeu a pergunta)
- A disponibilidade depende de configuracao por utilizador ou e uniforme?
    Uniforme
- Ha prioridade entre os metodos de fallback?
    Não

### 4. Primeiro Acesso / Registo Web (DEF-07-autenticacao-autorizacao)

- Existe fluxo de primeiro acesso/registo especifico para o canal web?
    Sim
- Se sim, como funciona a validacao de identidade inicial?
    É feita com a mesma API de Login
- O utilizador pode registar-se apenas pelo web ou necessita da app mobile primeiro?
    Pela Web ou pela APP. São processos semelhantes mas necessários em cada dispositivo.

### 5. Politicas de Password (DEF-07-autenticacao-autorizacao)
(Resposta geral do cliente: Todo este processo é gerido pelas API. Não estou a ver a necessidade de abordar este tema no front.)
- Quais os requisitos minimos de password (comprimento, complexidade)? 
    Sim, gerido pela API
- Ha politica de expiracao de password? Se sim, qual o periodo? 
    Sim, gerido pela API
- Ha mecanismo de bloqueio apos tentativas falhadas? Quantas tentativas? 
    Sim, gerido pela API
- Como funciona o fluxo de recuperacao/reset de password? 
    Sim, gerido pela API

### 6. Anti-automacao e Revogacao (DEF-07-autenticacao-autorizacao)

- Sera implementado CAPTCHA em algum fluxo (login, recuperacao password)?
    (A questionar)
- Ha mecanismo de logout de todos os dispositivos (panic button)?
    (A questionar)
- Como funciona a revogacao de tokens em caso de comprometimento?
    (A questionar)

### 7. Acessibilidade - WCAG (DEF-04-design-system)

- Qual o nivel de WCAG obrigatorio (A, AA, AAA)?
    Já respondido, AA
- Ha requisitos especificos de contraste ou tamanho de fonte?
    (A questionar)
- Sera necessaria auditoria de acessibilidade externa?
    (A questionar)

### 8. CDN para Assets Estaticos (DEF-04-stack-frontend)

- Sera utilizado CDN para assets estaticos?
    Deve ser uma decisão sua. Decida e informe os motivos.
- Se sim, qual provider (Azure CDN, Cloudflare, outro)?
    Decida.

---

## Prioridade Alta - Seguranca e Conformidade
(Resposta geral do cliente: Todo este processo é gerido pelas API. Não estou a ver a necessidade de abordar este tema no front.)
### 9. RGPD (DEF-08-seguranca-conformidade)

- Qual a base legal para tratamento de dados dos utilizadores?
- Existe DPO (Data Protection Officer) designado?

### 10. PCI-DSS (DEF-08-seguranca-conformidade)

- O canal web processa dados de cartao (PAN) diretamente?
- Se sim, qual o nivel de conformidade PCI-DSS necessario?
- A tokenizacao de cartoes e feita onde (frontend, backend, terceiro)?

### 11. Banco de Portugal (DEF-08-seguranca-conformidade)

- Quais os requisitos regulatorios especificos do Banco de Portugal aplicaveis?

### 12. Auditoria (DEF-08-seguranca-conformidade, DEF-11-observabilidade)

- Quais eventos devem ser registados para auditoria?
- Qual o periodo de retencao de logs de auditoria?
- Os logs devem ser imutaveis (write-once)?

### 13. Resposta a Incidentes (DEF-08-seguranca-conformidade)

- Existe plano de resposta a incidentes de seguranca?
- Quais os SLAs de resposta por severidade de vulnerabilidade?

---

## Prioridade Media - Infraestrutura e Operacoes

### 14. OpenShift e Ambientes (DEF-10-arquitetura-operacional)

- Qual o timeline previsto para migracao de AKS para OpenShift?
- Qual a versao do OpenShift que sera utilizada?

### 15. Observabilidade (DEF-11-observabilidade-operacoes)

- Confirmar reutilizacao do ELK Stack existente ou instancia dedicada?
- Ha complemento com Prometheus/Grafana para metricas?
- Qual a ferramenta de alerting em uso?

### 16. Disaster Recovery (DEF-10-arquitetura-operacional)

- Ha site de DR? Onde?
- Qual a estrategia de failover (automatico, manual)?

### 17. Feature Flags (DEF-10-arquitetura-operacional)

- Sera utilizado sistema de feature flags para rollout gradual?
- Se sim, qual ferramenta (LaunchDarkly, Unleash, custom)?

---

## Prioridade Media - Integracoes

### 18. Backend API e SLAs (DEF-09-integracao-interfaces)

- Quais os SLAs de disponibilidade do Backend API existente?
- Ha janelas de manutencao programadas que afetam integracoes?

### 19. Notificacoes (DEF-09-integracao-interfaces)

- Qual o provider de SMS em uso?
- Qual o provider de Push Notifications?
- Qual o provider de Email Transacional?

### 20. Cartoes (DEF-09-integracao-interfaces)

- Qual o provider de emissao/processamento de cartoes?
- Como funciona a integracao 3D Secure?

### 21. Open Banking / PSD2 (DEF-09-integracao-interfaces)

- O banco expoe APIs como ASPSP?
- O banco consome APIs de terceiros como TPP?
- Qual o modelo de gestao de consentimentos PSD2?

### 22. Message Broker (DEF-09-integracao-interfaces)

- Existe message broker em uso (RabbitMQ, Kafka, Azure Service Bus)?
- Quais eventos sao publicados/consumidos pelo canal web?

### 23. HSM - Hardware Security Module (DEF-09-integracao-interfaces)

- Qual HSM e utilizado pelo banco (Thales, AWS CloudHSM, Azure Dedicated HSM)?
- Quais operacoes do canal web requerem HSM (assinatura digital, encriptacao)?
- A integracao HSM ja esta disponivel via Backend API?

### 24. Identity Provider / SSO (DEF-09-integracao-interfaces)

- Existe Identity Provider corporativo (Azure AD, Okta, outro)?
- Ha requisitos de SSO entre o canal web e outros sistemas internos?
- O Identity Provider e o mesmo utilizado pela app mobile?

### 25. Document Management System (DEF-09-integracao-interfaces)

- Existe DMS centralizado para extratos e comprovativos?
- Os documentos sao gerados em tempo real ou pre-gerados?
- Ha requisitos de assinatura digital em documentos?

---

## Prioridade Media - Performance e Cache

### 26. Core Web Vitals (DEF-12-desempenho-fiabilidade)

- Quais metricas Core Web Vitals devem ser atingidas?
- Ha requisitos especificos de bundle size maximo?

### 27. Auto-scaling (DEF-12-desempenho-fiabilidade)

- Sera configurado Horizontal Pod Autoscaler (HPA)?
- Quais metricas devem disparar o auto-scaling?
- Quais os limites minimo e maximo de replicas?

### 28. Cache Strategy (DEF-06-arquitetura-dados)

- Qual o TTL para diferentes tipos de cache (sessao, publico, utilizador)?
- Como sera invalidado o cache?

---

## Prioridade Normal - Implementacao e Go-Live

### 29. Timeline (DEF-14-plano-migracao-implementacao)

- Qual a data prevista para go-live?
- O lancamento sera faseado (pilot/beta) ou big-bang?
- Qual a duracao prevista do periodo de hypercare?

### 30. Cutover (DEF-14-plano-migracao-implementacao)

- Qual a estrategia de cutover preferida (big-bang, phased, parallel)?
- Ha sistema HomeBanking web legado a substituir?

### 31. Criterios Go/No-Go (DEF-14-plano-migracao-implementacao)

- Quem sao os aprovadores para decisao de go-live?
- Quais os criterios minimos obrigatorios?

---

## Prioridade Normal - Governacao

### 32. Modelo de Trabalho (DEF-15-governacao-roadmap)

- Qual a metodologia de projeto (Agile, SAFe, tradicional)?
- Quem aprova decisoes tecnicas/arquiteturais?

### 33. Change Management (DEF-15-governacao-roadmap)

- Existe processo de Change Advisory Board (CAB)?
- Quem aprova mudancas em producao?

### 34. Roadmap (DEF-15-governacao-roadmap)

- Qual a cadencia de releases prevista?
- Qual a percentagem de capacidade alocada para divida tecnica?

---

## Prioridade Normal - Testes

### 35. Estrategia de Testes (DEF-13-estrategia-testes)

- Qual a cobertura de codigo minima requerida?
- Sera utilizado contract testing (Pact) para BFF<->Backend?
- Ha ambiente com dados anonimizados de producao?

### 36. Penetration Testing (DEF-08-seguranca-conformidade)

- Ha penetration testing periodico?
- Sera realizado pentest antes do go-live?

---

## Inconsistencias e Clarificacoes Necessarias

As seguintes inconsistencias foram identificadas no cruzamento entre definicoes e decisoes:

### 37. Retencao de Logs (DEF-02-requisitos-nao-funcionais vs DEC-008)

- DEF-02-nfr marca "Falta aprofundamento" para politica de retencao
- DEC-008 indica "definir politica conforme compliance"
- **Questao:** Qual o requisito regulatorio especifico? (tipico bancario: 7 anos)

### 38. Fluxo de Onboarding Web (DEF-09-integracao-interfaces)

- Questao 6 indica KYC "ja implementado no backend"
- Questao 7 sobre onboarding web esta "Necessita aprofundamento"
- **Questao:** O canal web tera fluxo de onboarding/registo proprio ou apenas login para utilizadores ja registados na app mobile?

### 39. Gateway de Pagamentos (DEF-09-integracao-interfaces)

- Catalogo de dependencias indica: Criticidade Alta, status "A validar"
- **Questao:** O Gateway de Pagamentos e o mesmo utilizado pela app mobile ou sera um novo?

### 40. Notificacoes - Reutilizacao (DEF-09-integracao-interfaces)

- Questoes 9-11 indicam "A definir no assessment"
- **Questao:** Confirmar se SMS, Push e Email serao os mesmos servicos da app mobile (reutilizacao) ou novos providers

---

## Prioridade Média - Segurança Adicional [NOVO v2.3]

### 41. Threat Modeling (DEF-08-seguranca-conformidade)

- Qual metodologia será utilizada para threat modeling (STRIDE, PASTA, outra)?
- Já foi realizada análise de ameaças para outros canais que possa ser reutilizada?

### 42. WAF - Web Application Firewall (DEF-08-seguranca-conformidade)

- Há WAF implementado na infraestrutura?
- Se sim, qual solução (Azure WAF, F5, Cloudflare)?
- Quais regras/políticas estão configuradas?

### 43. Segregação de Dados entre Ambientes (DEF-08-seguranca-conformidade)

- Qual a política de segregação de dados entre ambientes (dev/qa/prod)?
- É permitido uso de dados de produção em ambientes inferiores?
- Há processo de anonimização de dados para testes?

---

## Prioridade Média - Observabilidade Adicional [NOVO v2.3]

### 44. Tracing Distribuído (DEF-11-observabilidade-operacoes)

- Será implementado tracing distribuído (OpenTelemetry, Jaeger)?
- Como será feita a correlação de requests entre Frontend e BFF (correlation-id)?

### 45. Load Testing (DEF-12-desempenho-fiabilidade)

- Qual ferramenta de load testing será utilizada (k6, JMeter, Gatling)?
- Há ambiente dedicado para testes de carga?
- Quais cenários de carga devem ser validados antes do go-live?

---

## Prioridade Normal - UX Adicional [NOVO v2.3]

### 46. Pontos de Dor App Mobile (DEF-04-ux-guidelines)

- Existem pontos de dor conhecidos na app mobile que devem ser evitados no canal web?
- Há feedback de utilizadores documentado sobre a app mobile?

---

## Resumo por Area

| Area | Questoes | Criticidade |
|------|----------|-------------|
| Arquitetura (PWA, Sessao, Autenticacao) | 8 | Alta |
| Seguranca/Conformidade | 5 | Alta |
| Infraestrutura/Operacoes | 4 | Media |
| Integracoes (incl. HSM, SSO, DMS) | 8 | Media |
| Performance/Cache | 3 | Media |
| Implementacao | 3 | Normal |
| Governacao | 3 | Normal |
| Testes | 2 | Normal |
| Inconsistencias/Clarificacoes | 4 | Alta |
| Segurança Adicional (v2.3) | 3 | Média |
| Observabilidade Adicional (v2.3) | 2 | Média |
| UX Adicional (v2.3) | 1 | Normal |
| **Total** | **46** | - |

---

## Proximos Passos

Apos esta reuniao:

1. Atualizar as definicoes (DEF-*) com as respostas obtidas
2. Preencher decisoes nas definicoes que foram esclarecidas
3. Identificar questoes que requerem sessoes adicionais
4. Agendar reuniao de follow-up se necessario
5. Definir data alvo para entrega do HLD

---

## Notas da Reuniao

_Espaco para anotacoes durante a reuniao_

**Data da reuniao:**
**Participantes:**

### Respostas e Decisoes

| # | Questao | Resposta | Acao |
|---|---------|----------|------|
| 1 | PWA instalavel? | | |
| 2 | Sessao multi-canal? | | |
| 3 | WCAG nivel? | | |
| ... | ... | | |

---

## Historico de Versoes

| Versao | Data | Alteracoes |
|--------|------|------------|
| 1.0 | 2026-01-11 | Versao inicial |
| 2.0 | 2026-01-13 | Revisao apos consolidacao de duplicacoes nas definicoes. Adicionadas 4 questoes novas (CDN, Sessao Multi-Canal, Feature Flags, Core Web Vitals). Removidas questoes ja respondidas. Reorganizado por prioridade. |
| 2.1 | 2026-01-13 | Adicionadas 4 questoes de autenticacao pendentes das decisoes DEC-001/DEC-002: Fluxos Fallback (#3), Primeiro Acesso Web (#4), Politicas Password (#5), Anti-automacao e Revogacao (#6). Total de questoes: 33. |
| 2.2 | 2026-01-13 | Adicionadas 7 questoes de integracao (HSM #23, SSO #24, DMS #25) e 4 questoes de inconsistencias identificadas no cruzamento DEF/DEC (#37-40). Renumeracao de questoes. Total de questoes: 40. |
| 2.3 | 2026-01-14 | Consolidação de itens pendentes das definições DEF-04, DEF-08, DEF-10, DEF-11, DEF-12. Adicionadas 6 questões: Threat Modeling (#41), WAF (#42), Segregação Ambientes (#43), Tracing (#44), Load Testing (#45), Pontos de Dor Mobile (#46). Correcção ortográfica (português europeu). Total: 46 questões. |
