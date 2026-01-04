# Questoes Pendentes - Consolidacao

> **Data de geracao:** 2025-12-23
> **Objetivo:** Compilar todas as questoes sem resposta para revisao

---

## Instrucoes de Uso

1. **Responder questoes:** Preencha a resposta abaixo de cada questao (linha "R.:")
2. **Questoes invalidas:** Mova para a secao "Questoes Descartadas" no final
3. **Novos detalhes:** Adicione na secao "Informacoes Adicionais" no final
4. **Devolva este documento** ao assistente para incorporacao nas definicoes

---

## SEC-01: Contexto e Visao Geral

### DEF-01-solution-scope.md

**Q-01-001:** Quais funcionalidades do App Mobile devem estar presentes no MVP?
R.:

**Q-01-002:** Quais funcionalidades ficam para fases posteriores (Fase 1, Fase 2)?
R.:

**Q-01-003:** Quais integracoes com sistemas externos sao obrigatorias no MVP?
R.:

**Q-01-004:** Qual o papel do Siebel na nova arquitetura?
R.:

**Q-01-005:** Qual a relacao com o Core Banking (BI Core Banking)?
R.:

**Q-01-006:** Quais "Sistemas Externos" (Financeiros, Seguradoras, Parceiros) sao prioritarios?
R.:

### DEF-01-c4-context-diagram.md

**Q-01-007:** Quais as principais interacoes entre o WebSite e cada sistema de dependencias?
R.:

**Q-01-008:** Qual o papel exato do Blob Storage (apenas cofre de chaves/tokens ou tambem documentos)?
R.:

**Q-01-009:** Quais sistemas externos sao criticos para o MVP vs opcionais?
R.:

**Q-01-010:** O Backoffice de Gestao interage diretamente com o WebSite ou sao independentes?
R.:

**Q-01-011:** ~~Qual a relacao entre Siebel e o WebSite (direta ou via Core Banking)?~~
R.: **DESCARTADA** - Questão repetida (ver Q-01-004 e Q-01-005)

**Q-01-012:** As "APIs Estaticas" sao consumidas pelo WebSite? Qual o conteudo?
R.:

**Q-01-013:** Detalhes de integracao com sistemas externos:

| Sistema | Protocolo | Descricao |
|---------|-----------|-----------|
| Seguros | R.: | R.: |
| BTP | R.: | R.: |
| MBWay | R.: | R.: |
| Visa | R.: | R.: |
| Firebase | R.: | R.: |
| Google Maps | R.: | R.: |

### DEF-01-stack-tecnologica.md

**Q-01-014:** Quais pacotes de componentes React serao utilizados?
R.:

---

## SEC-02: Requisitos

### DEF-02-requisitos-nao-funcionais.md

**Q-02-001:** Quantos utilizadores simultaneos sao esperados?
R.:

**Q-02-002:** Qual o volume de transacoes esperado (TPS)?
R.:

**Q-02-003:** Qual o tempo maximo de recuperacao em caso de falha (RTO)?
R.:

**Q-02-004:** Qual a perda maxima de dados aceitavel (RPO)?
R.:

**Q-02-005:** Existem requisitos especificos do Banco de Portugal?
R.:

**Q-02-006:** Quais browsers e dispositivos devem ser suportados?
R.:

**Q-02-007:** Quais os requisitos de acessibilidade (WCAG level)?
R.:

### DEF-02-regras-calculos-negocio.md

**Q-02-008:** Quais calculos existem para Objetivos?
R.:

**Q-02-009:** Quais simulacoes existem para produtos de reforma?
R.:

**Q-02-010:** Existem outras regras de calculo importantes?
R.:

---

## SEC-03: Principios Arquiteturais

### DEF-03-principios-arquiteturais.md

**Q-03-001:** Como garantir consistencia entre equipas no uso dos principios arquiteturais?
R.:

**Q-03-002:** CQRS deve ser adotado? Em que contextos?
R.:

**Q-03-003:** Event Sourcing deve ser adotado? Em que contextos?
R.:

**Q-03-004:** Domain-Driven Design deve ser aplicado? Em que nivel?
R.:

**Q-03-005:** Microservices vs Modular Monolith - qual a abordagem preferida?
R.:

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

R.:

**Q-07-002:** Qual o fluxo de recuperacao de acesso (password esquecida)?
R.:

**Q-07-003:** Qual o modelo RBAC (Autorizacao por perfil) a implementar?
R.:

**Q-07-004:** Quais as politicas de Password (complexidade, expiracao)?
R.:

**Q-07-005:** Qual o procedimento de revogacao de tokens?
R.:

**Q-07-006:** Faz sentido encriptar o user e pass no envio do SPA para o BFF?

> **Contexto:** O documento do outro analista levantou esta questao. Atualmente o campo `encrypt` na API AUT_004 pode ser "Y" ou "N".

R.:

---

## SEC-08: Seguranca e Conformidade

