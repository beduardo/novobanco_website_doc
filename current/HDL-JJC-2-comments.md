# Document Comments

## Comment 1

**Location:** Paragraph 241

**Author:** Jorge Gomes Costa (novobanco DSI Direção) | **Date:** 2026-01-16 11:41:00

**Comment:**

Não reflete o fluxo que apresentámos e tem de ter mais detalhe para ser claro. Os serviços de BFF não têm apigw à frente (pelo menos à data), os serviços chamados pela app irão ter. Ou seja, deve refletir o fluxo apresentado na ultima sessão.

  ### Reply

  **Author:** Jorge Gomes Costa (novobanco DSI Direção) | **Date:** 2026-01-16 11:48:00

  **Comment:**

  Aqui tambem é relevante colocar os serviços da app que são necessários mas que não cabem neste sistema. Por exemplo os acessos diretos ao azure para algumas funcionalidades. Estes tem de ser visto como transitam para a nova realidade.

  ### Reply

  **Author:** Jorge Gomes Costa (novobanco DSI Direção) | **Date:** 2026-01-16 14:55:00

  **Comment:**

  Já vi que mais abaixo têm um boneco mais fiel ao que falámos. Porqu~e de aqui estar diferente?

---

## Comment 2

**Location:** Paragraph 250

**Author:** Jorge Gomes Costa (novobanco DSI Direção) | **Date:** 2026-01-16 11:45:00

**Commented text:**

> Reutilização da infraestrutura e serviços da aplicação mobile nativa existente - Tecnologias 100% Web (sem dependências de componentes nativos) - Conformidade com regulamentações bancárias portuguesas

**Comment:**

No que falámos anteriormente teriamos o BFF para suportar a componente web. Isto pode não ser relevante nesta fase mas será mais ainda quando tivermos mais canais com especificidades.

  ### Reply

  **Author:** Jorge Gomes Costa (novobanco DSI Direção) | **Date:** 2026-01-16 11:46:00

  **Commented text:**

  > Reutilização da infraestrutura e serviços da aplicação mobile nativa existente - Tecnologias 100% Web (sem dependências de componentes nativos) - Conformidade com regulamentações bancárias portuguesas

  **Comment:**

  Adicionalmente há o principio de poder optar pela incorporação de funcionalidades web na app (que pode contrariar a afirmaçao de não ter dependencias com os componentes nativos)

---

## Comment 3

**Location:** Paragraph 335

**Author:** Jorge Gomes Costa (novobanco DSI Direção) | **Date:** 2026-01-16 11:55:00

**Commented text:**

> O projeto HomeBanking Web visa disponibilizar aos clientes do Novo Banco uma plataforma web com funcionalidades equivalentes à aplicação mobile nativa existente. A solução reutilizará a infraestrutura e serviços já criados para a app mobile.

**Comment:**

Mais uma vez, no que temos atualmente o bff está a dar suporte ao spa. Pode ser quase proxy direta mas é assim que está. Há varias coisas que vêm daqui, como o tema dos logs ou segurança que têm de ser implementados em algum lado

---

## Comment 4

**Location:** Paragraph 585

**Author:** Jorge Gomes Costa (novobanco DSI Direção) | **Date:** 2026-01-16 11:58:00

**Commented text:**

> MVP: Todas as 35 funcionalidades fazem parte do MVP

**Comment:**

Era relevante ver como fazemos o switch, Na realidade naõ existe MVP mas deveriamos definir se teremos uma estrategia de bigbang ou outra porque isto pode influenciar o desenho e a infraestrutura

---

## Comment 5

**Location:** Paragraph 758

**Author:** Jorge Gomes Costa (novobanco DSI Direção) | **Date:** 2026-01-16 12:23:00

**Commented text:**

> Sim

**Comment:**

É importante calibrar este valor. Pedidos/segundo normal e em pico

---

## Comment 6

**Location:** Paragraph 855

**Author:** Jorge Gomes Costa (novobanco DSI Direção) | **Date:** 2026-01-16 14:13:00

**Commented text:**

> Reutilização de APIs e serviços da app mobile

**Comment:**

Mais uma vez-isto tem de ser afinado. A ideia será reutilizar mas não diretamente. Sempre falámos do BFF à frente para a Web

