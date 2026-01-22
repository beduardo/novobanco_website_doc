---
id: DEF-09-integracao-interfaces
aliases:
  - Integração e Interfaces Externas
tags:
  - nextreality-novobanco-website-definitions
  - definitions
  - integration
  - external-interfaces
  - core-banking
approved: true
created: 2026-01-04
hubs:
  - "[[nextreality]]"
para-code: R
reviewed: true
status: in-progress
---

# DEF-09: Integração & Interfaces Externas

> **Secção relacionada:** [9 - Integração & Interfaces Externas](../sections/SEC-09-integracao-interfaces-externas.md)

## Contexto

Definir as integrações do HomeBanking Web com sistemas internos e externos. O canal web reutiliza a infraestrutura da app mobile, portanto muitas integrações já existem. Este documento foca nas especificidades do canal web e decisões de integração.

## Catálogo de Dependências Externas

| Sistema | Tipo | Proprietário | Criticidade | Status |
|---------|------|--------------|-------------|--------|
| **ApiPsd2** | Autenticação PSD2 | NovoBanco | Alta | Existente |
| **ApiBBest** | APIs Bancárias | NovoBanco | Alta | Existente |
| **Microservices** | Lógica de Negócio | NovoBanco | Alta | A desenvolver |
| Core Banking APIs | Integração | NovoBanco | Alta | Existente |
| App Mobile Nativa | Referência | NovoBanco | Média | Existente |
| Azure Infrastructure | Plataforma | NovoBanco | Alta | Existente |
| Gateway de Pagamentos | Integração | [A DEFINIR] | Alta | A validar |
| KYC/AML Provider | Integração | [A DEFINIR] | Alta | A validar |
| SMS Gateway | Integração | [A DEFINIR] | Alta | A definir no assessment |
| Push Notifications Service | Integração | [A DEFINIR] | Média | A definir no assessment |
| Document Management System | Integração | [A DEFINIR] | Média | A validar |
| HSM (Hardware Security Module) | Segurança | [A DEFINIR] | Alta | A validar |
| Identity Provider (SSO) | Autenticação | [A DEFINIR] | Média | A validar |
| Email Service Provider | Notificações | [A DEFINIR] | Média | A definir no assessment |

> **Nota:** Sistemas marcados como "Existente" já estão integrados na app mobile e serão reutilizados.

## Perguntas a Responder

### Integração Core Banking

1. Quais serviços do Core Banking serão consumidos pelo canal web?
    Não há acesso direto. O BFF irá acessar uma api chamada Backend API (Um Facade geral) que se encarregará de acionar os backends devidos conforme chamadas.

2. O canal web utiliza as mesmas APIs que a app mobile ou há APIs específicas?
    As mesmas

3. Existe documentação das APIs do Core Banking disponível?
   não

4. Qual o protocolo de comunicação com o Core Banking (REST, SOAP, outro)?
   Entre BFF e BackendAPI será REST

5. Há transformação de dados necessária entre Core Banking e canal web?
   Sim. Isso estará a cargo do BFF

### Terceiros - KYC/AML

6. Qual provider de KYC/AML é utilizado?
   Isso já está implementado no backend. Não há requisitos para isto na aplicação.

7. O canal web terá fluxos de onboarding que requerem KYC?
   Necessita aprofundamento

8. Há verificações AML em tempo real para transações?
   Necessita aprofundamento

### Terceiros - Notificações

9. Qual gateway de SMS é utilizado?
   Será definido no assessment inicial do projeto.

10. Qual serviço de Push Notifications é utilizado?
   Será definido no assessment inicial do projeto.

11. Há serviço de email transacional?
   Será definido no assessment inicial do projeto.

12. O canal web gera notificações ou apenas as recebe?
    Gera e Recebe.

### Terceiros - Cartões

13. Qual provider de cartões é utilizado (emissão, processamento)?
    Necessita aprofundamento

14. O canal web permitirá operações de cartões (bloqueio, ativação, limites)?
    Sim

15. Há integração com 3D Secure para pagamentos online?
    _Pending_

### Open Banking PSD2

16. O banco expõe APIs de Open Banking (AISP, PISP)?
    Necessita aprofundamento

17. O canal web consumirá APIs de Open Banking de outros bancos?
    Necessita aprofundamento

18. Existe plataforma de gestão de consentimentos?
    Necessita aprofundamento

19. Qual o modelo de autorização para Open Banking (OAuth 2.0, OIDC)?
    Necessita aprofundamento

### Message Broker

