# Nao Conformidades - Comentarios JGC 2a Revisao (Word)

**Data:** 2026-03-02
**Origem:** Comentarios extraidos de novobanco-jcc-commented-20260219.md (documento Word comentado)
**Contexto:** Segunda revisao do documento HLD. O cliente (Jorge Gomes Costa - novobanco DSI Direcao) inseriu 29 comentarios no documento Word antes de parar a leitura no capitulo 9 por problemas persistentes.

---

## Resumo Executivo

Os 29 comentarios revelam **tres problemas estruturais** no documento:

1. **Papel do API Gateway incorreto** - O documento assume repetidamente que o APIGW e "apenas para Siebel", quando na realidade serve tambem os Microservices. Apenas o BFF e servicos Azure ficam fora.
2. **Falta de clareza nos fluxos de autenticacao** - Origens de tokens, propagacao de Bearer tokens, e fluxo SCA nao estao detalhados.
3. **Informacao nao alinhada com a realidade NB** - Stack frontend, versao .NET, estrutura de URLs, e detalhes de infraestrutura nao correspondem ao que existe ou foi acordado.

Os comentarios foram agrupados em **22 nao conformidades** por tema.

---

## NC-01: BFF Nao E a API Strategy Generica

**Gravidade:** ALTA
**Comentarios:** #1, #2
**Seccoes afetadas:** SEC-03 (3.1)

**Descricao:**
O documento apresenta o BFF como a API Strategy generica do sistema. O cliente esclarece que o BFF e especifico para o UI React. Os Microservices tem a sua propria estrategia. Alem disso, o acoplamento com sistemas legados nao e "Via BFF apenas", mas sim via BFF ou MS.

**O que o documento diz:**
- SEC-03 3.1: `API Strategy | BFF (Backend for Frontend) | Camada de agregacao especifica para o canal web, isolando sistemas legados`
- SEC-03 3.1: `Acoplamento Legados | Via BFF apenas`

**O que deveria dizer:**
- API Strategy: BFF para o canal web React; Microservices para logica de negocio nao implementavel em Siebel
- Acoplamento Legados: Via BFF ou MS

**Comentarios originais:**
- #1: "O API strategy nao sera o BFF de forma generica. BFF sera para o UI react."
- #2: "BFF ou MS"

**Acao requerida:**
1. Corrigir tabela de principios em SEC-03 3.1
2. Separar claramente o papel do BFF (frontend gateway) do papel dos MS (logica de negocio)

---

## NC-02: API Gateway Serve Siebel E Microservices

**Gravidade:** ALTA
**Comentarios:** #3, #4, #26
**Seccoes afetadas:** SEC-03 (3.2 diagrama, 3.3, 3.5), SEC-05 (5.4, 5.6), SEC-09 (9.1, 9.2, 9.8)

**Descricao:**
O documento afirma repetidamente que o API Gateway IBM e utilizado "apenas para Siebel". O cliente esclarece que o principio e que **tudo passa via APIGW, excepto o BFF e servicos Azure**. Ou seja, os Microservices tambem ficam por detras do API Gateway.

**Locais afetados no documento:**
- SEC-03 diagrama 3.2: nota `Apenas para Siebel` no API Gateway
- SEC-03 3.2 fluxo: `CAMADA_BFF --> GATEWAY : clientid + secret (Apenas Siebel)`
- SEC-03 3.3: `API Gateway | Roteamento para Siebel`
- SEC-03 3.5: `API Gateway (IBM) | Existente | Reutilizar | Apenas para Siebel`
- SEC-05 5.4 nota: "O API Gateway (IBM) e utilizado apenas para acesso aos Backend Services (Siebel)"
- SEC-09 9.1: `BFF → Microservices | Omni | Token de sessao | Logica de negocio (directo)`

**Comentarios originais:**
- #3: "Tirando o BFF, penso que o principio a colocar em cima da mesa e que tudo ira via APIGW. A APIGW nao sera apenas para SIEBEL mas tambem para os MS"
- #4: "Ou servicos azure" (excepcao ao APIGW)
- #26: "Estaria por detras da apigw, pelo menos pelo diagrama inicial?"

**Acao requerida:**
1. Atualizar diagrama de referencia (SEC-03 3.2) para mostrar MS atras do API Gateway
2. Remover todas as notas "apenas para Siebel" e substituir por "para Siebel e Microservices"
3. Atualizar todas as tabelas de comunicacao em SEC-03, SEC-05 e SEC-09
4. Fluxo: BFF → APIGW → MS (nao BFF → MS directo)
5. Excepcoes ao APIGW: apenas BFF e servicos Azure

