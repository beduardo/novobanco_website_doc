## Instrucoes de Uso

1. **Responder questoes:** Preencha a resposta abaixo de cada questao (linha "R.:")
2. **Questoes invalidas:** Mova para a secao "Questoes Descartadas" no final
3. **Novos detalhes:** Adicione na secao "Informacoes Adicionais" no final

---

## SEC-01: Contexto e Visao Geral

### DEF-01-solution-scope.md

**Q-01-001:** Quais funcionalidades do App Mobile devem estar presentes no MVP?
R.:A questionar - neste momento não temos o conceito de MVP definido, nem temos ainda definida a forma de passagem a produção, se vai ser tudo ou faseado.

**Q-01-002:** Quais funcionalidades ficam para fases posteriores (Fase 1, Fase 2)?
R.:A questionar - se houver definição de MVP

**Q-01-003:** Quais integracoes com sistemas externos sao obrigatorias no MVP?
R.:A questionar - se houver definição de MVP

**Q-01-004:** Qual o papel do Siebel na nova arquitetura?
R.:É o backend onde está toda a informação de negócio/cliente. Tem também regras de negócio e validações.

**Q-01-005:** Qual a relacao com o Core Banking (BI Core Banking)?
R.:Não há. A relação com o core banking é 100% via Siebel

**Q-01-006:** Quais "Sistemas Externos" (Financeiros, Seguradoras, Parceiros) sao prioritarios?
R.:A questionar - se houver definição de MVP, senão são todos prioritários

### DEF-01-c4-context-diagram.md

**Q-01-007:** Quais as principais interacoes entre o WebSite e cada sistema de dependencias?
R.:

**Q-01-008:** Qual o papel exato do Blob Storage (apenas cofre de chaves/tokens ou tambem documentos)?
R.:Se estamos a falar do SAS Storage é para chaves, mas não vai ser utilizado no site. Há Blob Storage para imagens e doc distribuidos por links presentes nas API.

**Q-01-009:** Quais sistemas externos sao criticos para o MVP vs opcionais?
R.:A questionar - se houver definição de MVP

**Q-01-010:** O Backoffice de Gestao interage diretamente com o WebSite ou sao independentes?
R.:O bakcoffice de gestão entrega conteúdos e regras por API ao Website e APP.

**Q-01-011:** Qual a relacao entre Siebel e o WebSite (direta ou via Core Banking)?
R.:pergunta está repetida

**Q-01-012:** As "APIs Estaticas" sao consumidas pelo WebSite? Qual o conteudo?
R.:São API que devem ser migradas para um dos sistemas a desenhar. Entregam listas de valores que servem para permitir selecção pelo utilizador

**Q-01-013:** Detalhes de integracao com sistemas externos:

| Sistema | Protocolo | Descricao |
|---------|-----------|-----------|
| Seguros | R.: API REST e HTTPS | R.: É um produto de consulta e subscrição|
| BTP 	| R.:API REST e HTTPS  | R.: É um produto de consulta e subscrição|
| MBWay | R.: Não vai ser usado no site| R.: |
| Visa | R.:  Não vai ser usado no site| R.: |
| Firebase | R.: API REST| R.: registo de estatisticas de acesso|
| Google Maps | R.: Biblioteca| R.: Fornece os mapas para consulta|

### DEF-01-stack-tecnologica.md

**Q-01-014:** Quais pacotes de componentes React serao utilizados?
R.:Não é suposto sermos nós a definir?

---

## SEC-02: Requisitos

### DEF-02-requisitos-nao-funcionais.md

**Q-02-001:** Quantos utilizadores simultaneos sao esperados?
R.:A questionar 

**Q-02-002:** Qual o volume de transacoes esperado (TPS)?
R.:

**Q-02-003:** Qual o tempo maximo de recuperacao em caso de falha (RTO)?
R.:A questionar - 

**Q-02-004:** Qual a perda maxima de dados aceitavel (RPO)?
R.:A questionar - 

**Q-02-005:** Existem requisitos especificos do Banco de Portugal?
R.:A questionar - 

**Q-02-006:** Quais browsers e dispositivos devem ser suportados?
R.: Todos os atuais (Questionar sobre browsers legados)

**Q-02-007:** Quais os requisitos de acessibilidade (WCAG level)?
R.:AA

---

## SEC-07: Autenticacao

### DEF-07-autenticacao-oauth.md

**Q-07-001:** [ALTA PRIORIDADE] Momento de Retorno do apiToken

> **Contexto:** Existe divergencia entre documentos sobre quando o `apiToken` e retornado.
>
> | Interpretacao | Descricao |
> |---------------|-----------|
> | A | apiToken retornado **antes** do OTP, OTP valida via API "secure" separada |
> | B | apiToken retornado **apos** validacao do OTP |

R.: A

**Q-07-002:** Qual o fluxo de recuperacao de acesso (password esquecida)?
R.:Vai ser igual à APP. É importante fazer parte do doc? 

**Q-07-003:** Qual o modelo RBAC (Autorizacao por perfil) a implementar?
R.:São geridas pelo Siebel. É importante fazer parte do doc?

**Q-07-004:** Quais as politicas de Password (complexidade, expiracao)?
R.:São geridas pelo Siebel. É importante fazer parte do doc?