20. Qual tecnologia de Message Broker é utilizada (RabbitMQ, Kafka, Azure Service Bus)?
    Necessita aprofundamento

21. Quais eventos são publicados/consumidos pelo canal web?
    Necessita aprofundamento

22. Há requisitos de ordenação ou exactly-once delivery?
    Necessita aprofundamento

23. Qual a estratégia de dead-letter para mensagens falhadas?
    Necessita aprofundamento

### Tratamento de Erros

> **Nota:** Padrões de resiliência (retry, circuit breaker) consolidados em [DEF-05-padroes-resiliencia.md](DEF-05-padroes-resiliencia.md)

24. Como são comunicados erros de integração ao utilizador?
    Mensagem de erro amigável + registo de log para troubleshooting

25. Quais integrações têm fallback definido?
    Autenticação (fallback OTP). Ver DEF-05-padroes-resiliencia.

### SLAs de Integração (Simplificado)

26. Quais são os SLAs de disponibilidade dos sistemas integrados?
    Necessita aprofundamento. Backend API deve ter SLA >= 99.9%

27. Há janelas de manutenção programadas que afetam integrações?
    Necessita aprofundamento

### API Management

28. Qual API Gateway é utilizado?
    IBM API Gateway (para acesso ao Siebel). O BFF acede directamente a ApiPsd2, ApiBBest e Microservices sem passar pelo Gateway.

29. Como é feito o rate limiting por integração?
    Necessita aprofundamento. Gerido pelo Gateway (IBM), não pelo BFF.

### Catálogo de Integrações (Simplificado)

30. Existe catálogo de APIs/serviços documentado?
    Necessita aprofundamento

31. Há ambiente de sandbox para testes de integração?
    Necessita aprofundamento

### HSM (Hardware Security Module)

32. Qual HSM é utilizado pelo banco (Thales, AWS CloudHSM, Azure Dedicated HSM)?
    Necessita aprofundamento

33. Quais operações do canal web requerem HSM (assinatura digital, encriptação de dados sensíveis)?
    Necessita aprofundamento

34. Existe integração HSM já disponível via Backend API?
    Necessita aprofundamento

35. O HSM é utilizado para armazenamento de chaves de encriptação de tokens?
    Necessita aprofundamento

### Identity Provider / SSO

36. Existe Identity Provider corporativo (Azure AD, Okta, outro)?
    Necessita aprofundamento

37. Há requisitos de SSO com outros sistemas internos do banco?
    Necessita aprofundamento

38. O SSO é aplicável ao canal web ou apenas a sistemas internos/backoffice?
    Necessita aprofundamento

39. O Identity Provider é o mesmo utilizado pela app mobile?
    Necessita aprofundamento

### Document Management System

40. Existe DMS centralizado para extratos e comprovativos?
    Necessita aprofundamento

41. Os documentos são gerados em tempo real ou pré-gerados?
    Necessita aprofundamento

42. Qual o formato de documentos suportado (PDF, outro)?
    Necessita aprofundamento

43. Há requisitos de assinatura digital em documentos?
    Necessita aprofundamento

### Notificações - Detalhamento

44. SMS Gateway, Push e Email serão os mesmos serviços da app mobile?
    Necessita aprofundamento

45. Há requisitos de templates de notificação específicos para o canal web?
    Necessita aprofundamento

46. Existe serviço de preferências de notificação do utilizador?
    Necessita aprofundamento

47. Há requisitos de notificações em tempo real (WebSocket) para o canal web?
    Necessita aprofundamento

## Catálogo de APIs - Backends do BFF

> **Fonte:** Diagramas de sequência do cliente

### APIs de Autenticação (ApiPsd2)

| Código | API | Descrição | Criticidade |
|--------|-----|-----------|-------------|
| AUT_004 | Authentication_checkLogin | Validação de credenciais e início de sessão | Alta |
| AUT_001 | ReenviaOTP | Solicita envio de OTP | Alta |
| DEV_005.2 | RegistarDispositivoSecure | Valida OTP e regista dispositivo | Alta |

### APIs de Dados do Cliente (ApiBBest)

| API | Descrição | Dados Retornados |
|-----|-----------|------------------|
| Client_getClientInformation | Informação do cliente | Nome, dados pessoais |
| Client_getClientContact | Contactos do cliente | Email, telefone, morada |
| Devices_getDevices | Dispositivos registados | Lista de dispositivos |
| MIFID_getInvestorProfile | Perfil de investidor | Perfil MIFID |
| Message_getInboxMessage | Mensagens | Inbox do utilizador |