---

## Comment 7

**Location:** Paragraph 868

**Author:** Jorge Gomes Costa (novobanco DSI Direção) | **Date:** 2026-01-16 14:14:00

**Commented text:**

> Tecnologias 100% Web (sem componentes nativos)

**Comment:**

Se quisermos colocar funcionalidades web na app vamos ter provavelmente de fazer uma integração mais forte para providenciar por exemplo navegaçao ou biometria. Se o objetivo e indicar que funcionalidades nativas não aparecem na web, então sim

---

## Comment 8

**Location:** Paragraph 916

**Author:** Jorge Gomes Costa (novobanco DSI Direção) | **Date:** 2026-01-16 14:16:00

**Commented text:**

> A validar

**Comment:**

Esclareçam este ponto: Isto é a documentação do lado dos serviços, do BEST? Do lado do consumo vocês têm esse conhecimento?

---

## Comment 9

**Location:** Paragraph 927

**Author:** Jorge Gomes Costa (novobanco DSI Direção) | **Date:** 2026-01-16 14:17:00

**Commented text:**

> validar

**Comment:**

A proposta com o react e .net é uma utilizaçao equivalente ao que estamos a usar a todos os contextos de canais internos e externos no NB pelo que deverá ser adequada. Sendo que é a que apresentámos, não a que está neste documento.

---

## Comment 10

**Location:** Paragraph 938

**Author:** Jorge Gomes Costa (novobanco DSI Direção) | **Date:** 2026-01-16 14:20:00

**Commented text:**

> A validar

**Comment:**

Diria que os requisitos de segurança são diferentes necessariamente. Isto porque o ecossistema nativo é mais protegido que o web. Se o que estamos a falar é do protocolo, existem alguns temas que necessitam revisão porque parecem ser potenciais temas de segurança. 

  ### Reply

  **Author:** Jorge Gomes Costa (novobanco DSI Direção) | **Date:** 2026-01-16 14:24:00

  **Commented text:**

  > A validar

  **Comment:**

  Um dos pontos que me parece que tem de ser mesmo revisto é o tema das credenciais retornadas no login. Em nativo diria que há argumento para questionar a sua presença, na web isto necessita de uma revisão sobre risco e vetores de ataque que possam comprometer as credenciais do banco nas plataformas

---

## Comment 11

**Location:** Paragraph 949

**Author:** Jorge Gomes Costa (novobanco DSI Direção) | **Date:** 2026-01-16 14:22:00

**Commented text:**

> Sim

**Comment:**

Terceiros é outras entidades ou outros sistemas? Neste documento deveriam estar identificados e termos solução para todas as coisas que não estejam presentes no middleware do BEST e que serão necessários para a solução (como os serviços em azure ou outros)

  ### Reply

  **Author:** Jorge Gomes Costa (novobanco DSI Direção) | **Date:** 2026-01-16 14:30:00

  **Commented text:**

  > Sim

  **Comment:**

  A abertura de conta tambem faz parte do projeto (sei que está a ser tratada separadamenete). Nesse caso há interações com terceiros ou não?

---

## Comment 12

**Location:** Paragraph 955

**Author:** Jorge Gomes Costa (novobanco DSI Direção) | **Date:** 2026-01-16 14:25:00

**Comment:**

Este diagrama não reflete o que temos falado

  ### Reply

  **Author:** Jorge Gomes Costa (novobanco DSI Direção) | **Date:** 2026-01-16 14:25:00

  **Comment:**

  O 3.2 já esta alinhado. Porque a diferença?

---

## Comment 13

**Location:** Paragraph 1045

**Author:** Jorge Gomes Costa (novobanco DSI Direção) | **Date:** 2026-01-16 14:26:00

**Commented text:**

> compliant 

**Comment:**

Assente em

---

## Comment 14

**Location:** Paragraph 1090

**Author:** Jorge Gomes Costa (novobanco DSI Direção) | **Date:** 2026-01-16 14:29:00

**Commented text:**

> Stack ELK

**Comment:**

Isto é os logs que apresentámos ou é outra coisa?

---

## Comment 15

**Location:** Paragraph 1121

**Author:** Jorge Gomes Costa (novobanco DSI Direção) | **Date:** 2026-01-16 14:58:00

