---
id: DEF-05-autenticacao-oauth
aliases:
  - Novo Banco Autenticação OAuth
tags:
  - nextreality-novobanco-website-definitions
  - definitions
approved: true
created: 2025-12-22
hubs:
  - "[[nextreality]]"
para-code: R
reviewed: true
status: completed
---
# DEF-05: Autenticação e OAuth

> **Secção relacionada:** [SEC-07 - Autenticação & Autorização](../sections/SEC-07-autenticacao-autorizacao.md)

## Contexto

Este documento define os fluxos de autenticação, mecanismos OAuth, gestão de tokens e integração com a App Mobile para autorização na plataforma de Homebanking do Novo Banco.

## Resumo dos Métodos de Autenticação

A plataforma suporta **4 métodos de autenticação**, ordenados por preferência:

| Caso | Método | Descrição | Recomendação |
|------|--------|-----------|--------------|
| 1 | QR Code Específico de Sessão | QR dinâmico por sessão, vinculação automática via App | **Principal** - Melhor UX e segurança |
| 2 | QR Code Genérico | QR fixo, utilizador recebe código para introduzir manualmente | Alternativo - Simplicidade |
| 3 | User + Pass + OTP SMS | Login tradicional com código OTP enviado por SMS | Fallback - Compatibilidade |
| 4 | User + Pass + Push App | Login tradicional com aprovação via notificação na App | Fallback - Sem SMS |

> **Nota:** Os casos 1 e 2 (QR Code) dispensam CAPTCHA por requererem dispositivo físico autorizado com biometria.

---

## Decisões Arquiteturais

### Resumo de Decisões

| Tópico | Decisão | Justificativa |
|--------|---------|---------------|
| Fluxos principais | QR Code (2 variantes) | Segurança via dispositivo autorizado + biometria |
| Gestão de tokens | BFF como intermediário | Frontend nunca expõe tokens reais |
| Armazenamento de tokens | Cache (Redis) no BFF | Performance e segurança |
| Anti-automação | QR Code + dispositivo autorizado | Dispensa CAPTCHA, requer App vinculada |
| Rate Limiting | Gateway | Centralizado, configurável |
| Sessões múltiplas | Permitidas | Browser + App podem coexistir |

---

## Fluxos de Autenticação

### Visão Geral dos Cenários

| Cenário | Descrição | Uso Recomendado |
|---------|-----------|-----------------|
| QR Code Genérico | Utilizador scan QR fixo, recebe código para introduzir | Fallback, simplicidade |
| QR Code Específico | QR dinâmico por sessão, vinculação automática | **Principal**, melhor UX |
| User + Pass + OTP SMS | Login tradicional com OTP via SMS | Fallback legacy |
| User + Pass + Push App | Login tradicional com aprovação na App | Fallback |

### Cenário Principal: QR Code Específico de Sessão

Este é o fluxo recomendado para a maioria dos utilizadores.

```plantuml
@startuml
skinparam sequenceMessageAlign center
skinparam responseMessageBelowArrow true

title Autenticação via QR Code Específico de Sessão

actor "Utilizador" as User
participant "Browser\n(Frontend)" as Browser
participant "App Mobile\n(Autorizada)" as App
participant "BFF" as BFF
participant "Backend\nAPI" as API
database "Cache\n(Redis)" as Cache

== Fase 1: Geração do QR Code ==
User -> Browser : Acede página de login
Browser -> BFF : GET /auth/qr-session
BFF -> API : POST /auth/create-pending-session
API -> API : Gera pending_session_id\n(UUID único)
API --> BFF : {pending_session_id, qr_data, expires_in: 120}
BFF -> Cache : Armazena pending_session\n(status: PENDING)
BFF --> Browser : {qr_image, pending_session_id}
Browser -> Browser : Exibe QR Code dinâmico
Browser -> BFF : WebSocket /auth/session-status\n{pending_session_id}
note right of Browser
Browser fica a escutar
por atualizações via
WebSocket ou polling
end note

== Fase 2: Scan e Autorização na App ==
User -> App : Scan QR Code
App -> App : Extrai pending_session_id\ndo QR Code
App -> App : Solicita biometria/PIN
User -> App : Confirma biometria
App -> API : POST /auth/authorize-session\n{pending_session_id, device_id, biometric_token}
API -> API : Valida dispositivo autorizado
API -> API : Valida pending_session existe\ne não expirou
API -> API : Gera apiToken
API -> API : Marca sessão como AUTHORIZED
API --> App : {status: "authorized"}

== Fase 3: Browser recebe autorização ==
API -> BFF : Callback ou evento\n(session authorized)
BFF -> Cache : Atualiza sessão\n(status: AUTHORIZED, tokens)
BFF -> Browser : WebSocket: session_authorized
Browser -> BFF : POST /auth/complete-session\n{pending_session_id}
BFF -> Cache : Recupera tokens reais
BFF -> BFF : Gera session_token (para frontend)
BFF -> Cache : Armazena mapeamento\n(session_token -> tokens reais)
BFF --> Browser : {session_token, user_info}
Browser -> Browser : Armazena session_token
Browser --> User : Login concluído

@enduml
```

