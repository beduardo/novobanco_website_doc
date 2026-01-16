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

> **Secção relacionada:** [1 - Sumário Executivo](../sections/SEC-01-sumario-executivo.md)

## Contexto

Este documento de arquitetura servirá como referência técnica para o desenvolvimento da plataforma HomeBanking web do Novo Banco. É necessário definir claramente os seus objetivos, escopo e público-alvo para garantir que o documento atenda às necessidades de todos os stakeholders.

## Perguntas a Responder

1. Qual é o objetivo principal deste documento de arquitetura?
    Definir de forma completa o cerne do projeto definindo tecnologias, arquitetura de infraestrutura e de software, processos de segurança e desenvolvimento. O presente documento visa criar um workbook de registo do levantamento das componentes críticas da aplicação e sua declinação baseada em tecnologias 100% WEB.

2. Quem são os leitores primários (developers, architects, gestores, auditores)?
    Arquitetos de Software, Desenvolvedores e Gestores de Projeto

3. Que decisões este documento deve suportar?
    Segurança, Casos de Uso e Compliance

4. Qual nível de detalhe técnico é esperado?
    HLD (High Level Design) para evitar soluções dúbias. Uma das fases da execução é a produção de documentos LLD (Low Level Design) para aprofundamento da solução, então o HLD não precisará de todas as informações para a execução da implementação, mas precisará das informações principais como a definição da arquitetura, tecnologias envolvidas, principais fluxos e descrição dos passos principais do projeto.

5. Este documento deve servir como baseline para auditoria/compliance?
    Sim.

6. Quais funcionalidades da app mobile estão in-scope para o HomeBanking web?
   Registo, Login, Recuperação de Acessos, Home, Área Pessoal, Património, Ordens Pendentes, Histórico de Operações, Outros Bancos, Dashboard, Carteiras, Saldos e Movimentos, Confirmação de Operações, Comprovativos e Extratos, Eventos Corporativos, Seguros de proteção, Área do Viajante, Bea, Warrants, Ações, ETF, Fundos, Obrigações, Carregamentos, MBWay (Somente componentes não SDK), Transferências, Pagamentos, Wishlist, Índices, Notícias externas, Temas investimento, Depósito a prazo, Leilões, Ofertas públicas, Unit linked, Robot Advisor, BTP
7. Quais funcionalidades estão explicitamente out-of-scope?
    MBWay

8. Existe um roadmap de fases de implementação?
    Não. Este deve ser um dos entregáveis do documento.

## Decisões

### Objetivo Principal do Documento
- **Decisão:** Workbook de arquitetura HLD (High Level Design) para definição completa do projeto HomeBanking Web, cobrindo tecnologias, arquitetura de infraestrutura e software, processos de segurança e desenvolvimento.
- **Justificação:** Necessidade de documentar as componentes críticas da aplicação e sua declinação em tecnologias 100% WEB, servindo como baseline para auditoria e compliance.
- **Alternativas consideradas:** LLD desde o início (descartado por complexidade inicial)

### Público-Alvo
- **Decisão:** Arquitetos de Software, Desenvolvedores e Gestores de Projeto
- **Justificação:** Perfis técnicos responsáveis pela implementação e gestão do projeto
- **Alternativas consideradas:** Incluir auditores e reguladores (podem consultar, mas não são público primário)

### Escopo Funcional (In-Scope)
- **Decisão:** 35 funcionalidades principais da app mobile serão replicadas no HomeBanking Web:
  - **Autenticação:** Registo, Login, Recuperação de Acessos
  - **Áreas Principais:** Home, Área Pessoal, Dashboard
  - **Património:** Património, Carteiras, Saldos e Movimentos
  - **Operações:** Ordens Pendentes, Histórico de Operações, Confirmação de Operações
  - **Documentos:** Comprovativos e Extratos
  - **Investimentos:** Warrants, Ações, ETF, Fundos, Obrigações, Índices, Temas Investimento, Depósito a Prazo, Leilões, Ofertas Públicas, Unit Linked, Robot Advisor, BTP
  - **Pagamentos:** Transferências, Pagamentos, Carregamentos, MBWay (apenas componentes não-SDK)
  - **Outros:** Outros Bancos, Eventos Corporativos, Seguros de Proteção, Área do Viajante, Bea, Wishlist, Notícias Externas
- **Justificação:** Paridade funcional com app mobile para oferecer experiência consistente aos clientes
- **Alternativas consideradas:** MVP reduzido (descartado - todas as funcionalidades fazem parte do MVP)

### Exclusões de Escopo (Out-of-Scope)
- **Decisão:** MBWay SDK (componentes nativos do SDK)
- **Justificação:** SDK MBWay é específico para aplicações mobile nativas e não compatível com ambiente web
- **Alternativas consideradas:** N/A

### Nível de Detalhe Técnico
- **Decisão:** HLD (High Level Design)
- **Justificação:** Evitar soluções dúbias mantendo flexibilidade para detalhamento posterior. Documentos LLD serão produzidos em fases subsequentes para aprofundamento da solução.
- **Alternativas consideradas:** LLD completo desde o início (descartado por ser prematuro)

## Restrições Conhecidas

- Reutilização da infraestrutura e serviços da app mobile nativa existente
- Conformidade com regulamentações bancárias portuguesas

## Referências

- [CONTEXT.md](../CONTEXT.md) - Contexto geral do projeto
- Documentação da app mobile existente (a fornecer)
