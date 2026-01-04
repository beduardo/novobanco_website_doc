---
id: DEF-01-c4-context-diagram
aliases:
  - Novo Banco C4 Context Diagram
tags:
  - nextreality-novobanco-website-definitions
approved: true
created: 2025-12-22
hubs:
  - "[[nextreality]]"
para-code: R
reviewed: true
---
# DEF-01: Diagrama de Contexto C4

> **Status:** em-progresso
> **Secao relacionada:** 01 - Sumario Executivo

## Contexto

Este documento define o diagrama de contexto C4 (Level 1/2) da solucao, identificando os principais sistemas, atores e suas relacoes. O diagrama serve como visao de alto nivel da arquitetura.

## Questoes a Responder

1. Quais as principais interacoes entre o WebSite e cada sistema de dependencias?
2. O App Mobile e o WebSite partilham as mesmas APIs ou tem backends separados?
R.: O WebSite possui um Back For Front para fazer suas interações com os diversos backends. Ele acederá os mesmos recursos que o App. O Frontend React só utilizará o BFF.
3. Qual o papel exato do Blob Storage (apenas cofre de chaves/tokens ou tambem documentos)?
R.: SAS Storage (chaves) não será utilizado no site. Blob Storage armazena imagens e documentos, distribuídos por links presentes nas APIs.
4. Quais sistemas externos sao criticos para o MVP vs opcionais?
5. O Backoffice de Gestao interage diretamente com o WebSite ou sao independentes?
6. Qual a relacao entre Siebel e o WebSite (direta ou via Core Banking)?
R.: Não há relação direta com Core Banking. A relação com o Core Banking é 100% via Siebel.
7. As "APIs Estaticas" sao consumidas pelo WebSite? Qual o conteudo?
R.: São APIs que devem ser migradas para um dos sistemas a desenhar. Entregam listas de valores que servem para permitir seleção pelo utilizador.

## Diagrama Atual

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
    Container(blob, "Blob Storage", "Azure Blob Storage", "Imagens e Documentos (acesso via links nas APIs)")
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

## Decisoes

### Sistemas Externos Identificados
| Sistema | Tipo | Protocolo | Descricao | Usado no Site |
|---------|------|-----------|-----------|---------------|
| Seguros | Externo | API REST / HTTPS | Produto de consulta e subscrição | Sim |
| BTP | Externo | API REST / HTTPS | Produto de consulta e subscrição | Sim |
| MBWay | Externo | - | Pagamentos móveis | **Não** |
| Visa | Externo | - | Serviços de cartão | **Não** |
| Firebase | Externo | API REST | Registo de estatísticas de acesso | Sim |
| Google Maps | Externo | Biblioteca JS | Mapas para localização (ATMs, Balcões) | Sim |

> **Nota:** MBWay e Visa são funcionalidades exclusivas do App Mobile e não serão integrados no WebSite.

### Relacao App Mobile vs WebSite
- **Decisao:** _Pendente_ (APIs partilhadas / Backends separados)
- **Justificativa:** _Pendente_

### Papel do Blob Storage
- **Decisao:** Acesso indireto via links nas APIs (não há integração direta do WebSite)
- **Conteudo armazenado:** Imagens e documentos
- **Nota:** SAS Storage (chaves/tokens) não será utilizado pelo WebSite

### Papel das APIs Estaticas
- **Decisao:** A migrar para um dos sistemas a desenhar
- **Tipo de dados:** Listas de valores para seleção pelo utilizador (dropdowns, combos, etc.)
- **Consumo:** Sim, consumidas pelo WebSite

## Restricoes Conhecidas

- Stack WebSite: React + .NET (C#)
- App Mobile: iOS / Android nativo
- Core Banking: Oracle (acesso exclusivo via Siebel - sem integração direta)
- Backoffice: Angular + .NET C# + SQL Server
- Siebel: IBM - backend principal que abstrai o Core Banking

## Referencias

- [SEC-01-sumario-executivo.md](../sections/SEC-01-sumario-executivo.md)
- [architectural_document_structure_novo_banco.md](../architectural_document_structure_novo_banco.md)
