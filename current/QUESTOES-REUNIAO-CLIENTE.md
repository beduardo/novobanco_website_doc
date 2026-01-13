# Questoes para Reuniao com Cliente

**Data:** 2026-01-13
**Projeto:** HomeBanking Web - HLD
**Objetivo:** Esclarecer questoes pendentes nas definicoes do HLD
**Versao:** 2.1 (adicionadas questoes de autenticacao)

---

## Prioridade Alta - Decisoes Arquiteturais

### 1. PWA e Funcionamento Offline (DEF-04-ux-guidelines)

- O HomeBanking Web deve funcionar como PWA instalavel?
- Ha requisitos de funcionamento offline? Se sim, quais funcionalidades?
- Qual o comportamento esperado em conectividade intermitente?

### 2. Sessao Multi-Canal (DEF-07-autenticacao-autorizacao)

- Como a sessao web se relaciona com a sessao mobile (mesmo utilizador)?
- Ha limite de sessoes ativas por utilizador?
- O login web deve fazer logout automatico de outras sessoes?

### 3. Fluxos de Autenticacao Fallback (DEF-07-autenticacao-autorizacao) [NOVO]

- Quais combinacoes de segundo fator estarao disponiveis no fallback (SMS OTP, App Push, ambos)?
- A disponibilidade depende de configuracao por utilizador ou e uniforme?
- Ha prioridade entre os metodos de fallback?

### 4. Primeiro Acesso / Registo Web (DEF-07-autenticacao-autorizacao) [NOVO]

- Existe fluxo de primeiro acesso/registo especifico para o canal web?
- Se sim, como funciona a validacao de identidade inicial?
- O utilizador pode registar-se apenas pelo web ou necessita da app mobile primeiro?

### 5. Politicas de Password (DEF-07-autenticacao-autorizacao) [NOVO]

- Quais os requisitos minimos de password (comprimento, complexidade)?
- Ha politica de expiracao de password? Se sim, qual o periodo?
- Ha mecanismo de bloqueio apos tentativas falhadas? Quantas tentativas?
- Como funciona o fluxo de recuperacao/reset de password?

### 6. Anti-automacao e Revogacao (DEF-07-autenticacao-autorizacao) [NOVO]

- Sera implementado CAPTCHA em algum fluxo (login, recuperacao password)?
- Ha mecanismo de logout de todos os dispositivos (panic button)?
- Como funciona a revogacao de tokens em caso de comprometimento?

### 7. Acessibilidade - WCAG (DEF-04-design-system)

- Qual o nivel de WCAG obrigatorio (A, AA, AAA)?
- Ha requisitos especificos de contraste ou tamanho de fonte?
- Sera necessaria auditoria de acessibilidade externa?

### 8. CDN para Assets Estaticos (DEF-04-stack-frontend)

- Sera utilizado CDN para assets estaticos?
- Se sim, qual provider (Azure CDN, Cloudflare, outro)?

---

## Prioridade Alta - Seguranca e Conformidade

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

---

## Prioridade Media - Performance e Cache

### 23. Core Web Vitals (DEF-12-desempenho-fiabilidade)

- Quais metricas Core Web Vitals devem ser atingidas?
- Ha requisitos especificos de bundle size maximo?

### 24. Auto-scaling (DEF-12-desempenho-fiabilidade)

- Sera configurado Horizontal Pod Autoscaler (HPA)?
- Quais metricas devem disparar o auto-scaling?
- Quais os limites minimo e maximo de replicas?

### 25. Cache Strategy (DEF-06-arquitetura-dados)

- Qual o TTL para diferentes tipos de cache (sessao, publico, utilizador)?
- Como sera invalidado o cache?

---

## Prioridade Normal - Implementacao e Go-Live

### 26. Timeline (DEF-14-plano-migracao-implementacao)

- Qual a data prevista para go-live?
- O lancamento sera faseado (pilot/beta) ou big-bang?
- Qual a duracao prevista do periodo de hypercare?

### 27. Cutover (DEF-14-plano-migracao-implementacao)

- Qual a estrategia de cutover preferida (big-bang, phased, parallel)?
- Ha sistema HomeBanking web legado a substituir?

### 28. Criterios Go/No-Go (DEF-14-plano-migracao-implementacao)

- Quem sao os aprovadores para decisao de go-live?
- Quais os criterios minimos obrigatorios?

---

## Prioridade Normal - Governacao

### 29. Modelo de Trabalho (DEF-15-governacao-roadmap)

- Qual a metodologia de projeto (Agile, SAFe, tradicional)?
- Quem aprova decisoes tecnicas/arquiteturais?

### 30. Change Management (DEF-15-governacao-roadmap)

- Existe processo de Change Advisory Board (CAB)?
- Quem aprova mudancas em producao?

### 31. Roadmap (DEF-15-governacao-roadmap)

- Qual a cadencia de releases prevista?
- Qual a percentagem de capacidade alocada para divida tecnica?

---

## Prioridade Normal - Testes

### 32. Estrategia de Testes (DEF-13-estrategia-testes)

- Qual a cobertura de codigo minima requerida?
- Sera utilizado contract testing (Pact) para BFF<->Backend?
- Ha ambiente com dados anonimizados de producao?

### 33. Penetration Testing (DEF-08-seguranca-conformidade)

- Ha penetration testing periodico?
- Sera realizado pentest antes do go-live?

---

## Resumo por Area

| Area | Questoes | Criticidade |
|------|----------|-------------|
| Arquitetura (PWA, Sessao, Autenticacao) | 8 | Alta |
| Seguranca/Conformidade | 5 | Alta |
| Infraestrutura/Operacoes | 4 | Media |
| Integracoes | 5 | Media |
| Performance/Cache | 3 | Media |
| Implementacao | 3 | Normal |
| Governacao | 3 | Normal |
| Testes | 2 | Normal |
| **Total** | **33** | - |

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
