# Nao Conformidades - Feedback JGC 2a Revisao

**Data:** 2026-02-19
**Origem:** E-mail Jorge Costa + Comentarios HDL-JJC-2-comments.md
**Contexto:** Segunda revisao do documento HLD. Cliente parou leitura no capitulo 9 por encontrar problemas persistentes da revisao anterior.

---

## Resumo Executivo

O feedback do cliente identifica dois problemas estruturais:

1. **Problemas nao corrigidos da 1a revisao** - Stack frontend e outros pontos mantidos apesar dos comentarios anteriores
2. **Desequilibrio do documento** - Excesso de detalhe em infraestrutura (que nao mapeia para a realidade do NB) e falta de foco no desenho aplicacional macro

O cliente define como **objetivo minimo** para o forum de arquitetura:
- Componentes ou sistemas envolvidos
- Fluxos entre componentes
- Mecanismos de seguranca
- Fluxo funcional, nomeadamente operacao
- Visao web e nativa (WebView embebido no app existente - cenario secundario/futuro)

---

## NC-01: Stack Frontend Nao Alinhada com NovoBanco

**Gravidade:** ALTA
**Comentarios:** #9, #20 (e-mail)
**Seccoes afetadas:** SEC-04 (4.6), DEC-009

**Descricao:**
O documento propoe uma stack frontend (Zustand, TanStack Query, Tailwind CSS, Vite, Vitest, Playwright) que **nao corresponde ao que o NovoBanco utiliza** nos seus canais internos e externos. O Jorge afirma explicitamente no e-mail: "tinha comentado que o stack de react nao e o que temos, mas mantiveram isso nesta versao."

No comentario #20, o Jorge indica que "Este stack temos de fechar em conjunto. Ha coisas que temos na framework mas outras temos alternativas" e que "a base ja foi alinhada com a Havas."

**O que o documento diz:**
- React 18+ / TypeScript / Vite / Zustand / TanStack Query / Tailwind CSS / Vitest / Playwright

