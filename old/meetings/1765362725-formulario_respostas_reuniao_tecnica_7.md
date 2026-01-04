---
id: 1765362725-formulario_respostas_reuniao_tecnica_7
aliases:
  - Questionário Técnico - Projeto Home Banking Web
tags:
  - nextreality-novobanco-website-meetings
  - questionario
  - questionario-tecnico
  - formulario
approved: true
created: 2025-12-10
due: 2025-12-31
end: unknown-due
hubs:
  - "[[nextreality]]"
para-code: R
reviewed: true
start: unknown-start
---
# Questionário Técnico - Projeto Home Banking Web

**Projeto:** Plataforma Web de Homebanking  
**Data da Reunião:** ___/___/______  
**Participantes:** _________________________________________________  
**Responsável pelo Preenchimento:** _________________________________

---

## Instruções de Preenchimento

- Marque os checkboxes com `[x]` quando confirmado
- Preencha os campos `___` com as respostas obtidas
- Use a coluna "Notas" para observações adicionais
- Itens marcados com ⚠️ são críticos/bloqueadores
- Itens marcados com 📋 requerem documentação adicional

---

# Parte 1: Infraestrutura

## 1.1 Cloud e Hosting

### Decisões Fundamentais

| Questão | Resposta | Notas |
|---------|----------|-------|
| Cloud Provider | [ ] AWS  [X] Azure  [ ] GCP  [ ] Híbrido  [ ] On-premises | |
| Modelo de Deployment | [ ] Kubernetes  [ ] VMs  [ ] Serverless  [ ] Containers (não-K8s) | |
| Região Principal | ___________________________________ | |
| Região DR (se aplicável) | ___________________________________ | |

### Kubernetes (se aplicável)

- [ ] Cluster já existe
- [ ] Cluster será criado para o projeto
- [ ] Managed (EKS/AKS/GKE) vs Self-hosted: _______________

| Configuração | Valor/Decisão | Notas |
|--------------|---------------|-------|
| Versão K8s | _______________ | |
| Namespaces por ambiente | [ ] Sim  [ ] Não - VPCs separadas | |
| Service Mesh | [ ] Istio  [ ] Linkerd  [ ] Não necessário | |
| Ingress Controller | [ ] NGINX  [ ] Traefik  [ ] Cloud-native | |

### Ambientes

| Ambiente | Existe? | Configuração | Responsável |
|----------|---------|--------------|-------------|
| DEV | [ ] Sim  [ ] Não | _____________ | _____________ |
| UAT | [ ] Sim  [ ] Não | _____________ | _____________ |
| PREPROD/Staging | [ ] Sim  [ ] Não | _____________ | _____________ |
| PROD | [ ] Sim  [ ] Não | _____________ | _____________ |

**Segregação entre ambientes:**
- [ ] Namespaces K8s diferentes
- [ ] VPCs/VNets separadas
- [ ] Clusters separados
- [ ] Subscriptions/Accounts separadas

---

## 1.2 API Gateway

⚠️ **Crítico para compliance PSD2**

| Questão | Resposta | Notas |
|---------|----------|-------|
| Solução atual | [ ] Kong  [ ] Apigee  [ ] AWS API GW  [ ] Azure APIM  [ ] Outro: _______ | |
| Rate Limiting disponível | [ ] Sim  [ ] Não  [ ] Parcial | |
| Throttling configurável por endpoint | [ ] Sim  [ ] Não | |
| Suporta OAuth 2.0/OIDC | [ ] Sim  [ ] Não | |
| WAF integrado | [ ] Sim  [ ] Não  [ ] Separado: _______ | |

**Configurações de Rate Limiting atuais:**
```
Requests por segundo (global): _______________
Requests por minuto (por user): _______________
Requests por minuto (por IP): _______________
```

---

## 1.3 Disaster Recovery e Alta Disponibilidade

| Métrica | Target Definido | Atual (se existir) | Notas |
|---------|-----------------|-------------------|-------|
| RTO (Recovery Time Objective) | _______ horas | _______ | |
| RPO (Recovery Point Objective) | _______ minutos | _______ | |
| Disponibilidade Target | _______ % | _______ % | |

**Estratégia de DR:**
- [ ] Multi-AZ (mesma região)
- [ ] Multi-Region (regiões diferentes)
- [ ] Active-Active
- [ ] Active-Passive
- [ ] Cold standby

**Testes de DR:**
- [ ] Já realizados periodicamente - Frequência: _______________
- [ ] Não realizados - Planeado para: _______________
- [ ] Não definido

---

## 1.4 Redes e Segurança de Infraestrutura