### Cenário Alternativo: QR Code Genérico

Utilizado quando o QR dinâmico não está disponível ou como opção simplificada.

```plantuml
@startuml
skinparam sequenceMessageAlign center
skinparam responseMessageBelowArrow true

title Autenticação via QR Code Genérico

actor "Utilizador" as User
participant "Browser\n(Frontend)" as Browser
participant "App Mobile\n(Autorizada)" as App
participant "BFF" as BFF
participant "Backend\nAPI" as API
database "Cache\n(Redis)" as Cache

== Fase 1: Início no Browser ==
User -> Browser : Acede página de login
Browser -> Browser : Exibe QR Code genérico\n(URL fixa da App)
note right of Browser
QR Code contém URL para
abrir a App com intent de
autenticação web
end note

== Fase 2: Scan e Autenticação na App ==
User -> App : Scan QR Code
App -> App : Abre e solicita\nbiometria/PIN
User -> App : Confirma biometria
App -> API : POST /auth/web-session\n{device_id, biometric_token}
API -> API : Valida dispositivo autorizado
API -> API : Gera session_code (código curto)
API --> App : {session_code: "A7X9K2", expires_in: 120}

== Fase 3: Vinculação Manual ==
App --> User : Exibe código: "A7X9K2"
User -> Browser : Introduz código manualmente
Browser -> BFF : POST /auth/link-session\n{session_code: "A7X9K2"}
BFF -> API : Valida session_code
API --> BFF : {apiToken, user_info}
BFF -> Cache : Armazena tokens reais\n(key: session_token_id)
BFF -> BFF : Gera session_token (para frontend)
BFF --> Browser : {session_token, user_info}
Browser -> Browser : Armazena session_token
Browser --> User : Login concluído

@enduml
```

### Cenário Fallback: User + Pass + OTP

Mantido para compatibilidade e casos onde o utilizador não tem a App.

```plantuml
@startuml
actor Utilizador
participant "Browser" as Web
participant "BFF" as BFF
participant "Backend API" as API
participant "OTP Service" as OTP

Utilizador -> Web : Username + Password
Web -> BFF : POST /auth/login\n{user, pass}
BFF -> API : Authentication_checkLogin
API --> BFF : needStrongAuthentication=Y, otp_id
BFF --> Web : {requires_otp: true, otp_id}
Web --> Utilizador : Solicita OTP
OTP -> Utilizador : Envia SMS
Utilizador -> Web : Introduz OTP
Web -> BFF : POST /auth/verify-otp\n{otp_id, otp_value}
BFF -> API : Login secure (otp_id, otp_value)
API --> BFF : {apiToken}
BFF -> BFF : Gera session_token
BFF --> Web : {session_token, user_info}
Web --> Utilizador : Acesso concedido
@enduml
```

### Cenário Fallback: User + Pass + Push App

```plantuml
@startuml
actor Utilizador
participant "Browser" as Web
participant "BFF" as BFF
participant "Backend API" as API
participant "App Mobile" as App

Utilizador -> Web : Username + Password
Web -> BFF : POST /auth/login\n{user, pass}
BFF -> API : Authentication_checkLogin
API --> BFF : needStrongAuthentication=Y
BFF --> Web : {requires_app_approval: true}
Web --> Utilizador : Aguarda aprovação na App
API -> App : Push notification
Utilizador -> App : Aprova acesso
App -> API : Confirmação
API --> BFF : Callback (approved)
BFF -> BFF : Gera session_token
BFF --> Web : {session_token, user_info}
Web --> Utilizador : Acesso concedido
@enduml
```

