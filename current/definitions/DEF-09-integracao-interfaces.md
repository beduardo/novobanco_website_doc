---
id: DEF-09-integracao-interfaces
aliases:
  - Integracao e Interfaces Externas
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

# DEF-09: Integracao & Interfaces Externas

> **Secção relacionada:** [9 - Integracao & Interfaces Externas](../sections/SEC-09-integracao-interfaces-externas.md)

## Contexto

Definir as integracoes do HomeBanking Web com sistemas internos e externos. O canal web reutiliza a infraestrutura da app mobile, portanto muitas integracoes ja existem. Este documento foca nas especificidades do canal web e decisoes de integracao.

## Catalogo de Dependencias Externas

| Sistema | Tipo | Proprietario | Criticidade | Status |
|---------|------|--------------|-------------|--------|
| Core Banking APIs | Integracao | NovoBanco | Alta | Existente |
| App Mobile Nativa | Referencia | NovoBanco | Media | Existente |
| Azure Infrastructure | Plataforma | NovoBanco | Alta | Existente |
| Gateway de Pagamentos | Integracao | [A DEFINIR] | Alta | A validar |
| KYC/AML Provider | Integracao | [A DEFINIR] | Alta | A validar |
| SMS Gateway | Integracao | [A DEFINIR] | Alta | A definir no assessment |
| Push Notifications Service | Integracao | [A DEFINIR] | Media | A definir no assessment |
| Document Management System | Integracao | [A DEFINIR] | Media | A validar |
| HSM (Hardware Security Module) | Seguranca | [A DEFINIR] | Alta | A validar |
| Identity Provider (SSO) | Autenticacao | [A DEFINIR] | Media | A validar |
| Email Service Provider | Notificacoes | [A DEFINIR] | Media | A definir no assessment |

> **Nota:** Sistemas marcados como "Existente" ja estao integrados na app mobile e serao reutilizados.

## Perguntas a Responder

### Integração Core Banking

1. Quais servicos do Core Banking serao consumidos pelo canal web?
    Não há acesso direto. O BFF irá acessar uma api chamada Backend API (Um Facade geral) que se encarregará de acionar os backends devidos conforme chamads.

2. O canal web utiliza as mesmas APIs que a app mobile ou ha APIs especificas?
    As mesmas

3. Existe documentacao das APIs do Core Banking disponivel?
   não

4. Qual o protocolo de comunicacao com o Core Banking (REST, SOAP, outro)?
   Entre BFF e BackendAPI será REST

5. Ha transformacao de dados necessaria entre Core Banking e canal web?
   Sim. Isso estarà cargo do BFF

### Terceiros - KYC/AML

6. Qual provider de KYC/AML e utilizado?
   Isso já está implementado no backend. Não há requisitos para isto na apliicação.

7. O canal web tera fluxos de onboarding que requerem KYC?
   Necessita aprofundamento

8. Ha verificacoes AML em tempo real para transacoes?
   Necessita aprofundamento

### Terceiros - Notificacoes

9. Qual gateway de SMS e utilizado?
   Será definido no assessment inicial do projeto.

10. Qual servico de Push Notifications e utilizado?
   Será definido no assessment inicial do projeto.

11. Ha servico de email transacional?
   Será definido no assessment inicial do projeto.

12. O canal web gera notificacoes ou apenas as recebe?
    Gera e Recebe.

### Terceiros - Cartoes

13. Qual provider de cartoes e utilizado (emissao, processamento)?
    Necessita aprofundamento

14. O canal web permitira operacoes de cartoes (bloqueio, ativacao, limites)?
    Sim

15. Ha integracao com 3D Secure para pagamentos online?
    _Pending_

### Open Banking PSD2

16. O banco expoe APIs de Open Banking (AISP, PISP)?
    Necessita aprofundamento

17. O canal web consumira APIs de Open Banking de outros bancos?
    Necessita aprofundamento

18. Existe plataforma de gestao de consentimentos?
    Necessita aprofundamento

19. Qual o modelo de autorizacao para Open Banking (OAuth 2.0, OIDC)?
    Necessita aprofundamento

### Message Broker

20. Qual tecnologia de Message Broker e utilizada (RabbitMQ, Kafka, Azure Service Bus)?
    Necessita aprofundamento

