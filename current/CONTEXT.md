---
id: CONTEXT
aliases: []
tags:
  - nextreality-novobanco-website
approved: true
created: 2026-01-01
hubs:
  - "[[nextreality]]"
para-code: R
reviewed: true
---
# CONTEXT
## Main Objectives
Especificações arquiteturais de desenvolvimento de Página HomeBanking para banco digital com parte das features equivalentes da aplicação mobile nativa.

## General Information
O documento deve ser um HLD com informações para o desenvolvimento do projeto, definindo todas as tecnologias e estruturas necessárias para isso. Ele deve ser completo para que uma equipa consiga preparar um plano de desenvolvimnento envolvendo desde o Assessment inicial para a definição completa das histórias de usuário até a entrega do software, passando por diagramas que apresentam como tudo será interligado, qual a arquitetura da aplicação, como deve ser entrege no ambiente (deployed) e como deve ser monitorada.

### Estes são outros pontos relevantes ao documento:

    - Definição da metodologia a utilizar na criação dos canais Best, no âmbito da atualização tecnológica
    - Identificação de perfis e características técnicas, nomeadamente:
        - Programação React
        - Programação nativa (iOS e Android)
        - Integração React no nativo
        - Integração do Gateway
        - Ligação com APIs Banco Best
        - Criação de business layer CMS (.NET, etc.)
        - Modelos de segurança
        - Tratamento de erros, diagnóstico, logs e monitorização
        - Requisitos de resiliência, isolamento e escalabilidade
        - Performance e utilização de cache
        - Outros aspetos técnicos relevantes
    - Definição do modelo de arquitetura global dos canais e aplicações conexas (CMS, backoffice, etc.)
    - Identificação de componentes de infraestrutura em falta no desenho atual (ex.: cache, GitHub, DevOps, Azure)
    - Modelo de trabalho entre equipas, incluindo ambientes de desenvolvimento novobanco e ligação com equipas externas15k

## Informações adicionais:
- A aplicação se utilizará de infraestrutura e serviços criados para a aplicação mobile nativa já existente.
- O cliente já possui um APP Mobile com features equivalente que devem ser replicadas.
- Deve definir os requisitos funcionais e não funcionais, atendendo os padrões internacionais.
- Um documento do Word deve ser gerado ao fim do trabalho. As seções precisam ser escritas de forma a facilitar que o conteúdo seja copiado para o edito Word.
- Devemos ter também um documento auxiliar com uma lista de perguntas pendentes para resposta. Este documento será utilizado em reuniões com o cliente para agilizar a captura de enformações e deve ser atualizado com frequência. Estas questões devem ser baseadas nas questões existentes nos documentos de definição.


## List of sections

| Section | Title | Description |
|---------|-------|-------------|
| 1 | Sumário Executivo | Descrever os objetivos deste documento e visão geral da arquitetura. |
| 2 | Contexto de Negócio & Requisitos | Descreve o contexto da solução e seus requisitos, informando as partes interessadas, requisitos funcionais e não funcionais e suas restrições |
| 3 | Visão Geral da Solução | Princípios de Arquitetura, Diagrama Conceptual, Casos de Uso |
| 4 | Experiência do Utilizador & Arquitetura Frontend | Arquitetura de Informação, Diretrizes UI/UX, Jornadas do Utilizador, Multi-idioma, PWA & Offline, Stack Frontend, Design System, Responsividade, Segurança, Performance Frontend |
| 5 | Arquitetura Backend & Serviços | Decomposição de Serviços, Arquitetura API, Comunicação, Modelo de Domínio, Rate Limiting, Resiliência, Versionamento API, Especificação API, Dependências, Padrões de Design |
| 6 | Arquitetura de Dados | Modelo de Dados, Armazenamento, Encriptação, Retenção, Backup & Restore, RGPD - Data Subject Rights, Classificação de Dados, Particionamento, Migração de Dados, Anonimização/Pseudonimização |
| 7 | Autenticação & Autorização | Autenticação, Autorização, Estratégia de Tokens, Gestão de Sessões, Políticas de Password, MFA Obrigatório, Single Sign-On (SSO), Fluxos de Autenticação, Revogação, Anti-automation |
| 8 | Segurança & Conformidade | Modelo de Ameaças, Controlos de Segurança, OWASP Top 10, Conformidade PSD2, Conformidade RGPD, PCI-DSS, Banco de Portugal, Registo de Auditoria, Resposta a Incidentes, Gestão de Vulnerabilidades, Segregação de Ambientes |
| 9 | Integração & Interfaces Externas | Integração Core Banking, Terceiros - KYC/AML, Terceiros - Notificações, Terceiros - Cartões, Open Banking PSD2, Gestão de Consentimentos, Message Broker, Tratamento de Erros, SLAs de Integração, Catálogo de Integrações, API Management |
| 10 | Arquitetura Operacional | Infraestrutura, Ambientes, Segregação, CI/CD Pipelines, Estratégia de Deploy, Infraestrutura como Código, Secrets Management, Container Registry, Disaster Recovery, Backup Strategy, Runbooks |
| 11 | Observabilidade & Operações | Stack de Observabilidade, Golden Signals, Métricas de Aplicação, Métricas de Negócio, Distributed Tracing, Logging Centralizado, SLIs (Service Level Indicators), SLOs (Service Level Objectives), SLAs (Service Level Agreements), Alertas, Dashboards Operacionais, Runbooks |
| 12 | Desempenho & Fiabilidade | Objetivos de Carga, Targets de Performance, Caching Strategy, Otimização Frontend, Otimização Backend, Auto-scaling, Capacity Planning, Failover, Resiliência, Load Testing |
| 13 | Estratégia de Testes | Testes Unitários, Testes de Integração, Testes de Contrato, Testes E2E, Testes de Performance, Testes de Segurança, Testes de Acessibilidade, Test Data Management, Testes de Regressão, Testes de Aceitação, Matriz de Responsabilidades |
| 14 | Plano de Migração & Implementação | Roadmap de Implementação, Estratégia de Cutover, Coexistência com Legado, Migração de Dados, Critérios Go/No-Go, Procedimentos de Rollback, Plano de Comunicação, Formação, Pilot/Beta Testing, Hypercare Period |
| 15 | Governação & Roadmap | Modelo de Governação, Gestão de Decisões, Roadmap de Produto, Gestão de Dívida Técnica, Processo de Gestão de Mudança, KPIs de Sucesso, Continuous Improvement |