**Q-07-005:** Qual o procedimento de revogacao de tokens?
R.:A questionar - 

---

## SEC-08: Seguranca e Conformidade

### DEF-08-seguranca-dados-sensiveis.md

**Q-08-001:** Quais outros dados sensiveis requerem tratamento especial (alem de cartoes e MBWay)?
R.:Telemóvel de segurança vem escondido

**Q-08-002:** Quais algoritmos de encriptacao sao utilizados?
R.:A questionar - 

### DEF-08-conformidade-regulatoria.md

**Q-08-003:** Quais requisitos PCI-DSS aplicaveis (depende do scope de cartoes)?
R.: A questionar - 

**Q-08-004:** Existem requisitos especificos do Banco de Portugal?
R.:A questionar - 

**Q-08-005:** Como garantir conformidade continua?
R.:A questionar - 

**Q-08-006:** Quais servicos PSD2 serao expostos?
R.: Não percebi a pergunta. Não está no nosso âmbito expor serviços PSD2. O que existe está implementado pelo banco

| Servico | Implementar? | Descricao |
|---------|--------------|-----------|
| AIS (Account Information) | R.: | R.: |
| PIS (Payment Initiation) | R.: | R.: |
| CBPII (Card-based Payment) | R.: | R.: |

---

## SEC-09: Integracoes

### DEF-09-integracoes.md

**Q-09-001:** Quais sao todas as APIs externas consumidas pela plataforma?
R.: São mais de 400. Pretendes que se descrevam todas?

**Q-09-002:** Qual o modelo de autenticacao para cada API?
R.:Há 3 modelos - anónimo para as listas ; Oauth 1.1 já descrito Oauth2 para as API de backoffice de gestão

**Q-09-003:** Quais sao os SLAs esperados por integracao?
R.:A questionar - 

**Q-09-004:** Qual a estrategia de fallback para cada integracao critica?
R.:A questionar - 

**Q-09-005:** Quais APIs requerem configuracao de rate limiting?
R.:A questionar - 

**Q-09-006:** Qual a versao da API SIBS utilizada?
R.:Não há API SIBS

**Q-09-007:** Quais endpoints especificos da SIBS?
R.:Não há

**Q-09-008:** Qual o modelo de certificados (eIDAS)?
R.:A questionar - 

### DEF-09-regras-transferencias.md

**Q-09-010:** Quais APIs sao utilizadas para cada tipo de transferencia?
R.:(Somente Siebel, variando endpoint e dados). Temos de ver para que vai servir a resposta. Não estamos a produzir documento de especificação de funcionalidades...

| Tipo | API |
|------|-----|
| Interna (0065) | R.: |
| Inter-bancaria nacional | R.: |
| SEPA | R.: |
| SWIFT/Internacional | R.: |

**Q-09-011:** Lista de paises SEPA?
R.: (Siebel) A questionar - mas temos de ver para que vai servir a resposta, antes de questionar

---

## SEC-10: Infraestrutura e CI/CD

### DEF-10-ambientes-cicd.md

**Q-10-001:** Feature Flags - LaunchDarkly (SaaS) ou Unleash (self-hosted)?
R.:A questionar (Hoje isto é implementado pelo Backoffice de Gestão - CMS Content Management Services)

---

## SEC-12: Performance e Resiliencia

### DEF-12-performance-resiliencia.md

**Q-12-001:** Quais os targets de performance?
R.:A questionar

**Q-12-002:** Qual a estrategia de caching?
R.: REDIS

**Q-12-003:** Como funciona o auto-scaling?
R.:A questionar

**Q-12-004:** Carga esperada por ambiente:
R.:A questionar

| Metrica | DEV | UAT | PROD |
|---------|-----|-----|------|
| Utilizadores simultaneos | R.: | R.: | R.: |
| Requests/segundo | R.: | R.: | R.: |
| Transacoes/hora | R.: | R.: | R.: |

---

## SEC-13: Estrategia de Testes

### DEF-13-estrategia-testes.md

**Q-13-001:** Qual a cobertura de testes esperada?
R.:A questionar

**Q-13-002:** Quais ferramentas de teste utilizar?
R.:A questionar

**Q-13-003:** Como gerir dados de teste?
R.:A questionar

**Q-13-004:** Qual o baseline de performance?
R.:A questionar

---

## SEC-14: Plano de Implementacao

### DEF-14-plano-implementacao.md

**Q-14-001:** Qual o roadmap de implementacao?
R.:A questionar

**Q-14-002:** Como coexistir com o sistema legado?
R.:A questionar

**Q-14-003:** Qual a estrategia de cutover?
R.:A questionar

**Q-14-004:** Como migrar dados?
R.: N/A

---

# Questoes Descartadas

> Mova :para esta secao as questoes que nao fazem sentido ou nao sao aplicaveis.
> Inclua uma breve justificativa.

| ID Questao | Justificativa |
|------------|---------------|
| | |

---

# Informacoes Adicionais

> Adicione aqui novos detalhes, contexto ou informacoes que possam gerar novas questoes ou esclarecer as existentes.

### Novos Detalhes

_Escreva aqui..._

### Novas Questoes Identificadas

_Se durante a revisao surgirem novas questoes, adicione aqui:_

**Q-XX-XXX:** [Nova questao]
R.:

