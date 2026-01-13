---
id: DEF-01-objetivos-documento
aliases:
  - Objetivos do Documento
tags:
  - nextreality-novobanco-website-definitions
  - definitions
  - objectives
approved: true
created: 2026-01-01
hubs:
  - "[[nextreality]]"
para-code: R
reviewed: true
status: completed
---

# DEF-01: Objetivos do Documento

> **Secao relacionada:** [1 - Sumario Executivo](../sections/SEC-01-sumario-executivo.md)

## Contexto

Este documento de arquitetura servira como referencia tecnica para o desenvolvimento da plataforma HomeBanking web do Novo Banco. E necessario definir claramente seus objetivos, escopo e publico-alvo para garantir que o documento atenda as necessidades de todos os stakeholders.

## Perguntas a Responder

1. Qual e o objetivo principal deste documento de arquitetura? 
    Definir de forma completa o cerne do projeto definindo tecnologias, arquitetura de infraestrutura e de software, processos de segurança e desenvolvimento. O presente documento visa criar um workbook de regito do levantamento das componentes críticas da aplicação e sua declinação baseada em tecnologias 100% WEB.

2. Quem sao os leitores primarios (developers, architects, gestores, auditores)?
    Arquitetos de Software, Desenvolvedores e Gerentes de Projeto

3. Que decisoes este documento deve suportar?
    Segurança, Casos de Uso e Compliance

4. Qual nivel de detalhe tecnico e esperado?
    HLD (High Level Design) para evitar soluções dúbias. Uma das fases da execução é a produção de documentos LLD (Low Level Design) para aprofundamento da solução, então o HLD não precisará de todas as informações para a execução da implementação, mas precisará das informações principais como a definição da arquitetura, tecnologias envolvidas, principais fluxos e descrição dos passos principais do projeto.

5. Este documento deve servir como baseline para auditoria/compliance?
    Sim.

6. Quais funcionalidades da app mobile estao in-scope para o HomeBanking web?
   Registo, Login, Recuperação de Acessos, Home, Área Pessoal, Património, Ordens Pendentes, Histórico de Operações, Outros Bancos, Dashboard, Carteiras, Saldos e Movimentos, Confirmação de Operações, Comprovativos e Extratos, Eventos Corporativos, Seguros de proteção, Área do Viajante, Bea, Warrants, Áções, ETF, Fundos, Obrigações, Caregamentos, MBWay (Somente componentes não SDK), Transferências, Pagamentos, Wishlist, Índices, Notícias eternas, Temas investimento, Depósito a prazo, Leilões, Ofertas públicas, Unit linked, Robot Advisor, BTP
7. Quais funcionalidades estao explicitamente out-of-scope?
    MBWay

8. Existe um roadmap de fases de implementacao?
    Não. Este deve ser um dos entregáveis do documento.

## Decisoes

### Objetivo Principal do Documento
- **Decisao:** Workbook de arquitetura HLD (High Level Design) para definicao completa do projeto HomeBanking Web, cobrindo tecnologias, arquitetura de infraestrutura e software, processos de seguranca e desenvolvimento.
- **Justificacao:** Necessidade de documentar as componentes criticas da aplicacao e sua declinacao em tecnologias 100% WEB, servindo como baseline para auditoria e compliance.
- **Alternativas consideradas:** LLD desde o inicio (descartado por complexidade inicial)

### Publico-Alvo
- **Decisao:** Arquitetos de Software, Desenvolvedores e Gerentes de Projeto
- **Justificacao:** Perfis tecnicos responsaveis pela implementacao e gestao do projeto
- **Alternativas consideradas:** Incluir auditores e reguladores (podem consultar, mas nao sao publico primario)

### Escopo Funcional (In-Scope)
- **Decisao:** 35 funcionalidades principais da app mobile serao replicadas no HomeBanking Web:
  - **Autenticacao:** Registo, Login, Recuperacao de Acessos
  - **Areas Principais:** Home, Area Pessoal, Dashboard
  - **Patrimonio:** Patrimonio, Carteiras, Saldos e Movimentos
  - **Operacoes:** Ordens Pendentes, Historico de Operacoes, Confirmacao de Operacoes
  - **Documentos:** Comprovativos e Extratos
  - **Investimentos:** Warrants, Acoes, ETF, Fundos, Obrigacoes, Indices, Temas Investimento, Deposito a Prazo, Leiloes, Ofertas Publicas, Unit Linked, Robot Advisor, BTP
  - **Pagamentos:** Transferencias, Pagamentos, Carregamentos, MBWay (apenas componentes nao-SDK)
  - **Outros:** Outros Bancos, Eventos Corporativos, Seguros de Protecao, Area do Viajante, Bea, Wishlist, Noticias Externas
- **Justificacao:** Paridade funcional com app mobile para oferecer experiencia consistente aos clientes
- **Alternativas consideradas:** MVP reduzido (descartado - todas as funcionalidades fazem parte do MVP)

### Exclusoes de Escopo (Out-of-Scope)
- **Decisao:** MBWay SDK (componentes nativos do SDK)
- **Justificacao:** SDK MBWay e especifico para aplicacoes mobile nativas e nao compativel com ambiente web
- **Alternativas consideradas:** N/A

### Nivel de Detalhe Tecnico
- **Decisao:** HLD (High Level Design)
- **Justificacao:** Evitar solucoes dubias mantendo flexibilidade para detalhamento posterior. Documentos LLD serao produzidos em fases subsequentes para aprofundamento da solucao.
- **Alternativas consideradas:** LLD completo desde o inicio (descartado por ser prematuro)

## Restricoes Conhecidas

- Reutilizacao da infraestrutura e servicos da app mobile nativa existente
- Conformidade com regulamentacoes bancarias portuguesas

## Referencias

- [CONTEXT.md](../CONTEXT.md) - Contexto geral do projeto
- Documentacao da app mobile existente (a fornecer)