---

## Estratégia de Tokens

### Arquitetura BFF como Intermediário

O BFF atua como intermediário de segurança, garantindo que o token real (apiToken) nunca é exposto ao Frontend.

```plantuml
@startuml
skinparam sequenceMessageAlign center

title Gestão de Tokens via BFF

participant "Frontend" as FE
participant "BFF" as BFF
database "Cache\n(Redis)" as Cache
participant "Backend API" as API

== Após Login Bem-Sucedido ==
BFF -> BFF : Recebe apiToken do Backend
BFF -> BFF : Gera session_token (opaco, UUID)
BFF -> Cache : SET session:{session_token}\n{apiToken, user_id, created_at, ttl}
BFF --> FE : {session_token} (apenas este)

== Requisições Subsequentes ==
FE -> BFF : GET /api/accounts\nHeader: X-Session-Token: {session_token}
BFF -> Cache : GET session:{session_token}
Cache --> BFF : {apiToken, ...}
BFF -> BFF : Valida TTL e integridade
BFF -> API : GET /accounts\nHeader: Authorization: OAuth {apiToken}...
API --> BFF : {accounts_data}
BFF --> FE : {accounts_data}

== Renovação Transparente ==
note over BFF
Se apiToken próximo de expirar,
BFF renova automaticamente
sem envolver o Frontend
end note

== Logout ==
FE -> BFF : POST /auth/logout\n{session_token}
BFF -> Cache : DEL session:{session_token}
BFF -> API : POST /auth/revoke (opcional)
BFF --> FE : {status: "logged_out"}

@enduml
```

### Tipos de Tokens

| Token | Localização | Propósito | Visibilidade |
|-------|-------------|-----------|--------------|
| session_token | Frontend (cookie/storage) | Identificar sessão no BFF | Frontend |
| apiToken | Cache do BFF | Autenticação com Backend | Apenas BFF |

### Ciclo de Vida dos Tokens

| Evento | Ação | Responsável |
|--------|------|-------------|
| Login bem-sucedido | Criar session_token, armazenar tokens reais | BFF |
| Requisição | Traduzir session_token para tokens reais | BFF |
| Proximidade de expiração | Renovar apiToken automaticamente | BFF |
| Logout | Eliminar session_token e tokens do cache | BFF |
| Inatividade (15 min) | Invalidar sessão | BFF |

---

## Protocolos OAuth por Backend

O BFF comunica com dois backends diferentes usando variantes de OAuth:

| Backend | Protocolo | Assinatura | Propósito |
|---------|-----------|------------|-----------|
| **ApiPsd2** | OAuth + SHA256 | `SHA256(consumer_key & GUID & timestamp & version & secret_key)` | Autenticação PSD2 |
| **ApiBBest** | OAuth 1.1 HMAC | `HMAC-SHA256(base_string, consumer_secret)` | APIs bancárias |

### Header de Identificação de Canal

Todas as chamadas ao backend devem incluir o header de identificação de canal:

```http
x-nb-channel: best.spa
```

---

## Protocolo OAuth 1.1 (ApiBBest)

### Tokens Anónimos (Pré-Login)

Utilizados para operações antes do login (ex: obter configurações).

| Token | Propósito | Armazenamento |
|-------|-----------|---------------|
| access_token_anonimo | Autenticação inicial | Código da App/BFF |
| consumer_key | Identificação do cliente | Código da App/BFF |
| secret_key | Assinatura de requests | Código da App/BFF |

### Estrutura do Header OAuth

```
Authorization: OAuth access_token={{access_token}},
                      oauth_consumer_key={{consumer_key}},
                      oauth_timestamp={{timestamp}},
                      oauth_version=1.1,
                      oauth_signature={{signature}},
                      oauth_guid={{GUID}}
```

### Geração de Assinatura

```plantuml
@startuml
start
:Gerar GUID;
:Gerar timestamp;
:Construir base_string;
note right
access_token%26
oauth_consumer_key%26
oauth_guid%26
oauth_timestamp%26
oauth_version%26
oauth_consumer_secret
end note
:HMAC SHA256 com consumer_secret;
:Encode Base64;
:URL Encode;
:signature_final;
stop
@enduml
```

