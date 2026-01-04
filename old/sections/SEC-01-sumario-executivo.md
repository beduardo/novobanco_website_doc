---
id: SEC-01-sumario-executivo
aliases:
  - Novo Banco Sumario Executivo
tags:
  - nextreality-novobanco-website-sections
approved: true
created: 2025-12-22
hubs:
  - "[[nextreality]]"
para-code: R
reviewed: true
---
# 01. Sumario Executivo > **Status:** estrutura
> **Definicoes necessarias:** DEF-01-business-objectives.md, DEF-01-solution-scope.md

## Proposito
Com a necessidade de upgrade do Siebel, abriu-se a oportunidade de criar as bases para um novo sistema de homebanking tendo como princípio orientador, ser o mais semelhante possível à APP móvel. 


---

## Conteudo

### Objetivos do Documento
O presente documento visa criar um workbook de registo do levantamento das componentes criticas da APP e sua declinação para uma arquitetura de sistemas baseado em tecnologias 100% web.

### Visao Geral da Solucao
_Aguardando informacoes das definicoes_

### Stack Tecnologica
_Aguardando informacoes das definicoes_

### Diagrama de Contexto (C4 Level 1)
```plantuml
@startuml
!include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/master/C4_Component.puml

HIDE_STEREOTYPE()
LAYOUT_LEFT_RIGHT()

' === Person ===
Person(client, "Cliente autenticado", "Utilizador autenticado via Portal / App")

' === Containers ===
Boundary(clientSolution, "Banking Client Access") {
    Container(appMobile, "App Mobile", "iOS / Android", "APP")
    Container(webSite, "WebSite", "React + .NET", "A aplicação que iremos construir")
}
Boundary(solutionDependencies, "Dependencies") {
    Container(blob, "Blob Storage", "Azure Blob Storage", "Cofre de Chaves e Tokens")
    System_Ext(extSystems, "Sistemas Externos", "Seguros / BTP / MBWay / Visa / Firebase / Google Maps")
    Component(apisEstaticas, "APIs Estáticas", "Software System", "Têm dados que decidimos não colocar na APP em JSON")
    Container(backoffice, "Backoffice de Gestão", "Componente Angular + .NET C# + SQL Server")
    Container(siebel, "Siebel", "Component: IBM")
    ContainerDb(coreBanking, "BB Core Banking", "Conta Bancária: Oracle", "Core Banking")
}
' === Relationships ===
Rel(client, clientSolution, "")
Rel(clientSolution, solutionDependencies, "")
'Rel(clientSolution, blob, "")
'Rel(clientSolution, extSystems, "")
'Rel(clientSolution, apisEstaticas, "")
'Rel(clientSolution, backoffice, "")
'Rel(clientSolution, siebel, "")
Rel(siebel, coreBanking, "")

@enduml
```

### Ambito do Projeto

#### Sistemas Incluidos
- Website: O sistema que iremos produzir
- App Mobile: App existente de onde iremos extrair as as features e requisitos para implementação das regras de negócio
- Siebel: Sistema de ligação ao Core e que rege o site
- Sistema de Ficheiros: Imagens de produtos e PDF
- Backoffice de Gestão: Conteúdos e regras
- Blob Storage: Chaves e Secrets
- API Estáticas: Listas de Valores
- Sistemas Externos: Seguros, BTP, MBWay, Visa, Firebase, Google Maps, Google API

### Value Proposition
_Aguardando informacoes das definicoes_

### Metricas de Sucesso (KPIs)
_Aguardando informacoes das definicoes_

### Principais Decisoes Arquiteturais
_Aguardando informacoes das definicoes_

### Restricoes Conhecidas
_Aguardando informacoes das definicoes_

---

## Entregaveis

- [ ] Documento executivo com sintese da solucao
- [x] Diagrama de contexto (C4 Level 1)
- [ ] Lista de sistemas no ambito vs fora de ambito
- [ ] Value proposition e beneficios esperados

---

## Definicoes Utilizadas

- [ ] [DEF-01-business-objectives.md](../definitions/DEF-01-business-objectives.md) - Status: estrutura
- [ ] [DEF-01-solution-scope.md](../definitions/DEF-01-solution-scope.md) - Status: estrutura
- [ ] [DEF-01-c4-context-diagram.md](../definitions/DEF-01-c4-context-diagram.md) - Status: estrutura
---

## Navegacao

| Anterior | Proximo |
|----------|---------|
| - | [02. Contexto de Negocio & Requisitos](SEC-02-contexto-negocio-requisitos.md) |