**Commented text:**

> A definir

**Comment:**

Entre plataformas?

---

## Comment 16

**Location:** Paragraph 1132

**Author:** Jorge Gomes Costa (novobanco DSI Direção) | **Date:** 2026-01-16 14:59:00

**Comment:**

Embora não seja primário, nem seja a diraçaõ para os serviços core do best, neste boneco tambem deveria contemplar o canal web a correr na app.

  ### Reply

  **Author:** Jorge Gomes Costa (novobanco DSI Direção) | **Date:** 2026-01-16 15:00:00

  **Comment:**

  Convinha esclarecer o tema dos backend services. Onde fica a validação do token neste desenho? O bff não faz, a apigw tambem não. Onde está?

  ### Reply

  **Author:** Jorge Gomes Costa (novobanco DSI Direção) | **Date:** 2026-01-16 15:02:00

  **Comment:**

  Uma coisa que eera importante era tentar avaliar se queremos 1 container por layer "banco best" ou se vamos segregar de alguma forma.

---

## Comment 17

**Location:** Paragraph 1291

**Author:** Jorge Gomes Costa (novobanco DSI Direção) | **Date:** 2026-01-16 15:05:00

**Commented text:**

> SCA obrigatório, ponto de entrada

**Comment:**

Talvez este requisitp possa ser trabalhado mais tarde mas é importante detalhar o tema de como serão implementadas as componentes de segurança. Há um serviço de login - o pin + pass vai em claro? Depois é criado algo que é devolvido no login, sendo que parte deveria ser em cookie secure/httponly para garantir que não é capturado em javascript

---

## Comment 18

**Location:** Paragraph 1707

**Author:** Jorge Gomes Costa (novobanco DSI Direção) | **Date:** 2026-01-16 15:06:00

**Commented text:**

> lazy loading de traduções 

**Comment:**

Lazy loading de serviço externo ou dentro da aplicaçao react?

---

## Comment 19

**Location:** Paragraph 1735

**Author:** Jorge Gomes Costa (novobanco DSI Direção) | **Date:** 2026-01-16 15:08:00

**Commented text:**

> Funcionamento OfflineA definirNecessita aprofundamento

**Comment:**

Neste momento não temos suporte para isto. A implementar temos de ver o que se pretende realmente. Uma coisa é suportar falhas de comunicaçao, outra coisa é fazer tudo offline quando a maior parte da funcionalidade depende de serviços remotos

  ### Reply

  **Author:** Jorge Gomes Costa (novobanco DSI Direção) | **Date:** 2026-01-16 15:08:00

  **Commented text:**

  > Funcionamento OfflineA definirNecessita aprofundamento

  **Comment:**

  No nb nunca houve caso de uso custo beneficio para isto

---

## Comment 20

**Location:** Paragraph 1760

**Author:** Jorge Gomes Costa (novobanco DSI Direção) | **Date:** 2026-01-16 15:15:00

**Comment:**

Este stack temos de fechar em conjunto. Há coisas que temos na framework mas outras temos alternativas.

  ### Reply

  **Author:** Jorge Gomes Costa (novobanco DSI Direção) | **Date:** 2026-01-16 15:25:00

  **Comment:**

  A base já foi alinhada tambem com a Havas

  ### Reply

  **Author:** Jorge Gomes Costa (novobanco DSI Direção) | **Date:** 2026-01-16 15:27:00

  **Comment:**

  Temos de alinhar tambem o 4.6.2. e o 3 para ver se estamos alinhados com o que é a vossa visão para a coisa. Aqui deveriamos de fazer uma sessão especifica de react.

  ### Reply

  **Author:** Jorge Gomes Costa (novobanco DSI Direção) | **Date:** 2026-01-16 15:30:00

  **Comment:**

  Idem 4.7 e 4.8

  ### Reply

  **Author:** Jorge Gomes Costa (novobanco DSI Direção) | **Date:** 2026-01-16 18:25:00

  **Comment:**

  O 4.9 teremos de detalhar melhor em ambito de implementaçao

---

## Comment 21

**Location:** Paragraph 1958

**Author:** Jorge Gomes Costa (novobanco DSI Direção) | **Date:** 2026-01-16 15:28:00

