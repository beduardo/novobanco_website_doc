---
id: QUESTOES-PENDENTES
aliases:
  - Questoes Pendentes de Aprofundamento
tags:
  - nextreality-novobanco-website
  - questionnaire
  - pending
created: 2026-01-10
status: draft
---

# Questoes Pendentes de Aprofundamento

Este documento consolida todas as questoes que necessitam de aprofundamento junto ao cliente e stakeholders para completar o documento de arquitetura do HomeBanking Web.

---

## Secao 0 - Questoes de Escopo (Identificadas na Reavaliacao)

> **PRIORIDADE ALTA:** Estas questoes devem ser respondidas antes de continuar com o desenvolvimento do documento.

### DEF-01: Objetivos do Documento

| # | Questao | Responsavel Sugerido | Impacto |
|---|---------|---------------------|---------|
| 1 | O documento HLD deve incluir especificacoes para as apps nativas iOS/Android ou apenas o canal Web? | Cliente / Arquitetura | Alto - Define escopo de todo o documento |
| 2 | A "integracao React no nativo" (mencionada no CONTEXT) e relevante para este documento? | Cliente / Arquitetura | Alto - Pode requerer novas secoes |
| 3 | O CMS e backoffice sao parte do escopo deste HLD ou serao documentos separados? | Cliente / Arquitetura | Medio - Define fronteiras do documento |
| 4 | Existe uma metodologia "canais Best" ja definida que deve ser referenciada? | Cliente | Medio - Pode afetar estrutura |

### DEF-02: Stakeholders

| # | Questao | Responsavel Sugerido | Impacto |
|---|---------|---------------------|---------|
| 5 | Existem equipas externas envolvidas no projeto? O CONTEXT menciona "ligacao com equipas externas" mas DEF-02 diz que nao ha. | Cliente / PM | Alto - Contradicao a resolver |
| 6 | Qual o modelo de trabalho entre equipas internas e externas (ambientes, comunicacao, responsabilidades)? | PM / Arquitetura | Alto - Definir governacao |
| 7 | Quais os perfis tecnicos necessarios para o projeto (React, nativo iOS/Android, .NET, Gateway, APIs)? | PM / RH | Medio - Alocacao de recursos |

### DEF-10: Arquitetura Operacional

| # | Questao | Responsavel Sugerido | Impacto |
|---|---------|---------------------|---------|
| 8 | O repositorio de codigo sera em GitHub (mencionado no CONTEXT) ou Azure Repos (documentado em DEF-10/SEC-10)? | Infraestrutura / Cliente | Alto - Afeta pipelines CI/CD |

---

## Secao 2 - Contexto de Negocio & Requisitos

### DEF-02: Requisitos Nao Funcionais

#### Padroes Internacionais
| # | Questao | Responsavel Sugerido |
|---|---------|---------------------|
| 8 | Quais padroes internacionais de NFR devem ser seguidos (ISO 25010, NIST, etc.)? O CONTEXT menciona que NFRs devem atender padroes internacionais. | Arquitetura / Compliance |

#### Seguranca
| # | Questao | Responsavel Sugerido |
|---|---------|---------------------|
| 1 | Quais certificacoes de seguranca sao requeridas? | Seguranca / Compliance |
| 2 | Ha requisitos especificos de encriptacao? | Seguranca |
| 3 | Qual e a politica de retencao de logs? | Compliance / Legal |

---

## Secao 4 - Experiencia do Utilizador & Frontend

### DEF-04: Stack Frontend

| # | Questao | Responsavel Sugerido |
|---|---------|---------------------|
| 1 | Ha requisitos especificos de bundle size maximo? | Arquitetura / Cliente |

### DEF-04: Design System

| # | Questao | Responsavel Sugerido |
|---|---------|---------------------|
| 1 | Ha componentes especificos do sector bancario a considerar? | UX / Cliente |
| 2 | Quais niveis de WCAG devem ser atingidos (A, AA, AAA)? | UX / Compliance |
| 3 | Ha requisitos especificos de contraste ou tamanho de fonte? | UX / Acessibilidade |

### DEF-04: UX Guidelines

| # | Questao | Responsavel Sugerido |
|---|---------|---------------------|
| 1 | Ha pontos de dor conhecidos na app mobile a evitar? | UX / Cliente |
| 2 | Ha requisitos de funcionamento offline (PWA)? | Arquitetura / Cliente |
| 3 | Sera implementado como PWA instalavel? | Arquitetura / Cliente |
| 4 | Como sera comunicada a seguranca ao utilizador? | UX / Seguranca |
| 5 | Ha requisitos de timeout de sessao com aviso previo? | Seguranca / UX |

---

## Secao 5 - Arquitetura Backend & Servicos