---

## NC-03: Diagrama Sugere BFF e MS Unicos

**Gravidade:** MEDIA
**Comentario:** #5
**Seccoes afetadas:** SEC-03 (3.2)

**Descricao:**
O diagrama de referencia mostra uma unica caixa "BFF Web" e uma unica caixa "Microservices", sugerindo que existe apenas um BFF e um MS para todo o BEST. O cliente questiona se esta e a representacao pretendida.

**Comentario original:**
- #5: "Este diagrama representa que so temos 1 unico BFF e um unico MS para todo o BEST?"

**Acao requerida:**
1. Clarificar no diagrama ou legenda que os blocos representam **categorias** de componentes (ou confirmar com cliente se e de facto uma unica instancia)
2. Se houver multiplos MS, representar isso adequadamente (ex: "Microservices (N)")
3. Adicionar nota explicativa sobre a granularidade

---

## NC-04: Protocolos OAuth - Diferenciacao Confusa

**Gravidade:** MEDIA
**Comentario:** #6
**Seccoes afetadas:** SEC-03 (3.2 - Protocolos de Comunicacao)

**Descricao:**
A seccao de protocolos de comunicacao lista dois protocolos OAuth distintos para comunicacao com Siebel (OAuth + SHA256 e OAuth 1.1 HMAC) sem explicar claramente a diferenca entre eles. O cliente nao consegue relacionar com o que foi discutido.

**O que o documento diz:**
- "OAuth + SHA256: Utilizado para comunicacao BFF↔Siebel (autenticacao PSD2)"
- "OAuth 1.1 HMAC: Utilizado para comunicacao BFF↔Siebel (APIs bancarias)"

**Comentario original:**
- #6: "Nao estou a conseguir relacionar estes Oauth com o que falamos. Qual a diferenca entre os 2?"

**Acao requerida:**
1. Clarificar a diferenca entre os dois protocolos OAuth ou unificar se forem o mesmo
2. Validar com equipa tecnica se esta diferenciacao e correta
3. Se necessario, simplificar para um unico protocolo com descricao clara

---

## NC-05: Mecanismo de Lookup de Token a Avaliar

**Gravidade:** BAIXA
**Comentario:** #7
**Seccoes afetadas:** SEC-03 (3.2 - Fluxo de Autenticacao)

**Descricao:**
O mecanismo de lookup de token (token_sessao_spa → tokens do utilizador) no Redis esta marcado como necessitando avaliacao pelo cliente.

**O que o documento diz:**
- SEC-03 3.2 tabela: `BFF | Redis | Lookup por token_sessao_spa → tokens do utilizador`

**Comentario original:**
- #7: "A avaliar"

**Acao requerida:**
1. Marcar este mecanismo como pendente de validacao
2. Incluir na agenda da sessao tecnica com equipa NB

---

## NC-06: Responsabilidades MS vs Siebel - Roteamento e Logica de Negocio

**Gravidade:** ALTA
**Comentarios:** #8, #10, #11
**Seccoes afetadas:** SEC-03 (3.3), SEC-05 (5.1)

**Descricao:**
O documento atribui responsabilidades de forma incompleta. O API Gateway faz roteamento apenas para Siebel (deveria incluir MS). Os Microservices sao descritos como responsaveis por "Logica de Negocio, regras de dominio" sem qualificar que isto se aplica apenas quando nao e possivel implementar no Siebel. E o routing para backend nao considera MS como destino.

**O que o documento diz:**
- SEC-03 3.3: `Microservices | Backend | Logica de Negocio, regras de dominio`
- SEC-03 3.3: `API Gateway | Infraestrutura | Roteamento para Siebel`
- SEC-05 5.1: Nao lista MS como destino de routing do BFF

**Comentarios originais:**
- #8: "Ou pelo MS nos pedidos em que ele for responsavel ou mediar a resposta."
- #10: "Quando nao passiveis de serem implementadas no siebel"
- #11: "Ou MS" (sobre roteamento para Siebel)

**Acao requerida:**
1. SEC-03 3.3: Qualificar MS como "Logica de Negocio quando nao implementavel em Siebel"
2. SEC-03 3.3: API Gateway deve rotear para "Siebel e Microservices"
3. SEC-05: Incluir MS como destino de chamadas, mediados pelo API Gateway

