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
status: structure
---

# DEF-09: Integracao & Interfaces Externas

> **Related section:** [9 - Integracao & Interfaces Externas](../sections/SEC-09-integracao-interfaces-externas.md)

## Context

Definir as integracoes do HomeBanking Web com sistemas internos e externos. O canal web reutiliza a infraestrutura da app mobile, portanto muitas integracoes ja existem. Este documento foca nas especificidades do canal web e decisoes de integracao.

## Questions to Answer

### Integracao Core Banking

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

24. Qual a estrategia padrao de retry para integracoes?
    - Erros transientes: Exponential backoff (3 retries)
    - Network Timeout: Imediate retry (1 retry)
    - Rate limiting: Fixed Delay (429 status)

25. Ha circuit breaker implementado? Qual biblioteca?
    Não. Será decidido no assessment da aplicação

26. Quais integracoes tem fallback definido?
    Necessita aprofundamento

27. Como sao comunicados erros de integracao ao utilizador?
    Mensagem de erro para aguardar e registo de log.

### SLAs de Integracao

28. Quais sao os SLAs de disponibilidade dos sistemas integrados?
    Necessita aprofundamento

29. Quais sao os tempos de resposta esperados (P50, P95, P99)?
    Necessita aprofundamento

30. Ha janelas de manutencao programadas que afetam integracoes?
    Necessita aprofundamento

### API Management

31. Qual API Gateway e utilizado?
    Azure API Gateway

32. Como e feito o rate limiting por integracao?
    Necessita aprofundamento

33. Ha throttling diferenciado por tipo de operacao?
    Necessita aprofundamento

34. Como e feito o monitoring de APIs?
    Necessita aprofundamento

### Catalogo de Integracoes

35. Existe catalogo de APIs/servicos documentado?
    Necessita aprofundamento

36. Qual ferramenta e usada para documentacao de APIs (Swagger UI, Redoc)?
    Necessita aprofundamento

37. Ha ambiente de sandbox para testes de integracao?
    Necessita aprofundamento

## Decisions

### Core Banking Integration
- **Decision:** _Pending_
- **Justification:** _Pending_
- **Alternatives considered:** _Pending_

### Third-party Providers
- **Decision:** _Pending_
- **Justification:** _Pending_
- **Alternatives considered:** _Pending_

### Message Broker
- **Decision:** _Pending_
- **Justification:** _Pending_
- **Alternatives considered:** _Pending_

### Open Banking
- **Decision:** _Pending_
- **Justification:** _Pending_
- **Alternatives considered:** _Pending_

### Error Handling
- **Decision:** _Pending_
- **Justification:** _Pending_
- **Alternatives considered:** _Pending_

## Known Constraints

- Reutilizacao da infraestrutura da app mobile
- Integracao via BFF (nao ha acesso direto do frontend a sistemas externos)
- Conformidade PSD2 para Open Banking
- SLAs de disponibilidade do Core Banking

## Related Decisions

- [DEC-007-padrao-bff.md](../decisions/DEC-007-padrao-bff.md) - BFF como ponto unico de integracao
- [DEC-010-stack-tecnologica-backend.md](../decisions/DEC-010-stack-tecnologica-backend.md) - Stack tecnologica backend

## References

- [DEF-05-arquitetura-bff.md](DEF-05-arquitetura-bff.md) - Arquitetura BFF
- [DEF-05-api-design.md](DEF-05-api-design.md) - Padroes de API
- [DEF-05-padroes-resiliencia.md](DEF-05-padroes-resiliencia.md) - Padroes de resiliencia
- Documentacao APIs Core Banking (a fornecer)
- PSD2 RTS - Open Banking requirements