### DEF-05: Arquitetura BFF

| # | Questao | Responsavel Sugerido |
|---|---------|---------------------|
| 1 | Ha requisitos de comunicacao assincrona (message queues)? | Arquitetura |
| 2 | Quais sao os requisitos de escalabilidade do BFF? | Infraestrutura |
| 3 | Ha requisitos de auto-scaling? | Infraestrutura |

### DEF-05: API Design

| # | Questao | Responsavel Sugerido |
|---|---------|---------------------|
| 1 | Qual sera a politica de deprecacao de versoes de API? | Arquitetura |
| 2 | Qual padrao de tratamento de erros sera adotado (RFC 7807)? | Arquitetura |
| 3 | Quais headers de cache serao utilizados? | Arquitetura |

### DEF-05: Padroes de Resiliencia

| # | Questao | Responsavel Sugerido |
|---|---------|---------------------|
| 1 | Sera implementado Circuit Breaker? Qual biblioteca (Polly)? | Arquitetura |
| 2 | Quais serao os thresholds de abertura do circuito? | Arquitetura |
| 3 | Qual sera o tempo de recuperacao do circuit breaker? | Arquitetura |
| 4 | Quais limites de rate limiting serao aplicados? | Arquitetura / Infra |
| 5 | Qual sera a frequencia de verificacao dos health checks? | Infraestrutura |

---

## Secao 6 - Arquitetura de Dados

### DEF-06: Arquitetura de Dados

#### Encriptacao
| # | Questao | Responsavel Sugerido |
|---|---------|---------------------|
| 1 | Quais dados devem ser encriptados em transito (TLS versao)? | Seguranca |

#### Retencao de Dados
| # | Questao | Responsavel Sugerido |
|---|---------|---------------------|
| 2 | Qual a politica de retencao para logs de acesso web? | Compliance / Legal |
| 3 | Qual a politica de retencao para dados de sessao? | Compliance |
| 4 | Ha requisitos especificos de retencao para auditoria? | Compliance / Auditoria |

#### Backup & Restore
| # | Questao | Responsavel Sugerido |
|---|---------|---------------------|
| 5 | Quais componentes do canal web requerem backup? | Infraestrutura |
| 6 | Qual a frequencia de backup? | Infraestrutura |
| 7 | Qual o RTO/RPO para restauro de dados? | Infraestrutura |

#### RGPD - Data Subject Rights
| # | Questao | Responsavel Sugerido |
|---|---------|---------------------|
| 8 | Como serao tratados pedidos de acesso a dados (Subject Access Requests)? | DPO / Legal |
| 9 | Como sera implementado o direito ao esquecimento? | DPO / Legal |
| 10 | Ha dados do canal web a incluir nas exportacoes de dados? | DPO |

#### Classificacao de Dados
| # | Questao | Responsavel Sugerido |
|---|---------|---------------------|
| 11 | Qual o esquema de classificacao de dados (publico, interno, confidencial, restrito)? | Seguranca / DPO |
| 12 | Quais dados do canal web sao considerados sensiveis/PII? | DPO |

#### Cache Strategy
| # | Questao | Responsavel Sugerido |
|---|---------|---------------------|
| 13 | Quais dados serao cacheados no BFF? | Arquitetura |
| 14 | Qual o TTL para diferentes tipos de cache? | Arquitetura |
| 15 | Como sera invalidado o cache? | Arquitetura |

---

## Secao 7 - Autenticacao & Autorizacao

### DEF-07: Autenticacao & Autorizacao

#### Fluxos de Autenticacao
| # | Questao | Responsavel Sugerido |
|---|---------|---------------------|
| 1 | Ha fluxo de primeiro acesso/registo especifico para web? | Produto / Seguranca |

#### Gestao de Sessoes
| # | Questao | Responsavel Sugerido |
|---|---------|---------------------|
| 2 | A sessao e exclusiva (logout de outras sessoes ao fazer login)? (Desejavel, aguarda aprovacao) | Cliente |

#### Politicas de Password
| # | Questao | Responsavel Sugerido |
|---|---------|---------------------|
| 3 | Quais os requisitos minimos de password (comprimento, complexidade)? | Seguranca |
| 4 | Ha politica de expiracao de password? | Seguranca |
| 5 | Como sera tratado o fluxo de recuperacao de password? | Seguranca / UX |
| 6 | Ha bloqueio apos tentativas falhadas? Quantas? | Seguranca |

#### Anti-automation
| # | Questao | Responsavel Sugerido |
|---|---------|---------------------|
| 7 | Sera implementado CAPTCHA? Em quais fluxos? | Seguranca |
| 8 | Ha rate limiting especifico para tentativas de login? | Seguranca |
| 9 | Como serao detetados e bloqueados bots? | Seguranca |