---

## NC-07: Inventario de Servicos Fora do Middleware BEST

**Gravidade:** MEDIA
**Comentario:** #9
**Seccoes afetadas:** SEC-03 (3.2 - Pendencias), SEC-09 (9.3)

**Descricao:**
O cliente reforça a necessidade de inventariar todos os servicos que nao passam pela gateway atual do BEST, sejam Azure ou outros. Esta pendencia ja esta parcialmente documentada mas o cliente enfatiza a importancia.

**Comentario original:**
- #9: "Para trabalhar neste sentido era importante inventariar os servicos que sao usados que nao passem pela gateway atual do best, quer sejam azure ou outros."

**Acao requerida:**
1. Elevar prioridade desta pendencia em SEC-03 e SEC-09
2. Incluir como acao prioritaria para sessao com equipa BEST
3. Nao limitar a "servicos Azure" - incluir qualquer servico fora do middleware BEST

---

## NC-08: Fluxo SCA Necessita Detalhe

**Gravidade:** ALTA
**Comentario:** #12
**Seccoes afetadas:** SEC-03 (3.4), SEC-07

**Descricao:**
O cliente pede explicitamente para detalhar o fluxo de SCA (Strong Customer Authentication). Atualmente, o documento menciona SCA como obrigatorio mas nao apresenta um diagrama de sequencia dedicado para o fluxo SCA em operacoes (transferencias, pagamentos).

**Comentario original:**
- #12: "Era importante detalhar o fluxo do sca"

**O que o documento tem:**
- SEC-03 3.4: Mencao generica "SCA obrigatorio conforme retorno da API"
- SEC-07 7.3: Tabela de MFA/SCA com informacao de alto nivel
- Faltam diagramas de sequencia para SCA em operacoes (nao-login)

**Acao requerida:**
1. Criar diagrama de sequencia do fluxo SCA para operacoes financeiras (transferencias, pagamentos)
2. Detalhar quando e como o SCA e trigado em operacoes apos login
3. Documentar interacao com app mobile para segundo fator em operacoes

---

## NC-09: "Fluxos Mobile Replicados na Web" Nao Validado

**Gravidade:** BAIXA
**Comentario:** #13
**Seccoes afetadas:** SEC-04 (4.2.1)

**Descricao:**
O principio de design "Paridade Mobile - Fluxos da app mobile replicados na web" e questionado pelo cliente. Os fluxos web podem ter diferencas significativas (navegacao sidebar vs tabs, responsividade, ausencia de biometria nativa).

**O que o documento diz:**
- SEC-04 4.2.1: `Paridade Mobile | Fluxos da app mobile replicados na web`

**Comentario original:**
- #13: "Isto e verdade?"

**Acao requerida:**
1. Reformular para "Fluxos inspirados na app mobile, adaptados ao contexto web"
2. Ou remover se nao for uma premissa validada

---

## NC-10: Coluna "Criticidade" Sem Definicao

**Gravidade:** BAIXA
**Comentario:** #14
**Seccoes afetadas:** SEC-04 (4.3.2)

**Descricao:**
A tabela de jornadas prioritarias inclui uma coluna "Criticidade" (Alta, Media) sem definir o que cada nivel significa.

**Comentario original:**
- #14: "O que representa esta coluna? O que quer dizer criticidade media, por exemplo?"

**Acao requerida:**
1. Adicionar definicao clara dos niveis de criticidade (Alta, Media, Baixa) com criterios
2. Ou substituir por termos mais claros (ex: "Prioridade de implementacao")

---

## NC-11: Retry em Operacoes Falhadas - Alinhar com App Nativa

**Gravidade:** BAIXA
**Comentario:** #15
**Seccoes afetadas:** SEC-04 (4.5)

**Descricao:**
O documento afirma que "Nao ha retry automatico com backoff exponencial para operacoes falhadas". O cliente questiona se este comportamento existe na app nativa, sugerindo que o web deveria estar alinhado.

**O que o documento diz:**
- SEC-04 4.5 nota: "Nao ha retry automatico com backoff exponencial para operacoes falhadas"

**Comentario original:**
- #15: "Isto existe na versao nativa app?"

**Acao requerida:**
1. Verificar se a app nativa tem retry com backoff exponencial
2. Alinhar comportamento web com nativo, ou justificar diferenca

