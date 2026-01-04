# Reuniao de Alinhamento Tecnico - Documento de Arquitetura

> **Data:** 2025-12-23
    > **Objetivo:** Obter decisoes tecnicas bloqueadoras para continuidade do documento de arquitetura
    > **Escopo:** Questoes tecnicas (excluindo requisitos funcionais de negocio)

---

## Estado Atual do Documento de Arquitetura

### Documentos Concluidos ou em Progresso

| Secao | Documento | Status | Observacoes |
|-------|-----------|--------|-------------|
| 01 | DEF-01-business-objectives.md | Concluido | Objetivos definidos |
| 01 | DEF-01-stack-tecnologica.md | Em progresso | React + C# confirmados |
| 02 | DEF-02-restricoes.md | Concluido | Azure, AKS, PSD2, RGPD |
| 02 | DEF-02-stakeholders.md | Concluido | Stakeholders identificados |
| 02 | DEF-02-requisitos-nao-funcionais.md | Parcial | SLA 99.95%, latencia <1s definidos |
| 03 | DEF-03-principios-arquiteturais.md | Parcial | SOLID, 12-Factor, CQRS/MediatR |
| 05 | DEF-05-arquitetura-backend.md | Concluido | BFF pattern, decomposicao de servicos |
| 07 | DEF-07-autenticacao-oauth.md | Em progresso | Fluxos QR Code e OAuth documentados |
| 09 | DEF-09-fluxo-transferencia.md | Concluido | Fluxo completo documentado |
| 09 | DEF-09-integracoes.md | Em progresso | APIs catalogadas, pendente detalhes |
| 10 | DEF-10-ambientes-cicd.md | Concluido | 4 ambientes, GitHub Actions, Blue-Green |
| 11 | DEF-11-observabilidade.md | Concluido | Prometheus, Grafana, ELK, Jaeger |

### Metricas de Progresso

- **Total de questoes respondidas:** ~50
- **Total de questoes pendentes:** 55
- **Questoes tecnicas bloqueadoras:** 8 (listadas abaixo)

---

## Questoes Tecnicas para Decisao

### PRIORIDADE ALTA

#### 1. Fluxo de Autenticacao - Momento do apiToken

| | |
|---|---|
| **ID** | Q-07-001 |
| **Documento** | [DEF-07-autenticacao-oauth.md](definitions/DEF-07-autenticacao-oauth.md) |
| **Secao** | SEC-07: Autenticacao & Autorizacao |

**Contexto:**
Existe divergencia na documentacao sobre quando o `apiToken` e retornado pela API `Authentication_checkLogin` (AUT_004):

| Interpretacao | Descricao |
|---------------|-----------|
| **A** | apiToken retornado **antes** do OTP, OTP valida via API "secure" separada |
| **B** | apiToken retornado **apos** validacao do OTP |

**Impacto se nao decidido:**
- Impossibilidade de finalizar diagramas de sequencia de autenticacao
- Design incorreto da gestao de sessoes no BFF
- Potenciais falhas de seguranca na implementacao

**Questao para o cliente:**
> Quando `needStrongAuthentication=Y`, o `apiToken` ja vem na resposta inicial ou so apos validacao do OTP?

**Decisao:**
_______________________________________________________________________

---

#### 2. Capacidade e Dimensionamento

| | |
|---|---|
| **ID** | Q-02-001, Q-02-002, Q-12-004 |
| **Documento** | [DEF-02-requisitos-nao-funcionais.md](definitions/DEF-02-requisitos-nao-funcionais.md), [DEF-12-performance-resiliencia.md](definitions/DEF-12-performance-resiliencia.md) |
| **Secao** | SEC-02: Requisitos, SEC-12: Performance |

**Contexto:**
Para dimensionar a infraestrutura Azure AKS precisamos de numeros de capacidade:

| Metrica | Necessario para | Valor Atual |
|---------|-----------------|-------------|
| Utilizadores simultaneos | Sizing pods, Redis, load balancers | _Pendente_ |
| Transacoes por segundo (TPS) | Rate limiting, auto-scaling | _Pendente_ |
| RTO (Recovery Time Objective) | Estrategia DR | _Pendente_ |
| RPO (Recovery Point Objective) | Frequencia backups | _Pendente_ |

**Impacto se nao decidido:**
- Impossibilidade de definir configuracoes de auto-scaling
- Risco de subdimensionamento ou custos excessivos
- Estrategia de DR incompleta

**Questao para o cliente:**
> Podem fornecer metricas do App Mobile atual como referencia? Ou estimativas de carga esperada?

**Decisao:**

| Metrica | Valor |
|---------|-------|
| Utilizadores simultaneos | |
| TPS | |
| RTO | |
| RPO | |

---

#### 3. Granularidade - Microservices vs Modular Monolith

| | |
|---|---|
| **ID** | Q-03-005 |
| **Documento** | [DEF-03-principios-arquiteturais.md](definitions/DEF-03-principios-arquiteturais.md), [DEF-05-arquitetura-backend.md](definitions/DEF-05-arquitetura-backend.md) |
| **Secao** | SEC-03: Principios, SEC-05: Backend |

**Contexto:**
Duas abordagens possiveis para o backend:

| Abordagem | Vantagens | Desvantagens |
|-----------|-----------|--------------|
| **Microservices** | Escalabilidade independente, deploy isolado | Complexidade operacional, latencia inter-servicos |
| **Modular Monolith** | Simplicidade, menor latencia | Scaling uniforme, deploy conjunto |

**O que ja temos definido:**
- BFF como camada de orquestracao (confirmado)
- Dominios identificados: Autenticacao, Contas, Pagamentos, Cartoes, Notificacoes

**Impacto se nao decidido:**
- Estrutura de repositorios indefinida
- Pipelines CI/CD incompletos
- Estimativas de custos de infraestrutura imprecisas

**Questao para o cliente:**
> Qual a preferencia: servicos independentes por dominio ou BFF monolitico modular?

**Decisao:**
- [ ] Microservices (servicos independentes)
- [ ] Modular Monolith (BFF unico com modulos)
- [ ] Hibrido (especificar)

---

### PRIORIDADE MEDIA

#### 4. Encriptacao de Credenciais SPA-BFF

| | |
|---|---|
| **ID** | Q-07-006 |
| **Documento** | [DEF-07-autenticacao-oauth.md](definitions/DEF-07-autenticacao-oauth.md), [DEF-08-seguranca-dados-sensiveis.md](definitions/DEF-08-seguranca-dados-sensiveis.md) |
| **Secao** | SEC-07: Autenticacao, SEC-08: Seguranca |

**Contexto:**
A API `Authentication_checkLogin` suporta o campo `encrypt` com valores "Y" ou "N". A comunicacao SPA-BFF ja usa HTTPS (TLS 1.3), mas pode haver requisito adicional de encriptacao aplicacional.

**Questao para o cliente:**
> E necessario encriptar user/pass no payload alem do TLS? Existe requisito de seguranca do banco para isso?

**Decisao:**
- [ ] Apenas TLS (encrypt=N)
- [ ] Encriptacao adicional (encrypt=Y) - Qual algoritmo?

_______________________________________________________________________

---

#### 5. Servicos PSD2 a Expor

| | |
|---|---|
| **ID** | Q-08-006 |
| **Documento** | [DEF-08-conformidade-regulatoria.md](definitions/DEF-08-conformidade-regulatoria.md), [DEF-09-integracoes.md](definitions/DEF-09-integracoes.md) |
| **Secao** | SEC-08: Conformidade, SEC-09: Integracoes |

**Contexto:**
PSD2 define tres tipos de servicos que podem ser expostos a terceiros (TPPs):