### APIs de Contas e Movimentos (ApiBBest)

| API | Descrição | Dados Retornados |
|-----|-----------|------------------|
| Account_getAccounts | Lista de contas | Contas do cliente |
| Account_getMovements | Movimentos | Extracto de movimentos |
| Statement_getUserStatement | Património | Posição patrimonial |

### APIs de Cartões (ApiBBest)

| API | Descrição | Dados Retornados |
|-----|-----------|------------------|
| CCards_getCreditCards | Cartões de crédito | Lista e detalhes |
| DCards_getDebitCards | Cartões de débito | Lista e detalhes |

### APIs de Operações (ApiBBest)

| API | Descrição | Dados Retornados |
|-----|-----------|------------------|
| Operation_getOperationConfirmation | Confirmação de operações | Estado de operações |
| Schedule_getSchedules | Agendamentos | Operações agendadas |
| Permanent_getPermanentOrders | Ordens permanentes | Lista de ordens |
| CorpAction_getOngoingClosedCA | Operações corporativas | Corporate actions |

### APIs PSD2/SIBS (ApiBBest)

| API | Descrição | Dados Retornados |
|-----|-----------|------------------|
| SIBS_getConsentStatus | Estado de consentimento PSD2 | Status |
| SIBS_getConsentAccount | Contas com consentimento | Lista de contas |

### APIs de Transferências (ApiBBest)

| API | Descrição | Uso |
|-----|-----------|-----|
| API Beneficiários | Lista de beneficiários | Selecção de destinatário |
| API COPS | Consulta de titular (IBAN nacional) | Validação PT50 |
| API VOP | Verificação de nome | Confirmação de titular |
| API Simulação | Simulação de transferência | Pré-cálculo de custos |
| API Transferência | Execução de transferência | Operação efectiva |

### APIs de Backoffice (CMS)

| API | Descrição | Dados Retornados |
|-----|-----------|------------------|
| Notícias | Conteúdo noticioso | Lista de notícias |
| Novidades | Novidades do banco | Lista de novidades |
| Alertas | Alertas ao utilizador | Lista de alertas |
| Publicidades | Cards promocionais | Estrutura de publicidade |

> **Nota:** Este catálogo foi extraído dos diagramas de sequência. Solicitar documentação detalhada (contratos OpenAPI/Swagger) à equipa de backend.

### Autenticação por Backend

| Backend | Protocolo | Token Usado |
|---------|-----------|-------------|
| ApiPsd2 | OAuth + SHA256 | access_token_anonimo (pré-login) / apiToken (pós-login) |
| ApiBBest | OAuth 1.1 HMAC | apiToken |
| Microservices | Protocolo Omni | Token de sessão |
| Siebel (via Gateway) | BEST | Bearer Token |

---

## Decisões

### Integração Core Banking
- **Decisão:** _Pendente_
- **Justificação:** _Pendente_
- **Alternativas consideradas:** _Pendente_

### Fornecedores Terceiros
- **Decisão:** _Pendente_
- **Justificação:** _Pendente_
- **Alternativas consideradas:** _Pendente_

### Message Broker
- **Decisão:** _Pendente_
- **Justificação:** _Pendente_
- **Alternativas consideradas:** _Pendente_

### Open Banking
- **Decisão:** _Pendente_
- **Justificação:** _Pendente_
- **Alternativas consideradas:** _Pendente_

### Tratamento de Erros
- **Decisão:** _Pendente_
- **Justificação:** _Pendente_
- **Alternativas consideradas:** _Pendente_

## Restrições Conhecidas

- Reutilização da infraestrutura da app mobile
- Integração via BFF (não há acesso direto do frontend a sistemas externos)
- Conformidade PSD2 para Open Banking
- SLAs de disponibilidade do Core Banking

## Decisões Relacionadas

- [DEC-007-padrao-bff.md](../decisions/DEC-007-padrao-bff.md) - BFF como ponto único de integração
- [DEC-010-stack-tecnologica-backend.md](../decisions/DEC-010-stack-tecnologica-backend.md) - Stack tecnológica backend

## Referências

- [DEF-05-arquitetura-bff.md](DEF-05-arquitetura-bff.md) - Arquitetura BFF
- [DEF-05-api-design.md](DEF-05-api-design.md) - Padrões de API
- [DEF-05-padroes-resiliencia.md](DEF-05-padroes-resiliencia.md) - Padrões de resiliência
- Documentação APIs Core Banking (a fornecer)
- PSD2 RTS - Open Banking requirements