---

## NC-12: Stack Frontend Nao Representa o Acordado

**Gravidade:** ALTA
**Comentarios:** #16
**Seccoes afetadas:** SEC-04 (4.6), DEC-009

**Descricao:**
O cliente indica explicitamente que a stack frontend (Zustand, TanStack Query, Tailwind CSS, Vite, Vitest, Playwright) nao representa o que foi acordado. Este e um problema ja identificado na 1a revisao mas que persiste.

**O que o documento diz:**
- SEC-04 4.6.1: React 18+ / TypeScript / Vite / Zustand / TanStack Query / Tailwind CSS / Vitest / Playwright

**Comentario original:**
- #16: "Nao representa o acordado"

**Acao requerida:**
1. Agendar sessao especifica de React com equipa NB para alinhar stack
2. Atualizar DEC-009 e SEC-04 com a stack acordada
3. A nota em SEC-04 4.6 ja menciona necessidade de sessao, mas o conteudo permanece desatualizado

---

## NC-13: Versao .NET Deve Ser 10

**Gravidade:** MEDIA
**Comentario:** #17
**Seccoes afetadas:** SEC-03 (3.2, 3.3, 3.5), SEC-04 (diagrama frontend), SEC-05 (5.1, 5.2.2), SEC-09 (9.2), SEC-10 (10.1), DEC-010

**Descricao:**
O documento refere ".NET 8" como tecnologia do BFF e Microservices em multiplos locais. O cliente corrige para ".NET 10".

**Locais identificados:**
- SEC-03 diagrama 3.2: `BFF Web (.NET 8)`
- SEC-03 3.3: `BFF Web | .NET 8`, `Microservices | .NET 8`
- SEC-03 3.5: `BFF Web (.NET 8)`, `Microservices (.NET 8)`
- SEC-04 diagrama: `.NET 8 API`
- SEC-05 5.1: `BFF Web | C# .NET 8`
- SEC-05 5.2.1 diagrama: `BFF Web (.NET 8)`
- SEC-05 5.2.2: `Runtime | .NET 8`
- SEC-09 9.2: `.NET 8`
- SEC-10 10.1 diagrama: `BFF (.NET 8)`, `Auth Service (.NET 8)`

**Comentario original:**
- #17: "10" (sobre .NET 8)

**Acao requerida:**
1. Substituicao global de ".NET 8" por ".NET 10" em todas as seccoes, definicoes e decisoes

---

## NC-14: Estrutura de URLs e Convencoes API Nao Alinhadas

**Gravidade:** MEDIA
**Comentario:** #18 (+ reply)
**Seccoes afetadas:** SEC-05 (5.3.2, 5.3.3, 5.8)

**Descricao:**
A estrutura de endpoints proposta (`/api/v1/...`) nao segue as convencoes do NovoBanco. O cliente indica regras especificas para o BFF.

**O que o documento diz:**
```
/api/v1/
├── auth/
├── accounts/
├── payments/
├── investments/
└── documents/
```

**O que deveria dizer segundo o cliente:**
```
/web/ocb/<servicobest>/best/
├── auth/
├── accounts/
...
```

**Regras do cliente:**
- Prefixo: `/web/ocb/<servicobest>/best`
- Remover `/api` para consistencia com o resto
- Assumir v1 para todos, versionamento ao servico (nao ao API)
- Metodo HTTP recomendado: **POST** (recomendacao arquitectural)
- Versionamento alternativo: ao resource se abordagem REST

**Comentarios originais:**
- #18: "Se isto e do BFF a estrutura nao sera assim, pelo menos os primeiros niveis. Ha-de ser qq coisa como /web/ocb/<servicobest>/best como prefixo."
- #18 reply: "Ou servico ou ao resource se forem por abordagem rest. Ja agora, em contexto de arquitetura, a recomendacao que nos deram e usar POST"

**Acao requerida:**
1. Atualizar estrutura de endpoints em SEC-05 5.3.3
2. Atualizar estrategia de versionamento em SEC-05 5.3.2 (por servico, nao por API)
3. Documentar POST como metodo padrao recomendado
4. Atualizar SEC-05 5.8

---

## NC-15: Fluxo de Bearer Token e Cookies - Origens Nao Claras

**Gravidade:** ALTA
**Comentarios:** #19, #20, #21 (+ reply)
**Seccoes afetadas:** SEC-03 (3.2), SEC-05 (5.4), SEC-07