| Servico | Descricao | Obrigatorio? |
|---------|-----------|--------------|
| **AIS** | Account Information Service | Sim (se oferecer contas) |
| **PIS** | Payment Initiation Service | Sim (se oferecer pagamentos) |
| **CBPII** | Card-based Payment Instrument Issuer | Depende |

**O que ja temos:**
- APIs SIBS identificadas: `SIBS_getConsentStatus`, `SIBS_getConsentAccount`

**Questao para o cliente:**
> Quais servicos PSD2 o WebSite deve expor? Todos os tres ou apenas AIS/PIS?

**Decisao:**

| Servico | Implementar? |
|---------|--------------|
| AIS | [ ] Sim / [ ] Nao |
| PIS | [ ] Sim / [ ] Nao |
| CBPII | [ ] Sim / [ ] Nao |

---

#### 6. Certificados eIDAS e mTLS

| | |
|---|---|
| **ID** | Q-09-008 |
| **Documento** | [DEF-09-integracoes.md](definitions/DEF-09-integracoes.md), [DEF-08-conformidade-regulatoria.md](definitions/DEF-08-conformidade-regulatoria.md) |
| **Secao** | SEC-09: Integracoes, SEC-08: Conformidade |

**Contexto:**
Integracoes PSD2 com SIBS requerem certificados qualificados (eIDAS). Precisamos saber:
- Quem fornece os certificados (SIBS, CA externa)?
- Qual o modelo de renovacao?
- mTLS e obrigatorio para todas as APIs ou apenas PSD2?

**Questao para o cliente:**
> Qual o modelo de certificados para integracao SIBS? Ja existem certificados ou precisam ser adquiridos?

**Decisao:**
_______________________________________________________________________

---

#### 7. Feature Flags - Tooling

| | |
|---|---|
| **ID** | Q-10-001 |
| **Documento** | [DEF-10-ambientes-cicd.md](definitions/DEF-10-ambientes-cicd.md) |
| **Secao** | SEC-10: Infraestrutura |

**Contexto:**
Para releases progressivos (Canary, feature toggles) precisamos de uma solucao:

| Opcao | Tipo | Custo | Complexidade |
|-------|------|-------|--------------|
| **LaunchDarkly** | SaaS | ~$500-2000/mes | Baixa |
| **Unleash** | Self-hosted (OSS) | Infra apenas | Media |

**O que ja temos definido:**
- Blue-Green e Canary releases planeados
- Azure AKS como plataforma

**Questao para o cliente:**
> Preferencia por SaaS (LaunchDarkly) ou self-hosted (Unleash)? Existe restricao de custos ou de dados em SaaS externo?

**Decisao:**
- [ ] LaunchDarkly (SaaS)
- [ ] Unleash (self-hosted)
- [ ] Outro: ________________

---

#### 8. Compatibilidade de Browsers e Acessibilidade

| | |
|---|---|
| **ID** | Q-02-006, Q-02-007 |
| **Documento** | [DEF-02-requisitos-nao-funcionais.md](definitions/DEF-02-requisitos-nao-funcionais.md), [DEF-04-experiencia-utilizador-frontend.md](definitions/DEF-04-experiencia-utilizador-frontend.md) |
| **Secao** | SEC-02: Requisitos, SEC-04: Frontend |

**Contexto:**
Decisoes de compatibilidade afetam escolhas de bibliotecas e testes:

| Aspecto | Opcoes |
|---------|--------|
| **Browsers** | Ultimas 2 versoes? IE11? Safari iOS? |
| **WCAG** | Level A, AA, ou AAA? |
| **Dispositivos** | Desktop only? Responsive? |

**Questao para o cliente:**
> Quais browsers minimos devem ser suportados? Qual nivel WCAG e obrigatorio?

**Decisao:**

| Aspecto | Decisao |
|---------|---------|
| Browsers minimos | |
| WCAG Level | [ ] A / [ ] AA / [ ] AAA |
| Mobile responsive | [ ] Sim / [ ] Nao |

