# Document Comments

## Comment 1

**Location:** Paragraph 1767

**Author:** Jorge Gomes Costa (novobanco DSI Direção) | **Date:** 2026-02-19 12:06:00

**Commented text:**

> BFF (Backend for Frontend)

**Comment:**

O API strategy não será o BFF de forma genérica. BFF será para o UI react.

---

## Comment 2

**Location:** Paragraph 1791

**Author:** Jorge Gomes Costa (novobanco DSI Direção) | **Date:** 2026-02-19 12:06:00

**Commented text:**

> Via BFF apenas

**Comment:**

BFF ou MS

---

## Comment 3

**Location:** Paragraph 1871

**Author:** Jorge Gomes Costa (novobanco DSI Direção) | **Date:** 2026-02-19 12:10:00

**Comment:**

Tirando o BFF, penso que o principio a colocar em cima da mesa e que tudo irá via APIGW.
A APIGW não será apenas para SIEBEL mas tambem para os MS

---

## Comment 4

**Location:** Paragraph 1871

**Author:** Jorge Gomes Costa (novobanco DSI Direção) | **Date:** 2026-02-19 12:10:00

**Comment:**

Ou serviços azure

---

## Comment 5

**Location:** Paragraph 1871

**Author:** Jorge Gomes Costa (novobanco DSI Direção) | **Date:** 2026-02-19 12:11:00

**Comment:**

Este diagrama representa que só temos 1 único BFF e um único MS para todo o BEST?

---

## Comment 6

**Location:** Paragraph 1933

**Author:** Jorge Gomes Costa (novobanco DSI Direção) | **Date:** 2026-02-19 12:13:00

**Commented text:**

> OAuth + SHA256: Utilizado para comunicação BFF↔ApiPsd2 (autenticação) - OAuth 1.1 HMAC: Utilizado para comunicação BFF↔ApiBBest (APIs bancárias)

**Comment:**

Não estou a conseguir relacionar estes Oauth com o que falámos. Qual a diferença entre os 2?

---

## Comment 7

**Location:** Paragraph 2015

**Author:** Jorge Gomes Costa (novobanco DSI Direção) | **Date:** 2026-02-19 12:16:00

**Commented text:**

> Lookup por token_sessao_spa → tokens do utilizador

**Comment:**

A avaliar

---

## Comment 8

**Location:** Paragraph 2079

**Author:** Jorge Gomes Costa (novobanco DSI Direção) | **Date:** 2026-02-19 12:24:00

**Commented text:**

> Siebel

**Comment:**

Ou pelo MS nos pedidos em que ele for responsável ou mediar a resposta.

---

## Comment 9

**Location:** Paragraph 2110

**Author:** Jorge Gomes Costa (novobanco DSI Direção) | **Date:** 2026-02-19 12:25:00

**Commented text:**

> Identificar quais serviços Azure são acedidos diretamente pelo BFF

**Comment:**

Para trabalhar neste sentido era importante inventariar os serviços que são usados que não passem pela gateway atual do best, quer sejam azure ou outros.

---

## Comment 10

**Location:** Paragraph 2222

**Author:** Jorge Gomes Costa (novobanco DSI Direção) | **Date:** 2026-02-19 12:26:00

**Commented text:**

> Lógica de Negócio, regras de domínio

**Comment:**

Quando não passíveis de serem implementadas no siebel

---

## Comment 11

**Location:** Paragraph 2236

**Author:** Jorge Gomes Costa (novobanco DSI Direção) | **Date:** 2026-02-19 12:26:00

**Commented text:**

> Roteamento para Siebel

**Comment:**

Ou MS

---

## Comment 12

**Location:** Paragraph 2407

**Author:** Jorge Gomes Costa (novobanco DSI Direção) | **Date:** 2026-02-19 12:27:00

**Commented text:**

> SCA 

**Comment:**

Era importante detalhar o fluxo do sca

---

## Comment 13

**Location:** Paragraph 2735

**Author:** Jorge Gomes Costa (novobanco DSI Direção) | **Date:** 2026-02-19 12:28:00

**Commented text:**

> Fluxos da app mobile replicados na web

**Comment:**

Isto é verdade?

---

## Comment 14

**Location:** Paragraph 2910

**Author:** Jorge Gomes Costa (novobanco DSI Direção) | **Date:** 2026-02-19 12:29:00

**Commented text:**

> Criticidade

**Comment:**

O que representa esta coluna? O que quer dizer criticidade media, por exemplo?

---

## Comment 15

**Location:** Paragraph 3109

**Author:** Jorge Gomes Costa (novobanco DSI Direção) | **Date:** 2026-02-19 12:30:00

**Commented text:**

> Não há retry automático com backoff exponencial para operações falhadas 

**Comment:**

Isto existe na versão nativa app?

---

## Comment 16

**Location:** Paragraph 3146

**Author:** Jorge Gomes Costa (novobanco DSI Direção) | **Date:** 2026-02-19 12:32:00

**Commented text:**

> Stack Tecnológica

**Comment:**

Não representa o acordado

---

## Comment 17

**Location:** Paragraph 4101

**Author:** Jorge Gomes Costa (novobanco DSI Direção) | **Date:** 2026-02-19 12:36:00

**Commented text:**

> .NET 8

**Comment:**

10

---

## Comment 18

**Location:** Paragraph 4332

**Author:** Jorge Gomes Costa (novobanco DSI Direção) | **Date:** 2026-02-19 12:40:00

**Commented text:**