**Descricao:**
O cliente identifica falta de clareza em tres pontos criticos do fluxo de autenticacao:
1. O diagrama APIGW nao torna claro que o bearer token e propagado e de onde vem
2. A origem do cookie de sessao (HttpOnly, Secure) nao esta clara
3. A origem e calculo do Bearer Token propagado nao estao descritos

**Comentarios originais:**
- #19: "Convinha tornar claro que o bearer passa na chamada a apigw e de onde vem. No diagrama como esta parece que a apigw gera um bearer que nao tem qq relacao com o que acontece antes"
- #20: "Origem?" (sobre Cookie de sessao HttpOnly, Secure)
- #21: "Origem?" e reply: "Era importante descrever de onde isto vem e como e calculado"

**Acao requerida:**
1. Explicitar no diagrama e texto a cadeia completa: de onde vem o Bearer Token, como e obtido, como chega a APIGW
2. Clarificar quem gera o cookie de sessao e em que momento
3. Descrever o calculo/obtencao do Bearer Token (flow completo)
4. Garantir que diagramas de SEC-03, SEC-05 e SEC-07 sao consistentes neste fluxo

---

## NC-16: Diferenciacao de Acesso App vs React

**Gravidade:** MEDIA
**Comentario:** #22
**Seccoes afetadas:** SEC-05 (5.5), SEC-06

**Descricao:**
O documento afirma que o "canal web consome os mesmos backend services e modelo de dominio" sem distinguir os pontos de acesso. O cliente esclarece: a app acede ao nivel do APIGW, o React acede ao nivel do BFF.

**Comentario original:**
- #22: "A app a nivel da apigw, o react a nivel do bff."

**Acao requerida:**
1. Clarificar no documento que App Mobile acede via APIGW e React (Web) acede via BFF
2. Atualizar diagramas que mostrem esta diferenciacao
3. Garantir que o modelo de dominio reflecte esta separacao de pontos de acesso

---

## NC-17: Referencia a "Equipa de Autenticacao do NovoBanco" Inexistente

**Gravidade:** BAIXA
**Comentario:** #23
**Seccoes afetadas:** SEC-07 (7.1)

**Descricao:**
SEC-07 7.1 contem a nota "Esta seccao necessita de validacao mais detalhada com equipa de autenticacao do NovoBanco." O cliente reage com "???", indicando que esta equipa nao existe como tal.

**Comentario original:**
- #23: "???"

**Acao requerida:**
1. Reformular para referenciar a equipa correta (ex: "equipa de seguranca" ou "equipa de arquitectura do Banco Best")

---

## NC-18: SessionId em URL - Ma Pratica

**Gravidade:** MEDIA
**Comentario:** #24
**Seccoes afetadas:** SEC-07 (7.2.1)

**Descricao:**
O fluxo de QR Code utiliza `/auth/qr-code/status/{sessionId}` com o sessionId no URL. O cliente identifica isto como ma pratica e questiona o que e esta "session", tempos de vida, etc.

**O que o documento diz:**
- SEC-07 7.2.1: `GET /auth/qr-code/status/{sessionId}`
- Detalhes de tempo de vida da sessao QR nao estao claros

**Comentario original:**
- #24: "Nao consegui ver o fluxo com detalhe e nao e claro o que e esta session nem tempos de vida etc. mas normalmente e ma pratica ter session no url"

**Acao requerida:**
1. Mover sessionId do URL para header ou body
2. Documentar tempo de vida da sessao QR Code
3. Detalhar o ciclo de vida desta "session" especifica (diferente da sessao de utilizador)

---

## NC-19: OAuth Server e Refresh de Tokens

**Gravidade:** MEDIA
**Comentario:** #25
**Seccoes afetadas:** SEC-07 (7.5)

**Descricao:**
O diagrama de tokens (SEC-07 7.5) referencia um "OAuth Server" nos Backend Services. O cliente questiona se este servidor OAuth ja existe e se fazem refresh de token.

**Comentario original:**
- #25: "Este oauth server ja existe atualmente e fazem refresh do token?"

**Acao requerida:**
1. Validar se o OAuth Server existe na infraestrutura atual
2. Documentar se existe mecanismo de refresh de token
3. Se nao existir, remover referencia ou marcar como componente novo a desenvolver

---

## NC-20: AuthService e Validacao de Token pelo Siebel