#### Revogacao
| # | Questao | Responsavel Sugerido |
|---|---------|---------------------|
| 10 | Como serao revogadas sessoes em caso de comprometimento? | Seguranca |
| 11 | Ha mecanismo de "logout de todos os dispositivos"? | Seguranca |
| 12 | Como sera tratada a revogacao de tokens ao mudar password? | Seguranca |

---

## Secao 8 - Seguranca & Conformidade

### DEF-08: Seguranca & Conformidade

#### Modelo de Ameacas
| # | Questao | Responsavel Sugerido |
|---|---------|---------------------|
| 1 | Quais sao as principais ameacas identificadas para o canal web? | Seguranca |
| 2 | Qual metodologia sera usada para threat modeling (STRIDE, PASTA)? | Seguranca |

#### Controlos de Seguranca
| # | Questao | Responsavel Sugerido |
|---|---------|---------------------|
| 3 | Ha WAF (Web Application Firewall)? Qual? | Infraestrutura / Seguranca |

#### OWASP Top 10
| # | Questao | Responsavel Sugerido |
|---|---------|---------------------|
| 4 | Quais controlos especificos para cada categoria OWASP Top 10? | Seguranca |
| 5 | Ha ferramentas de SAST/DAST integradas no pipeline? | DevSecOps |
| 6 | Qual a frequencia de scans de vulnerabilidades? | Seguranca |

#### Conformidade PSD2
| # | Questao | Responsavel Sugerido |
|---|---------|---------------------|
| 7 | Como sera implementado o Dynamic Linking (valor + beneficiario)? | Arquitetura / Compliance |
| 8 | Como sera tratada a comunicacao segura (TLS 1.2+)? | Infraestrutura |

#### Conformidade RGPD
| # | Questao | Responsavel Sugerido |
|---|---------|---------------------|
| 9 | Qual a base legal para tratamento de dados? | DPO / Legal |
| 10 | Como sera obtido o consentimento do utilizador? | DPO / UX |
| 11 | Ha DPO (Data Protection Officer) designado? | Legal |
| 12 | Como serao documentadas as atividades de tratamento (ROPA)? | DPO |

#### PCI-DSS
| # | Questao | Responsavel Sugerido |
|---|---------|---------------------|
| 13 | O canal web processara dados de cartao (PAN)? | Produto / Compliance |
| 14 | Se sim, qual o nivel de conformidade PCI-DSS requerido? | Compliance |
| 15 | Ha tokenizacao de dados de cartao? | Arquitetura |

#### Banco de Portugal
| # | Questao | Responsavel Sugerido |
|---|---------|---------------------|
| 16 | Quais requisitos regulatorios especificos do BdP se aplicam? | Compliance |
| 17 | Ha requisitos de reporte ao BdP? | Compliance |

#### Registo de Auditoria
| # | Questao | Responsavel Sugerido |
|---|---------|---------------------|
| 18 | Quais eventos devem ser registados para auditoria? | Compliance / Seguranca |
| 19 | Qual o formato do log de auditoria? | Arquitetura |
| 20 | Qual o periodo de retencao dos logs de auditoria? | Compliance / Legal |
| 21 | Ha requisitos de imutabilidade dos logs? | Seguranca |

#### Resposta a Incidentes
| # | Questao | Responsavel Sugerido |
|---|---------|---------------------|
| 22 | Existe plano de resposta a incidentes de seguranca? | Seguranca |
| 23 | Quais sao os tempos de resposta definidos (SLAs)? | Seguranca / Operacoes |
| 24 | Ha equipa de resposta a incidentes (CSIRT)? | Seguranca |

#### Gestao de Vulnerabilidades
| # | Questao | Responsavel Sugerido |
|---|---------|---------------------|
| 25 | Qual o processo de gestao de vulnerabilidades? | Seguranca |
| 26 | Quais SLAs para correcao de vulnerabilidades (critica, alta, media, baixa)? | Seguranca |
| 27 | Ha programa de bug bounty? | Seguranca |

#### Segregacao de Ambientes
| # | Questao | Responsavel Sugerido |
|---|---------|---------------------|
| 28 | Como serao segregados os ambientes (dev, staging, prod)? | Infraestrutura |
| 29 | Ha requisitos de segregacao de dados entre ambientes? | Seguranca |

---

## Secao 9 - Integracao & Interfaces Externas

### DEF-09: Integracao & Interfaces Externas

#### Terceiros - KYC/AML
| # | Questao | Responsavel Sugerido |
|---|---------|---------------------|
| 1 | O canal web tera fluxos de onboarding que requerem KYC? | Produto |
| 2 | Ha verificacoes AML em tempo real para transacoes? | Compliance |

