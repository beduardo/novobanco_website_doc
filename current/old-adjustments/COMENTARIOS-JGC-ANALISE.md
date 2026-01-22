# Análise de Comentários - Jorge Gomes Costa (JGC)

**Documento Original:** HLD-HomeBanking-Web (Word)
**Data dos Comentários:** 2026-01-16
**Autor dos Comentários:** Jorge Gomes Costa (novobanco DSI Direção)
**Total de Comentários:** 54

---

## Legenda de Status

| Status | Significado |
|--------|-------------|
| [ ] | Pendente |
| [~] | Em progresso |
| [x] | Resolvido |
| [?] | Necessita esclarecimento do cliente |

---

## TEMA A - Arquitetura BFF e Fluxo de Serviços (CRÍTICO)

**Prioridade:** ALTA
**Seções afetadas:** SEC-01, SEC-02, SEC-03, SEC-05, SEC-09
**Status:** [x] Resolvido (2026-01-21)

### Resolução Aplicada

- Criada decisão [DEC-011-diagrama-arquitetura-unico.md](decisions/DEC-011-diagrama-arquitetura-unico.md)
- Diagrama 3.2 atualizado como referência principal
- Seções SEC-01, SEC-05, SEC-09 atualizadas para referenciar diagrama 3.2
- Fluxo corrigido: Frontend → BFF → API Gateway (IBM) → Siebel → Core Banking
- Adicionada informação: Siebel valida o token
- Adicionados Serviços Azure (acesso direto pelo BFF) com nota de pendência

### Problema Principal

Os diagramas e descrições do documento não refletem a arquitetura real discutida nas sessões com o cliente. O ponto crítico é:

- **BFF NÃO tem API Gateway à frente** (pelo menos à data atual)
- **Serviços chamados pela app** é que têm API Gateway
- O BFF já existe e dá suporte ao SPA atual (pode ser quase proxy direto)

### Comentários Relacionados

| # | Parágrafo | Citação | Comentário JGC |
|---|-----------|---------|----------------|
| 1 | 241 | (diagrama) | "Não reflete o fluxo que apresentámos e tem de ter mais detalhe para ser claro. Os serviços de BFF não têm apigw à frente (pelo menos à data), os serviços chamados pela app irão ter." |
| 1 (reply) | 241 | - | "Aqui também é relevante colocar os serviços da app que são necessários mas que não cabem neste sistema. Por exemplo os acessos diretos ao azure para algumas funcionalidades." |
| 1 (reply 2) | 241 | - | "Já vi que mais abaixo têm um boneco mais fiel ao que falámos. Porquê de aqui estar diferente?" |
| 3 | 335 | "O projeto HomeBanking Web visa..." | "Mais uma vez, no que temos atualmente o bff está a dar suporte ao spa. Pode ser quase proxy direta mas é assim que está. Há várias coisas que vêm daqui, como o tema dos logs ou segurança que têm de ser implementados em algum lado" |
| 6 | 855 | "Reutilização de APIs e serviços da app mobile" | "Mais uma vez isto tem de ser afinado. A ideia será reutilizar mas não diretamente. Sempre falámos do BFF à frente para a Web" |
| 12 | 955 | (diagrama) | "Este diagrama não reflete o que temos falado" |
| 12 (reply) | 955 | - | "O 3.2 já está alinhado. Porque a diferença?" |
| 16 | 1132 | (diagrama) | "Embora não seja primário, nem seja a direção para os serviços core do best, neste boneco também deveria contemplar o canal web a correr na app." |
| 16 (reply) | 1132 | - | "Convinha esclarecer o tema dos backend services. Onde fica a validação do token neste desenho? O bff não faz, a apigw também não. Onde está?" |
| 16 (reply 2) | 1132 | - | "Uma coisa que era importante era tentar avaliar se queremos 1 container por layer 'banco best' ou se vamos segregar de alguma forma." |
| 23 | 2496 | "Rate LimitingNaoResponsabilidade do Gateway" | "Resubmissões?" |
| 23 (reply) | 2496 | - | "Atenção que no BFF não há APIGW à frente" |
| 24 | 2582 | (diagrama de autenticação) | "Da última sessão, o bearer tem de passar para lá da APIGW. Para a apigw é clientid+secret" |
| 29 | 2967 | "Bearer token para backend services" | "Os backend services como representados na figura não estão preparados para receber o bearer." |
| 34 | 3512 | (diagrama) | "A apigw não aparece porque estão a simplificar o desenho?" |
| 40 | 4473 | (diagrama) | "O backend api é o siebel? Quem trata do token tendo em conta que está atrás da apigw?" |
| 40 (reply) | 4473 | - | "A minha sugestão seria fazer um boneco com isto e referenciar. Têm vários muito parecidos e qualquer alteração depois têm de fazer em todos." |
| 40 (reply 2) | 4473 | - | "O BFF é 1 'container' o resto é o quê?" |
| 41 | 4568 | (diagrama) | "A apigw é da IBM. Mais uma vez - da conversa que tivemos com eles o token não é mapeado nela. Faltam coisas no boneco." |

### Arquitetura Correta (a implementar)