**Gravidade:** ALTA
**Comentario:** #27
**Seccoes afetadas:** SEC-07 (7.2.1, 7.2.2), SEC-10 (10.1 diagrama)

**Descricao:**
O documento mostra um "Auth Service (MicroService)" que guarda/calcula o token para enviar para o Siebel. O cliente questiona se o Siebel consegue validar este token. Se nao conseguir, o MS deveria estar atras da APIGW.

**Comentario original:**
- #27: "Estao a colocar o authservice porque e o que guarda/calcula o token para enviar para o siebel. Tem a certeza que o siebel consegue validar o token? Se nao der o ms devera estar atras da apigw"

**Acao requerida:**
1. Validar com equipa tecnica se Siebel consegue validar tokens gerados pelo AuthService
2. Se nao conseguir, colocar AuthService atras do APIGW
3. Clarificar o papel do AuthService vs BFF na gestao de tokens
4. Consistencia: se MS devem estar atras do APIGW (NC-02), o AuthService tambem deve

---

## NC-21: Seccao de Infraestrutura com Incorrecoes

**Gravidade:** ALTA
**Comentario:** #28
**Seccoes afetadas:** SEC-10 (10.2, 10.3 a 10.7)

**Descricao:**
O cliente indica que a seccao de infraestrutura tem varias incorrecoes e questiona se faz sentido estar no documento HLD. Exemplos: a nomenclatura dos namespaces pode nao ser a indicada (vem da equipa de infra), e detalhes de CI/CD podem nao corresponder a realidade.

**Comentario original:**
- #28: "Este tema de infra tem varias incorrecoes e penso que nao fara muito sentido estar neste documento. Por exemplo a nomenclatura dos namespaces podera nao ser esta. Vem da equipa de infra."

**O que o documento diz:**
- SEC-10 10.2: Namespaces `best-web-dev`, `best-web-qa`, `best-web-prod`
- SEC-10 10.3-10.7: Detalhes de CI/CD, deploy strategy, secrets, registry

**Acao requerida:**
1. Avaliar se SEC-10 deve ser significativamente simplificada
2. Remover ou marcar como "indicativo" todos os detalhes de infra nao validados
3. Referenciar documentacao existente de infraestrutura quando disponivel
4. Sessao com equipa de infraestrutura NB para validar o que esta correto

---

## NC-22: Rollback de Base de Dados

**Gravidade:** BAIXA
**Comentario:** #29
**Seccoes afetadas:** SEC-10 (10.4)

**Descricao:**
A estrategia de rollback menciona apenas "Automatico via Kubernetes". O cliente questiona o que acontece com rollback de base de dados, se houver.

**Comentario original:**
- #29: "E bd se houver?"

**Acao requerida:**
1. Adicionar consideracao sobre rollback de base de dados na estrategia de deploy
2. Documentar se existem migracoes de BD e como sao revertidas
3. Nota: canal web e descrito como stateless (dados no backend existente), mas confirmar se MS ou BFF tem BD propria

---

## Matriz de Prioridades

| Prioridade | NC | Descricao | Comentarios |
|---|---|---|---|
| **ALTA** | NC-02 | APIGW serve Siebel E Microservices | #3, #4, #26 |
| **ALTA** | NC-01 | BFF nao e API strategy generica | #1, #2 |
| **ALTA** | NC-06 | Responsabilidades MS vs Siebel incorretas | #8, #10, #11 |
| **ALTA** | NC-08 | Fluxo SCA necessita detalhe | #12 |
| **ALTA** | NC-12 | Stack frontend nao representa o acordado | #16 |
| **ALTA** | NC-15 | Bearer token e cookies - origens nao claras | #19, #20, #21 |
| **ALTA** | NC-20 | AuthService e validacao de token pelo Siebel | #27 |
| **ALTA** | NC-21 | Seccao de infraestrutura com incorrecoes | #28 |
| **MEDIA** | NC-03 | Diagrama sugere BFF e MS unicos | #5 |
| **MEDIA** | NC-04 | Protocolos OAuth confusos | #6 |
| **MEDIA** | NC-07 | Inventario de servicos fora do middleware BEST | #9 |
| **MEDIA** | NC-13 | .NET 10 (nao 8) | #17 |
| **MEDIA** | NC-14 | Estrutura URLs e convencoes API | #18 |
| **MEDIA** | NC-16 | Diferenciacao acesso App vs React | #22 |
| **MEDIA** | NC-18 | SessionId em URL - ma pratica | #24 |
| **MEDIA** | NC-19 | OAuth Server e refresh de tokens | #25 |
| **BAIXA** | NC-05 | Lookup de token a avaliar | #7 |
| **BAIXA** | NC-09 | "Fluxos mobile replicados" nao validado | #13 |
| **BAIXA** | NC-10 | Coluna "Criticidade" sem definicao | #14 |
| **BAIXA** | NC-11 | Retry em operacoes - alinhar com app nativa | #15 |
| **BAIXA** | NC-17 | Referencia a equipa inexistente | #23 |
| **BAIXA** | NC-22 | Rollback de base de dados | #29 |