**Commented text:**

> Figma (design) + Storybook (desenvolvimento)

**Comment:**

Os componentes estão a ser desenvolvido pela Havas

  ### Reply

  **Author:** Jorge Gomes Costa (novobanco DSI Direção) | **Date:** 2026-01-16 15:29:00

  **Commented text:**

  > Figma (design) + Storybook (desenvolvimento)

  **Comment:**

  (pelo menos o ambito inicial). Sem storybook

---

## Comment 22

**Location:** Paragraph 2309

**Author:** Jorge Gomes Costa (novobanco DSI Direção) | **Date:** 2026-01-16 18:31:00

**Comment:**

O tema do log a partir do frontend tem alguns desafios (noemadamente de segurança) e custos face ao beneficio. A discutir, sabendo das vantages que tem usar

  ### Reply

  **Author:** Jorge Gomes Costa (novobanco DSI Direção) | **Date:** 2026-01-16 18:32:00

  **Comment:**

  Neste boneco e nos outros não deveriamos ter o siebel pelo menos à frente dos serviços core? Não me parece que este reflita o modelo claramente

---

## Comment 23

**Location:** Paragraph 2496

**Author:** Jorge Gomes Costa (novobanco DSI Direção) | **Date:** 2026-01-16 18:33:00

**Commented text:**

> Rate LimitingNaoResponsabilidade do Gateway

**Comment:**

Ressumbissões?

  ### Reply

  **Author:** Jorge Gomes Costa (novobanco DSI Direção) | **Date:** 2026-01-16 18:33:00

  **Commented text:**

  > Rate LimitingNaoResponsabilidade do Gateway

  **Comment:**

  Atençaõ que no BFF não há APIGW à frente

---

## Comment 24

**Location:** Paragraph 2582

**Author:** Jorge Gomes Costa (novobanco DSI Direção) | **Date:** 2026-01-16 18:35:00

**Comment:**

Da ultima sessão, o bearer tem de passar para lá da APIGW. Para a apigw e clientid+secret

---

## Comment 25

**Location:** Paragraph 2636

**Author:** Jorge Gomes Costa (novobanco DSI Direção) | **Date:** 2026-01-16 18:35:00

**Commented text:**

> Message QueuesA definir - Necessita aprofundamento

**Comment:**

Algum caso de uso concreto?

---

## Comment 26

**Location:** Paragraph 2786

**Author:** Jorge Gomes Costa (novobanco DSI Direção) | **Date:** 2026-01-16 18:37:00

**Commented text:**

> BulkheadNao previsto-

**Comment:**

O formato disto depende de quantos serviços forem. Se é um "best" ou se é uma organizçao diferente, por dominio, ou um best para a componentte de negocio e outros especializados ao lado que não estejam cobertos no siebel

  ### Reply

  **Author:** Jorge Gomes Costa (novobanco DSI Direção) | **Date:** 2026-01-16 18:41:00

  **Commented text:**

  > BulkheadNao previsto-

  **Comment:**

  Se percebo mais a baixo estão a propor autonomizar um authservice???

---

## Comment 27

**Location:** Paragraph 2834

**Author:** Jorge Gomes Costa (novobanco DSI Direção) | **Date:** 2026-01-16 18:38:00

**Commented text:**

> OpenAPI 3.0

**Comment:**

3.1

---

## Comment 28

**Location:** Paragraph 2909

**Author:** Jorge Gomes Costa (novobanco DSI Direção) | **Date:** 2026-01-16 18:39:00

**Commented text:**

> Degradacao graceful (sem logs)

**Comment:**

Se percebo, sem logs continuamos. Validar com o negócio

---

## Comment 29

**Location:** Paragraph 2967

**Author:** Jorge Gomes Costa (novobanco DSI Direção) | **Date:** 2026-01-16 18:40:00

**Commented text:**

> Bearer token para backend services

**Comment:**

Os backend services como representados na figura não estão preparados para receber o bearer.

---

## Comment 30

**Location:** Paragraph 2993

**Author:** Jorge Gomes Costa (novobanco DSI Direção) | **Date:** 2026-01-16 18:43:00

**Comment:**

O que representam como retangulos são serviços autonomos? 

---

## Comment 31

**Location:** Paragraph 3146