---

## Códigos de Operação ApiPsd2

| Código | Operação | Descrição | Token Usado |
|--------|----------|-----------|-------------|
| AUT_004 | Authentication_checkLogin | Validação de credenciais | access_token_anonimo |
| AUT_001 | ReenviaOTP | Solicita envio de OTP | apiToken |
| DEV_005.2 | RegistarDispositivoSecure | Valida OTP e regista dispositivo | apiToken |
| CLI_005 | ConsultaCliente | Consulta dados do cliente (pós-login) | apiToken |

---

## API Authentication_checkLogin (AUT_004)

### Parâmetros do Login - Canal Web

| Parâmetro | Descrição | Valor Web |
|-----------|-----------|-----------|
| `user` | Identificador do utilizador | Input do utilizador |
| `pass` | Password (pode ser cifrada) | Input do utilizador |
| `encrypt` | Indica se password está cifrada | "Y" ou "N" |
| `device_id` | Identificador do dispositivo | User-Agent ou GUID gerado |
| `app_version` | Versão da aplicação | Versão do SPA |
| `so_id` | Sistema operativo | "SPA" |

### Request

```json
{
    "user": "5.9.85.7.4.0.5.82",
    "pass": "",
    "token": "98.110.54.101.115.111",
    "encrypt": "Y",
    "device_id": "Device Id 3",
    "app_version": "1.0",
    "so_id": "2"
}
```

| Campo | Descrição |
|-------|-----------|
| user | Username encriptado |
| pass | Password encriptada (vazio se biometria) |
| token | Token biométrico (se aplicável) |
| encrypt | Flag de encriptação (Y/N) |
| device_id | Identificador do dispositivo |
| app_version | Versão da aplicação |
| so_id | ID do sistema operativo |

### Response

```json
{
    "returnCode": "0",
    "returnMsg": "Sucesso",
    "outputData": {
        "apiToken": "914e55d8ea3b4e19b1aa63c9efbad2ba",
        "mustChangePassword": "N",
        "needStrongAuthentication": "N",
        "firstLogin": "N",
        "otp_id": null,
    }
}
```

### Flags de Resposta

| Flag | Valor | Ação |
|------|-------|------|
| mustChangePassword | Y | Forçar alteração de password |
| needStrongAuthentication | Y | Solicitar OTP, usar otp_id |
| firstLogin | Y | Mostrar wizard de preferências |

---

## Autenticação Forte (SCA) - PSD2

### Fatores de Autenticação

| Fator | Tipo | Exemplos |
|-------|------|----------|
| Conhecimento | Algo que sabe | Password, PIN |
| Posse | Algo que tem | Telemóvel, App autorizada |
| Inerência | Algo que é | Biometria (fingerprint, face) |

### Operações que Requerem SCA

| Operação | SCA Obrigatória | Fatores |
|----------|-----------------|---------|
| Login | Sim | 2 fatores (QR Code + Biometria) |
| Transferências | Sim | Confirmação na App |
| Pagamentos | Sim | Confirmação na App |
| Alteração de dados sensíveis | Sim | Confirmação na App |
| Consultas | Não | Após login válido |

---

## Gestão de Sessões

### Ciclo de Vida

```plantuml
@startuml
[*] --> Anonimo : Início
Anonimo --> PendingQR : QR Code gerado
PendingQR --> Autenticado : App autoriza
PendingQR --> Anonimo : QR expira (120s)
Anonimo --> Autenticando : Login tradicional
Autenticando --> Autenticado : Sucesso
Autenticando --> Anonimo : Falha
Autenticado --> Ativo : Primeira requisição
Ativo --> Ativo : Requisições (renova TTL)
Ativo --> Warning : 10 min inatividade
Warning --> Ativo : Utilizador ativo
Warning --> Expirado : 5 min adicionais
Expirado --> Anonimo : Sessão terminada
Ativo --> Anonimo : Logout manual
@enduml
```

### Timeouts

| Evento | Tempo | Ação |
|--------|-------|------|
| QR Code expiração | 120 seg | Gerar novo QR |
| Inatividade warning | 10 min | Notificar utilizador |
| Inatividade logout | 15 min | Terminar sessão |
| Token expiration | Configurável | BFF renova automaticamente |

