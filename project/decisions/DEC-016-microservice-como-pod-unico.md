---
id: "DEC-016"
title: "MicroService como Pod Único"
status: "accepted"
created: 2026-04-17
context: "DEF-12"
affects-definitions:
  - "DEF-12"
  - "DEF-19"
affects-sections:
  - "SEC-03"
  - "SEC-05"
  - "SEC-09"
---

# DEC-016: MicroService como Pod Único

## Context

A arquitectura do HomeBanking Web inicialmente descrevia uma camada de "Microservices" (plural), sugerindo potencialmente múltiplos serviços autónomos de lógica de negócio. Esta terminologia plural criava ambiguidade sobre quantos componentes seriam efectivamente desenvolvidos e deployados.

Para a entrega inicial, é necessário clarificar que esta camada consiste num único componente, e estabelecer o seu posicionamento na topologia de rede: o MicroService fica **atrás do API Gateway IBM**, tal como o Siebel. O BFF não acede directamente ao MicroService — fá-lo sempre via Gateway.

## Decision

A camada de lógica de negócio é constituída por **um único MicroService** (.NET 8), deployado como um único Pod em OpenShift, posicionado atrás do API Gateway IBM.

- O componente denomina-se **"MicroService"** (singular)
- É um único Pod em OpenShift, não uma colecção de microserviços
- Responsável por lógica de negócio além das capacidades do Siebel
- **Acedido pelo BFF via API Gateway IBM**, usando Protocolo Omni (não directamente)
- O API Gateway IBM roteia para Siebel **e** para o MicroService
- Todas as referências a "Microservices" (plural) no documento são substituídas por "MicroService" (singular)

## Consequences

- Deploy simplificado: um único container/Pod a gerir em OpenShift
- Codebase único para toda a lógica de negócio do canal web
- A separação arquitectural BFF (orquestração/apresentação) vs MicroService (lógica de negócio) mantém-se inalterada
- O API Gateway IBM deixa de ser exclusivamente para Siebel — é o ponto de entrada para Siebel e MicroService
- A nota "API Gateway apenas para Siebel" em DEF-12 e em diagramas deve ser rectificada
- Todas as secções e definições do documento devem reflectir o singular "MicroService" e o acesso via Gateway
