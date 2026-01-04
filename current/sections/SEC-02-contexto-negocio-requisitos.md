---
aliases:
  - Contexto de Negocio e Requisitos
tags:
  - nextreality-novobanco-website-sections
  - sections
  - business-context
  - requirements
approved: true
created: 2026-01-01
hubs:
  - "[[nextreality]]"
para-code: R
reviewed: true
status: in-progress
---

# 2. Contexto de Negocio & Requisitos

> **Definicoes requeridas:**
> - [DEF-02-stakeholders.md](../definitions/DEF-02-stakeholders.md) - Status: in-progress
> - [DEF-02-requisitos-funcionais.md](../definitions/DEF-02-requisitos-funcionais.md) - Status: completed
> - [DEF-02-requisitos-nao-funcionais.md](../definitions/DEF-02-requisitos-nao-funcionais.md) - Status: completed
>
> **Decisoes relacionadas:**
> - Nenhuma decisao arquitetural nesta secao (requisitos e contexto de negocio)

## Proposito

Descrever o contexto da solucao HomeBanking Web, suas partes interessadas, requisitos funcionais e nao funcionais, restricoes e dependencias.

## Conteudo

### 2.1 Contexto de Negocio

O projeto HomeBanking Web visa disponibilizar aos clientes do Novo Banco uma plataforma web com funcionalidades equivalentes a aplicacao mobile nativa existente. A solucao reutilizara a infraestrutura e servicos ja criados para a app mobile.

**Drivers de Negocio:**
- Oferecer canal alternativo ao mobile para clientes que preferem acesso via browser
- Paridade funcional entre canais para experiencia consistente
- Reutilizacao de investimentos ja realizados na infraestrutura mobile

### 2.2 Partes Interessadas (Stakeholders)

| Stakeholder | Papel | Status |
|-------------|-------|--------|
| Sponsors | _A definir_ | Pendente |
| Equipas Tecnicas | _A definir_ | Pendente |
| Operacoes | _A definir_ | Pendente |
| Areas de Negocio | _A definir_ | Pendente |
| Utilizadores Finais | Clientes do Novo Banco | Definido |
| Entidades Externas | Nao aplicavel | Definido |

**Nota:** O projeto nao envolve diretamente entidades externas (reguladores, parceiros, fornecedores). As integracoes com terceiros sao as ja existentes na app mobile.

### 2.3 Requisitos Funcionais

#### 2.3.1 Funcionalidades por Categoria

| Categoria | Funcionalidades | Quantidade |
|-----------|-----------------|------------|
| **Autenticacao** | Registo, Login, Recuperacao de Acessos | 3 |
| **Areas Principais** | Home, Area Pessoal, Dashboard | 3 |
| **Patrimonio** | Patrimonio, Carteiras, Saldos e Movimentos | 3 |
| **Operacoes** | Ordens Pendentes, Historico de Operacoes, Confirmacao de Operacoes | 3 |
| **Documentos** | Comprovativos e Extratos | 2 |
| **Investimentos** | Warrants, Acoes, ETF, Fundos, Obrigacoes, Indices, Temas Investimento, Deposito a Prazo, Leiloes, Ofertas Publicas, Unit Linked, Robot Advisor, BTP | 13 |
| **Pagamentos** | Transferencias, Pagamentos, Carregamentos, MBWay (nao-SDK) | 4 |
| **Outros** | Outros Bancos, Eventos Corporativos, Seguros de Protecao, Area do Viajante, Bea, Wishlist, Noticias Externas | 7 |
| **TOTAL** | | **35** |

#### 2.3.2 Estrategia de Priorizacao

- **Criterio:** Priorizacao por dependencia entre funcionalidades
- **MVP:** Todas as 35 funcionalidades fazem parte do MVP
- **Funcionalidades Exclusivas Web:** Nenhuma (paridade com mobile)

#### 2.3.3 Suporte Multi-idioma

| Idioma | Prioridade |
|--------|------------|
| Portugues | Principal |
| Ingles | Secundario |
| Espanhol | Secundario |

#### 2.3.4 Acessibilidade

- **Status:** _A definir_ - Requer aprofundamento
- **Referencia:** WCAG 2.1 AA (a considerar)

### 2.4 Requisitos Nao Funcionais

#### 2.4.1 Performance

| Metrica | Valor | Observacao |
|---------|-------|------------|
| Tempo resposta operacoes criticas | max 3 segundos | Transacoes, consultas |
| Throughput | 10 TPS | Transacoes por segundo |
| Tempo carregamento pagina inicial | max 10 segundos | First Contentful Paint |

#### 2.4.2 Disponibilidade

| Metrica | Valor | Observacao |
|---------|-------|------------|
| SLA Disponibilidade | 99.9% | ~8.76 horas downtime/ano |
| RTO | 30 minutos | Recovery Time Objective |
| RPO | 5 minutos | Recovery Point Objective |
| Janelas Manutencao | Sim | Programadas |

