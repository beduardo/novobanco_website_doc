---
id: DEF-15-governacao-roadmap
aliases:
  - Governacao e Roadmap
tags:
  - nextreality-novobanco-website-definitions
  - definitions
  - governance
  - roadmap
  - technical-debt
approved: true
created: 2026-01-08
hubs:
  - "[[nextreality]]"
para-code: R
reviewed: true
status: completed
---

# DEF-15: Governacao & Roadmap

> **Secao relacionada:** [SEC-15 - Governacao & Roadmap](../sections/SEC-15-governacao-roadmap.md)

## Contexto

Definir o modelo de governacao e roadmap do HomeBanking Web, incluindo modelo de governacao, gestao de decisoes arquiteturais, roadmap de produto, gestao de divida tecnica, processo de gestao de mudanca, KPIs de sucesso e continuous improvement.

---

## Modelo de Governanca

### Estrutura Organizacional

```plantuml
@startuml
skinparam backgroundColor white

title Estrutura de Governanca - HomeBanking Web

rectangle "Steering Committee" as steering {
    card "Sponsor"
    card "PO"
    card "Tech Lead"
}

rectangle "Delivery Team" as delivery {
    rectangle "Frontend" as fe {
        card "Lead"
        card "Developers"
    }
    rectangle "Backend" as be {
        card "Lead"
        card "Developers"
    }
    rectangle "QA" as qa {
        card "Lead"
        card "QA Engineers"
    }
}

rectangle "Support Functions" as support {
    card "DevOps"
    card "Security"
    card "UX"
}

steering --> delivery : Direction
support --> delivery : Support

@enduml
```

### Papeis e Responsabilidades

| Papel | Responsabilidades |
|-------|-------------------|
| **Sponsor** | Aprovacao estrategica, budget, escalacao |
| **Product Owner** | Backlog, priorizacao, aceitacao |
| **Tech Lead** | Decisoes tecnicas, arquitetura, quality |
| **Scrum Master** | Processo, impedimentos, cerimonias |
| **Frontend Lead** | Arquitetura frontend, code review |
| **Backend Lead** | Arquitetura BFF, code review |
| **QA Lead** | Estrategia de testes, qualidade |
| **DevOps** | Infraestrutura, CI/CD, operacoes |
| **Security** | Validacao de seguranca, compliance |

### Modelo de Trabalho

| Aspecto | Especificacao |
|---------|---------------|
| Metodologia | Scrum (2-week sprints) |
| Cerimonias | Daily, Planning, Review, Retro |
| Ferramentas | Azure DevOps (boards), Teams |
| Reporting | Sprint Review + Monthly Report |

---

## Gestao de Decisoes Arquiteturais

### Processo de Decisao

```plantuml
@startuml
skinparam backgroundColor white

title Processo de Decisao Arquitetural (ADR)

start
:Identificar necessidade de decisao;
:Criar ADR (status: proposed);

:Analisar alternativas;
:Documentar pros/cons;

:Tech Review;
if (Impacto alto?) then (sim)
    :Steering Committee;
    if (Aprovado?) then (sim)
        :Atualizar status: accepted;
    else (nao)
        :Revisar ou rejeitar;
        stop
    endif
else (nao)
    :Tech Lead aprova;
    :Atualizar status: accepted;
endif

:Comunicar equipa;
:Implementar;
stop

@enduml
```

### Tipos de Decisao

| Tipo | Aprovador | Exemplos |
|------|-----------|----------|
| **Estrategica** | Steering Committee | Stack tecnologica, arquitetura global |
| **Tatica** | Tech Lead | Padroes de codigo, bibliotecas |
| **Operacional** | Lead da area | Configuracoes, tooling |

### ADRs do Projeto

| ID | Decisao | Status | Data |
|----|---------|--------|------|
| DEC-001 | Estrategia de autenticacao web | Accepted | 2026-01-04 |
| DEC-002 | Gestao de sessoes e tokens | Accepted | 2026-01-04 |
| DEC-003 | Modelo de autorizacao ABAC | Accepted | 2026-01-04 |
| DEC-004 | Controlos de seguranca frontend | Accepted | 2026-01-04 |
| DEC-005 | Armazenamento de dados canal web | Accepted | 2026-01-04 |
| DEC-006 | Estrategia de containers OpenShift | Accepted | 2026-01-04 |
| DEC-007 | Padrao BFF | Accepted | 2026-01-04 |
| DEC-008 | Stack de observabilidade ELK | Accepted | 2026-01-04 |
| DEC-009 | Stack tecnologica frontend | Accepted | 2026-01-04 |
| DEC-010 | Stack tecnologica backend | Accepted | 2026-01-04 |

---

## Roadmap de Produto

### Visao de Longo Prazo