#### Terceiros - Cartoes
| # | Questao | Responsavel Sugerido |
|---|---------|---------------------|
| 3 | Qual provider de cartoes e utilizado (emissao, processamento)? | Produto |
| 4 | Ha integracao com 3D Secure para pagamentos online? | Produto / Seguranca |

#### Open Banking PSD2
| # | Questao | Responsavel Sugerido |
|---|---------|---------------------|
| 5 | O banco expoe APIs de Open Banking (AISP, PISP)? | Arquitetura |
| 6 | O canal web consumira APIs de Open Banking de outros bancos? | Produto |
| 7 | Existe plataforma de gestao de consentimentos? | Arquitetura |
| 8 | Qual o modelo de autorizacao para Open Banking (OAuth 2.0, OIDC)? | Arquitetura |

#### Message Broker
| # | Questao | Responsavel Sugerido |
|---|---------|---------------------|
| 9 | Qual tecnologia de Message Broker e utilizada (RabbitMQ, Kafka, Azure Service Bus)? | Infraestrutura |
| 10 | Quais eventos sao publicados/consumidos pelo canal web? | Arquitetura |
| 11 | Ha requisitos de ordenacao ou exactly-once delivery? | Arquitetura |
| 12 | Qual a estrategia de dead-letter para mensagens falhadas? | Arquitetura |

#### Tratamento de Erros
| # | Questao | Responsavel Sugerido |
|---|---------|---------------------|
| 13 | Quais integracoes tem fallback definido? | Arquitetura |

#### SLAs de Integracao
| # | Questao | Responsavel Sugerido |
|---|---------|---------------------|
| 14 | Quais sao os SLAs de disponibilidade dos sistemas integrados? | Infraestrutura |
| 15 | Quais sao os tempos de resposta esperados (P50, P95, P99)? | Arquitetura |
| 16 | Ha janelas de manutencao programadas que afetam integracoes? | Operacoes |

#### API Management
| # | Questao | Responsavel Sugerido |
|---|---------|---------------------|
| 17 | Como e feito o rate limiting por integracao? | Infraestrutura |
| 18 | Ha throttling diferenciado por tipo de operacao? | Arquitetura |
| 19 | Como e feito o monitoring de APIs? | Operacoes |

#### Catalogo de Integracoes
| # | Questao | Responsavel Sugerido |
|---|---------|---------------------|
| 20 | Existe catalogo de APIs/servicos documentado? | Arquitetura |
| 21 | Qual ferramenta e usada para documentacao de APIs (Swagger UI, Redoc)? | Arquitetura |
| 22 | Ha ambiente de sandbox para testes de integracao? | Infraestrutura |

---

## Secao 10 - Arquitetura Operacional

### DEF-10: Arquitetura Operacional

#### Infraestrutura
| # | Questao | Responsavel Sugerido |
|---|---------|---------------------|
| 1 | Quantos clusters OpenShift existem (producao, DR)? | Infraestrutura |
| 2 | Qual a topologia de rede (DMZ, zonas de seguranca)? | Infraestrutura |

#### Ambientes
| # | Questao | Responsavel Sugerido |
|---|---------|---------------------|
| 3 | Qual a estrategia de promocao entre ambientes? | DevOps |

#### Segregacao
| # | Questao | Responsavel Sugerido |
|---|---------|---------------------|
| 4 | Ha segregacao de rede entre ambientes? | Infraestrutura |
| 5 | Quais controlos de acesso existem por ambiente? | Seguranca |

#### Estrategia de Deploy
| # | Questao | Responsavel Sugerido |
|---|---------|---------------------|
| 6 | Qual a janela de deploy para producao? | Operacoes |
| 7 | Ha deploys automaticos ou requerem aprovacao manual? | DevOps |
| 8 | Qual o tempo maximo de downtime aceitavel durante deploy? | Operacoes |

#### Infraestrutura como Codigo (IaC)
| # | Questao | Responsavel Sugerido |
|---|---------|---------------------|
| 9 | Qual ferramenta de IaC e utilizada (Terraform, Ansible, Helm)? | Infraestrutura |
| 10 | Como sao geridos os templates/charts? | Infraestrutura |
| 11 | Ha versionamento de infraestrutura? | Infraestrutura |

#### Secrets Management
| # | Questao | Responsavel Sugerido |
|---|---------|---------------------|
| 12 | Qual a politica de rotacao de secrets? | Seguranca |

#### Container Registry
| # | Questao | Responsavel Sugerido |
|---|---------|---------------------|
| 13 | Ha scanning de vulnerabilidades nas imagens? | DevSecOps |
| 14 | Qual a politica de retencao de imagens? | Infraestrutura |