| Componente | Existe? | Solução | Notas |
|------------|---------|---------|-------|
| Load Balancer | [ ] Sim  [ ] Não | _______________ | |
| WAF | [ ] Sim  [ ] Não | _______________ | |
| DDoS Protection | [ ] Sim  [ ] Não | _______________ | |
| IDS/IPS | [ ] Sim  [ ] Não | _______________ | |
| VPN/Private Link | [ ] Sim  [ ] Não | _______________ | |

**Network Policies:**
- [ ] Definidas e implementadas
- [ ] Em desenvolvimento
- [ ] Não definidas

---

# Parte 2: Engenharia de Software e DevOps

## 2.1 CI/CD Pipeline

### Ferramentas

| Componente | Ferramenta Homologada | Alternativa Permitida |
|------------|----------------------|----------------------|
| Source Control | [ ] GitLab  [ ] GitHub  [ ] Azure DevOps  [ ] Bitbucket | |
| CI/CD | [ ] GitLab CI  [ ] GitHub Actions  [ ] Jenkins  [ ] Azure Pipelines | |
| Artifact Registry | _______________ | |
| Container Registry | _______________ | |

### Estratégia de Branching

- [ ] GitFlow
- [ ] Trunk-based Development
- [ ] GitHub Flow
- [ ] Outro: _______________

**Branch Protection Rules:**
- [ ] PR obrigatório para main/master
- [ ] Aprovações mínimas: ___
- [ ] Build obrigatório passar
- [ ] Testes obrigatórios passar
- [ ] Code review obrigatório

### Quality Gates

| Gate | Obrigatório? | Threshold | Ferramenta |
|------|--------------|-----------|------------|
| Unit Tests | [ ] Sim  [ ] Não | Cobertura mín: ___% | _______________ |
| Integration Tests | [ ] Sim  [ ] Não | Cobertura mín: ___% | _______________ |
| SAST (Security Static) | [ ] Sim  [ ] Não | _______________ | [ ] SonarQube  [ ] Checkmarx  [ ] Outro |
| DAST (Security Dynamic) | [ ] Sim  [ ] Não | _______________ | [ ] OWASP ZAP  [ ] Burp  [ ] Outro |
| Dependency Scanning | [ ] Sim  [ ] Não | _______________ | [ ] Snyk  [ ] Dependabot  [ ] Outro |
| Container Scanning | [ ] Sim  [ ] Não | _______________ | [ ] Trivy  [ ] Snyk  [ ] Outro |
| Linting | [ ] Sim  [ ] Não | _______________ | _______________ |

### Deploy Strategy

**Estratégia para Produção:**
- [ ] Blue-Green Deployment
- [ ] Canary Releases
- [ ] Rolling Update
- [ ] Feature Flags - Ferramenta: _______________
- [ ] Outro: _______________

**Rollback:**
- [ ] Automático em caso de falha
- [ ] Manual com aprovação
- [ ] Tempo máximo para rollback: _______________ minutos

---

## 2.2 Governação de Código

### Code Review

| Aspecto | Definição |
|---------|-----------|
| Aprovadores mínimos | ___ pessoa(s) |
| Tempo máximo para review | ___ horas/dias |
| Checklist de review existe? | [ ] Sim  [ ] Não |
| Automated review tools | _______________ |

### Architecture Decision Records (ADRs)

- [ ] Template definido
- [ ] Repositório para ADRs: _______________
- [ ] Processo de aprovação definido
- [ ] Não utilizado atualmente

### Boards e Gestão

| Aspecto | Ferramenta | Notas |
|---------|------------|-------|
| Architecture Review Board (ARB) | [ ] Existe  [ ] Não existe | Cadência: _______________ |
| Change Advisory Board (CAB) | [ ] Existe  [ ] Não existe | Cadência: _______________ |
| Tool de gestão de projeto | _______________ | |

---

## 2.3 Secrets Management

| Questão | Resposta |
|---------|----------|
| Solução | [ ] HashiCorp Vault  [ ] AWS Secrets Manager  [ ] Azure Key Vault  [ ] Outro: _______ |
| Rotação automática | [ ] Sim  [ ] Não  [ ] Parcial |
| Secrets por ambiente | [ ] Segregados  [ ] Compartilhados (⚠️ risco) |
| Acesso via | [ ] API  [ ] Sidecar  [ ] Init container  [ ] Env vars |

---

# Parte 3: Arquitetura Aplicacional

## 3.1 Frontend (React SPA)

### Stack Tecnológico