### Sessões Múltiplas

- **Permitido:** Um utilizador pode ter múltiplas sessões simultâneas
- **Justificativa:** Browser e App coexistem naturalmente (App necessária para autorizar Browser)
- **Rastreabilidade:** Cada sessão tem session_token único, permitindo auditoria

---

## Anti-Automação e Segurança

### Mecanismos Implementados

| Mecanismo | Descrição | Responsável |
|-----------|-----------|-------------|
| QR Code + Dispositivo autorizado | Requer App previamente vinculada | Backend |
| Biometria | Confirma identidade do utilizador | App Mobile |
| Rate Limiting | Limita tentativas por IP/utilizador | **Gateway** |
| Device fingerprint | Identifica dispositivos suspeitos | Backend |

### Dispensa de CAPTCHA

O fluxo via QR Code dispensa CAPTCHA porque:
1. Requer dispositivo físico (App instalada)
2. Requer dispositivo previamente autorizado pelo cliente
3. Requer autenticação biométrica na App
4. QR Code expira em 120 segundos

---

## Dependências

| Componente | Responsabilidade | Status |
|------------|------------------|--------|
| App Mobile | Scan QR, biometria, autorização | Existente |
| Backend API | Gestão de tokens, validação | Existente |
| BFF | Intermediário de tokens, session_token | A implementar |
| Cache (Redis) | Armazenamento de sessões/tokens | A implementar |
| Gateway | Rate Limiting, WAF | **Dependência externa** |
| WebSocket Server | Notificação de sessão autorizada | A implementar |

---

## Questões Pendentes de Confirmação

### Q-07-001: Momento de Retorno do apiToken

> **Status:** Aguarda confirmação do analista
> **Origem:** Conflito entre DEF-GEN-other-auth-flow.md e fluxos existentes

**Contexto:**
Existe divergência entre documentos sobre quando o `apiToken` é retornado:

| Interpretação | Descrição |
|---------------|-----------|
| A | apiToken retornado **antes** do OTP, OTP valida via API "secure" separada |
| B | apiToken retornado **após** validação do OTP |

**Evidência do novo documento (DEF-GEN-other-auth-flow.md):**
```
BFF-->ApiBBest: Authentication_checkLogin
BFF<--ApiBBest: "apiToken":"914e55d8ea3b4e19b1aa63c9efbad2ba", ...
BFF-->SPA: Pede OTP
SPA-->BFF: Envia OTP
BFF-->ApiBBest: Chamar API de secure
```

**Questão para o analista:**
- O `apiToken` é retornado imediatamente no `Authentication_checkLogin`, mesmo quando `needStrongAuthentication=Y`?
- Ou o `apiToken` só é disponibilizado após a validação do OTP na API "secure"?

---

## Responsabilidades Geridas pelo Siebel

As seguintes funcionalidades são geridas inteiramente pelo Siebel (backend), não sendo responsabilidade do novo WebSite:

| Funcionalidade | Responsável | Notas |
|----------------|-------------|-------|
| Recuperação de acesso (password esquecida) | Siebel | Fluxo igual à APP Mobile |
| RBAC (Autorização por perfil) | Siebel | Perfis e permissões definidos no backend |
| Políticas de Password (complexidade, expiração) | Siebel | Regras centralizadas no backend |

---

## Itens Pendentes

| Tópico | Estado | Prioridade |
|--------|--------|------------|
| **Q-07-001: Momento do apiToken** | Aguarda confirmação | **Alta** |
| Procedimento de revogação de tokens | A definir | Média |

---

## Decisões Relacionadas

- [DEC-001-estrategia-autenticacao-web.md](../decisions/DEC-001-estrategia-autenticacao-web.md) - Estratégia de autenticação
- [DEC-002-gestao-sessoes-tokens.md](../decisions/DEC-002-gestao-sessoes-tokens.md) - Gestão de sessões e tokens

## Referências

- [SEC-07-autenticacao-autorizacao.md](../sections/SEC-07-autenticacao-autorizacao.md)
- [DEF-09-fluxo-transferencia.md](DEF-09-fluxo-transferencia.md)
- [DEF-02-restricoes.md](DEF-02-restricoes.md) - RST-CMP-001 (Autenticação vinculada)
- PSD2 RTS on Strong Customer Authentication