#### Disaster Recovery
| # | Questao | Responsavel Sugerido |
|---|---------|---------------------|
| 15 | Qual o RTO (Recovery Time Objective)? | Infraestrutura |
| 16 | Qual o RPO (Recovery Point Objective)? | Infraestrutura |
| 17 | Ha site de DR? Onde? | Infraestrutura |
| 18 | Qual a estrategia de failover (automatico, manual)? | Infraestrutura |
| 19 | Com que frequencia sao testados os procedimentos de DR? | Infraestrutura |

#### Runbooks
| # | Questao | Responsavel Sugerido |
|---|---------|---------------------|
| 20 | Existem runbooks documentados para operacoes comuns? | Operacoes |
| 21 | Ha runbooks para incidentes de seguranca? | Seguranca |
| 22 | Como sao mantidos e versionados os runbooks? | Operacoes |

---

## Secao 11 - Observabilidade & Operacoes

### DEF-11: Observabilidade & Operacoes

#### Stack de Observabilidade
| # | Questao | Responsavel Sugerido |
|---|---------|---------------------|
| 1 | A stack ELK existente sera reutilizada ou ha instancia dedicada? | Infraestrutura |
| 2 | Ha complemento com Prometheus/Grafana para metricas? | Infraestrutura |
| 3 | Qual a versao do ELK Stack utilizada? | Infraestrutura |

#### Golden Signals
| # | Questao | Responsavel Sugerido |
|---|---------|---------------------|
| 4 | Quais metricas golden signals serao monitorizadas? | Arquitetura |
| 5 | Quais sao os thresholds aceitaveis para cada signal? | Arquitetura / SRE |

#### Metricas de Aplicacao
| # | Questao | Responsavel Sugerido |
|---|---------|---------------------|
| 6 | Quais metricas de aplicacao serao capturadas no Frontend? | Arquitetura |
| 7 | Quais metricas de aplicacao serao capturadas no BFF? | Arquitetura |
| 8 | Ha requisitos de metricas customizadas? | Arquitetura |

#### Metricas de Negocio
| # | Questao | Responsavel Sugerido |
|---|---------|---------------------|
| 9 | Quais metricas de negocio devem ser capturadas? | Produto |
| 10 | Ha dashboards de negocio requeridos? | Produto |

#### Distributed Tracing
| # | Questao | Responsavel Sugerido |
|---|---------|---------------------|
| 11 | Sera implementado tracing distribuido? | Arquitetura |
| 12 | Qual ferramenta de tracing (Jaeger, Zipkin, Application Insights)? | Arquitetura |
| 13 | Como sera feita a correlacao entre Frontend e BFF? | Arquitetura |

#### Logging Centralizado
| # | Questao | Responsavel Sugerido |
|---|---------|---------------------|
| 14 | Qual o formato de logs (JSON estruturado, texto)? | Arquitetura |
| 15 | Quais campos sao obrigatorios em cada log entry? | Arquitetura |
| 16 | Qual a politica de retencao de logs? | Compliance |
| 17 | Ha requisitos de mascaramento de dados sensiveis nos logs? | Seguranca |

#### SLIs/SLOs/SLAs
| # | Questao | Responsavel Sugerido |
|---|---------|---------------------|
| 18 | Quais SLIs serao definidos para o HomeBanking Web? | Arquitetura / SRE |
| 19 | Como serao medidos os SLIs? | SRE |
| 20 | Quais sao os SLOs target (disponibilidade, latencia, erro)? | Arquitetura / Cliente |
| 21 | Ha error budget definido? | Arquitetura |
| 22 | Existem SLAs contratuais para o HomeBanking Web? | Comercial / Legal |
| 23 | Quais sao as penalidades por incumprimento de SLA? | Legal |

#### Alertas
| # | Questao | Responsavel Sugerido |
|---|---------|---------------------|
| 24 | Quais alertas serao configurados? | SRE / Operacoes |
| 25 | Qual a ferramenta de alerting (PagerDuty, OpsGenie, Email)? | Infraestrutura |
| 26 | Quais sao os niveis de severidade dos alertas? | Operacoes |
| 27 | Qual a politica de escalacao? | Operacoes |

#### Dashboards Operacionais
| # | Questao | Responsavel Sugerido |
|---|---------|---------------------|
| 28 | Quais dashboards operacionais sao necessarios? | Operacoes |
| 29 | Quem tem acesso aos dashboards? | Operacoes / Seguranca |
| 30 | Ha requisitos de dashboards em tempo real? | Operacoes |

---

## Secao 12 - Desempenho & Fiabilidade

### DEF-12: Desempenho & Fiabilidade

#### Objetivos de Carga
| # | Questao | Responsavel Sugerido |
|---|---------|---------------------|
| 1 | Ha picos de utilizacao previstos? Quando? | Produto |

