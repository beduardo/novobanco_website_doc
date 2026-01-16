---
id: DEF-15-governacao-roadmap
aliases:
  - Governação e Roadmap
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

# DEF-15: Governação & Roadmap

> **Secção relacionada:** [SEC-15 - Governação & Roadmap](../sections/SEC-15-governacao-roadmap.md)

## Contexto

Definir o modelo de governação e roadmap do HomeBanking Web, incluindo modelo de governação, gestão de decisões arquiteturais, roadmap de produto, gestão de dívida técnica, processo de gestão de mudança, KPIs de sucesso e continuous improvement.

---

## Modelo de Governança

### Estrutura Organizacional

```plantuml
@startuml
skinparam backgroundColor white

title Estrutura de Governança - HomeBanking Web

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

### Papéis e Responsabilidades

| Papel | Responsabilidades |
|-------|-------------------|
| **Sponsor** | Aprovação estratégica, budget, escalação |
| **Product Owner** | Backlog, priorização, aceitação |
| **Tech Lead** | Decisões técnicas, arquitetura, quality |
| **Scrum Master** | Processo, impedimentos, cerimónias |
| **Frontend Lead** | Arquitetura frontend, code review |
| **Backend Lead** | Arquitetura BFF, code review |
| **QA Lead** | Estratégia de testes, qualidade |
| **DevOps** | Infraestrutura, CI/CD, operações |
| **Security** | Validação de segurança, compliance |

### Modelo de Trabalho

| Aspecto | Especificação |
|---------|---------------|
| Metodologia | Scrum (2-week sprints) |
| Cerimónias | Daily, Planning, Review, Retro |
| Ferramentas | Azure DevOps (boards), Teams |
| Reporting | Sprint Review + Monthly Report |

---

## Gestão de Decisões Arquiteturais

### Processo de Decisão

```plantuml
@startuml
skinparam backgroundColor white

title Processo de Decisão Arquitetural (ADR)

start
:Identificar necessidade de decisão;
:Criar ADR (status: proposed);

:Analisar alternativas;
:Documentar pros/cons;

:Tech Review;
if (Impacto alto?) then (sim)
    :Steering Committee;
    if (Aprovado?) then (sim)
        :Atualizar status: accepted;
    else (não)
        :Revisar ou rejeitar;
        stop
    endif
else (não)
    :Tech Lead aprova;
    :Atualizar status: accepted;
endif

:Comunicar equipa;
:Implementar;
stop

@enduml
```

### Tipos de Decisão

| Tipo | Aprovador | Exemplos |
|------|-----------|----------|
| **Estratégica** | Steering Committee | Stack tecnológica, arquitetura global |
| **Tática** | Tech Lead | Padrões de código, bibliotecas |
| **Operacional** | Lead da área | Configurações, tooling |

### ADRs do Projeto

| ID | Decisão | Status | Data |
|----|---------|--------|------|
| DEC-001 | Estratégia de autenticação web | Accepted | 2026-01-04 |
| DEC-002 | Gestão de sessões e tokens | Accepted | 2026-01-04 |
| DEC-003 | Modelo de autorização ABAC | Accepted | 2026-01-04 |
| DEC-004 | Controlos de segurança frontend | Accepted | 2026-01-04 |
| DEC-005 | Armazenamento de dados canal web | Accepted | 2026-01-04 |
| DEC-006 | Estratégia de containers OpenShift | Accepted | 2026-01-04 |
| DEC-007 | Padrão BFF | Accepted | 2026-01-04 |
| DEC-008 | Stack de observabilidade ELK | Accepted | 2026-01-04 |
| DEC-009 | Stack tecnológica frontend | Accepted | 2026-01-04 |
| DEC-010 | Stack tecnológica backend | Accepted | 2026-01-04 |

---

## Roadmap de Produto

### Visão de Longo Prazo

```plantuml
@startuml
skinparam backgroundColor white

title Roadmap - Visão de Longo Prazo

|2026 Q1-Q2|
:MVP + Go-Live;
note right: 35 features (paridade mobile)

|2026 Q3|
:Evolução v1.1;
note right
- Melhorias UX
- Performance
- Feedback users
end note