```plantuml
@startuml
skinparam backgroundColor white

title Roadmap - Visao de Longo Prazo

|2026 Q1-Q2|
:MVP + Go-Live;
note right: 35 features (paridade mobile)

|2026 Q3|
:Evolucao v1.1;
note right
- Melhorias UX
- Performance
- Feedback users
end note

|2026 Q4|
:Novas Features;
note right
- Features exclusivas web
- Integracao Open Banking
end note

|2027+|
:Expansao;
note right
- Novos canais
- Personalizacao
- AI/ML features
end note

@enduml
```

### Backlog de Features Pos-MVP

| Feature | Prioridade | Estimativa | Dependencias |
|---------|------------|------------|--------------|
| Dashboard personalizavel | P2 | M | MVP |
| Notificacoes web push | P2 | S | MVP |
| Modo escuro | P3 | S | Design System |
| Exportacao de extratos PDF | P2 | M | MVP |
| Comparador de produtos | P3 | L | Backend API |
| Chat com assistente | P3 | XL | Chatbot platform |

### Release Cadence

| Tipo | Frequencia | Conteudo |
|------|------------|----------|
| **Major** | Trimestral | Novas features significativas |
| **Minor** | Mensal | Melhorias e features pequenas |
| **Patch** | Semanal (se necessario) | Bug fixes, seguranca |

---

## Gestao de Divida Tecnica

### Estrategia

```plantuml
@startuml
skinparam backgroundColor white

title Gestao de Divida Tecnica

|Identificacao|
start
:Code Review;
:Metricas (SonarQube);
:Retrospectivas;

|Classificacao|
:Priorizar por impacto;
note right
Alto: Seguranca, Performance
Medio: Maintainability
Baixo: Codigo morto
end note

|Alocacao|
:Reservar 20% da capacidade;
:Incluir no sprint planning;

|Execucao|
:Resolver divida tecnica;
:Documentar melhoria;

|Monitorizacao|
:Atualizar metricas;
:Reportar progresso;
stop

@enduml
```

### Categorias de Divida Tecnica

| Categoria | Exemplos | Prioridade |
|-----------|----------|------------|
| **Seguranca** | Vulnerabilidades, outdated dependencies | Critica |
| **Performance** | Queries lentas, memory leaks | Alta |
| **Arquitetura** | Code smells, tight coupling | Media |
| **Codigo** | Duplicacao, complexidade ciclomatica | Media |
| **Testes** | Baixa cobertura, testes frageis | Media |
| **Documentacao** | APIs nao documentadas | Baixa |

### Metricas de Divida Tecnica

| Metrica | Ferramenta | Target |
|---------|------------|--------|
| Code Coverage | Istanbul/Coverlet | >= 80% |
| Cyclomatic Complexity | SonarQube | < 15 por metodo |
| Duplicated Lines | SonarQube | < 3% |
| Technical Debt Ratio | SonarQube | < 5% |
| Outdated Dependencies | Dependabot | 0 critical |

### Alocacao de Capacidade

| Sprint | Features | Divida Tecnica | Bugs |
|--------|----------|----------------|------|
| Normal | 70% | 20% | 10% |
| Pre-release | 50% | 30% | 20% |
| Pos-release | 40% | 20% | 40% |

---

## Processo de Gestao de Mudanca

### Change Advisory Board (CAB)

| Tipo de Mudanca | Aprovacao | Lead Time |
|-----------------|-----------|-----------|
| **Standard** | Automatica (CI/CD) | Imediato |
| **Normal** | Tech Lead | 1 dia |
| **Emergency** | On-call + Tech Lead | Imediato |
| **Major** | CAB | 1 semana |

### Fluxo de Mudanca

```plantuml
@startuml
skinparam backgroundColor white

title Processo de Change Management

start
:Request de Mudanca;
:Classificar tipo;

switch (Tipo?)
case (Standard)
    :Deploy automatico;
case (Normal)
    :Tech Lead review;
    :Agendar deploy;
case (Emergency)
    :Aprovacao rapida;
    :Deploy imediato;
    :Post-mortem;
case (Major)
    :CAB meeting;
    :Risk assessment;
    :Agendar janela;
endswitch

:Executar mudanca;
:Validar;
:Documentar;
stop

@enduml
```

### Janelas de Mudanca

| Ambiente | Janela | Restricoes |
|----------|--------|------------|
| dev | 24/7 | Nenhuma |
| qa | 24/7 | Nenhuma |
| prod (standard) | 9h-18h dias uteis | Evitar sextas |
| prod (major) | Sabados 6h-10h | Comunicacao previa |

---

## KPIs de Sucesso

### KPIs Tecnicos