**O que deveria dizer:**
- A stack deve refletir o que foi apresentado pelo NB ou, no minimo, indicar que esta pendente de alinhamento em sessao especifica de React (comentario #20 reply 3).

**Acao requerida:**
1. Agendar sessao especifica de React com equipa NB para alinhar stack
2. Atualizar DEC-009 e SEC-04 com a stack acordada
3. Rever seccoes 4.6.2, 4.6.3, 4.7, 4.8 conforme comentario #20

---

## NC-02: Infraestrutura CI/CD Nao Corresponde a Realidade

**Gravidade:** ALTA
**Comentario:** #51
**Seccoes afetadas:** SEC-10 (10.3 a 10.7)

**Descricao:**
A seccao 10 descreve uma infraestrutura CI/CD baseada em Azure (Azure Repos, Azure Pipelines, Azure Container Registry, Azure Key Vault, Terraform) que **pode nao corresponder ao que o NovoBanco tem implementado**. O Jorge indica: "Isto ja se encontra implementado. Sera reutilizar o que existe. Ha coisas que descrevem corretamente o que esta, outras nem por isso, outras nem tenho visibilidade de como esta."

O Jorge questiona se esta seccao faz sentido estar no documento HLD, sugerindo que deveria ser a equipa de infraestrutura a descrever.

**O que o documento diz:**
- Azure Repos (Git), Azure Pipelines, ACR, Azure Key Vault, Helm + Terraform, GitFlow

**O que deveria dizer:**
- Descrever apenas o que e conhecido e validado com equipa de infra do NB
- Ou remover detalhes de infraestrutura que nao sao da responsabilidade do HLD aplicacional

**Acao requerida:**
1. Sessao com equipa de infraestrutura NB para validar o que esta correto
2. Remover ou simplificar o que nao e da responsabilidade do documento
3. Referenciar documentacao existente de infraestrutura quando disponivel

---

## NC-03: ApiPsd2 e ApiBBest Ainda Referenciados Separadamente

**Gravidade:** MEDIA
**Origem:** CORRECOES.md item 1 (correcao da 1a revisao, nao aplicada)
**Seccoes afetadas:** SEC-03 (legenda diagrama 3.2, tabela de protocolos), SEC-09 (9.3 nota)

**Descricao:**
O CORRECOES.md da 1a revisao indica que ApiPsd2 e ApiBBest sao parte do Siebel e devem ser unificados. Esta correcao nao foi aplicada. A legenda do diagrama em SEC-03 (linha 163) ainda lista "ApiPsd2, ApiBBest" como componentes separados, e SEC-09 (linha 92) ainda os referencia.

**O que o documento diz:**
- Legenda SEC-03: "Verde | Componentes existentes (reutilizar): F5, ApiPsd2, ApiBBest, API Gateway, Siebel"
- Protocolos SEC-03: "OAuth + SHA256: Utilizado para comunicacao BFF - ApiPsd2" e "OAuth 1.1 HMAC: Utilizado para comunicacao BFF - ApiBBest"
- SEC-09: "o BFF acede directamente a ApiPsd2, ApiBBest e Microservices"

**O que deveria dizer:**
- Unificar sob "Siebel" conforme instrucao do cliente (ApiPsd2 e ApiBBest sao interfaces do Siebel, nao componentes separados)

**Acao requerida:**
1. Remover ApiPsd2 e ApiBBest como componentes separados em todos os diagramas e textos
2. Unificar como Siebel
3. Atualizar tabela de protocolos de comunicacao em SEC-03

---

## NC-04: Referencias a "Novo Banco" em Vez de "Banco Best"

**Gravidade:** MEDIA
**Comentario:** CORRECOES.md item 2
**Seccoes afetadas:** SEC-01, SEC-02, SEC-03, SEC-04 e potencialmente outras

**Descricao:**
O cliente instruiu que todas as referencias a "Novo Banco" devem ser substituidas por "Banco Best". Existem ocorrencias nao corrigidas em:

| Seccao | Linha | Texto |
|--------|-------|-------|
| SEC-01 | 28 | "projeto HomeBanking Web do Novo Banco" |
| SEC-02 | 38 | "clientes do Novo Banco" |
| SEC-02 | 57 | "Clientes do Novo Banco" |
| SEC-03 | 217 | "Cliente particular do Novo Banco" |

**Acao requerida:**
1. Substituicao global de "Novo Banco" por "Banco Best" em todas as seccoes

---

## NC-05: MBWay na Contagem de Funcionalidades

**Gravidade:** MEDIA
**Comentario:** CORRECOES.md item 3
**Seccoes afetadas:** SEC-02 (2.3.1)

**Descricao:**
SEC-01 corretamente exclui MBWay no Out-of-Scope. No entanto, SEC-02 (linha 76) ainda lista "MBWay (nao-SDK)" como funcionalidade de Pagamentos, contribuindo para a contagem total de 35.

**O que o documento diz:**
- Pagamentos: "Transferencias, Pagamentos, Carregamentos, MBWay (nao-SDK) | 4"
- Total: 35

**O que deveria dizer:**
- Pagamentos: "Transferencias, Pagamentos, Carregamentos | 3"
- Total: 34 (ou renumerar)

**Acao requerida:**
1. Remover MBWay da tabela de funcionalidades em SEC-02
2. Ajustar contagem total
3. Verificar se SEC-01 tambem precisa de ajuste na contagem

---

## NC-06: Excesso de Detalhe Infraestrutural vs Falta de Desenho Aplicacional

**Gravidade:** ALTA (estrutural)
**Comentario:** E-mail JGC
**Seccoes afetadas:** SEC-10, SEC-11, SEC-12 (excesso) vs SEC-03 (falta)

**Descricao:**
O Jorge identifica um desequilibrio fundamental: "O documento tem muito detalhe, inclusive de informacao que e puramente de infraestrutura e que nao mapeia para o que temos, descurando um pouco a componente macro de desenho aplicacional que deveria ser abordada nesta fase."

**Deficit identificado nos objetivos minimos:**
1. **Fluxos funcionais de operacao** - Nao existem diagramas de fluxo funcional para operacoes core (transferencia end-to-end, consulta de saldos, pagamentos). Apenas casos de uso de alto nivel em SEC-03 (3.4).

**Nota:** O cenario "web na app" (WebView embebido no app nativo existente) e secundario/futuro e ja esta adequadamente coberto pela nota em SEC-03. Nao constitui lacuna.

**Acao requerida:**
1. Adicionar fluxos funcionais de operacao (pelo menos login, transferencia, consulta) como diagramas de sequencia em SEC-03 ou SEC-05
2. Avaliar se seccoes 10-12 devem ser simplificadas ou remetidas para documentacao de infraestrutura

---

## NC-07: Asserções Potencialmente Irrealistas

**Gravidade:** MEDIA
**Comentario:** E-mail JGC
**Seccoes afetadas:** Varias

**Descricao:**
O Jorge alerta: "Teria muito cuidado com algumas assercoes do documento pois ou nao enquadram no que temos ou poderao comprometer o projeto a objetivos menos realistas."

**Exemplos identificados:**
- SLA de 99.9% (SEC-02 linha 115) - sem validacao com infra real
- RTO de 30 minutos (SEC-02 linha 116) - sem validacao
- Throughput de 10 TPS / 400 utilizadores concorrentes (SEC-02 linhas 106, 124) - valores provisorios sem calibracao
- Metricas frontend (LCP < 2.5s, FID < 100ms) - sem baseline real
- DR com cluster replica standby (SEC-06) - pode nao existir

**Acao requerida:**
1. Marcar claramente todos os valores nao validados como "provisorios/estimativas"
2. Não comprometer com SLAs sem validacao da equipa de infraestrutura
3. Calibrar com metricas reais da app mobile

---

## NC-08: Picos de Utilizacao - Especificacao Incorreta

**Gravidade:** BAIXA
**Comentario:** CORRECOES.md item 4
**Seccoes afetadas:** SEC-02 (2.4.3)

**Descricao:**
SEC-02 indica picos "Apos envio de campanhas" (generico). O cliente especifica que picos sao **somente com newsletter**.

**Acao requerida:**
1. Substituir "Apos envio de campanhas" por "Apos envio de newsletters"

---

## Matriz de Prioridades

| Prioridade | NC | Descricao |
|---|---|---|
| **ALTA** | NC-01 | Stack frontend nao alinhada |
| **ALTA** | NC-02 | CI/CD nao corresponde a realidade |
| **ALTA** | NC-06 | Falta desenho aplicacional / excesso infra |
| **MEDIA** | NC-03 | ApiPsd2/ApiBBest como Siebel |
| **MEDIA** | NC-04 | "Novo Banco" → "Banco Best" |
| **MEDIA** | NC-05 | MBWay na contagem |
| **MEDIA** | NC-07 | Assercoes potencialmente irrealistas |
| **BAIXA** | NC-08 | Picos = newsletter |

---

## Sessoes Requeridas (Acao Imediata)

| Sessao | Objetivo | Participantes |
|--------|----------|---------------|
| **React/Frontend** | Alinhar stack (NC-01), seccoes 4.6-4.9 | Equipa Dev NB + Havas + NextReality |
| **Infraestrutura** | Validar CI/CD (NC-02), observabilidade | Equipa Infra NB |
| **Arquitetura** | Desenho aplicacional macro (NC-06), visao web+nativa | Arquitetura NB + NextReality |
| **BEST** | Validacao de informacao tecnica (pedido no e-mail JGC) | Equipa BEST |

---

## Historico

| Data | Acao |
|------|------|
| 2026-02-19 | Criacao do documento com analise de 54 comentarios e e-mail JGC |