| Componente | Decisão | Alternativa | Notas |
|------------|---------|-------------|-------|
| Framework | React (definido) | | Versão: ___ |
| State Management | [ ] Redux  [ ] Zustand  [ ] Recoil  [ ] Context API  [ ] React Query | | |
| HTTP Client | [ ] Axios  [ ] Fetch  [ ] React Query  [ ] SWR | | |
| Routing | [ ] React Router v6  [ ] Outro: _______ | | |
| UI Components | [ ] MUI  [ ] Ant Design  [ ] Chakra  [ ] Custom  [ ] Outro: _______ | | |
| Form Handling | [ ] React Hook Form  [ ] Formik  [ ] Outro: _______ | | |
| Bundler | [ ] Vite  [ ] Webpack  [ ] Outro: _______ | | |
| Testing | [ ] Jest  [ ] Vitest  [ ] React Testing Library | | |
| E2E Testing | [ ] Cypress  [ ] Playwright  [ ] Outro: _______ | | |

### Design System

- [ ] Existe design system corporativo - Nome: _______________
- [ ] Será criado para o projeto
- [ ] Usar library externa sem customização

📋 **Documentação necessária:**
- [ ] Storybook ou similar
- [ ] Style guide
- [ ] Brand guidelines

### Performance Targets

| Métrica | Target | Notas |
|---------|--------|-------|
| Initial Bundle Size | < ___ KB | |
| Largest Contentful Paint (LCP) | < ___ s | |
| First Input Delay (FID) | < ___ ms | |
| Cumulative Layout Shift (CLS) | < ___ | |
| Time to Interactive (TTI) | < ___ s | |

### Segurança Frontend

| Aspecto | Implementação |
|---------|---------------|
| Token Storage | [ ] Memory only  [ ] sessionStorage  [ ] httpOnly cookies |
| CSP Headers | [ ] Definidos  [ ] A definir |
| XSS Protection | [ ] DOMPurify  [ ] Outro: _______ |
| CSRF Protection | [ ] Tokens  [ ] SameSite cookies  [ ] Outro |

### PWA / Offline

- [ ] PWA é requisito para MVP
- [ ] PWA para fases futuras
- [ ] Não é requisito
- [ ] Service Workers para cache de assets apenas

---

## 3.2 Backend (C# BFF)

### Stack Tecnológico

| Componente | Decisão | Notas |
|------------|---------|-------|
| .NET Version | [ ] .NET 6 (LTS)  [ ] .NET 7  [ ] .NET 8 (LTS) | |
| API Style | [ ] Controllers  [ ] Minimal APIs  [ ] Híbrido | |
| ORM | [ ] EF Core  [ ] Dapper  [ ] Outro: _______ | |
| Validation | [ ] FluentValidation  [ ] DataAnnotations  [ ] Outro | |
| Mediator | [ ] MediatR  [ ] Não usar | |
| Logging | [ ] Serilog  [ ] NLog  [ ] Microsoft.Extensions.Logging | |
| HTTP Client | [ ] HttpClientFactory + Polly  [ ] Refit  [ ] Outro | |

### Padrões Arquiteturais

**Arquitetura Escolhida:**
- [ ] Clean Architecture
- [ ] Onion Architecture
- [ ] Vertical Slice Architecture
- [ ] N-Layer tradicional
- [ ] Outro: _______________

**Padrões de Design a Utilizar:**
- [ ] Repository Pattern
- [ ] Unit of Work
- [ ] CQRS (Command Query Responsibility Segregation)
- [ ] Mediator Pattern
- [ ] Factory Pattern
- [ ] Strategy Pattern
- [ ] Decorator Pattern

### Resiliência

| Padrão | Implementar? | Configuração |
|--------|--------------|--------------|
| Circuit Breaker | [ ] Sim  [ ] Não | Threshold: ___ falhas em ___ segundos |
| Retry Policy | [ ] Sim  [ ] Não | Max retries: ___, Backoff: [ ] Exponential  [ ] Linear |
| Timeout | [ ] Sim  [ ] Não | Default: ___ segundos |
| Bulkhead | [ ] Sim  [ ] Não | Max concurrent: ___ |
| Fallback | [ ] Sim  [ ] Não | Estratégia: _______________ |

### Error Handling

| Aspecto | Decisão |
|---------|---------|
| Error Response Format | [ ] Problem Details (RFC 7807)  [ ] Custom  [ ] Outro |
| Error Codes Catalog | [ ] A criar  [ ] Existe: _______________ |
| Exception Handling | [ ] Global middleware  [ ] Por controller  [ ] Híbrido |

---

## 3.3 Persistência de Sessões