```
┌─────────────┐     ┌─────────┐     ┌─────────────┐     ┌─────────────────┐
│ Frontend    │────▶│   BFF   │────▶│ API Gateway │────▶│ Backend Services│
│ Web (SPA)   │     │  (.NET) │     │    (IBM)    │     │    (Siebel)     │
└─────────────┘     └─────────┘     └─────────────┘     └─────────────────┘
                         │
                         │ (sem APIGW)
                         │
                    ┌────┴────┐
                    │ Serviços│
                    │ Azure   │
                    │ (outros)│
                    └─────────┘
```

**Fluxo de Autenticação:**
- Frontend → BFF: Cookie de sessão
- BFF → API Gateway: client_id + client_secret
- API Gateway → Backend: Bearer token propagado

### Questões Pendentes (para o Cliente)

- [x] Onde fica a validação do token? - **Resolvido: Siebel valida o token**
- [ ] Quais serviços Azure são acedidos diretamente (fora do middleware BEST)? - **Aguarda informação do cliente**
- [ ] 1 container por layer ou segregação diferente? - **Aguarda decisão do cliente**
- [ ] Como transitar os serviços Azure para a nova realidade? - **Aguarda informação do cliente**

### Ações Concluídas

1. [x] Criar diagrama de arquitetura de referência único - **DEC-011 criada**
2. [x] Atualizar todos os diagramas nas seções para referenciar o diagrama único - **SEC-01, SEC-05, SEC-09 atualizados**
3. [x] Corrigir fluxo BFF → APIGW → Backend Services - **Diagramas corrigidos**
4. [x] Adicionar serviços Azure que não passam pelo middleware - **Adicionado ao diagrama 3.2**
5. [x] Documentar onde fica validação de token - **Siebel valida (SEC-03, SEC-05, SEC-09)**
6. [ ] Esclarecer organização de containers - **Aguarda decisão do cliente**

---

## TEMA B - Diagramas Inconsistentes

**Prioridade:** ALTA
**Seções afetadas:** SEC-01, SEC-03, SEC-05, SEC-09
**Status:** [x] Resolvido (2026-01-21)

### Resolução Aplicada

- Criada decisão DEC-011: Diagrama de Arquitetura Único
- Diagrama 3.2 é agora a referência principal
- Diagramas duplicados removidos das seções SEC-01, SEC-05, SEC-09
- Todas as seções referenciam o diagrama 3.2

### Problema Principal

Existem múltiplos diagramas semelhantes ao longo do documento que não estão alinhados entre si. O cliente sugere criar um diagrama de referência único.

### Comentários Relacionados

| # | Parágrafo | Comentário JGC |
|---|-----------|----------------|
| 1 (reply 2) | 241 | "Já vi que mais abaixo têm um boneco mais fiel ao que falámos. Porquê de aqui estar diferente?" |
| 12 | 955 | "Este diagrama não reflete o que temos falado" |
| 12 (reply) | 955 | "O 3.2 já está alinhado. Porque a diferença?" |
| 22 (reply) | 2309 | "Neste boneco e nos outros não deveríamos ter o siebel pelo menos à frente dos serviços core? Não me parece que este reflita o modelo claramente" |
| 40 (reply) | 4473 | "A minha sugestão seria fazer um boneco com isto e referenciar. Têm vários muito parecidos e qualquer alteração depois têm de fazer em todos." |
| 46 | 5540 | "Acho que este diagrama também confunde. Depende do que querem expressar…." |

### Diagramas a Rever

1. Diagrama 1 (SEC-01) - Visão Geral Arquitetura
2. Diagrama 2 (SEC-02) - Dependências
3. Diagrama 3 (SEC-03) - Arquitetura Conceptual C4
4. Diagrama 5 (SEC-03) - Integração com Infraestrutura
5. Diagrama 10 (SEC-05) - Decomposição de Serviços
6. Diagrama 11 (SEC-05) - Arquitetura BFF
7. Diagrama 25 (SEC-09) - Arquitetura de Integração
8. Diagrama 26 (SEC-09) - Acesso Core Banking
9. Diagrama 28 (SEC-09) - API Gateway

### Ações Concluídas

1. [x] Criar diagrama de arquitetura de referência (master) - **DEC-011, SEC-03 3.2**
2. [x] Decidir quais diagramas manter vs referenciar o master - **DEC-011 documenta a decisão**
3. [x] Garantir consistência em todos os diagramas mantidos - **Diagramas de detalhe são específicos**
4. [x] Incluir Siebel à frente dos serviços core onde relevante - **SEC-03, SEC-05, SEC-09**

---

## TEMA C - MVP e Estratégia de Switch

**Prioridade:** MÉDIA
**Seção afetada:** SEC-02
**Status:** [x] Resolvido (2026-01-21)

### Resolução Aplicada

- Reformulada secção 2.3.2: "MVP" substituído por "Âmbito"
- Adicionada nova secção 2.8 "Estratégia de Lançamento"
- Registada pendência para definição da estratégia de cutover
- Adicionado item pendente na tabela de SEC-02

### Problema Principal

O documento menciona "MVP: Todas as 35 funcionalidades fazem parte do MVP", mas na realidade não existe MVP. É necessário definir a estratégia de cutover (big bang ou incremental).

### Comentários Relacionados