> /api/v1/├── auth/│   ├── login│   ├── logout│   ├── refresh│   └── validate├── accounts/│   ├── {id}│   ├── {id}/balance│   └── {id}/movements├── payments/│   ├── transfers│   └── bills├── investments/│   ├── portfolio│   ├── orders│   └── products└── documents/    ├── statements    └── receipts

**Comment:**

Se isto é do BFF a estrutura não será assim, pelo menos os primeiros niveis. Há-de ser qq coisa como /web/ocb/<servicobest>/best como prefixo. Daí para baixo é que se poderá criar essa estrutura. Tiraria o api para ficar consistente com o resto e assumia o v1 para todos. Faria o versionamento ao serviço e não ao api

  ### Reply

  **Author:** Jorge Gomes Costa (novobanco DSI Direção) | **Date:** 2026-02-19 12:43:00

  **Commented text:**

  > /api/v1/├── auth/│   ├── login│   ├── logout│   ├── refresh│   └── validate├── accounts/│   ├── {id}│   ├── {id}/balance│   └── {id}/movements├── payments/│   ├── transfers│   └── bills├── investments/│   ├── portfolio│   ├── orders│   └── products└── documents/    ├── statements    └── receipts

  **Comment:**

  Ou serviço ou ao resource se forem por abordagem rest. Ja agora, em contexto de arquitetura, a recomendaçao que nos deram é usar POST

---

## Comment 19

**Location:** Paragraph 4342

**Author:** Jorge Gomes Costa (novobanco DSI Direção) | **Date:** 2026-02-19 12:41:00

**Comment:**

Convinha tornar claro que o bearer passa na chamada à apigw e de onde vem. No diagrama como está parece que a apigw gera um bearer que não tem qq relação com o que acontece antes

---

## Comment 20

**Location:** Paragraph 4374

**Author:** Jorge Gomes Costa (novobanco DSI Direção) | **Date:** 2026-02-19 12:44:00

**Commented text:**

> Cookie de sessao (HttpOnly, Secure)

**Comment:**

Origem?

---

## Comment 21

**Location:** Paragraph 4408

**Author:** Jorge Gomes Costa (novobanco DSI Direção) | **Date:** 2026-02-19 12:44:00

**Commented text:**

> Bearer Token (propagado)

**Comment:**

Origem?

  ### Reply

  **Author:** Jorge Gomes Costa (novobanco DSI Direção) | **Date:** 2026-02-19 12:46:00

  **Commented text:**

  > Bearer Token (propagado)

  **Comment:**

  Era importante descrever de onde isto vem e como e calculado

---

## Comment 22

**Location:** Paragraph 5209

**Author:** Jorge Gomes Costa (novobanco DSI Direção) | **Date:** 2026-02-19 12:46:00

**Commented text:**

> Canal web consome os mesmos backend services e modelo de domínio

**Comment:**

A app a nivel da apigw, o react a nivel do bff.

---

## Comment 23

**Location:** Paragraph 5588

**Author:** Jorge Gomes Costa (novobanco DSI Direção) | **Date:** 2026-02-19 12:47:00

**Commented text:**

> equipa de autenticação do NovoBanco.

**Comment:**

???

---

## Comment 24

**Location:** Paragraph 5723

**Author:** Jorge Gomes Costa (novobanco DSI Direção) | **Date:** 2026-02-19 17:37:00

**Commented text:**

> /auth/qr-code/status/{sessionId}

**Comment:**

Não consegui ver o fluxo com detalhe e não é claro o que e esta session nem tempos de vida etc. mas normalmente é ma pratica ter session no url

---

## Comment 25

**Location:** Paragraph 6397

**Author:** Jorge Gomes Costa (novobanco DSI Direção) | **Date:** 2026-02-19 17:41:00

**Comment:**

Este oauth server já existe atualmente e fazem refresh do token?

---

## Comment 26

**Location:** Paragraph 8200

**Author:** Jorge Gomes Costa (novobanco DSI Direção) | **Date:** 2026-02-19 18:05:00

**Commented text:**

> acedida directamente pelo BFF via Protocolo Omni

**Comment:**

Estaria por detrás da apigw, pelo menos pelo diagrama inicial?
O que querem dizer com diretamente neste contexto

---

## Comment 27

**Location:** Paragraph 8931

**Author:** Jorge Gomes Costa (novobanco DSI Direção) | **Date:** 2026-02-19 19:01:00

**Comment:**

Estão a colocar o authservice porque é o que guarda/calcula o token para enviar para o siebel. Têm a certeza que o siebel consegue validar o token? Se não der o ms deverá estar atrás da apigw

---

## Comment 28

**Location:** Paragraph 9062

**Author:** Jorge Gomes Costa (novobanco DSI Direção) | **Date:** 2026-02-19 19:04:00

**Commented text:**

> A aplicação utiliza três ambientes, segregados por namespaces no cluster OpenShift.AmbientePropósitoNamespacePromoçãodevDesenvolvimento e integraçãobest-web-devAutomática (CI)qaTestes integrados e UATbest-web-qaAutomática (após dev OK)prodProduçãobest-web-prodManual (aprovação)

**Comment:**

Este tema de infra tem várias incorreções e penso que não fará muito sentido estar neste documento. Por exemplo a nomeclatura dos namespaces poderá não ser esta. Vem da equipa de infra.

---

## Comment 29

**Location:** Paragraph 9378

**Author:** Jorge Gomes Costa (novobanco DSI Direção) | **Date:** 2026-02-19 19:05:00

**Commented text:**

> RollbackAutomático via Kubernetes

**Comment:**

E bd se houver?

---