|2026 Q4|
:Novas Features;
note right
- Features exclusivas web
- Integração Open Banking
end note

|2027+|
:Expansão;
note right
- Novos canais
- Personalização
- AI/ML features
end note

@enduml
```

### Backlog de Features Pós-MVP

| Feature | Prioridade | Estimativa | Dependências |
|---------|------------|------------|--------------|
| Dashboard personalizável | P2 | M | MVP |
| Notificações web push | P2 | S | MVP |
| Modo escuro | P3 | S | Design System |
| Exportação de extratos PDF | P2 | M | MVP |
| Comparador de produtos | P3 | L | Backend API |
| Chat com assistente | P3 | XL | Chatbot platform |

### Release Cadence

| Tipo | Frequência | Conteúdo |
|------|------------|----------|
| **Major** | Trimestral | Novas features significativas |
| **Minor** | Mensal | Melhorias e features pequenas |
| **Patch** | Semanal (se necessário) | Bug fixes, segurança |

---

## Gestão de Dívida Técnica

### Estratégia

```plantuml
@startuml
skinparam backgroundColor white

title Gestão de Dívida Técnica

|Identificação|
start
:Code Review;
:Métricas (SonarQube);
:Retrospectivas;

|Classificação|
:Priorizar por impacto;
note right
Alto: Segurança, Performance
Médio: Maintainability
Baixo: Código morto
end note

|Alocação|
:Reservar 20% da capacidade;
:Incluir no sprint planning;

|Execução|
:Resolver dívida técnica;
:Documentar melhoria;

|Monitorização|
:Atualizar métricas;
:Reportar progresso;
stop

@enduml
```

### Categorias de Dívida Técnica

| Categoria | Exemplos | Prioridade |
|-----------|----------|------------|
| **Segurança** | Vulnerabilidades, outdated dependencies | Crítica |
| **Performance** | Queries lentas, memory leaks | Alta |
| **Arquitetura** | Code smells, tight coupling | Média |
| **Código** | Duplicação, complexidade ciclomática | Média |
| **Testes** | Baixa cobertura, testes frágeis | Média |
| **Documentação** | APIs não documentadas | Baixa |

### Métricas de Dívida Técnica

| Métrica | Ferramenta | Target |
|---------|------------|--------|
| Code Coverage | Istanbul/Coverlet | >= 80% |
| Cyclomatic Complexity | SonarQube | < 15 por método |
| Duplicated Lines | SonarQube | < 3% |
| Technical Debt Ratio | SonarQube | < 5% |
| Outdated Dependencies | Dependabot | 0 critical |

### Alocação de Capacidade

| Sprint | Features | Dívida Técnica | Bugs |
|--------|----------|----------------|------|
| Normal | 70% | 20% | 10% |
| Pre-release | 50% | 30% | 20% |
| Pós-release | 40% | 20% | 40% |

---

## Processo de Gestão de Mudança

### Change Advisory Board (CAB)

| Tipo de Mudança | Aprovação | Lead Time |
|-----------------|-----------|-----------|
| **Standard** | Automática (CI/CD) | Imediato |
| **Normal** | Tech Lead | 1 dia |
| **Emergency** | On-call + Tech Lead | Imediato |
| **Major** | CAB | 1 semana |

### Fluxo de Mudança

```plantuml
@startuml
skinparam backgroundColor white

title Processo de Change Management

start
:Request de Mudança;
:Classificar tipo;

switch (Tipo?)
case (Standard)
    :Deploy automático;
case (Normal)
    :Tech Lead review;
    :Agendar deploy;
case (Emergency)
    :Aprovação rápida;
    :Deploy imediato;
    :Post-mortem;
case (Major)
    :CAB meeting;
    :Risk assessment;
    :Agendar janela;
endswitch

:Executar mudança;
:Validar;
:Documentar;
stop