#### Targets de Performance
| # | Questao | Responsavel Sugerido |
|---|---------|---------------------|
| 2 | Quais metricas Core Web Vitals devem ser atingidas? | Arquitetura |
| 3 | Qual o time to first byte (TTFB) target? | Arquitetura |

#### Caching Strategy
| # | Questao | Responsavel Sugerido |
|---|---------|---------------------|
| 4 | Quais dados podem ser cached no cliente (browser)? | Arquitetura |
| 5 | Qual a estrategia de cache no BFF? | Arquitetura |
| 6 | Sera utilizado Redis para cache? Qual TTL? | Arquitetura |
| 7 | Ha requisitos de invalidacao de cache? | Arquitetura |

#### Otimizacao Frontend
| # | Questao | Responsavel Sugerido |
|---|---------|---------------------|
| 8 | Sera utilizado lazy loading de componentes? | Frontend |
| 9 | Sera utilizado code splitting? | Frontend |
| 10 | Ha requisitos de bundle size maximo? | Arquitetura |
| 11 | Sera utilizado Service Worker para cache? | Frontend |

#### Otimizacao Backend
| # | Questao | Responsavel Sugerido |
|---|---------|---------------------|
| 12 | Sera utilizado connection pooling? Qual o tamanho? | Arquitetura |
| 13 | Ha limites de payload nas APIs? | Arquitetura |
| 14 | Sera utilizado compressao (gzip/brotli)? | Arquitetura |
| 15 | Ha requisitos de paginacao nas listagens? | Arquitetura |

#### Auto-scaling
| # | Questao | Responsavel Sugerido |
|---|---------|---------------------|
| 16 | Sera configurado Horizontal Pod Autoscaler (HPA)? | Infraestrutura |
| 17 | Quais metricas disparam o auto-scaling? | Infraestrutura |
| 18 | Quais os limites minimo e maximo de replicas? | Infraestrutura |
| 19 | Qual o cooldown period apos scale down? | Infraestrutura |

#### Capacity Planning
| # | Questao | Responsavel Sugerido |
|---|---------|---------------------|
| 20 | Qual o resource request para CPU/Memoria? | Infraestrutura |
| 21 | Qual o resource limit para CPU/Memoria? | Infraestrutura |
| 22 | Ha requirements de burst capacity? | Infraestrutura |

#### Failover & Resiliencia
| # | Questao | Responsavel Sugerido |
|---|---------|---------------------|
| 23 | Qual a estrategia de failover entre pods? | Infraestrutura |
| 24 | Ha Pod Disruption Budget configurado? | Infraestrutura |

#### Load Testing
| # | Questao | Responsavel Sugerido |
|---|---------|---------------------|
| 25 | Qual a ferramenta de load testing a utilizar? | QA |
| 26 | Qual a frequencia de execucao dos load tests? | QA |
| 27 | Quais cenarios serao testados? | QA |
| 28 | Quais sao os criterios de aceitacao do load test? | Arquitetura / QA |

---

## Secao 13 - Estrategia de Testes

### DEF-13: Estrategia de Testes

#### Testes Unitarios
| # | Questao | Responsavel Sugerido |
|---|---------|---------------------|
| 1 | Qual o framework de testes unitarios para o Frontend? | Arquitetura |
| 2 | Qual o framework de testes unitarios para o BFF? | Arquitetura |
| 3 | Qual a cobertura de codigo minima requerida? | Arquitetura / QA |
| 4 | Os testes unitarios bloqueiam o pipeline se falharem? | DevOps |

#### Testes de Integracao
| # | Questao | Responsavel Sugerido |
|---|---------|---------------------|
| 5 | Qual o framework de testes de integracao? | Arquitetura |
| 6 | Como sao mockados os servicos externos? | QA |
| 7 | Ha ambiente dedicado para testes de integracao? | Infraestrutura |

#### Testes de Contrato
| # | Questao | Responsavel Sugerido |
|---|---------|---------------------|
| 8 | Sera utilizado contract testing (ex: Pact)? | Arquitetura |
| 9 | Quem e responsavel por manter os contratos? | Arquitetura |
| 10 | Como sao validados os contratos com Backend API? | Arquitetura |

#### Testes E2E
| # | Questao | Responsavel Sugerido |
|---|---------|---------------------|
| 11 | Qual o framework de testes E2E (Cypress, Playwright)? | QA |
| 12 | Quais cenarios criticos serao cobertos? | QA / Produto |
| 13 | Os testes E2E executam em que ambiente? | QA |
| 14 | Os testes E2E bloqueiam o pipeline? | DevOps |