**Author:** Jorge Gomes Costa (novobanco DSI Direção) | **Date:** 2026-01-16 18:46:00

**Commented text:**

> Não há dados específicos do canal web que não existam na app mobileCanal web consome os mesmos backend services e modelo de domínio

**Comment:**

Isto quer dizer que não há funcionalidade nem layouts que possam necessitar de novos dadsos?

---

## Comment 32

**Location:** Paragraph 3218

**Author:** Jorge Gomes Costa (novobanco DSI Direção) | **Date:** 2026-01-16 18:47:00

**Commented text:**

> Sem requisitos específicos

**Comment:**

A detalhar em ambito de projeto. Estamos a trabalhar sobre isto

---

## Comment 33

**Location:** Paragraph 3419

**Author:** Jorge Gomes Costa (novobanco DSI Direção) | **Date:** 2026-01-16 18:50:00

**Commented text:**

> Visão Geral de Autenticação

**Comment:**

A validar com mais detalhe. Não consigo no feedback de hoje

---

## Comment 34

**Location:** Paragraph 3512

**Author:** Jorge Gomes Costa (novobanco DSI Direção) | **Date:** 2026-01-16 18:51:00

**Comment:**

A apigw não aparece porque estão a simplificar o desenho?

---

## Comment 35

**Location:** Paragraph 3592

**Author:** Jorge Gomes Costa (novobanco DSI Direção) | **Date:** 2026-01-16 18:53:00

**Comment:**

Os temos são sugestões. Deveria ser por configuraçaõ

---

## Comment 36

**Location:** Paragraph 3624

**Author:** Jorge Gomes Costa (novobanco DSI Direção) | **Date:** 2026-01-16 18:53:00

**Commented text:**

> Desejável (pendente aprovação cliente)

**Comment:**

O que isto quer dizer?

---

## Comment 37

**Location:** Paragraph 3711

**Author:** Jorge Gomes Costa (novobanco DSI Direção) | **Date:** 2026-01-16 18:55:00

**Commented text:**

> AspetoDecisãoModeloABAC híbrido com RBACRoleAtributo do sujeito (quando necessário)AtributosSujeito, Recurso, Ação, AmbientePermissões por operaçãoSim (consulta vs transação)Atributos considerados:CategoriaAtributosSujeitoUtilizador, role, tipo de cliente, segmentoRecursoTipo de conta, produto, limiteAçãoConsulta, transação, configuraçãoAmbienteCanal (web), horário, localização, dispositivoNota: Roles e perfis específicos serão definidos no assessment inicial do projeto.

**Comment:**

Isto encaixa em que layer? Quem e responsavel pela validaçao?

---

## Comment 38

**Location:** Paragraph 4028

**Author:** Jorge Gomes Costa (novobanco DSI Direção) | **Date:** 2026-01-16 18:56:00

**Commented text:**

> Evitar; se necessário, atenção a atualizações de terceiros

**Comment:**

não usar

---

## Comment 39

**Location:** Paragraph 4068

**Author:** Jorge Gomes Costa (novobanco DSI Direção) | **Date:** 2026-01-16 18:58:00

**Commented text:**

> innerHTML e eval proibidos via lint e SonarQube

**Comment:**

Idem para dangerouslySetInnerHTML  

---

## Comment 40

**Location:** Paragraph 4473

**Author:** Jorge Gomes Costa (novobanco DSI Direção) | **Date:** 2026-01-16 19:00:00

**Comment:**

O backend api é o siebel? Quem trata do token tendo em conta que esta atras da apigw?

  ### Reply

  **Author:** Jorge Gomes Costa (novobanco DSI Direção) | **Date:** 2026-01-16 19:01:00

  **Comment:**

  A minha sgestão seria fazer um boneco com isto e referenciar. Têm varios muito parecidos e qq alteraçaõ depois têm de fazer em todos.

  ### Reply

  **Author:** Jorge Gomes Costa (novobanco DSI Direção) | **Date:** 2026-01-16 19:02:00

  **Comment:**

  O BFF eh 1 "container" o resto e o quê?

---

## Comment 41

**Location:** Paragraph 4568

**Author:** Jorge Gomes Costa (novobanco DSI Direção) | **Date:** 2026-01-16 19:03:00

