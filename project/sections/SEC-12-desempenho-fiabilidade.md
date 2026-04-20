---
id: "SEC-12"
title: "Desempenho e Fiabilidade"
status: "completed"
created: "2026-01-08"
updated: "2026-04-18"
depends-on-definitions:
  - "DEF-22"
depends-on-decisions:
  - "DEC-025"
word-count: 0
---

# 12. Desempenho & Fiabilidade

## Definições e Decisões

> **Definição:** [DEF-22-desempenho-fiabilidade.md](../definitions/DEF-22-desempenho-fiabilidade.md)

## Propósito

Definir os objetivos de desempenho e a estratégia de fiabilidade do HomeBanking Web, incluindo targets de performance, caching, auto-scaling e testes de carga.

## Conteúdo

### 12.1 Objetivos de Desempenho

Os targets são baseados nos requisitos não funcionais (DEF-02):

| Métrica | Target | Fonte |
|---------|--------|-------|
| **Utilizadores Concorrentes** | 400 | DEF-02 |
| **Throughput** | 10 TPS | DEF-02 |
| **Tempo de Resposta (P95)** | < 3 segundos | DEF-02 |
| **Tempo de Carregamento Inicial** | < 10 segundos | DEF-02 |
| **Disponibilidade** | 99.9% | DEF-02 |
| **Crescimento Anual** | 5% | DEF-02 |

> **Pendência:** Estes targets são valores provisórios. Necessário obter métricas reais da app mobile para calibrar: pedidos/segundo (normal e pico), padrões de sazonalidade (fim de mês, períodos fiscais).

### 12.2 Core Web Vitals

| Métrica | Target | Classificação |
|---------|--------|---------------|
| **LCP** (Largest Contentful Paint) | < 2.5s | Good |
| **FID** (First Input Delay) | < 100ms | Good |
| **CLS** (Cumulative Layout Shift) | < 0.1 | Good |
| **TTFB** (Time to First Byte) | < 800ms | Good |
| **FCP** (First Contentful Paint) | < 1.8s | Good |

### 12.3 Perfil de Carga

```plantuml
@startuml
skinparam backgroundColor white

title Perfil de Carga - HomeBanking Web

rectangle "Carga Normal" {
    card "200 utilizadores"
    card "5 TPS"
    card "CPU: 30-40%"
}

rectangle "Carga Pico" {
    card "400 utilizadores"
    card "10 TPS"
    card "CPU: 60-70%"
}

rectangle "Carga Stress" {
    card "600 utilizadores"
    card "15 TPS"
    card "CPU: 80-90%"
}

note bottom of "Carga Pico"
Picos esperados:
- Fim de mês
- Períodos fiscais
- Campanhas
end note

@enduml
```

### 12.4 Estratégia de Cache

```plantuml
@startuml
skinparam backgroundColor white

title Camadas de Cache

actor User
participant "Browser" as browser
participant "BFF" as bff
database "Redis" as redis
participant "Backend" as api

User -> browser : Request
browser -> browser : Local Storage\n(sessão, prefs)

browser -> bff : API Request
bff -> redis : Cache lookup
alt Cache HIT
    redis --> bff : Cached data
    bff --> browser : Response (fast)
else Cache MISS
    bff -> api : Backend call
    api --> bff : Data
    bff -> redis : Cache store
    bff --> browser : Response
end

@enduml
```

#### Níveis de Cache

| Nível | Dados | TTL |
|-------|-------|-----|
| **Browser** | Assets estáticos (JS, CSS, imagens) | Longo (com cache busting) |
| **Browser** | Local Storage (sessão, prefs) | Sessão |
| **BFF (Redis)** | Sessões, tokens, dados partilhados | Variável |

#### TTL por Tipo de Dado (Redis)

| Dado | TTL | Justificação |
|------|-----|--------------|
| Sessão do utilizador | 10 min | Inatividade timeout |
| Tokens OAuth | Variável | Alinhado com expiração |
| Configurações do sistema | 5 min | Baixa frequência de mudança |
| Dados de referência (países, bancos) | 1 hora | Dados estáticos |
| Cotações/Taxas | 1 min | Dados voláteis |

**Princípio:** Dados sensíveis (contas, transações) NÃO são cacheados.

#### Cache Invalidation

| Evento | Ação |
|--------|------|
| Logout | Invalidar sessão no Redis |
| Transação executada | Invalidar cache de saldos (se aplicável) |
| Deploy | Versionar assets (cache busting) |
| Configuração alterada | Invalidar cache de config |

### 12.5 Otimização Frontend

#### Bundle Optimization