| # | Parágrafo | Citação | Comentário JGC |
|---|-----------|---------|----------------|
| 4 | 585 | "MVP: Todas as 35 funcionalidades fazem parte do MVP" | "Era relevante ver como fazemos o switch. Na realidade não existe MVP mas deveríamos definir se teremos uma estratégia de bigbang ou outra porque isto pode influenciar o desenho e a infraestrutura" |

### Questões Pendentes (para o Cliente)

- [ ] Estratégia de cutover: big bang ou incremental? - **Aguarda decisão do cliente**
- [ ] Impacto na infraestrutura conforme estratégia escolhida? - **Depende da estratégia**
- [ ] Coexistência temporária de canais? - **Aguarda decisão do cliente**

### Ações Concluídas

1. [x] Remover ou reformular menção a "MVP" - **Reformulado para "Âmbito"**
2. [x] Adicionar secção sobre estratégia de cutover/switch - **SEC-02 secção 2.8**
3. [x] Documentar impactos na infraestrutura conforme estratégia - **Registado como pendência**

---

## TEMA D - Performance e Throughput

**Prioridade:** MÉDIA
**Seções afetadas:** SEC-02, SEC-12
**Status:** [x] Resolvido (2026-01-21)

### Resolução Aplicada

- Adicionada nota em SEC-02 (2.4.1) indicando que valores são provisórios
- Adicionada nota em SEC-12 (12.1) indicando necessidade de calibração
- Registadas pendências para obtenção de métricas reais do cliente
- Adicionada secção de itens pendentes em SEC-12

### Problema Principal

Os valores de throughput (10 TPS) precisam ser calibrados com valores reais de utilização normal e em pico.

### Comentários Relacionados

| # | Parágrafo | Citação | Comentário JGC |
|---|-----------|---------|----------------|
| 5 | 758 | "Sim" (referente a throughput) | "É importante calibrar este valor. Pedidos/segundo normal e em pico" |

### Questões Pendentes (para o Cliente)

- [ ] Valores de throughput da app mobile atual (normal e pico)? - **Aguarda métricas do cliente**
- [ ] Projeção de crescimento para o canal web? - **Aguarda informação do cliente**
- [ ] Sazonalidade (fim de mês, períodos fiscais)? - **Aguarda informação do cliente**

### Ações Concluídas

1. [ ] Obter métricas reais da app mobile - **Pendência registada para o cliente**
2. [ ] Definir valores de throughput: normal, pico, máximo - **Aguarda métricas**
3. [x] Atualizar SEC-02 (2.4.1) e SEC-12 com nota de calibração - **Notas adicionadas**

---

## TEMA E - Segurança Web vs Mobile (CRÍTICO)

**Prioridade:** ALTA
**Seções afetadas:** SEC-07, SEC-08
**Status:** [x] Resolvido (2026-01-21)

### Resolução Aplicada

**SEC-08 - Nova secção 8.3.6 adicionada:**
- Tabela comparativa de diferenças de ambiente (mobile vs web)
- Vetores de ataque específicos do web com mitigações
- Tratamento de dados sensíveis em ambiente web
- Pendências de revisão de segurança registadas

**SEC-07 - Nova secção 7.2.3 adicionada:**
- Especificação de transmissão de credenciais
- Dados retornados no login e seus destinos
- Configuração de cookies de sessão (HttpOnly, Secure, SameSite)
- Pendências de alta prioridade registadas

**Correções adicionais (Tema G):**
- CDN: "Evitar" → "Não usar"
- `dangerouslySetInnerHTML` adicionado aos proibidos

**Pendências criadas para o cliente:**
- Revisão de dados retornados no login
- Avaliação de cifra de PIN além de TLS
- Avaliação de credenciais do banco em ambiente web

### Problema Principal

Os requisitos de segurança são **diferentes** entre ambiente nativo (mobile) e web. O ambiente web é menos protegido e necessita revisão específica de riscos, especialmente:
- Credenciais retornadas no login
- PIN e password em claro
- Tokens e cookies

### Comentários Relacionados

| # | Parágrafo | Citação | Comentário JGC |
|---|-----------|---------|----------------|
| 10 | 938 | "A validar" (requisitos segurança) | "Diria que os requisitos de segurança são diferentes necessariamente. Isto porque o ecossistema nativo é mais protegido que o web. Se o que estamos a falar é do protocolo, existem alguns temas que necessitam revisão porque parecem ser potenciais temas de segurança." |
| 10 (reply) | 938 | - | "Um dos pontos que me parece que tem de ser mesmo revisto é o tema das credenciais retornadas no login. Em nativo diria que há argumento para questionar a sua presença, na web isto necessita de uma revisão sobre risco e vetores de ataque que possam comprometer as credenciais do banco nas plataformas" |
| 17 | 1291 | "SCA obrigatório, ponto de entrada" | "Talvez este requisito possa ser trabalhado mais tarde mas é importante detalhar o tema de como serão implementadas as componentes de segurança. Há um serviço de login - o pin + pass vai em claro? Depois é criado algo que é devolvido no login, sendo que parte deveria ser em cookie secure/httponly para garantir que não é capturado em javascript" |

### Questões Pendentes (para o Cliente/Segurança)

- [ ] Que credenciais são retornadas no login da app mobile? - **Aguarda informação do cliente**
- [ ] Revisão de risco para exposição dessas credenciais em web - **Aguarda equipa de segurança**
- [ ] PIN + password vão em claro ou cifrados? - **Aguarda decisão de segurança**
- [x] Quais dados devem estar em cookie secure/httponly? - **Documentado em SEC-07 7.2.3**