#### Testes de Performance
| # | Questao | Responsavel Sugerido |
|---|---------|---------------------|
| 15 | Qual a ferramenta de testes de performance? | QA |
| 16 | Quais cenarios de carga serao testados? | QA |
| 17 | Quando sao executados os testes de performance? | QA |

#### Testes de Seguranca
| # | Questao | Responsavel Sugerido |
|---|---------|---------------------|
| 18 | Quais ferramentas SAST sao utilizadas? | DevSecOps |
| 19 | Quais ferramentas DAST sao utilizadas? | DevSecOps |
| 20 | Ha penetration testing periodico? | Seguranca |
| 21 | Como sao geridos os findings de seguranca? | Seguranca |

#### Testes de Acessibilidade
| # | Questao | Responsavel Sugerido |
|---|---------|---------------------|
| 22 | Quais guidelines de acessibilidade (WCAG)? | UX |
| 23 | Quais ferramentas de teste de acessibilidade? | QA |
| 24 | Ha testes automatizados de acessibilidade? | QA |

#### Test Data Management
| # | Questao | Responsavel Sugerido |
|---|---------|---------------------|
| 25 | Como sao geridos os dados de teste? | QA |
| 26 | Ha ambiente com dados anonimizados de producao? | QA / DPO |
| 27 | Como sao criados os fixtures de teste? | QA |

#### Testes de Regressao
| # | Questao | Responsavel Sugerido |
|---|---------|---------------------|
| 28 | Qual a estrategia de smoke tests? | QA |
| 29 | Qual a frequencia de execucao da regressao? | QA |

#### Testes de Aceitacao
| # | Questao | Responsavel Sugerido |
|---|---------|---------------------|
| 30 | Quem executa os testes de aceitacao? | QA / Cliente |
| 31 | Ha ambiente UAT dedicado? | Infraestrutura |
| 32 | Quais os criterios de aceitacao? | Produto |

#### Matriz de Responsabilidades
| # | Questao | Responsavel Sugerido |
|---|---------|---------------------|
| 33 | Quem e responsavel por cada tipo de teste? | PM |
| 34 | Qual o processo de report de bugs? | QA |

---

## Secao 14 - Plano de Migracao & Implementacao

### DEF-14: Plano de Migracao & Implementacao

#### Roadmap de Implementacao
| # | Questao | Responsavel Sugerido |
|---|---------|---------------------|
| 1 | Qual a data prevista para go-live? | PM / Cliente |
| 2 | Quais as fases de implementacao? | PM |
| 3 | Ha MVP definido? Quais funcionalidades? | Produto |
| 4 | Ha dependencias externas que afetam o roadmap? | PM |

#### Estrategia de Cutover
| # | Questao | Responsavel Sugerido |
|---|---------|---------------------|
| 5 | Qual a estrategia de cutover (big bang, phased, parallel)? | Arquitetura / Operacoes |
| 6 | Ha janela de cutover definida? | Operacoes |
| 7 | Qual o tempo estimado de cutover? | Operacoes |

#### Coexistencia com Legado
| # | Questao | Responsavel Sugerido |
|---|---------|---------------------|
| 8 | Ha sistema HomeBanking web legado a substituir? | Cliente |
| 9 | Se sim, qual a estrategia de coexistencia? | Arquitetura |
| 10 | Qual o periodo de transicao? | PM |
| 11 | Ha URLs a manter para retrocompatibilidade? | Arquitetura |

#### Migracao de Dados
| # | Questao | Responsavel Sugerido |
|---|---------|---------------------|
| 12 | Ha dados a migrar de sistemas legados? | Arquitetura |
| 13 | Quais dados necessitam migracao? | Arquitetura |
| 14 | Qual a estrategia de migracao de dados? | Arquitetura |
| 15 | Ha validacao pos-migracao? | QA |

#### Criterios Go/No-Go
| # | Questao | Responsavel Sugerido |
|---|---------|---------------------|
| 16 | Quais os criterios funcionais para go-live? | Produto |
| 17 | Quais os criterios nao funcionais para go-live? | Arquitetura |
| 18 | Quais os criterios de seguranca para go-live? | Seguranca |
| 19 | Quem aprova o go-live? | Cliente / PM |

#### Procedimentos de Rollback
| # | Questao | Responsavel Sugerido |
|---|---------|---------------------|
| 20 | Qual a estrategia de rollback? | Operacoes |
| 21 | Qual o tempo maximo para decisao de rollback? | Operacoes |
| 22 | Ha runbook de rollback documentado? | Operacoes |

#### Plano de Comunicacao
| # | Questao | Responsavel Sugerido |
|---|---------|---------------------|
| 23 | Como serao comunicadas as mudancas aos utilizadores? | Marketing / PM |
| 24 | Ha campanha de awareness pre-lancamento? | Marketing |
| 25 | Quais os canais de comunicacao (email, in-app, SMS)? | Marketing |