---

## Correlacao com Comentarios

| Comentario | NC | Tema |
|---|---|---|
| #1 | NC-01 | BFF nao e API strategy generica |
| #2 | NC-01 | Acoplamento legados: BFF ou MS |
| #3 | NC-02 | APIGW serve Siebel e MS |
| #4 | NC-02 | Excepcao APIGW: servicos Azure |
| #5 | NC-03 | BFF e MS unicos no diagrama |
| #6 | NC-04 | Protocolos OAuth confusos |
| #7 | NC-05 | Lookup token a avaliar |
| #8 | NC-06 | Siebel ou MS como responsavel |
| #9 | NC-07 | Inventario servicos fora BEST |
| #10 | NC-06 | MS: logica quando nao no Siebel |
| #11 | NC-06 | Roteamento para Siebel ou MS |
| #12 | NC-08 | Detalhar fluxo SCA |
| #13 | NC-09 | Fluxos mobile replicados? |
| #14 | NC-10 | Criticidade sem definicao |
| #15 | NC-11 | Retry existe no nativo? |
| #16 | NC-12 | Stack frontend nao acordada |
| #17 | NC-13 | .NET 10, nao 8 |
| #18 | NC-14 | URLs e convencoes API |
| #19 | NC-15 | Bearer token na APIGW |
| #20 | NC-15 | Origem cookie sessao |
| #21 | NC-15 | Origem Bearer Token |
| #22 | NC-16 | App via APIGW, React via BFF |
| #23 | NC-17 | Equipa inexistente |
| #24 | NC-18 | SessionId em URL |
| #25 | NC-19 | OAuth Server existe? |
| #26 | NC-02 | MS atras do APIGW |
| #27 | NC-20 | AuthService e validacao Siebel |
| #28 | NC-21 | Infra com incorrecoes |
| #29 | NC-22 | Rollback de BD |

---

## Temas Transversais Identificados

### Tema A: Papel do API Gateway (NC-01, NC-02, NC-06)
O principal problema estrutural. Toda a arquitectura de comunicacao no documento assume que o APIGW e "apenas para Siebel". A correcao deste tema impacta diagramas e textos em SEC-03, SEC-05 e SEC-09.

### Tema B: Fluxos de Autenticacao e Tokens (NC-04, NC-05, NC-08, NC-15, NC-18, NC-19, NC-20)
O segundo tema mais critico. O cliente questiona repetidamente a origem e propagacao de tokens, o fluxo SCA, e a viabilidade do AuthService. Requer um redesenho coerente dos fluxos de autenticacao.

### Tema C: Alinhamento com Realidade NB (NC-07, NC-12, NC-13, NC-14, NC-16, NC-21)
Varios itens nao correspondem a realidade do NovoBanco: stack frontend, versao .NET, URLs, infraestrutura. Requerem sessoes de alinhamento com equipas NB.

---

## Sessoes Requeridas

| Sessao | NCs Relacionadas | Participantes |
|--------|------------------|---------------|
| **Arquitectura / APIGW** | NC-01, NC-02, NC-03, NC-06 | Arquitectura NB + NextReality |
| **Autenticacao / Tokens** | NC-04, NC-05, NC-08, NC-15, NC-19, NC-20 | Equipa Seguranca NB + NextReality |
| **React / Frontend** | NC-12, NC-14 | Equipa Dev NB + Havas + NextReality |
| **Infraestrutura** | NC-21 | Equipa Infra NB |
| **BEST / Servicos** | NC-07, NC-16 | Equipa BEST |

---

## Historico

| Data | Acao |
|------|------|
| 2026-03-02 | Criacao do documento com analise completa dos 29 comentarios de novobanco-jcc-commented-20260219.md |