| Técnica | Implementação | Impacto |
|---------|---------------|---------|
| Code Splitting | React.lazy() + Suspense | Reduz initial bundle |
| Tree Shaking | Webpack/Vite config | Remove código não utilizado |
| Lazy Loading | Componentes e rotas | Carrega sob demanda |
| Minification | Terser (JS), CSSNano | Reduz tamanho |
| Compression | gzip/Brotli | 70-90% redução |

#### Budget de Bundle

| Métrica | Limite | Ação se exceder |
|---------|--------|-----------------|
| Initial JS | < 200KB (gzipped) | Code split |
| Initial CSS | < 50KB (gzipped) | Purge CSS |
| Largest chunk | < 100KB | Split ou lazy load |
| Total assets | < 1MB | Review dependencies |

#### Otimização de Assets

| Asset | Estratégia |
|-------|------------|
| Imagens | WebP format, lazy loading, srcset |
| Fontes | WOFF2, font-display: swap, subset |
| Icons | SVG sprite ou icon font |
| CSS | Critical CSS inline, defer restante |

### 12.6 Otimização Backend (BFF)

#### Connection Pooling

| Conexão | Pool Size | Timeout |
|---------|-----------|---------|
| Redis | 10-20 | 5s |
| HTTP Client (Backend) | 100 | 30s |

#### Compressão

| Tipo | Configuração |
|------|--------------|
| Response | gzip (nível 6) |
| Threshold | > 1KB |
| Content-Types | application/json, text/html |

### 12.7 Auto-Scaling

> **Nota (DEC-025):** Os parâmetros de auto-scaling (HPA) — min/max réplicas, targets de CPU e memória, janelas de estabilização de scale-up e scale-down — são definidos e validados pela equipa de infraestrutura do Novo Banco. A equipa de desenvolvimento expõe os health check endpoints necessários para que o HPA funcione corretamente.

### 12.8 Capacity Planning

> **Nota (DEC-025):** Os resource requests e limits por container (CPU e memória) são definidos e validados pela equipa de infraestrutura do Novo Banco, em função das quotas e políticas de namespace existentes na plataforma OpenShift.

### 12.9 Resiliência

| Padrão | Implementação |
|--------|---------------|
| **Circuit Breaker** | Polly (.NET) |
| **Retry** | Não implementado (DEC-022) |
| **Timeout** | Configurável por endpoint |
| **Bulkhead** | Limite de conexões |
| **Health Checks** | Liveness + Readiness probes |

#### Pod Disruption Budget

> **Nota (DEC-025):** A política de Pod Disruption Budget (PDB) é definida e configurada pela equipa de infraestrutura do Novo Banco.

### 12.10 Load Testing

> **Nota (DEC-025):** A estratégia de load testing — ferramentas aprovadas, cenários obrigatórios e critérios de aceitação — é definida pela equipa de infraestrutura e QA do Novo Banco. A equipa de desenvolvimento adapta os testes ao pipeline e plataforma existentes.

## Decisões Referenciadas

- [DEC-025-parametros-operacionais-de-plataforma-definidos-pelo-banco.md](../decisions/DEC-025-parametros-operacionais-de-plataforma-definidos-pelo-banco.md) - Auto-scaling, capacity planning, PDB e load testing seguem padrões do banco
- [DEC-006-estrategia-containers-openshift.md](../decisions/DEC-006-estrategia-containers-openshift.md) - Containers e auto-scaling
- [DEC-007-padrao-bff.md](../decisions/DEC-007-padrao-bff.md) - BFF (cache, resiliência)
- [DEC-009-stack-tecnologica-frontend.md](../decisions/DEC-009-stack-tecnologica-frontend.md) - Stack frontend
- [DEC-010-stack-tecnologica-backend.md](../decisions/DEC-010-stack-tecnologica-backend.md) - Stack backend

## Definições Utilizadas

- [DEF-22-desempenho-fiabilidade.md](../definitions/DEF-22-desempenho-fiabilidade.md) - Detalhes completos
- [DEF-04-requisitos-nao-funcionais.md](../definitions/DEF-04-requisitos-nao-funcionais.md) - NFRs de performance
- [DEF-15-padroes-resiliencia.md](../definitions/DEF-15-padroes-resiliencia.md) - Padrões de resiliência

## Itens Pendentes

| Item | Responsável | Prioridade |
|------|-------------|------------|
| **Calibração de métricas de performance** | Cliente/Infraestrutura | Alta |
| Obter throughput real da app mobile (normal e pico) | Cliente | Alta |
| Padrões de sazonalidade (fim de mês, períodos fiscais) | Cliente | Média |
