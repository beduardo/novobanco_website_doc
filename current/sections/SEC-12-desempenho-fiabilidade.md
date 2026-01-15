---
id: SEC-12-desempenho-fiabilidade
aliases:
  - Desempenho e Fiabilidade
tags:
  - nextreality-novobanco-website-sections
  - sections
  - performance
  - reliability
  - scalability
approved: true
created: 2026-01-08
hubs:
  - "[[nextreality]]"
para-code: R
reviewed: true
status: completed
---

# 12. Desempenho & Fiabilidade

> **Definicao:** [DEF-12-desempenho-fiabilidade.md](../definitions/DEF-12-desempenho-fiabilidade.md)

## Proposito

Definir os objetivos de desempenho e a estrategia de fiabilidade do HomeBanking Web, incluindo targets de performance, caching, auto-scaling e testes de carga.

## Conteudo

### 12.1 Objetivos de Desempenho

Os targets sao baseados nos requisitos nao funcionais (DEF-02):

| Metrica | Target | Fonte |
|---------|--------|-------|
| **Utilizadores Concorrentes** | 400 | DEF-02 |
| **Throughput** | 10 TPS | DEF-02 |
| **Tempo de Resposta (P95)** | < 3 segundos | DEF-02 |
| **Tempo de Carregamento Inicial** | < 10 segundos | DEF-02 |
| **Disponibilidade** | 99.9% | DEF-02 |
| **Crescimento Anual** | 5% | DEF-02 |

### 12.2 Core Web Vitals

| Metrica | Target | Classificacao |
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
- Fim de mes
- Periodos fiscais
- Campanhas
end note

@enduml
```

### 12.4 Estrategia de Cache

```plantuml
@startuml
skinparam backgroundColor white

title Camadas de Cache

actor User
participant "Browser" as browser
participant "CDN" as cdn
participant "BFF" as bff
database "Redis" as redis
participant "Backend" as api

User -> browser : Request
browser -> browser : Local Storage\n(sessao, prefs)
browser -> cdn : Static assets\n(js, css, images)
cdn --> browser : Cache hit

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

#### Niveis de Cache

| Nivel | Dados | TTL |
|-------|-------|-----|
| **Browser** | Assets estaticos (JS, CSS, imagens) | Longo (com cache busting) |
| **Browser** | Local Storage (sessao, prefs) | Sessao |
| **CDN** | JS, CSS, imagens, fontes | 24 horas |
| **BFF (Redis)** | Sessoes, tokens, dados partilhados | Variavel |

#### TTL por Tipo de Dado (Redis)

| Dado | TTL | Justificacao |
|------|-----|--------------|
| Sessao do utilizador | 10 min | Inatividade timeout |
| Tokens OAuth | Variavel | Alinhado com expiracao |
| Configuracoes do sistema | 5 min | Baixa frequencia de mudanca |
| Dados de referencia (paises, bancos) | 1 hora | Dados estaticos |
| Cotacoes/Taxas | 1 min | Dados volateis |

**Principio:** Dados sensiveis (contas, transacoes) NAO sao cacheados.

#### Cache Invalidation

| Evento | Acao |
|--------|------|
| Logout | Invalidar sessao no Redis |
| Transacao executada | Invalidar cache de saldos (se aplicavel) |
| Deploy | Versionar assets (cache busting) |
| Configuracao alterada | Invalidar cache de config |

### 12.5 Otimizacao Frontend

#### Bundle Optimization

| Tecnica | Implementacao | Impacto |
|---------|---------------|---------|
| Code Splitting | React.lazy() + Suspense | Reduz initial bundle |
| Tree Shaking | Webpack/Vite config | Remove codigo nao utilizado |
| Lazy Loading | Componentes e rotas | Carrega sob demanda |
| Minification | Terser (JS), CSSNano | Reduz tamanho |
| Compression | gzip/Brotli | 70-90% reducao |

#### Budget de Bundle

| Metrica | Limite | Acao se exceder |
|---------|--------|-----------------|
| Initial JS | < 200KB (gzipped) | Code split |
| Initial CSS | < 50KB (gzipped) | Purge CSS |
| Largest chunk | < 100KB | Split ou lazy load |
| Total assets | < 1MB | Review dependencies |

#### Otimizacao de Assets

| Asset | Estrategia |
|-------|------------|
| Imagens | WebP format, lazy loading, srcset |
| Fontes | WOFF2, font-display: swap, subset |
| Icons | SVG sprite ou icon font |
| CSS | Critical CSS inline, defer restante |

### 12.6 Otimizacao Backend (BFF)

#### Connection Pooling

| Conexao | Pool Size | Timeout |
|---------|-----------|---------|
| Redis | 10-20 | 5s |
| HTTP Client (Backend) | 100 | 30s |

#### Compressao