@enduml
```

### Janelas de Mudança

| Ambiente | Janela | Restrições |
|----------|--------|------------|
| dev | 24/7 | Nenhuma |
| qa | 24/7 | Nenhuma |
| prod (standard) | 9h-18h dias úteis | Evitar sextas |
| prod (major) | Sábados 6h-10h | Comunicação prévia |

---

## KPIs de Sucesso

### KPIs Técnicos

| KPI | Métrica | Target | Medição |
|-----|---------|--------|---------|
| **Disponibilidade** | Uptime % | 99.9% | Mensal |
| **Latência** | Response time P95 | < 3s | Diário |
| **Taxa de Erro** | Error rate | < 0.1% | Diário |
| **MTTR** | Mean Time To Recover | < 30 min | Por incidente |
| **Deploy Frequency** | Deploys/semana | >= 2 | Semanal |
| **Lead Time** | Commit to prod | < 1 dia | Por deploy |
| **Change Failure Rate** | Deploys com rollback | < 5% | Mensal |

### KPIs de Produto

| KPI | Métrica | Target | Medição |
|-----|---------|--------|---------|
| **Adoção** | Utilizadores ativos | +20% Q/Q | Mensal |
| **Engagement** | Sessões/utilizador | >= 5/mês | Mensal |
| **Satisfação** | NPS | >= 40 | Trimestral |
| **Task Success** | Taxa de conclusão de fluxos | >= 95% | Semanal |
| **Time on Task** | Tempo médio por operação | Baseline -10% | Mensal |

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

### Cerimónias de Melhoria

| Cerimónia | Frequência | Participantes | Output |
|-----------|------------|---------------|--------|
| Sprint Retro | 2 semanas | Equipa | Action items |
| Tech Retro | Mensal | Tech team | Tech improvements |
| Post-mortem | Por incidente | Envolvidos | Lessons learned |
| Architecture Review | Trimestral | Leads + Arquiteto | ADRs, Roadmap |

### Feedback Loops

```plantuml
@startuml
skinparam backgroundColor white

title Ciclo de Melhoria Contínua

start
:Coletar feedback;
note right
- Métricas
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

### Métricas de Maturidade

| Área | Nível Atual | Target | Ações |
|------|-------------|--------|-------|
| CI/CD | 3 | 4 | Automação de testes |
| Observability | 3 | 4 | Tracing distribuído |
| Security | 3 | 4 | DAST automatizado |
| Documentation | 2 | 3 | API docs automáticas |

---

## Questões Pendentes de Confirmação

| ID | Questão | Responsável | Prioridade |
|----|---------|-------------|------------|
| Q-15-001 | Modelo de governação formal | Sponsor | Média |
| Q-15-002 | Composição do CAB | Sponsor | Média |
| Q-15-003 | Budget para dívida técnica (20%) | PO | Alta |
| Q-15-004 | Frequência de releases pós-MVP | PO | Média |
| Q-15-005 | KPIs de negócio adicionais | Produto | Baixa |

---

## Decisões

### Governance Model
- **Decisão:** Scrum com sprints de 2 semanas
- **Justificação:** Flexibilidade, feedback rápido, alinhado com práticas agile
- **Alternativas consideradas:** Kanban (menos estrutura), SAFe (overkill)

### Change Management
- **Decisão:** Modelo tiered (Standard/Normal/Emergency/Major)
- **Justificação:** Balanço entre agilidade e controle
- **Alternativas consideradas:** CAB para todas as mudanças (muito rígido)

### Technical Debt Management
- **Decisão:** 20% da capacidade alocada para dívida técnica
- **Justificação:** Manter qualidade sem bloquear features
- **Alternativas consideradas:** Sprints dedicados (disruptivo)

### Release Cadence
- **Decisão:** Major trimestral, Minor mensal, Patch semanal
- **Justificação:** Previsibilidade para stakeholders, flexibilidade para correções
- **Alternativas consideradas:** Continuous deployment (risco maior)

---

## Decisões Relacionadas

- All architectural decisions (DEC-001 to DEC-010)

## Referências

- [CONTEXT.md](../CONTEXT.md) - Contexto do projeto
- [DEF-10-arquitetura-operacional.md](DEF-10-arquitetura-operacional.md) - CI/CD
- [DEF-02-stakeholders.md](DEF-02-stakeholders.md) - Stakeholders
- TOGAF - Architecture Governance
- Accelerate (DORA metrics)
- Spotify Model - Engineering Culture