⚠️ **Crítico para segurança**

| Questão | Decisão | Notas |
|---------|---------|-------|
| Sessões armazenadas em | [ ] Redis  [ ] Database  [ ] Memory (⚠️ não recomendado para prod) | |
| Timeout de inatividade | ___ minutos | |
| Timeout absoluto | ___ minutos | |
| Multi-device | [ ] Permitido  [ ] Single device only | |
| Sliding expiration | [ ] Sim  [ ] Não | |

**Dados na Sessão:**
```
[ ] User ID
[ ] Device ID
[ ] Access Token
[ ] Refresh Token
[ ] IP Address
[ ] User Agent
[ ] Last Activity Timestamp
[ ] Permissions/Roles
[ ] Outros: _______________
```

**Sincronização entre tabs:**
- [ ] BroadcastChannel API
- [ ] localStorage events
- [ ] Não necessário
- [ ] Outro: _______________

---

# Parte 4: Integrações

## 4.1 Sistemas Externos - Mapeamento

⚠️ **Gap identificado nos documentos - necessita esclarecimento**

### Siebel (Core Banking)

| Aspecto | Resposta |
|---------|----------|
| Protocolo | [ ] REST  [ ] SOAP  [ ] Proprietário  [ ] Outro: _______ |
| Formato de dados | [ ] JSON  [ ] XML  [ ] Outro: _______ |
| Autenticação | [ ] API Key  [ ] OAuth  [ ] Certificado  [ ] Outro: _______ |
| Documentação disponível | [ ] Sim - Local: _______________  [ ] Não |
| SLA de disponibilidade | _______ % |
| Timeout recomendado | _______ segundos |
| Rate limits | _______ requests/segundo |

### MBWay

| Aspecto | Resposta |
|---------|----------|
| Componentes via SDK | _______________________________________________ |
| Componentes via API | _______________________________________________ |
| Versão Web disponível | [ ] Sim  [ ] Não  [ ] Parcial |
| Documentação | [ ] Disponível  [ ] A solicitar |

### Outros Sistemas

| Sistema | Protocolo | Formato | Auth | SLA | Timeout | Notas |
|---------|-----------|---------|------|-----|---------|-------|
| BTP | [ ] REST [ ] SOAP [ ] File [ ] MQ | [ ] JSON [ ] XML | _______ | ___% | ___s | |
| VISA | [ ] REST [ ] ISO8583 [ ] Outro | _______ | _______ | ___% | ___s | |
| Firebase | [ ] REST [ ] SDK | [ ] JSON | _______ | ___% | ___s | Push notifications |
| Google Maps | [ ] REST | [ ] JSON | API Key | ___% | ___s | |
| Seguros | [ ] REST [ ] Redirect [ ] Outro | _______ | _______ | ___% | ___s | |
| KYC/AML Provider | _______ | _______ | _______ | ___% | ___s | |
| SMS Gateway | _______ | _______ | _______ | ___% | ___s | Provider: _______ |
| Email Service | _______ | _______ | _______ | ___% | ___s | Provider: _______ |

### Message Broker (se aplicável)

- [ ] Não utilizado atualmente
- [ ] RabbitMQ
- [ ] Apache Kafka
- [ ] Azure Service Bus
- [ ] AWS SQS/SNS
- [ ] NATS
- [ ] Outro: _______________

**Se utilizado:**
| Configuração | Valor |
|--------------|-------|
| Dead Letter Queue | [ ] Configurada  [ ] Não |
| Retry Policy | _______________ |
| Message TTL | _______________ |

---

## 4.2 Idempotência em Operações Financeiras

⚠️ **Crítico para integridade de dados**

- [ ] Idempotency keys implementadas
- [ ] A implementar
- [ ] Não considerado (⚠️ risco)

| Configuração | Valor |
|--------------|-------|
| Header para idempotency key | _______________ (ex: X-Idempotency-Key) |
| Janela de idempotência | _______________ horas |
| Storage de keys | [ ] Redis  [ ] Database  [ ] Outro |
| Operações cobertas | [ ] Todas financeiras  [ ] Apenas transferências  [ ] Lista: _______________ |

---

# Parte 5: Autenticação e Autorização

## 5.1 Fluxo de Autenticação

### OAuth / Token Flow

| Aspecto | Decisão | Notas |
|---------|---------|-------|
| Flow Type | [ ] Authorization Code + PKCE  [ ] Implicit (⚠️ deprecated)  [ ] Custom | |
| Token Type | [ ] JWT  [ ] Opaque + Session Store  [ ] Híbrido | |
| Access Token Lifetime | ___ minutos | |
| Refresh Token Lifetime | ___ dias | |
| Refresh Token Rotation | [ ] Sim  [ ] Não | |