| Tipo | Configuracao |
|------|--------------|
| Response | gzip (nivel 6) |
| Threshold | > 1KB |
| Content-Types | application/json, text/html |

#### Async/Non-blocking

```plantuml
@startuml
skinparam backgroundColor white

title Pattern: Async Processing

participant "BFF" as bff
participant "Backend API" as api1
participant "Backend API 2" as api2
participant "Backend API 3" as api3

bff -> api1 : Request 1 (async)
bff -> api2 : Request 2 (async)
bff -> api3 : Request 3 (async)

api1 --> bff : Response 1
api2 --> bff : Response 2
api3 --> bff : Response 3

bff -> bff : Aggregate results
note right: Task.WhenAll() em .NET

@enduml
```

### 12.7 Auto-Scaling

| Aspecto | Abordagem |
|---------|-----------|
| **Mecanismo** | Horizontal Pod Autoscaler (HPA) |
| **Metricas** | CPU, Memory |
| **CPU Target** | 70% |
| **Memory Target** | 80% |

#### Configuracao por Componente

| Componente | Min Replicas | Max Replicas | CPU Target | Memory Target |
|------------|--------------|--------------|------------|---------------|
| Frontend | 2 | 6 | 70% | 80% |
| BFF | 2 | 10 | 70% | 80% |

#### Scale-up vs Scale-down

| Evento | Tempo | Acao |
|--------|-------|------|
| Scale-up | 60s estabilizacao | Duplicar replicas |
| Scale-down | 300s estabilizacao | Reduzir 50% |

> **Nota:** Scale-down mais conservador para evitar oscilacoes.

### 12.8 Capacity Planning

#### Resource Requests/Limits

| Componente | CPU Request | CPU Limit | Memory Request | Memory Limit |
|------------|-------------|-----------|----------------|--------------|
| Frontend | 100m | 500m | 128Mi | 256Mi |
| BFF | 250m | 1000m | 256Mi | 512Mi |

#### Estimativa de Recursos (400 users)

| Componente | Pods | CPU Total | Memory Total |
|------------|------|-----------|--------------|
| Frontend | 2 | 1 vCPU | 512Mi |
| BFF | 4 | 4 vCPU | 2Gi |
| **Total** | 6 | **5 vCPU** | **2.5Gi** |

### 12.9 Resiliencia

| Padrao | Implementacao |
|--------|---------------|
| **Circuit Breaker** | Polly (.NET) |
| **Retry** | Exponential backoff (3 tentativas) |
| **Timeout** | Configuravel por endpoint |
| **Bulkhead** | Limite de conexoes |
| **Health Checks** | Liveness + Readiness probes |

#### Pod Disruption Budget

| Aspecto | Configuracao |
|---------|--------------|
| minAvailable | 50% |
| Proposito | Garantir disponibilidade durante manutencao |

### 12.10 Load Testing

#### Ferramenta

| Ferramenta | Uso | Justificacao |
|------------|-----|--------------|
| **k6** | Load testing principal | Scripting em JS, integracao CI/CD |

#### Cenarios de Teste

| Cenario | Users | Duracao | Objetivo |
|---------|-------|---------|----------|
| Smoke | 10 | 5 min | Validar ambiente |
| Load | 400 | 30 min | Validar capacidade nominal |
| Stress | 600 | 15 min | Identificar limites |
| Soak | 200 | 4 horas | Identificar memory leaks |

#### Criterios de Aceitacao

| Metrica | Criterio | Fail |
|---------|----------|------|
| Response Time P95 | < 3s | > 5s |
| Error Rate | < 0.1% | > 1% |
| Throughput | >= 10 TPS | < 8 TPS |
| CPU (peak) | < 80% | > 90% |
| Memory (peak) | < 80% | > 90% |

## Decisoes Referenciadas

- [DEC-006-estrategia-containers-openshift.md](../decisions/DEC-006-estrategia-containers-openshift.md) - Containers e auto-scaling
- [DEC-007-padrao-bff.md](../decisions/DEC-007-padrao-bff.md) - BFF (cache, resiliencia)
- [DEC-009-stack-tecnologica-frontend.md](../decisions/DEC-009-stack-tecnologica-frontend.md) - Stack frontend
- [DEC-010-stack-tecnologica-backend.md](../decisions/DEC-010-stack-tecnologica-backend.md) - Stack backend

## Definicoes Utilizadas

- [DEF-12-desempenho-fiabilidade.md](../definitions/DEF-12-desempenho-fiabilidade.md) - Detalhes completos
- [DEF-02-requisitos-nao-funcionais.md](../definitions/DEF-02-requisitos-nao-funcionais.md) - NFRs de performance
- [DEF-05-padroes-resiliencia.md](../definitions/DEF-05-padroes-resiliencia.md) - Padroes de resiliencia