#### 2.4.3 Escalabilidade

| Metrica | Valor | Observacao |
|---------|-------|------------|
| Utilizadores concorrentes | 400 | Baseline |
| Crescimento anual | 5% | Projecao 3 anos |
| Picos de utilizacao | Sim | Fim de mes, periodos fiscais |

#### 2.4.4 Seguranca

| Requisito | Status | Observacao |
|-----------|--------|------------|
| Certificacoes | _A definir_ | ISO 27001, PCI-DSS a considerar |
| Encriptacao | _A definir_ | TLS 1.3, AES-256 a considerar |
| Retencao de logs | _A definir_ | 7 anos (tipico bancario) a validar |

#### 2.4.5 Compatibilidade

| Requisito | Especificacao |
|-----------|---------------|
| Browsers | Chrome, Edge, Safari (versoes atuais + 2 anteriores) |
| Responsividade | Design responsivo obrigatorio |
| Dispositivos moveis | Suporte via design responsivo |

### 2.5 Restricoes

| Tipo | Restricao | Impacto |
|------|-----------|---------|
| **Tecnica** | Reutilizacao de APIs e servicos da app mobile | Define integracao com backend existente |
| **Tecnica** | Tecnologias 100% Web (sem componentes nativos) | MBWay SDK out-of-scope |
| **Regulatoria** | Conformidade PSD2 | Autenticacao forte (SCA) obrigatoria |
| **Regulatoria** | Regulamentacoes Banco de Portugal | Requisitos de seguranca e auditoria |

### 2.6 Pressupostos

| ID | Pressuposto | Validado |
|----|-------------|----------|
| P1 | APIs da app mobile estao disponiveis e documentadas | A validar |
| P2 | Infraestrutura existente suporta canal web adicional | A validar |
| P3 | Requisitos de seguranca sao os mesmos da app mobile | A validar |
| P4 | Nao ha necessidade de novas integracoes com terceiros | Sim |

### 2.7 Dependencias

```plantuml
@startuml
skinparam backgroundColor #FEFEFE

package "HomeBanking Web" {
    [Frontend Web] as FE
}

package "Dependencias Existentes" {
    [API Gateway] as APIGW
    [Backend Services] as BE
    [Core Banking] as CORE
    [Servicos Terceiros\n(KYC, Cartoes, etc)] as THIRD
}

FE --> APIGW : Depende
APIGW --> BE : Depende
BE --> CORE : Depende
BE --> THIRD : Depende

note right of FE
  Nova componente
end note

note right of APIGW
  Componentes existentes
  (app mobile)
end note
@enduml
```

| Dependencia | Tipo | Critica |
|-------------|------|---------|
| API Gateway | Infraestrutura existente | Sim |
| Backend Services | Servicos existentes | Sim |
| Core Banking | Sistema legado | Sim |
| Servicos Terceiros | Integracoes existentes | Sim |

## Entregaveis

- [x] Descricao do contexto de negocio
- [ ] Matriz de stakeholders com papeis e responsabilidades (parcial)
- [x] Lista priorizada de requisitos funcionais
- [x] Lista de requisitos nao funcionais com metricas
- [x] Documentacao de restricoes tecnicas e de negocio
- [x] Lista de pressupostos validados
- [x] Mapa de dependencias

## Definicoes Utilizadas

- [ ] [DEF-02-stakeholders.md](../definitions/DEF-02-stakeholders.md) - Status: in-progress (informacoes pendentes)
- [x] [DEF-02-requisitos-funcionais.md](../definitions/DEF-02-requisitos-funcionais.md) - Status: completed
- [x] [DEF-02-requisitos-nao-funcionais.md](../definitions/DEF-02-requisitos-nao-funcionais.md) - Status: completed

## Decisoes Referenciadas

_Nenhuma decisao arquitetural nesta secao. Esta secao documenta contexto de negocio, requisitos funcionais e nao funcionais, que sao inputs para decisoes arquiteturais nas secoes seguintes._

## Itens Pendentes

Os seguintes itens requerem informacao adicional:

| Item | Documento | Responsavel |
|------|-----------|-------------|
| Stakeholders (sponsors, equipas, governacao) | DEF-02-stakeholders | Gestao do Projeto |
| Requisitos de Acessibilidade WCAG | DEF-02-requisitos-funcionais | Equipa UX |
| Certificacoes de Seguranca | DEF-02-requisitos-nao-funcionais | Area de Seguranca |
| Requisitos de Encriptacao | DEF-02-requisitos-nao-funcionais | Area de Seguranca |
| Politica de Retencao de Logs | DEF-02-requisitos-nao-funcionais | Compliance |
