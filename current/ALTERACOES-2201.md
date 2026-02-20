**SEC-01 - Sumário Executivo**

- Removido diagrama de arquitetura local, substituído por referência ao diagrama central na secção 3.2
- Adicionada decisão arquitetural DEC-011 (diagrama de arquitetura único)
- Actualizada descrição dos princípios fundamentais para incluir padrão BFF

---
**SEC-02 - Contexto de Negócio e Requisitos**

- Clarificações no contexto de negócio e requisitos funcionais

---
**SEC-03 - Visão Geral da Solução**

- Criado diagrama de arquitetura de referência único e consolidado
- Adicionados novos componentes ao diagrama: F5, Redis Cluster, Microservices, ApiPsd2, ApiBBest
- Documentados protocolos de comunicação (Omni, OAuth + SHA256, OAuth 1.1 HMAC)
- Esclarecimento sobre papel do API Gateway IBM (apenas routing para Siebel)
- Adicionada nota sobre cenário secundário "Web na App" (WebView)
- Adicionados diagramas de sequência para fluxos principais
- Actualizada tabela de componentes com tecnologias definidas (React, .NET 8)
- Confirmado OpenShift como plataforma de deployment

---
**SEC-04 - Experiência de Utilizador e Frontend**

- Detalhamento da experiência de utilizador e componentes frontend
- Clarificações sobre responsividade e acessibilidade
- Removido diagrama de fluxo de decisão de biblioteca de componentes (secção 4.7.3)

---
**SEC-05 - Arquitetura de Backend e Serviços**

- Simplificação e alinhamento com diagrama de arquitetura central
- Ajustes na descrição da camada BFF
- Confirmado OpenShift como plataforma de deployment
- Clarificações sobre integração com sistemas existentes
- Removido diagrama de fluxo de autenticação

---
**SEC-06 - Arquitetura de Dados**

- Refinamentos na arquitectura de dados
- Ajustes na documentação de modelos e persistência
- Corrigido diagrama de fluxo de dados: adicionado componente Siebel entre API Gateway e bases de dados do Core Banking

---
**SEC-07 - Autenticação e Autorização**

- Detalhes adicionados aos Diagramas de fluxo de autenticação
- Documentados códigos de operação da ApiPsd2 (AUT_004, AUT_001, DEV_005.2)
- Adicionada secção sobre SCA Condicional (flag needStrongAuthentication)
- Detalhamento do fluxo de gestão de sessão com Redis
- Adicionada nota sobre segurança na transmissão de credenciais em ambiente web
- Melhorias gerais na documentação de fluxos de autenticação
- Reformulado diagrama do fluxo QR Code: adicionado mecanismo de polling, estados da sessão (PENDING, AUTHORIZED, EXPIRED), e endpoints detalhados
- Adicionada tabela de endpoints do fluxo QR Code: `/auth/qr-code/generate`, `/auth/qr-code/status/{sessionId}`, `/auth/qr-code/authorize`, `/auth/qr-code/link`
- Reformulado diagrama do fluxo Fallback: introduzido "Auth Service (MicroService)" como intermediário entre BFF e ApiPsd2
- Removido método "App Push" do fallback - segundo fator fallback é agora apenas SMS OTP

---
**SEC-08 - Segurança e Conformidade**

- Adicionada nova subsecção 8.3.6 "Considerações de Segurança Web vs Mobile"
- Documentados vetores de ataque específicos do ambiente web (XSS, CSRF, Man-in-the-Browser, Session Hijacking)
- Definidas estratégias de mitigação para armazenamento de dados sensíveis
- Proibição explícita de CDN - todos os recursos devem ser servidos localmente
- Adicionada proibição de dangerouslySetInnerHTML nas regras de lint/SAST
- Identificadas pendências de revisão de segurança (credenciais no login, PIN, teclado virtual, certificate pinning)

---
**SEC-09 - Integração e Interfaces Externas**

- Simplificação e alinhamento com diagrama de arquitetura central
- Expansão dos detalhes de integrações com sistemas externos
- Adicionados diagramas de sequência para integrações
- Actualizada documentação de protocolos de comunicação

---
**SEC-10 - Arquitetura Operacional**

- Definido OpenShift como plataforma de orquestração de contentores principal
- Simplificada e consolidada a secção de Arquitetura Operacional
- Removidas referências a alternativas de deployment
- Pequenos ajustes textuais

---
**SEC-11 - Observabilidade e Operações**

- Adicionadas clarificações sobre observabilidade
- Complementos sobre monitorização e logging

---
**SEC-12 - Desempenho e Fiabilidade**

- Complementos sobre desempenho e fiabilidade
- Clarificações sobre métricas e SLAs