| KPI | Metrica | Target | Medicao |
|-----|---------|--------|---------|
| **Disponibilidade** | Uptime % | 99.9% | Mensal |
| **Latencia** | Response time P95 | < 3s | Diario |
| **Taxa de Erro** | Error rate | < 0.1% | Diario |
| **MTTR** | Mean Time To Recover | < 30 min | Por incidente |
| **Deploy Frequency** | Deploys/semana | >= 2 | Semanal |
| **Lead Time** | Commit to prod | < 1 dia | Por deploy |
| **Change Failure Rate** | Deploys com rollback | < 5% | Mensal |

### KPIs de Produto

| KPI | Metrica | Target | Medicao |
|-----|---------|--------|---------|
| **Adocao** | Utilizadores ativos | +20% Q/Q | Mensal |
| **Engagement** | Sessoes/utilizador | >= 5/mes | Mensal |
| **Satisfacao** | NPS | >= 40 | Trimestral |
| **Task Success** | Taxa de conclusao de fluxos | >= 95% | Semanal |
| **Time on Task** | Tempo medio por operacao | Baseline -10% | Mensal |

### Dashboard de KPIs

```
+--------------------------------------------------+
|  HomeBanking Web - KPIs Dashboard                |
+--------------------------------------------------+
|                                                  |
|  [Availability]    [Latency P95]    [Error Rate] |
|     99.95%            2.1s            0.03%      |
|     [====]           [====]          [====]      |
|                                                  |
+--------------------------------------------------+
|  [MTTR]        [Deploy Freq]    [Lead Time]     |
|    15 min          3/week          0.5 days     |
|                                                  |
+--------------------------------------------------+
|  [Active Users]    [NPS]        [Task Success]   |
|     12,500          45             97%           |
|                                                  |
+--------------------------------------------------+
```

---

## Continuous Improvement

### Cerimonias de Melhoria

| Cerimonia | Frequencia | Participantes | Output |
|-----------|------------|---------------|--------|
| Sprint Retro | 2 semanas | Equipa | Action items |
| Tech Retro | Mensal | Tech team | Tech improvements |
| Post-mortem | Por incidente | Envolvidos | Lessons learned |
| Architecture Review | Trimestral | Leads + Arquiteto | ADRs, Roadmap |

### Feedback Loops

```plantuml
@startuml
skinparam backgroundColor white

title Ciclo de Melhoria Continua

start
:Coletar feedback;
note right
- Metricas
- Retros
- Incidents
- User feedback
end note

:Analisar e priorizar;
:Planear melhorias;
:Implementar;
:Medir impacto;
:Documentar aprendizados;
stop

@enduml
```

### Metricas de Maturidade

| Area | Nivel Atual | Target | Acoes |
|------|-------------|--------|-------|
| CI/CD | 3 | 4 | Automacao de testes |
| Observability | 3 | 4 | Tracing distribuido |
| Security | 3 | 4 | DAST automatizado |
| Documentation | 2 | 3 | API docs automaticas |

---

## Questoes Pendentes de Confirmacao

| ID | Questao | Responsavel | Prioridade |
|----|---------|-------------|------------|
| Q-15-001 | Modelo de governanca formal | Sponsor | Media |
| Q-15-002 | Composicao do CAB | Sponsor | Media |
| Q-15-003 | Budget para divida tecnica (20%) | PO | Alta |
| Q-15-004 | Frequencia de releases pos-MVP | PO | Media |
| Q-15-005 | KPIs de negocio adicionais | Produto | Baixa |

---

## Decisoes

### Governance Model
- **Decisao:** Scrum com sprints de 2 semanas
- **Justificacao:** Flexibilidade, feedback rapido, alinhado com praticas agile
- **Alternativas consideradas:** Kanban (menos estrutura), SAFe (overkill)

### Change Management
- **Decisao:** Modelo tiered (Standard/Normal/Emergency/Major)
- **Justificacao:** Balanco entre agilidade e controle
- **Alternativas consideradas:** CAB para todas as mudancas (muito rigido)

### Technical Debt Management
- **Decisao:** 20% da capacidade alocada para divida tecnica
- **Justificacao:** Manter qualidade sem bloquear features
- **Alternativas consideradas:** Sprints dedicados (disruptivo)

### Release Cadence
- **Decisao:** Major trimestral, Minor mensal, Patch semanal
- **Justificacao:** Previsibilidade para stakeholders, flexibilidade para correcoes
- **Alternativas consideradas:** Continuous deployment (risco maior)

---

## Decisoes Relacionadas

- All architectural decisions (DEC-001 to DEC-010)

## Referencias

- [CONTEXT.md](../CONTEXT.md) - Contexto do projeto
- [DEF-10-arquitetura-operacional.md](DEF-10-arquitetura-operacional.md) - CI/CD
- [DEF-02-stakeholders.md](DEF-02-stakeholders.md) - Stakeholders
- TOGAF - Architecture Governance
- Accelerate (DORA metrics)
- Spotify Model - Engineering Culture