### Ações Concluídas

1. [x] Adicionar secção específica sobre diferenças de segurança web vs mobile - **SEC-08 8.3.6**
2. [ ] Documentar revisão de risco para credenciais no login - **Pendência registada nas seções**
3. [x] Especificar implementação de segurança: cookies, tokens, cifra - **SEC-07 7.2.3**
4. [x] Listar vetores de ataque específicos do ambiente web - **SEC-08 8.3.6**
5. [x] Definir mitigações para cada vetor - **SEC-08 8.3.6**

---

## TEMA F - Terceiros e Serviços Não Cobertos

**Prioridade:** MÉDIA-ALTA
**Seção afetada:** SEC-09
**Status:** [x] Resolvido (2026-01-21)

### Resolução Aplicada

- Adicionada nova secção 9.6 "Serviços Fora do Middleware BEST" em SEC-09
- Documentada estrutura para identificação de serviços Azure e outros
- Adicionada nota sobre verificação de notificações na app mobile (secção 9.4)
- Registadas pendências para obtenção de lista completa do cliente
- Adicionados itens pendentes na tabela de SEC-09

### Problema Principal

Existem serviços utilizados pela app mobile que não estão no middleware BEST (ex: serviços em Azure). Estes precisam ser identificados e documentados, incluindo como transitam para a nova realidade.

### Comentários Relacionados

| # | Parágrafo | Citação | Comentário JGC |
|---|-----------|---------|----------------|
| 1 (reply) | 241 | - | "Aqui também é relevante colocar os serviços da app que são necessários mas que não cabem neste sistema. Por exemplo os acessos diretos ao azure para algumas funcionalidades. Estes têm de ser vistos como transitam para a nova realidade." |
| 11 | 949 | "Sim" (terceiros) | "Terceiros é outras entidades ou outros sistemas? Neste documento deveriam estar identificados e termos solução para todas as coisas que não estejam presentes no middleware do BEST e que serão necessários para a solução (como os serviços em azure ou outros)" |
| 11 (reply) | 949 | - | "A abertura de conta também faz parte do projeto (sei que está a ser tratada separadamente). Nesse caso há interações com terceiros ou não?" |
| 42 | 4837 | "O canal web pode acionar envio de notificações..." | "Isto já existe em app?" |

### Questões Pendentes (para o Cliente)

- [ ] Lista de serviços Azure usados diretamente pela app mobile - **Aguarda informação do cliente**
- [ ] Abertura de conta tem interações com terceiros? - **Aguarda informação do cliente**
- [ ] Como esses serviços transitam para o canal web? - **Aguarda informação do cliente**
- [ ] Notificações de confirmação de transferência existem na app? - **Aguarda informação do cliente**

### Ações Concluídas

1. [x] Adicionar secção para serviços fora do middleware BEST - **SEC-09 secção 9.6**
2. [x] Documentar estrutura para identificação de serviços - **SEC-09 secção 9.6**
3. [ ] Obter lista completa de serviços fora do middleware BEST - **Pendência registada para o cliente**
4. [ ] Clarificar integrações da abertura de conta - **Pendência registada para o cliente**
5. [x] Adicionar nota sobre notificações existentes - **SEC-09 secção 9.4**

---

## TEMA G - Stack Tecnológica e Correções

**Prioridade:** MÉDIA
**Seções afetadas:** SEC-04, SEC-05, SEC-08, SEC-09
**Status:** [x] Resolvido (2026-01-21)

### Correções Aplicadas

- [x] OpenAPI 3.0 → 3.1 (SEC-05)
- [x] Message Broker: Kafka ou JMS (SEC-09)
- [x] CDN: "Não usar" (SEC-08)
- [x] dangerouslySetInnerHTML proibido (SEC-08)
- [x] "compliant" → "Assente em" (SEC-03, SEC-05)

### Correções Diretas Necessárias

| # | Parágrafo | Atual | Correção |
|---|-----------|-------|----------|
| 27 | 2834 | "OpenAPI 3.0" | **"OpenAPI 3.1"** |
| 38 | 4028 | "Evitar; se necessário..." (CDN) | **"Não usar"** |
| 39 | 4068 | "innerHTML e eval proibidos..." | Adicionar **"dangerouslySetInnerHTML"** |
| 44 | 5121 | "RabbitMQ, Kafka, Azure Service Bus" | **"Kafka ou JMS"** (remover RabbitMQ e Azure Service Bus) |
| 13 | 1045 | "compliant" | **"Assente em"** (correção linguística) |

### Comentários Relacionados

| # | Parágrafo | Citação | Comentário JGC |
|---|-----------|---------|----------------|
| 9 | 927 | "validar" (stack) | "A proposta com o react e .net é uma utilização equivalente ao que estamos a usar a todos os contextos de canais internos e externos no NB pelo que deverá ser adequada. Sendo que é a que apresentámos, não a que está neste documento." |
| 13 | 1045 | "compliant" | "Assente em" |
| 27 | 2834 | "OpenAPI 3.0" | "3.1" |
| 38 | 4028 | "Evitar; se necessário..." | "não usar" |
| 39 | 4068 | "innerHTML e eval proibidos..." | "Idem para dangerouslySetInnerHTML" |
| 44 | 5121 | "Tecnologia (RabbitMQ, Kafka, Azure Service Bus)" | "À partida kafka ou jms" |