📋 **Documentação necessária:** Detalhar customizações proprietárias mencionadas nos documentos

**Customizações OAuth Atuais (APP Mobile):**
```
_______________________________________________________________________________
_______________________________________________________________________________
_______________________________________________________________________________
```

### Authentication Server

- [ ] Dedicado (standalone)
- [ ] Integrado no BFF
- [ ] Terceiro (Keycloak, Auth0, etc.): _______________

### MFA (Multi-Factor Authentication)

| Método | Suportado? | Obrigatório para |
|--------|------------|------------------|
| TOTP (Authenticator App) | [ ] Sim  [ ] Não | _______________ |
| SMS OTP | [ ] Sim  [ ] Não | _______________ |
| Email OTP | [ ] Sim  [ ] Não | _______________ |
| Biometria (WebAuthn) | [ ] Sim  [ ] Não  [ ] Futuro | _______________ |
| Push Notification | [ ] Sim  [ ] Não | _______________ |

**Triggers para Step-up Authentication:**
- [ ] Transações acima de €___
- [ ] Alteração de dados sensíveis
- [ ] Novo dispositivo
- [ ] Login de localização diferente
- [ ] Outros: _______________

### Device Binding

- [ ] Implementado na APP Mobile
- [ ] Será implementado na Web
- [ ] Não aplicável à Web

**Se implementado:**
| Aspecto | Implementação |
|---------|---------------|
| Device Fingerprint | [ ] Sim - Library: _______________  [ ] Não |
| Max dispositivos por user | ___ |
| Gestão de dispositivos pelo user | [ ] Sim  [ ] Não |

---

## 5.2 Autorização

### RBAC (Role-Based Access Control)

| Role | Descrição | Permissões Principais |
|------|-----------|----------------------|
| _____________ | _____________ | _____________ |
| _____________ | _____________ | _____________ |
| _____________ | _____________ | _____________ |
| _____________ | _____________ | _____________ |

**Matriz RBAC completa:**
- [ ] Existe - Local: _______________
- [ ] A criar

### PSD2 Scopes

- [ ] Implementados para TPPs
- [ ] Não aplicável (sem Open Banking)

---

# Parte 6: Compliance e Regulamentação

## 6.1 PSD2 / SCA

⚠️ **Requisito regulatório obrigatório**

| Requisito | Status | Responsável | Notas |
|-----------|--------|-------------|-------|
| Strong Customer Authentication | [ ] Conforme  [ ] Em progresso  [ ] Não iniciado | | |
| Delegated Authentication | [ ] Implementado  [ ] N/A | | |
| TPP Access (Open Banking) | [ ] Implementado  [ ] N/A  [ ] Planeado | | |
| Transaction Risk Analysis | [ ] Implementado  [ ] N/A | | |
| Dynamic Linking | [ ] Implementado  [ ] Em progresso | | |

📋 **Checklist PSD2 SCA disponível?** [ ] Sim - Local: _______________  [ ] Não - A criar

---

## 6.2 RGPD / GDPR

| Requisito | Status | Responsável | Notas |
|-----------|--------|-------------|-------|
| Privacy by Design | [ ] Implementado  [ ] Em progresso | | |
| DPIA realizada | [ ] Sim  [ ] Não  [ ] Em progresso | | |
| DPO designado | [ ] Sim - Nome: _______________  [ ] Não | | |
| Consent Management | [ ] Implementado  [ ] A implementar | | |
| Direito ao Esquecimento | [ ] Processo definido  [ ] A definir | | |
| Portabilidade de Dados | [ ] Processo definido  [ ] A definir | | |
| Breach Notification | [ ] Processo definido  [ ] A definir | | |

📋 **Documentação RGPD necessária:**
- [ ] DPIA (Data Protection Impact Assessment)
- [ ] Registo de Atividades de Tratamento
- [ ] Políticas de Privacidade
- [ ] Procedimentos de Breach Notification

---

## 6.3 Banco de Portugal

| Aviso/Instrução | Aplicável? | Status | Notas |
|-----------------|------------|--------|-------|
| Aviso 4/2021 (Cibersegurança) | [ ] Sim  [ ] Não | [ ] Conforme  [ ] A verificar | |
| Instrução 8/2021 (Outsourcing) | [ ] Sim  [ ] Não | [ ] Conforme  [ ] A verificar | |
| Outros: _______________ | [ ] Sim  [ ] Não | [ ] Conforme  [ ] A verificar | |