**Comment:**

A apigw é da ibm. Mais uma vez - da conversa que tivemos com eles o token não e mapeado nela. Faltam coisas no boneco,

---

## Comment 42

**Location:** Paragraph 4837

**Author:** Jorge Gomes Costa (novobanco DSI Direção) | **Date:** 2026-01-16 19:04:00

**Commented text:**

> O canal web pode acionar envio de notificacoes (ex: confirmacao de transferencia)

**Comment:**

Isto já existe em app?

---

## Comment 43

**Location:** Paragraph 4904

**Author:** Jorge Gomes Costa (novobanco DSI Direção) | **Date:** 2026-01-16 19:05:00

**Comment:**

O requerer notificaçaõ será um requisito de negócio e não de frontend.

  ### Reply

  **Author:** Jorge Gomes Costa (novobanco DSI Direção) | **Date:** 2026-01-16 19:06:00

  **Comment:**

  Isto naõ eh contrario ah assunção anterior que não havia dados especificos para web?

---

## Comment 44

**Location:** Paragraph 5121

**Author:** Jorge Gomes Costa (novobanco DSI Direção) | **Date:** 2026-01-16 19:07:00

**Commented text:**

> Tecnologia (RabbitMQ, Kafka, Azure Service Bus)

**Comment:**

À partida kafka ou jms

---

## Comment 45

**Location:** Paragraph 5217

**Author:** Jorge Gomes Costa (novobanco DSI Direção) | **Date:** 2026-01-16 19:07:00

**Commented text:**

> Erros de servidor (5xx)

**Comment:**

Estão a fazer isto na app?

---

## Comment 46

**Location:** Paragraph 5540

**Author:** Jorge Gomes Costa (novobanco DSI Direção) | **Date:** 2026-01-16 19:09:00

**Comment:**

Acho que este diagrama tambem confunde. Depende do que querem expressar….

---

## Comment 47

**Location:** Paragraph 5595

**Author:** Jorge Gomes Costa (novobanco DSI Direção) | **Date:** 2026-01-16 19:10:00

**Comment:**

Não eh AKS, eh openshift

  ### Reply

  **Author:** Jorge Gomes Costa (novobanco DSI Direção) | **Date:** 2026-01-16 19:11:00

  **Comment:**

  Neste contexto já não é Kibana mas não será relevante, penso

---

## Comment 48

**Location:** Paragraph 5622

**Author:** Jorge Gomes Costa (novobanco DSI Direção) | **Date:** 2026-01-16 19:12:00

**Commented text:**

> Plataforma futuraOpenShift (em homologação)

**Comment:**

Não percebi o atual/em homologaçao

---

## Comment 49

**Location:** Paragraph 5648

**Author:** Jorge Gomes Costa (novobanco DSI Direção) | **Date:** 2026-01-16 19:14:00

**Commented text:**

> Requisitos de Imagens Container (OpenShift-Compliant)RequisitoDescriçãoUtilizador não-rootContainer executa como utilizador arbitrário (UID &gt; 1000)Filesystem read-onlyVolumes temporários montados explicitamentePortas &gt; 1024Não utilizar portas privilegiadasBase imageRed Hat UBI (Universal Base Image) recomendadoHealth checksLiveness e Readiness probes obrigatórios

**Comment:**

Mais ou menos assim. 

---

## Comment 50

**Location:** Paragraph 5743

**Author:** Jorge Gomes Costa (novobanco DSI Direção) | **Date:** 2026-01-16 19:14:00

**Commented text:**

> prodProduçãohomebanking-prodManual (aprovação)

**Comment:**

Aqui temos de ver se isto entra no cluster nb. Os nomes podem não ser estes porque deveria descrever o best

  ### Reply

  **Author:** Jorge Gomes Costa (novobanco DSI Direção) | **Date:** 2026-01-16 19:16:00

  **Commented text:**

  > prodProduçãohomebanking-prodManual (aprovação)

  **Comment:**

  Era importante descrever os ambientes produtivos e não produtivos e onde vai ficar nos vários ambientes, nomeadamente se existe ou não F5

---

## Comment 51

**Location:** Paragraph 5798

**Author:** Jorge Gomes Costa (novobanco DSI Direção) | **Date:** 2026-01-16 19:18:00