### Ações Concluídas

1. [x] Corrigir OpenAPI 3.0 → 3.1 - **SEC-05**
2. [x] Alterar política de CDN para "Não usar" - **SEC-08**
3. [x] Adicionar dangerouslySetInnerHTML aos proibidos - **SEC-08**
4. [x] Corrigir opções de message broker para Kafka ou JMS - **SEC-09**
5. [x] Substituir "compliant" por "Assente em" - **SEC-03, SEC-05**
6. [x] Verificar se stack React/.NET está corretamente descrita - **SEC-04, SEC-05**

---

## TEMA H - Infraestrutura e Plataforma

**Prioridade:** MÉDIA-ALTA
**Seção afetada:** SEC-10
**Status:** [x] Resolvido (2026-01-21)

### Resolução Aplicada

- AKS substituído por **OpenShift** em toda a seção
- Diagrama atualizado com OpenShift Cluster e backend existente (IBM API Gateway, Siebel)
- Namespaces alterados de "homebanking-*" para **"best-web-*"**
- Seção de CI/CD simplificada (reutiliza pipeline existente)
- Seções de Secrets e Container Registry simplificadas (reutilizam infraestrutura existente)
- Adicionada lista de pendências para validação com equipa de infraestrutura
- Nota sobre F5 por ambiente adicionada

### Problema Principal

A infraestrutura descrita não corresponde à realidade. O ambiente é **OpenShift**, não AKS.

### Comentários Relacionados

| # | Parágrafo | Citação | Comentário JGC |
|---|-----------|---------|----------------|
| 47 | 5595 | (diagrama infraestrutura) | "Não é AKS, é openshift" |
| 47 (reply) | 5595 | - | "Neste contexto já não é Kibana mas não será relevante, penso" |
| 48 | 5622 | "Plataforma futuraOpenShift (em homologação)" | "Não percebi o atual/em homologação" |
| 49 | 5648 | (requisitos container OpenShift) | "Mais ou menos assim." |
| 50 | 5743 | "prodProduçãohomebanking-prodManual (aprovação)" | "Aqui temos de ver se isto entra no cluster nb. Os nomes podem não ser estes porque deveria descrever o best" |
| 50 (reply) | 5743 | - | "Era importante descrever os ambientes produtivos e não produtivos e onde vai ficar nos vários ambientes, nomeadamente se existe ou não F5" |

### Correções Necessárias

| Item | Atual | Correção |
|------|-------|----------|
| Plataforma | AKS | **OpenShift** |
| Logging | Kibana | Verificar se relevante |
| Namespaces | homebanking-* | Nomes que descrevam o BEST |

### Questões Pendentes (para Equipa de Infraestrutura)

- [ ] Clarificar "atual" vs "em homologação" para OpenShift - **Aguarda validação infra**
- [x] Definir nomes corretos dos namespaces (devem descrever BEST) - **best-web-* definido**
- [ ] Definir ambientes produtivos vs não produtivos - **Aguarda validação infra**
- [ ] Existe F5 em todos os ambientes? - **Aguarda validação infra**
- [ ] Projeto entra no cluster NB? - **Aguarda validação infra**

### Ações Concluídas

1. [x] Substituir AKS por OpenShift em toda a seção - **SEC-10 atualizada**
2. [ ] Clarificar situação atual da plataforma - **Aguarda validação infra**
3. [x] Definir nomenclatura correta de namespaces - **best-web-dev/qa/prod**
4. [ ] Documentar ambientes com/sem F5 - **Pendência registada em SEC-10**
5. [x] Validar requisitos de container OpenShift - **SEC-10 atualizada**

---

## TEMA I - CI/CD e DevOps

**Prioridade:** BAIXA
**Seção afetada:** SEC-10
**Status:** [x] Resolvido (2026-01-21)

### Resolução Aplicada

- Seção de CI/CD simplificada conforme indicação do cliente
- Removidos detalhes de ferramentas específicas (Azure Pipelines, ACR, etc.)
- Adicionada nota indicando que reutiliza pipeline existente
- Mantidos apenas requisitos mínimos de Quality Gates
- Pendência adicionada para validação com equipa de infraestrutura

### Problema Principal

A seção de CI/CD descreve em detalhe algo que já existe e será reutilizado. Pode não fazer sentido detalhar neste documento.

### Comentários Relacionados

| # | Parágrafo | Comentário JGC |
|---|-----------|----------------|
| 51 | 5798 | "Isto já se encontra implementado. Será reutilizar o que existe. Há coisas que descrevem corretamente o que está, outras nem por isso, outras nem tenho visibilidade de como está. Teria de ser a equipa de infra a descrever. Pode não fazer sentido estar neste documento." |

### Questões Pendentes (para Equipa de Infraestrutura)

- [x] Manter seção de CI/CD detalhada ou simplificar? - **Simplificado**
- [ ] Equipa de infra deve validar/descrever? - **Aguarda sessão com infra**

### Ações Concluídas