**Departamento de Compliance validou arquitetura?**
- [ ] Sim - Data: ___/___/______
- [ ] Não - Agendar para: ___/___/______
- [ ] Em progresso

---

## 6.4 PCI-DSS (se aplicável)

**Processamento de cartões na plataforma?**
- [ ] Sim - PCI-DSS aplicável
- [ ] Não - Redirect para processador externo
- [ ] Tokenização apenas

Se aplicável:
| Requisito | Status |
|-----------|--------|
| Segmentação de rede | [ ] Conforme  [ ] A implementar |
| Tokenização de PAN | [ ] Conforme  [ ] A implementar |
| Auditoria anual | [ ] Planeada - Data: _______________  [ ] Não planeada |

---

## 6.5 Auditoria e Logs

| Tipo de Log | Retenção | Storage | Notas |
|-------------|----------|---------|-------|
| Logs de Auditoria (ações utilizador) | ___ anos | _______________ | |
| Logs de Auditoria (admin) | ___ anos | _______________ | |
| Logs Técnicos | ___ ano(s) | _______________ | |
| Logs de Segurança | ___ anos | _______________ | |
| Sessões | ___ dias | _______________ | |

**Eventos a auditar obrigatoriamente:**
```
[ ] Login/Logout
[ ] Falhas de autenticação
[ ] Transações financeiras
[ ] Alterações de dados pessoais
[ ] Alterações de limites
[ ] Gestão de beneficiários
[ ] Acesso a dados sensíveis
[ ] Alterações de configuração
[ ] Outros: _______________
```

---

## 6.6 Testes de Segurança

| Teste | Frequência | Último | Próximo | Provider |
|-------|------------|--------|---------|----------|
| Penetration Testing | [ ] Anual  [ ] Semestral  [ ] Outro | ___/___/___ | ___/___/___ | _______________ |
| SAST | [ ] Contínuo  [ ] Release  [ ] Outro | | | _______________ |
| DAST | [ ] Contínuo  [ ] Release  [ ] Outro | | | _______________ |
| Vulnerability Assessment | _______________ | ___/___/___ | ___/___/___ | _______________ |

---

# Parte 7: Observabilidade

## 7.1 Stack de Monitorização

| Componente | Ferramenta | Notas |
|------------|------------|-------|
| Métricas | [ ] Prometheus  [ ] Datadog  [ ] New Relic  [ ] CloudWatch  [ ] Outro: _______ | |
| Dashboards | [ ] Grafana  [ ] Datadog  [ ] CloudWatch  [ ] Outro: _______ | |
| Logs | [ ] ELK  [ ] EFK  [ ] Loki  [ ] CloudWatch  [ ] Splunk  [ ] Outro: _______ | |
| Tracing | [ ] Jaeger  [ ] Tempo  [ ] Zipkin  [ ] X-Ray  [ ] Outro: _______ | |
| APM | [ ] Datadog  [ ] New Relic  [ ] Dynatrace  [ ] Application Insights  [ ] Outro: _______ | |
| Alerting | [ ] PagerDuty  [ ] OpsGenie  [ ] Slack  [ ] Outro: _______ | |

### OpenTelemetry

- [ ] Adotado como standard
- [ ] A avaliar
- [ ] Não utilizado

---

## 7.2 SLIs / SLOs / SLAs

### Service Level Indicators (SLIs)

| Indicador | Target | Medição |
|-----------|--------|---------|
| Disponibilidade | ___% | |
| Latência p50 | ___ ms | |
| Latência p95 | ___ ms | |
| Latência p99 | ___ ms | |
| Taxa de Erro | < ___% | |
| Throughput | ___ TPS | |

### Service Level Objectives (SLOs)

| Serviço | Disponibilidade | Latência p95 | Error Rate |
|---------|-----------------|--------------|------------|
| Login | ___% | ___ ms | < ___% |
| Transferências | ___% | ___ ms | < ___% |
| Consultas | ___% | ___ ms | < ___% |
| Pagamentos | ___% | ___ ms | < ___% |

### Error Budget

- [ ] Definido - Policy: _______________
- [ ] Não definido

---

## 7.3 Alertas Críticos

| Alerta | Threshold | Severidade | Notificação |
|--------|-----------|------------|-------------|
| Error rate elevada | > ___% por ___ min | [ ] Critical  [ ] Warning | |
| Latência elevada | p99 > ___ ms por ___ min | [ ] Critical  [ ] Warning | |
| Falhas auth consecutivas | > ___ em ___ min | [ ] Critical  [ ] Warning | |
| Circuit breaker aberto | Qualquer | [ ] Critical  [ ] Warning | |
| CPU/Memory alta | > ___% por ___ min | [ ] Critical  [ ] Warning | |
| Disk space baixo | < ___% livre | [ ] Critical  [ ] Warning | |
| SSL cert expiring | < ___ dias | [ ] Critical  [ ] Warning | |