#### Formacao
| # | Questao | Responsavel Sugerido |
|---|---------|---------------------|
| 26 | Ha formacao para equipas internas? | PM |
| 27 | Ha formacao para utilizadores finais? | PM |
| 28 | Ha documentacao de utilizador? | Produto |

#### Pilot/Beta Testing
| # | Questao | Responsavel Sugerido |
|---|---------|---------------------|
| 29 | Sera realizado pilot/beta testing? | PM / QA |
| 30 | Qual o criterio de selecao de utilizadores beta? | Produto |
| 31 | Qual a duracao do periodo beta? | PM |

#### Hypercare Period
| # | Questao | Responsavel Sugerido |
|---|---------|---------------------|
| 32 | Qual a duracao do periodo de hypercare? | Operacoes |
| 33 | Qual a equipa de suporte durante hypercare? | Operacoes |
| 34 | Quais os SLAs durante hypercare? | Operacoes |

---

## Secao 15 - Governacao & Roadmap

### DEF-15: Governacao & Roadmap

#### Modelo de Governacao
| # | Questao | Responsavel Sugerido |
|---|---------|---------------------|
| 1 | Qual o modelo de governacao do projeto (Agile, SAFe, tradicional)? | PM |
| 2 | Quais os papeis e responsabilidades na governacao? | PM |
| 3 | Qual a frequencia de reunioes de steering? | PM |
| 4 | Quem sao os stakeholders principais? | PM |
| 5 | Como sao escalados os riscos e issues? | PM |

#### Gestao de Decisoes
| # | Questao | Responsavel Sugerido |
|---|---------|---------------------|
| 6 | Qual o processo de tomada de decisao arquitetural? | Arquitetura |
| 7 | Quem aprova decisoes tecnicas? | Arquitetura |
| 8 | Como sao documentadas as decisoes (ADRs)? | Arquitetura |
| 9 | Qual o processo de revisao de decisoes? | Arquitetura |

#### Roadmap de Produto
| # | Questao | Responsavel Sugerido |
|---|---------|---------------------|
| 10 | Qual o roadmap de funcionalidades pos-MVP? | Produto |
| 11 | Qual a frequencia de releases? | PM |
| 12 | Como e priorizado o backlog? | Produto |
| 13 | Ha features planeadas para fases futuras? | Produto |

#### Gestao de Divida Tecnica
| # | Questao | Responsavel Sugerido |
|---|---------|---------------------|
| 14 | Como e identificada a divida tecnica? | Arquitetura |
| 15 | Como e priorizada a divida tecnica? | Arquitetura / Produto |
| 16 | Qual a % de capacidade alocada a divida tecnica? | PM |
| 17 | Quem e responsavel por gerir a divida tecnica? | Arquitetura |

#### Processo de Gestao de Mudanca
| # | Questao | Responsavel Sugerido |
|---|---------|---------------------|
| 18 | Qual o processo de change management? | Operacoes |
| 19 | Quem aprova mudancas em producao? | Operacoes |
| 20 | Qual o lead time minimo para mudancas? | Operacoes |
| 21 | Ha CAB (Change Advisory Board)? | Operacoes |

#### KPIs de Sucesso
| # | Questao | Responsavel Sugerido |
|---|---------|---------------------|
| 22 | Quais os KPIs de negocio do projeto? | Produto |
| 23 | Quais os KPIs tecnicos do projeto? | Arquitetura |
| 24 | Qual a frequencia de revisao de KPIs? | PM |
| 25 | Quem e responsavel pelos KPIs? | PM / Produto |

#### Continuous Improvement
| # | Questao | Responsavel Sugerido |
|---|---------|---------------------|
| 26 | Qual o processo de retrospetivas? | Scrum Master |
| 27 | Como sao implementadas as melhorias? | PM |
| 28 | Ha processo de lessons learned? | PM |
| 29 | Como e medida a maturidade do processo? | PM |

---

## Resumo por Area

| Area | Total de Questoes |
|------|-------------------|
| Seguranca / Compliance | ~45 |
| Infraestrutura / Operacoes | ~40 |
| Arquitetura | ~35 |
| Produto / UX | ~20 |
| QA / Testes | ~25 |
| PM / Governacao | ~25 |
| DPO / Legal | ~15 |
| **TOTAL** | **~205** |

---

## Proximos Passos

1. Agendar sessoes de levantamento por area
2. Priorizar questoes criticas para o MVP
3. Documentar respostas nos ficheiros DEF correspondentes
4. Atualizar secoes (SEC) com informacao consolidada
5. Validar decisoes arquiteturais pendentes