1. [x] Decidir nível de detalhe para CI/CD - **Simplificado**
2. [ ] Se manter, validar com equipa de infra - **Pendência registada em SEC-10**
3. [x] Se simplificar, indicar apenas que reutiliza pipeline existente - **SEC-10 atualizada**

---

## TEMA J - Logging e Observabilidade

**Prioridade:** MÉDIA
**Seções afetadas:** SEC-05, SEC-11
**Status:** [x] Resolvido (2026-01-21)

### Resolução Aplicada

- Adicionada nota de pendência em SEC-11 (11.2) para confirmar ELK Stack com NB
- Adicionada nota sobre desafios de logging do frontend (segurança, custos) em SEC-11 (11.2)
- Adicionada nota sobre mascaramento vs cifragem em SEC-11 (11.4)
- Adicionada secção "Itens Pendentes" em SEC-11 com todas as questões

### Problema Principal

Questões sobre a stack de logging (ELK), logs do frontend (desafios de segurança), e mascaramento vs cifragem de dados sensíveis.

### Comentários Relacionados

| # | Parágrafo | Citação | Comentário JGC |
|---|-----------|---------|----------------|
| 14 | 1090 | "Stack ELK" | "Isto é os logs que apresentámos ou é outra coisa?" |
| 22 | 2309 | (diagrama logging) | "O tema do log a partir do frontend tem alguns desafios (nomeadamente de segurança) e custos face ao benefício. A discutir, sabendo das vantagens que tem usar" |
| 22 (reply) | 2309 | - | "Neste boneco e nos outros não deveríamos ter o siebel pelo menos à frente dos serviços core? Não me parece que este reflita o modelo claramente" |
| 53 | 6655 | "11.4 Logging" | "Podemos partilhar a estrutura dos logs" |
| 54 | 6833 | "TokensNunca logar" | "Sobre estes campos - nunca necessitam para diagnóstico ou auditoria dos campos não mascarados? Ou seja, em vez de mascarar, cifrar" |

### Questões Pendentes (para o Cliente)

- [ ] ELK Stack é o que foi apresentado pelo NB? - **Aguarda confirmação infra**
- [ ] Logging do frontend: implementar ou não? (custo/benefício) - **Aguarda decisão cliente/segurança**
- [ ] Mascaramento vs cifragem para auditoria/diagnóstico - **Aguarda decisão segurança**
- [ ] NB pode partilhar estrutura de logs existente? - **Aguarda informação infra**

### Ações Concluídas

1. [x] Documentar pendência de confirmação do ELK Stack - **SEC-11 secção 11.2**
2. [x] Documentar desafios de logging do frontend - **SEC-11 secção 11.2**
3. [x] Documentar questão de mascaramento vs cifragem - **SEC-11 secção 11.4**
4. [ ] Obter estrutura de logs do NB para alinhar - **Pendência registada para o cliente**

---

## TEMA K - Offline e PWA

**Prioridade:** BAIXA
**Seção afetada:** SEC-04 (4.5)
**Status:** [x] Resolvido (2026-01-21)

### Resolução Aplicada

- Secção 4.5 já indicava "Não" para PWA/Offline (atualização anterior)
- Adicionada nota sobre tratamento de falhas de comunicação (retry, feedback, mensagens)
- Removida referência a Service Workers na secção de caching (4.10.2)
- Checkbox de entregáveis marcado como concluído

### Problema Principal

O documento menciona "A definir" para funcionalidades offline/PWA, mas o cliente indica que isto nunca foi suportado no NB e o custo/benefício não justifica.

### Comentários Relacionados

| # | Parágrafo | Citação | Comentário JGC |
|---|-----------|---------|----------------|
| 19 | 1735 | "Funcionamento OfflineA definirNecessita aprofundamento" | "Neste momento não temos suporte para isto. A implementar temos de ver o que se pretende realmente. Uma coisa é suportar falhas de comunicação, outra coisa é fazer tudo offline quando a maior parte da funcionalidade depende de serviços remotos" |
| 19 (reply) | 1735 | - | "No nb nunca houve caso de uso custo benefício para isto" |

### Ações Concluídas

1. [x] Marcar funcionalidades offline como "Não aplicável" - **SEC-04 secção 4.5**
2. [x] Documentar tratamento de falhas de comunicação (retry, feedback) - **SEC-04 secção 4.5**
3. [x] Remover referência a Service Workers - **SEC-04 secção 4.10.2**
4. [x] Atualizar checkbox de entregáveis - **SEC-04 Entregáveis**

---

## TEMA L - Design System e Componentes

**Prioridade:** MÉDIA
**Seção afetada:** SEC-04 (4.6, 4.7)
**Status:** [x] Resolvido (2026-01-21)

### Resolução Aplicada

- Adicionada nota de pendência em SEC-04 (4.6) sobre sessão específica de React
- Atualizada secção 4.7.1: componentes pela Havas, Storybook em fase posterior
- Adicionada nota em SEC-04 (4.9) sobre detalhes em âmbito de implementação
- Adicionados itens pendentes em SEC-04 para sessão React e alinhamento

### Problema Principal

A stack frontend e design system precisam ser fechados em conjunto com o NB. Os componentes estão a ser desenvolvidos pela Havas, sem Storybook no âmbito inicial.

### Comentários Relacionados