---

## 7.4 Logging

| Aspecto | Decisão |
|---------|---------|
| Formato | [ ] JSON estruturado  [ ] Plain text |
| Correlation ID | [ ] Propagado entre serviços  [ ] Apenas interno |
| PII Masking | [ ] Automático  [ ] Manual  [ ] Não implementado (⚠️) |
| Log Levels por ambiente | DEV: ___  UAT: ___  PROD: ___ |

---

# Parte 8: Testes

## 8.1 Estratégia de Testes

| Tipo | Cobertura Target | Framework | Responsável |
|------|------------------|-----------|-------------|
| Unit Tests (Frontend) | ___% | _______________ | Developers |
| Unit Tests (Backend) | ___% | _______________ | Developers |
| Integration Tests | ___% | _______________ | Developers |
| Contract Tests | [ ] Sim  [ ] Não | _______________ | |
| E2E Tests | Jornadas críticas | _______________ | QA |
| Performance Tests | _______________ | _______________ | |
| Security Tests | SAST/DAST | _______________ | DevSecOps |
| Accessibility Tests | WCAG 2.2 AA | _______________ | |

## 8.2 Test Data Management

| Aspecto | Decisão |
|---------|---------|
| Dados de teste | [ ] Sintéticos  [ ] Produção anonimizada  [ ] Híbrido |
| Refresh de dados UAT | [ ] Diário  [ ] Semanal  [ ] Manual |
| Masking/Anonimização | [ ] Automático  [ ] Manual  [ ] Scripts: _______________ |

## 8.3 UAT (User Acceptance Testing)

| Aspecto | Definição |
|---------|-----------|
| Responsável | _______________ |
| Critérios de aceitação | [ ] Definidos  [ ] A definir |
| Test cases documentados | [ ] Sim  [ ] Não |
| Sign-off necessário de | _______________ |

---

# Parte 9: Paridade Web vs Mobile

## 9.1 Features Exclusivas

### Exclusivas Mobile (não disponíveis na Web)

```
[ ] Biometria nativa (Face ID / Touch ID)
[ ] NFC
[ ] Push notifications nativas
[ ] MBWay SDK completo
[ ] Câmara para scan de documentos
[ ] Outros: _______________
```

### Exclusivas Web

```
[ ] Exportação PDF/Excel
[ ] Múltiplas tabs simultâneas
[ ] Atalhos de teclado
[ ] Print-friendly views
[ ] Outros: _______________
```

## 9.2 Funcionalidades a Clarificar

| Feature | Mobile | Web (decisão) | Notas |
|---------|--------|---------------|-------|
| Biometria | Face ID / Touch ID | [ ] WebAuthn  [ ] Não suportado  [ ] Futuro | |
| Push Notifications | Firebase | [ ] Web Push  [ ] Não suportado | |
| MBWay | SDK Nativo | [ ] API only  [ ] Redirect  [ ] N/A | |
| Deep Linking | Universal Links | [ ] URL routes  [ ] N/A | |
| Offline Mode | Sim | [ ] PWA  [ ] Não suportado | |

---

# Parte 10: Performance

## 10.1 Targets de Carga

| Métrica | Target | Pico | Notas |
|---------|--------|------|-------|
| Sessões simultâneas | _______________ | _______________ | |
| Transactions per Second (TPS) | _______________ | _______________ | |
| Requests per Second | _______________ | _______________ | |

## 10.2 Targets de Resposta

| Operação | Target (p95) | Target (p99) |
|----------|--------------|--------------|
| Login | ___ ms | ___ ms |
| Dashboard/Home | ___ ms | ___ ms |
| Consulta saldos | ___ ms | ___ ms |
| Lista movimentos | ___ ms | ___ ms |
| Transferência | ___ ms | ___ ms |
| Pagamento | ___ ms | ___ ms |

## 10.3 Caching Strategy

| Camada | Tecnologia | TTL Default | Dados |
|--------|------------|-------------|-------|
| CDN | _______________ | ___ | Assets estáticos |
| Application Cache | [ ] Redis  [ ] In-memory  [ ] Outro | ___ | _______________ |
| Session Cache | [ ] Redis  [ ] Database | ___ | Sessões |
| Database Cache | [ ] Query cache  [ ] Resultado cache | ___ | _______________ |

## 10.4 Auto-scaling

| Métrica | Threshold Scale-up | Threshold Scale-down | Min Replicas | Max Replicas |
|---------|-------------------|---------------------|--------------|--------------|
| CPU | > ___% | < ___% | ___ | ___ |
| Memory | > ___% | < ___% | ___ | ___ |
| Custom: ___ | ___ | ___ | ___ | ___ |

---

# Parte 11: Base de Dados

## 11.1 Tecnologia

| Tipo | Tecnologia | Versão | Notas |
|------|------------|--------|-------|
| Relacional (principal) | [ ] PostgreSQL  [ ] SQL Server  [ ] Oracle  [ ] MySQL | ___ | |
| Cache | [ ] Redis  [ ] Memcached | ___ | |
| Document Store (se aplicável) | [ ] MongoDB  [ ] CosmosDB  [ ] N/A | ___ | |
| Search (se aplicável) | [ ] Elasticsearch  [ ] OpenSearch  [ ] N/A | ___ | |

## 11.2 Configurações

| Aspecto | Configuração |
|---------|--------------|
| Connection Pool Size | ___ |
| Read Replicas | [ ] Sim - Quantidade: ___  [ ] Não |
| Particionamento | [ ] Por data  [ ] Por tenant  [ ] Não |
| Backup Frequency | [ ] Incremental: ___  [ ] Full: ___ |
| Point-in-time Recovery | [ ] Sim - Janela: ___  [ ] Não |

## 11.3 Encriptação

| Tipo | Implementação | Key Management |
|------|---------------|----------------|
| At-rest | [ ] Sim  [ ] Não | _______________ |
| In-transit (TLS) | [ ] Sim  [ ] Não | |
| Field-level (PII) | [ ] Sim  [ ] Não  [ ] A avaliar | _______________ |

---

# Parte 12: Ações e Follow-ups

## 12.1 Decisões Tomadas na Reunião

| # | Decisão | Responsável | Prazo |
|---|---------|-------------|-------|
| 1 | | | |
| 2 | | | |
| 3 | | | |
| 4 | | | |
| 5 | | | |

## 12.2 Questões em Aberto (Requerem Follow-up)

| # | Questão | Responsável por Esclarecer | Prazo |
|---|---------|---------------------------|-------|
| 1 | | | |
| 2 | | | |
| 3 | | | |
| 4 | | | |
| 5 | | | |

## 12.3 Documentação a Produzir

| # | Documento | Responsável | Prazo | Status |
|---|-----------|-------------|-------|--------|
| 1 | | | | [ ] Não iniciado  [ ] Em progresso  [ ] Concluído |
| 2 | | | | [ ] Não iniciado  [ ] Em progresso  [ ] Concluído |
| 3 | | | | [ ] Não iniciado  [ ] Em progresso  [ ] Concluído |
| 4 | | | | [ ] Não iniciado  [ ] Em progresso  [ ] Concluído |
| 5 | | | | [ ] Não iniciado  [ ] Em progresso  [ ] Concluído |

## 12.4 Riscos Identificados

| # | Risco | Probabilidade | Impacto | Mitigação Proposta | Owner |
|---|-------|---------------|---------|-------------------|-------|
| 1 | | [ ] Alta  [ ] Média  [ ] Baixa | [ ] Crítico  [ ] Alto  [ ] Médio  [ ] Baixo | | |
| 2 | | [ ] Alta  [ ] Média  [ ] Baixa | [ ] Crítico  [ ] Alto  [ ] Médio  [ ] Baixo | | |
| 3 | | [ ] Alta  [ ] Média  [ ] Baixa | [ ] Crítico  [ ] Alto  [ ] Médio  [ ] Baixo | | |

## 12.5 Próximos Passos

| # | Ação | Responsável | Prazo |
|---|------|-------------|-------|
| 1 | | | |
| 2 | | | |
| 3 | | | |

---

# Notas Adicionais da Reunião

```
________________________________________________________________________________
________________________________________________________________________________
________________________________________________________________________________
________________________________________________________________________________
________________________________________________________________________________
________________________________________________________________________________
________________________________________________________________________________
________________________________________________________________________________
________________________________________________________________________________
________________________________________________________________________________
________________________________________________________________________________
________________________________________________________________________________
________________________________________________________________________________
________________________________________________________________________________
________________________________________________________________________________
```

---

**Próxima Reunião:** ___/___/______ às ___:___  
**Pauta Prevista:** _______________________________________________

---

*Documento gerado em: ___/___/______*  
*Última atualização: ___/___/______*