### DEF-08-seguranca-dados-sensiveis.md

**Q-08-001:** Quais outros dados sensiveis requerem tratamento especial (alem de cartoes e MBWay)?
R.:

**Q-08-002:** Quais algoritmos de encriptacao sao utilizados?
R.:

### DEF-08-conformidade-regulatoria.md

**Q-08-003:** Quais requisitos PCI-DSS aplicaveis (depende do scope de cartoes)?
R.:

**Q-08-004:** Existem requisitos especificos do Banco de Portugal?
R.:

**Q-08-005:** Como garantir conformidade continua?
R.:

**Q-08-006:** Quais servicos PSD2 serao expostos?

| Servico | Implementar? | Descricao |
|---------|--------------|-----------|
| AIS (Account Information) | R.: | R.: |
| PIS (Payment Initiation) | R.: | R.: |
| CBPII (Card-based Payment) | R.: | R.: |

---

## SEC-09: Integracoes

### DEF-09-integracoes.md

**Q-09-001:** Quais sao todas as APIs externas consumidas pela plataforma?
R.:

**Q-09-002:** Qual o modelo de autenticacao para cada API?
R.:

**Q-09-003:** Quais sao os SLAs esperados por integracao?
R.:

**Q-09-004:** Qual a estrategia de fallback para cada integracao critica?
R.:

**Q-09-005:** Quais APIs requerem configuracao de rate limiting?
R.:

**Q-09-006:** Qual a versao da API SIBS utilizada?
R.:

**Q-09-007:** Quais endpoints especificos da SIBS?
R.:

**Q-09-008:** Qual o modelo de certificados (eIDAS)?
R.:

**Q-09-009:** Configuracao da API Backoffice:

| Parametro | Valor |
|-----------|-------|
| Token_Endpoint | R.: |
| clientid | R.: |
| ClientScopes | R.: |
| authorizationpoint | R.: |

### DEF-09-regras-transferencias.md

**Q-09-010:** Quais APIs sao utilizadas para cada tipo de transferencia?

| Tipo | API |
|------|-----|
| Interna (0065) | R.: |
| Inter-bancaria nacional | R.: |
| SEPA | R.: |
| SWIFT/Internacional | R.: |

**Q-09-011:** Lista de paises SEPA?
R.:

---

## SEC-10: Infraestrutura e CI/CD

### DEF-10-ambientes-cicd.md

**Q-10-001:** Feature Flags - LaunchDarkly (SaaS) ou Unleash (self-hosted)?
R.:

---

## SEC-12: Performance e Resiliencia

### DEF-12-performance-resiliencia.md

**Q-12-001:** Quais os targets de performance?
R.:

**Q-12-002:** Qual a estrategia de caching?
R.:

**Q-12-003:** Como funciona o auto-scaling?
R.:

**Q-12-004:** Carga esperada por ambiente:

| Metrica | DEV | UAT | PROD |
|---------|-----|-----|------|
| Utilizadores simultaneos | R.: | R.: | R.: |
| Requests/segundo | R.: | R.: | R.: |
| Transacoes/hora | R.: | R.: | R.: |

---

## SEC-13: Estrategia de Testes

### DEF-13-estrategia-testes.md

**Q-13-001:** Qual a cobertura de testes esperada?
R.:

**Q-13-002:** Quais ferramentas de teste utilizar?
R.:

**Q-13-003:** Como gerir dados de teste?
R.:

**Q-13-004:** Qual o baseline de performance?
R.:

---

## SEC-14: Plano de Implementacao

### DEF-14-plano-implementacao.md

**Q-14-001:** Qual o roadmap de implementacao?
R.:

**Q-14-002:** Como coexistir com o sistema legado?
R.:

**Q-14-003:** Qual a estrategia de cutover?
R.:

**Q-14-004:** Como migrar dados?
R.:

---

# Questoes Descartadas

> Mova para esta secao as questoes que nao fazem sentido ou nao sao aplicaveis.
> Inclua uma breve justificativa.

| ID Questao | Justificativa |
|------------|---------------|
| Q-01-011 | Questão repetida - mesmo conteúdo de Q-01-004 e Q-01-005 |
| Q-09-006 | Não existe API SIBS - informação incorreta |
| Q-09-007 | Não existe API SIBS - informação incorreta |

---

# Informacoes Adicionais

> Adicione aqui novos detalhes, contexto ou informacoes que possam gerar novas questoes ou esclarecer as existentes.

### Novos Detalhes

_Escreva aqui..._

### Novas Questoes Identificadas

_Se durante a revisao surgirem novas questoes, adicione aqui:_

**Q-XX-XXX:** [Nova questao]
R.:

---

# Historico de Revisoes

| Data | Autor | Alteracoes |
|------|-------|------------|
| 2025-12-23 | Assistente | Documento criado com 54 questoes pendentes |
| 2025-12-23 | Assistente | Incorporadas respostas do analista: 15 questões respondidas, 3 descartadas |