| # | Parágrafo | Citação | Comentário JGC |
|---|-----------|---------|----------------|
| 20 | 1760 | (stack frontend) | "Este stack temos de fechar em conjunto. Há coisas que temos na framework mas outras temos alternativas." |
| 20 (reply) | 1760 | - | "A base já foi alinhada também com a Havas" |
| 20 (reply 2) | 1760 | - | "Temos de alinhar também o 4.6.2. e o 3 para ver se estamos alinhados com o que é a vossa visão para a coisa. Aqui deveríamos de fazer uma sessão específica de react." |
| 20 (reply 3) | 1760 | - | "Idem 4.7 e 4.8" |
| 20 (reply 4) | 1760 | - | "O 4.9 teremos de detalhar melhor em âmbito de implementação" |
| 21 | 1958 | "Figma (design) + Storybook (desenvolvimento)" | "Os componentes estão a ser desenvolvido pela Havas" |
| 21 (reply) | 1958 | - | "(pelo menos o âmbito inicial). Sem storybook" |

### Questões Pendentes (para o Cliente)

- [ ] Sessão específica de React para alinhar stack? - **Aguarda agendamento**
- [ ] Quais alternativas existem na framework do NB? - **Aguarda sessão React**
- [ ] O que já foi alinhado com a Havas? - **Base alinhada, detalhes em sessão**

### Ações Concluídas

1. [x] Documentar necessidade de sessão técnica de React - **SEC-04 secção 4.6**
2. [x] Indicar secções a validar (4.6.2, 4.6.3, 4.7, 4.8) - **SEC-04 secção 4.7.1**
3. [x] Atualizar referência a Storybook (fase posterior) - **SEC-04 secção 4.7.1**
4. [x] Indicar que componentes são desenvolvidos pela Havas - **SEC-04 secção 4.7.1**
5. [x] Indicar que 4.9 será detalhado em implementação - **SEC-04 secção 4.9**

---

## TEMA M - Pontos Menores e Clarificações

**Prioridade:** BAIXA-MÉDIA
**Status:** [x] Resolvido (2026-01-21)

### Resolução Aplicada

- SEC-02: Reformulado "Tecnologias 100% Web" para clarificar significado
- SEC-04: Clarificado lazy loading de traduções (interno à app React)
- SEC-05: Adicionadas notas sobre Message Queues, Bulkhead e degradação graceful
- SEC-06: Clarificados dados específicos web e encriptação como "em definição"
- SEC-07: Adicionadas pendência de validação, tempos configuráveis, responsabilidade ABAC
- SEC-09: Adicionadas notas sobre notificações (requisito de negócio) e retry 5xx

### Lista de Pontos

| # | Parágrafo | Seção | Citação | Comentário JGC | Ação |
|---|-----------|-------|---------|----------------|------|
| 2 | 250 | SEC-01/02 | "Reutilização da infraestrutura..." | "No que falámos anteriormente teríamos o BFF para suportar a componente web. Isto pode não ser relevante nesta fase mas será mais ainda quando tivermos mais canais com especificidades." | Adicionar nota sobre BFF multi-canal |
| 2 (reply) | 250 | SEC-01/02 | - | "Adicionalmente há o princípio de poder optar pela incorporação de funcionalidades web na app (que pode contrariar a afirmação de não ter dependências com os componentes nativos)" | Clarificar princípio de web-in-app |
| 7 | 868 | SEC-02 | "Tecnologias 100% Web (sem componentes nativos)" | "Se quisermos colocar funcionalidades web na app vamos ter provavelmente de fazer uma integração mais forte para providenciar por exemplo navegação ou biometria. Se o objetivo é indicar que funcionalidades nativas não aparecem na web, então sim" | Reformular para clarificar |
| 8 | 916 | SEC-02 | "A validar" (documentação) | "Esclareçam este ponto: Isto é a documentação do lado dos serviços, do BEST? Do lado do consumo vocês têm esse conhecimento?" | Clarificar fonte de documentação |
| 15 | 1121 | SEC-08 | "A definir" (segregação) | "Entre plataformas?" | Clarificar contexto |
| 18 | 1707 | SEC-04 | "lazy loading de traduções" | "Lazy loading de serviço externo ou dentro da aplicação react?" | Clarificar se é externo ou interno |
| 25 | 2636 | SEC-05 | "Message QueuesA definir..." | "Algum caso de uso concreto?" | Identificar casos de uso |
| 26 | 2786 | SEC-05 | "BulkheadNao previsto-" | "O formato disto depende de quantos serviços forem. Se é um 'best' ou se é uma organização diferente, por domínio, ou um best para a componente de negócio e outros especializados ao lado que não estejam cobertos no siebel" | Esclarecer organização de serviços |
| 26 (reply) | 2786 | SEC-05 | - | "Se percebo mais abaixo estão a propor autonomizar um authservice???" | Clarificar proposta de AuthService |
| 28 | 2909 | SEC-05 | "Degradação graceful (sem logs)" | "Se percebo, sem logs continuamos. Validar com o negócio" | Validar com negócio |
| 30 | 2993 | SEC-05 | (diagrama) | "O que representam como retângulos são serviços autónomos?" | Clarificar representação |
| 31 | 3146 | SEC-06 | "Não há dados específicos..." | "Isto quer dizer que não há funcionalidade nem layouts que possam necessitar de novos dados?" | Clarificar |
| 32 | 3218 | SEC-06 | "Sem requisitos específicos" | "A detalhar em âmbito de projeto. Estamos a trabalhar sobre isto" | Indicar como "em definição" |
| 33 | 3419 | SEC-07 | "Visão Geral de Autenticação" | "A validar com mais detalhe. Não consigo no feedback de hoje" | Agendar validação |
| 35 | 3592 | SEC-07 | (tempos de sessão) | "Os tempos são sugestões. Deveria ser por configuração" | Indicar como configuráveis |
| 36 | 3624 | SEC-07 | "Desejável (pendente aprovação cliente)" | "O que isto quer dizer?" | Clarificar redação |
| 37 | 3711 | SEC-07 | (ABAC/RBAC) | "Isto encaixa em que layer? Quem é responsável pela validação?" | Definir responsabilidade |
| 43 | 4904 | SEC-09 | (notificações) | "O requerer notificação será um requisito de negócio e não de frontend." | Mover para requisitos de negócio |
| 43 (reply) | 4904 | SEC-09 | - | "Isto não é contrário à assunção anterior que não havia dados específicos para web?" | Verificar consistência |
| 45 | 5217 | SEC-09 | "Erros de servidor (5xx)" | "Estão a fazer isto na app?" | Verificar implementação atual |