**Commented text:**

> CI/CD PipelineStack de CI/CDComponenteFerramentaRepositórioAzure Repos (Git)CI/CD PlatformAzure PipelinesContainer RegistryAzure Container Registry (ACR)SecretsAzure Key VaultIaCHelm Charts + TerraformBranchingGitFlowEstratégia de Branching (GitFlow)BranchPropósitoDeploy Automáticofeature/*Desenvolvimento de featuresNãodevelopIntegração contínuaDEVrelease/*Preparação de releaseQAmainProduçãoPROD (c/ aprovação)hotfix/*Correções urgentesPROD (c/ aprovação)Pipeline OverviewPipeline CI/CDFigura: Pipeline CI/CDQuality GatesGateFerramentaThresholdBloqueanteUnit TestsVitest / xUnit100% passSimCode CoverageIstanbul / Coverlet&gt;= 80%SimSASTSonarQube / Checkmarx0 Critical, 0 HighSimLintESLint / .NET Analyzers0 errorsSimBuildAzure PipelinesSuccessSim10.4 Estratégia de DeployAspetoEspecificaçãoEstratégiaRolling UpdateZero downtimeSimmaxSurge25%maxUnavailable0Réplicas mínimas2Health checksReadiness + Liveness probesRollbackAutomático via KubernetesAprovações por AmbienteAmbienteAprovaçãoAprovadoresDEVAutomática-QAAutomática-PRODManualTech Lead + PO10.5 Secrets ManagementAspetoEspecificaçãoFerramentaAzure Key VaultInjeçãoSecret Store CSI DriverAcessoManaged Identity por namespaceRotaçãoSuportada (CSI driver faz refresh)Secrets geridosConnection strings, API keys, certificadosInjeção de Secrets via CSI DriverFigura: Injeção de Secrets via CSI DriverPolítica de RotaçãoTipo de SecretFrequênciaResponsávelAPI Keys90 diasAutomáticoCertificados TLSAnualInfraDB Credentials180 diasDBA10.6 Container RegistryAspetoConfiguraçãoRegistryAzure Container Registry (ACR)AutenticaçãoManaged IdentityScanningMicrosoft Defender for ContainersRetenção90 dias para tags não-latestNamingacr.azurecr.io/homebanking/{component}:{version}Tagging StrategyTagUso{semver}Versão semântica (ex: 1.2.3){branch}-{sha}Feature branches (ex: develop-abc1234)latestÚltima versão de produção10.7 Disaster RecoveryAspetoConfiguraçãoTipoCluster réplica (standby passivo)RTO30 minutosRPO5 minutosFailoverManual (decisão de negócio)Nota: Canal web é stateless. Dados estão no backend existente com DR próprio. DR do canal web foca na disponibilidade da aplicação.

**Comment:**

Isto já se encontra implementado. Será reutilizar o que existe. Há coisas que descrevem corretamente o que está, outras nem por isso, outras nem tenho visibilidade de como estah. Teria de ser a equipa de infra a descrever. Pode não fazer sentido estar neste documento.

---

## Comment 52

**Location:** Paragraph 6426

**Author:** Jorge Gomes Costa (novobanco DSI Direção) | **Date:** 2026-01-16 19:19:00

**Commented text:**

> 11. Observabilidade &amp; Operações

**Comment:**

Marcar sessao para rever com equipa de infra. Penso que seria prudente perceber os requisitos concretos. Atenção que coisas que não são realmente usadas no dia a dia, a serem implementadas terao custos.

---

## Comment 53

**Location:** Paragraph 6655

**Author:** Jorge Gomes Costa (novobanco DSI Direção) | **Date:** 2026-01-16 19:20:00

**Commented text:**

> 11.4 Logging

**Comment:**

Podemos partilhar a estrutura dos logs

---

## Comment 54

**Location:** Paragraph 6833

**Author:** Jorge Gomes Costa (novobanco DSI Direção) | **Date:** 2026-01-16 19:22:00

**Commented text:**

> TokensNunca logar

**Comment:**

Sobre estes campos - nunca necessitam para diagnostico ou auditoria dos campos não mascarados? Ou seja, em vez de mascarar, cifrar

---