---

## Resumo de Decisoes Necessarias

| # | Topico | Prioridade | Documento Relacionado |
|---|--------|------------|----------------------|
| 1 | Momento do apiToken | Alta | DEF-07-autenticacao-oauth.md |
| 2 | Capacidade (utilizadores, TPS, RTO/RPO) | Alta | DEF-02-requisitos-nao-funcionais.md |
| 3 | Microservices vs Modular Monolith | Alta | DEF-03-principios-arquiteturais.md |
| 4 | Encriptacao credenciais SPA-BFF | Media | DEF-07-autenticacao-oauth.md |
| 5 | Servicos PSD2 (AIS/PIS/CBPII) | Media | DEF-08-conformidade-regulatoria.md |
| 6 | Certificados eIDAS/mTLS | Media | DEF-09-integracoes.md |
| 7 | Feature Flags (LaunchDarkly/Unleash) | Media | DEF-10-ambientes-cicd.md |
| 8 | Browsers e WCAG | Media | DEF-02-requisitos-nao-funcionais.md |

---

## Proximos Passos Apos Reuniao

1. Incorporar decisoes nos documentos de definicao (`DEF-*.md`)
2. Atualizar `QUESTOES_PENDENTES.md` com respostas obtidas
3. Gerar diagramas finais de autenticacao (apos Q-07-001)
4. Definir configuracoes de infraestrutura (apos metricas de capacidade)
5. Avancar para redacao das secoes (`SEC-*.md`)

---

## Anexo: Estrutura de Pastas do Projeto

```
website/
├── TASK_DEFINITION.md                    # Plano de execucao
├── QUESTOES_PENDENTES.md                 # 55 questoes pendentes
├── REUNIAO_CLIENTE_2025-12-23.md         # Este documento
├── definitions/                          # 28 documentos de definicao
│   ├── DEF-01-*.md                       # Contexto e visao
│   ├── DEF-02-*.md                       # Requisitos
│   ├── DEF-03-*.md                       # Principios
│   ├── DEF-05-*.md                       # Backend
│   ├── DEF-07-*.md                       # Autenticacao
│   ├── DEF-08-*.md                       # Seguranca
│   ├── DEF-09-*.md                       # Integracoes
│   ├── DEF-10-*.md                       # Infraestrutura
│   ├── DEF-11-*.md                       # Observabilidade
│   ├── DEF-12-*.md                       # Performance
│   ├── DEF-13-*.md                       # Testes
│   ├── DEF-14-*.md                       # Implementacao
│   └── DEF-15-*.md                       # Governacao
└── sections/                             # Secoes do documento final (a criar)
```

---

*Documento preparado para reuniao de alinhamento tecnico*

# NOTAS DA REUNÃO
- Autenticação com Cache usando Redis. O ApiToken ficará no Redis e o BFF precisará criar um token intermediário que vinculará a sessão do browser com este API token. Um cookie de sessão deverá ser gerado com este token e enviado na resposta. Somente quem tem este token de sessão poderá utilizar o token vinculado.
    - O BFF deverá vincular o utilizador a todos os tokens para permitir listar todos os tokens atuais para o utilizador. E também identificar todos os browser vinculados.
- O BFF ficará ANTES do API Gateway (SPA -> F5 -> BFF -> GATEWAY -> DEPENDENCIA)
- Distribuir as regras de negócio entre Microserviços
- A aplicaçAo precisa se lembrar de determinadas informaçöes do usuário entre as sessões no período de 30 minutos ou até ele fazer alguma transação
- Há uma encriptação para os dados do utilizador no momento do pedido de autenticação. Verificar junto ao app

# TAREFAS DA REUNIÃO
- Preparar a lista de perguntas para serem enviadas
- Preparar o documento draft com a estrutura dos iniciais
- 
- 