---

## TEMA N - Observabilidade (Sessão Adicional)

**Prioridade:** MÉDIA
**Seção afetada:** SEC-11
**Status:** [x] Resolvido (2026-01-21)

### Resolução Aplicada

- Adicionada nota de destaque no início de SEC-11 sobre sessão requerida
- Adicionada referência a avaliação de custo/benefício
- Sessão com infraestrutura já documentada nos Itens Pendentes (Tema J)

### Comentário Relacionado

| # | Parágrafo | Citação | Comentário JGC |
|---|-----------|---------|----------------|
| 52 | 6426 | "11. Observabilidade & Operações" | "Marcar sessão para rever com equipa de infra. Penso que seria prudente perceber os requisitos concretos. Atenção que coisas que não são realmente usadas no dia a dia, a serem implementadas terão custos." |

### Ações Concluídas

1. [x] Documentar necessidade de sessão com equipa de infra - **SEC-11 nota inicial + Itens Pendentes**
2. [x] Registar necessidade de identificar requisitos concretos - **SEC-11 Itens Pendentes**
3. [x] Documentar avaliação de custo/benefício - **SEC-11 nota inicial**

---

## Resumo de Ações por Seção

| Seção | Temas | Prioridade |
|-------|-------|------------|
| SEC-01 | A, B | Alta |
| SEC-02 | A, B, C, D, M | Alta |
| SEC-03 | A, B | Alta |
| SEC-04 | G, K, L, M | Média |
| SEC-05 | A, B, G, J, M | Alta |
| SEC-06 | M | Baixa |
| SEC-07 | E, M | Alta |
| SEC-08 | E, G, M | Alta |
| SEC-09 | A, B, F, G, M | Alta |
| SEC-10 | H, I | Média |
| SEC-11 | J, N | Média |
| SEC-12 | D | Média |

---

## Histórico de Atualizações

| Data | Ação | Responsável |
|------|------|-------------|
| 2026-01-20 | Criação do documento de análise | NextReality |
| 2026-01-21 | Resolução Tema A e B: Diagrama único, arquitetura corrigida | NextReality |
| 2026-01-21 | Resolução parcial Tema G: OpenAPI 3.1, Kafka/JMS | NextReality |
| 2026-01-21 | Resolução Tema E: Segurança Web vs Mobile (SEC-07, SEC-08) | NextReality |
| 2026-01-21 | Resolução adicional Tema G: CDN, dangerouslySetInnerHTML | NextReality |
| 2026-01-21 | Resolução Tema H e I: OpenShift, namespaces best-web-*, CI/CD simplificado | NextReality |
| 2026-01-21 | Resolução completa Tema G: "compliant" → "Assente em" (SEC-03, SEC-05) | NextReality |
| 2026-01-21 | Verificação e consolidação: checkboxes atualizados, pendências clarificadas | NextReality |
| 2026-01-21 | Resolução Tema C: MVP reformulado, secção 2.8 Estratégia de Lançamento adicionada | NextReality |
| 2026-01-21 | Resolução Tema D: Notas de calibração em SEC-02 e SEC-12, pendências registadas | NextReality |
| 2026-01-21 | Resolução Tema F: Secção 9.6 adicionada em SEC-09, pendências registadas | NextReality |
| 2026-01-21 | Resolução Tema J: Notas de logging em SEC-11, pendências registadas | NextReality |
| 2026-01-21 | Resolução Tema K: PWA/Offline marcado como N/A, tratamento de falhas documentado | NextReality |
| 2026-01-21 | Resolução Tema L: Design System atualizado, Havas e Storybook documentados | NextReality |
| 2026-01-21 | Resolução Tema M: Clarificações em SEC-02/04/05/06/07/09 | NextReality |
| 2026-01-21 | Resolução Tema N: Nota de sessão e custo/benefício em SEC-11 | NextReality |
| 2026-01-21 | **TODOS OS 14 TEMAS RESOLVIDOS** | NextReality |