21. Quais eventos sao publicados/consumidos pelo canal web?
    Necessita aprofundamento

22. Ha requisitos de ordenacao ou exactly-once delivery?
    Necessita aprofundamento

23. Qual a estrategia de dead-letter para mensagens falhadas?
    Necessita aprofundamento

### Tratamento de Erros

> **Nota:** Padroes de resiliencia (retry, circuit breaker) consolidados em [DEF-05-padroes-resiliencia.md](DEF-05-padroes-resiliencia.md)

24. Como sao comunicados erros de integracao ao utilizador?
    Mensagem de erro amigavel + registo de log para troubleshooting

25. Quais integracoes tem fallback definido?
    Autenticacao (fallback OTP). Ver DEF-05-padroes-resiliencia.

### SLAs de Integracao (Simplificado)

26. Quais sao os SLAs de disponibilidade dos sistemas integrados?
    Necessita aprofundamento. Backend API deve ter SLA >= 99.9%

27. Ha janelas de manutencao programadas que afetam integracoes?
    Necessita aprofundamento

### API Management

28. Qual API Gateway e utilizado?
    Azure API Gateway

29. Como e feito o rate limiting por integracao?
    Necessita aprofundamento. Gerido pelo Gateway, nao pelo BFF.

### Catalogo de Integracoes (Simplificado)

30. Existe catalogo de APIs/servicos documentado?
    Necessita aprofundamento

31. Ha ambiente de sandbox para testes de integracao?
    Necessita aprofundamento

### HSM (Hardware Security Module)

32. Qual HSM e utilizado pelo banco (Thales, AWS CloudHSM, Azure Dedicated HSM)?
    Necessita aprofundamento

33. Quais operacoes do canal web requerem HSM (assinatura digital, encriptacao de dados sensiveis)?
    Necessita aprofundamento

34. Existe integracao HSM ja disponivel via Backend API?
    Necessita aprofundamento

35. O HSM e utilizado para armazenamento de chaves de encriptacao de tokens?
    Necessita aprofundamento

### Identity Provider / SSO

36. Existe Identity Provider corporativo (Azure AD, Okta, outro)?
    Necessita aprofundamento

37. Ha requisitos de SSO com outros sistemas internos do banco?
    Necessita aprofundamento

38. O SSO e aplicavel ao canal web ou apenas a sistemas internos/backoffice?
    Necessita aprofundamento

39. O Identity Provider e o mesmo utilizado pela app mobile?
    Necessita aprofundamento

### Document Management System

40. Existe DMS centralizado para extratos e comprovativos?
    Necessita aprofundamento

41. Os documentos sao gerados em tempo real ou pre-gerados?
    Necessita aprofundamento

42. Qual o formato de documentos suportado (PDF, outro)?
    Necessita aprofundamento

43. Ha requisitos de assinatura digital em documentos?
    Necessita aprofundamento

### Notificacoes - Detalhamento

44. SMS Gateway, Push e Email serao os mesmos servicos da app mobile?
    Necessita aprofundamento

45. Ha requisitos de templates de notificacao especificos para o canal web?
    Necessita aprofundamento

46. Existe servico de preferencias de notificacao do utilizador?
    Necessita aprofundamento

47. Ha requisitos de notificacoes em tempo real (WebSocket) para o canal web?
    Necessita aprofundamento

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

- Reutilizacao da infraestrutura da app mobile
- Integracao via BFF (nao ha acesso direto do frontend a sistemas externos)
- Conformidade PSD2 para Open Banking
- SLAs de disponibilidade do Core Banking

## Decisões Relacionadas

- [DEC-007-padrao-bff.md](../decisions/DEC-007-padrao-bff.md) - BFF como ponto unico de integracao
- [DEC-010-stack-tecnologica-backend.md](../decisions/DEC-010-stack-tecnologica-backend.md) - Stack tecnologica backend

## Referências

- [DEF-05-arquitetura-bff.md](DEF-05-arquitetura-bff.md) - Arquitetura BFF
- [DEF-05-api-design.md](DEF-05-api-design.md) - Padroes de API
- [DEF-05-padroes-resiliencia.md](DEF-05-padroes-resiliencia.md) - Padroes de resiliencia
- Documentacao APIs Core Banking (a fornecer)
- PSD2 RTS - Open Banking requirements
