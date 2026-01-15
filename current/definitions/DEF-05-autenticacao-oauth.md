---
id: DEF-05-autenticacao-oauth
aliases:
  - Novo Banco Autenticacao OAuth
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
# DEF-05: Autenticacao e OAuth

> **Secao relacionada:** [SEC-07 - Autenticacao & Autorizacao](../sections/SEC-07-autenticacao-autorizacao.md)

## Contexto

Este documento define os fluxos de autenticacao, mecanismos OAuth, gestao de tokens e integracao com a App Mobile para autorizacao na plataforma de Homebanking do Novo Banco.

## Resumo dos Metodos de Autenticacao

A plataforma suporta **4 metodos de autenticacao**, ordenados por preferencia:

| Caso | Metodo | Descricao | Recomendacao |
|------|--------|-----------|--------------|
| 1 | QR Code Especifico de Sessao | QR dinamico por sessao, vinculacao automatica via App | **Principal** - Melhor UX e seguranca |
| 2 | QR Code Generico | QR fixo, utilizador recebe codigo para introduzir manualmente | Alternativo - Simplicidade |
| 3 | User + Pass + OTP SMS | Login tradicional com codigo OTP enviado por SMS | Fallback - Compatibilidade |
| 4 | User + Pass + Push App | Login tradicional com aprovacao via notificacao na App | Fallback - Sem SMS |

> **Nota:** Os casos 1 e 2 (QR Code) dispensam CAPTCHA por requererem dispositivo fisico autorizado com biometria.

---

## Decisoes Arquitecturais

### Resumo de Decisoes

| Topico | Decisao | Justificativa |
|--------|---------|---------------|
| Fluxos principais | QR Code (2 variantes) | Seguranca via dispositivo autorizado + biometria |
| Gestao de tokens | BFF como intermediario | Frontend nunca expoe tokens reais |
| Armazenamento de tokens | Cache (Redis) no BFF | Performance e seguranca |
| Anti-automacao | QR Code + dispositivo autorizado | Dispensa CAPTCHA, requer App vinculada |
| Rate Limiting | Gateway | Centralizado, configuravel |
| Sessoes multiplas | Permitidas | Browser + App podem coexistir |

---

## Fluxos de Autenticacao

### Visao Geral dos Cenarios

| Cenario | Descricao | Uso Recomendado |
|---------|-----------|-----------------|
| QR Code Generico | Utilizador scan QR fixo, recebe codigo para introduzir | Fallback, simplicidade |
| QR Code Especifico | QR dinamico por sessao, vinculacao automatica | **Principal**, melhor UX |
| User + Pass + OTP SMS | Login tradicional com OTP via SMS | Fallback legacy |
| User + Pass + Push App | Login tradicional com aprovacao na App | Fallback |

### Cenario Principal: QR Code Especifico de Sessao

Este e o fluxo recomendado para a maioria dos utilizadores.

```plantuml
@startuml
skinparam sequenceMessageAlign center
skinparam responseMessageBelowArrow true

title Autenticacao via QR Code Especifico de Sessao

actor "Utilizador" as User
participant "Browser\n(Frontend)" as Browser
participant "App Mobile\n(Autorizada)" as App
participant "BFF" as BFF
participant "Backend\nAPI" as API
database "Cache\n(Redis)" as Cache

== Fase 1: Geracao do QR Code ==
User -> Browser : Acede pagina de login
Browser -> BFF : GET /auth/qr-session
BFF -> API : POST /auth/create-pending-session
API -> API : Gera pending_session_id\n(UUID unico)
API --> BFF : {pending_session_id, qr_data, expires_in: 120}
BFF -> Cache : Armazena pending_session\n(status: PENDING)
BFF --> Browser : {qr_image, pending_session_id}
Browser -> Browser : Exibe QR Code dinamico
Browser -> BFF : WebSocket /auth/session-status\n{pending_session_id}
note right of Browser
Browser fica a escutar
por atualizacoes via
WebSocket ou polling
end note

== Fase 2: Scan e Autorizacao na App ==
User -> App : Scan QR Code
App -> App : Extrai pending_session_id\ndo QR Code
App -> App : Solicita biometria/PIN
User -> App : Confirma biometria
App -> API : POST /auth/authorize-session\n{pending_session_id, device_id, biometric_token}
API -> API : Valida dispositivo autorizado
API -> API : Valida pending_session existe\ne nao expirou
API -> API : Gera apiToken
API -> API : Marca sessao como AUTHORIZED
API --> App : {status: "authorized"}

== Fase 3: Browser recebe autorizacao ==
API -> BFF : Callback ou evento\n(session authorized)
BFF -> Cache : Atualiza sessao\n(status: AUTHORIZED, tokens)
BFF -> Browser : WebSocket: session_authorized
Browser -> BFF : POST /auth/complete-session\n{pending_session_id}
BFF -> Cache : Recupera tokens reais
BFF -> BFF : Gera session_token (para frontend)
BFF -> Cache : Armazena mapeamento\n(session_token -> tokens reais)
BFF --> Browser : {session_token, user_info}
Browser -> Browser : Armazena session_token
Browser --> User : Login concluido

@enduml
```

### Cenario Alternativo: QR Code Generico

Utilizado quando o QR dinamico nao esta disponivel ou como opcao simplificada.

```plantuml
@startuml
skinparam sequenceMessageAlign center
skinparam responseMessageBelowArrow true

title Autenticacao via QR Code Generico

actor "Utilizador" as User
participant "Browser\n(Frontend)" as Browser
participant "App Mobile\n(Autorizada)" as App
participant "BFF" as BFF
participant "Backend\nAPI" as API
database "Cache\n(Redis)" as Cache

== Fase 1: Inicio no Browser ==
User -> Browser : Acede pagina de login
Browser -> Browser : Exibe QR Code generico\n(URL fixa da App)
note right of Browser
QR Code contem URL para
abrir a App com intent de
autenticacao web
end note

== Fase 2: Scan e Autenticacao na App ==
User -> App : Scan QR Code
App -> App : Abre e solicita\nbiometria/PIN
User -> App : Confirma biometria
App -> API : POST /auth/web-session\n{device_id, biometric_token}
API -> API : Valida dispositivo autorizado
API -> API : Gera session_code (codigo curto)
API --> App : {session_code: "A7X9K2", expires_in: 120}

== Fase 3: Vinculacao Manual ==
App --> User : Exibe codigo: "A7X9K2"
User -> Browser : Introduz codigo manualmente
Browser -> BFF : POST /auth/link-session\n{session_code: "A7X9K2"}
BFF -> API : Valida session_code
API --> BFF : {apiToken, user_info}
BFF -> Cache : Armazena tokens reais\n(key: session_token_id)
BFF -> BFF : Gera session_token (para frontend)
BFF --> Browser : {session_token, user_info}
Browser -> Browser : Armazena session_token
Browser --> User : Login concluido

@enduml
```

### Cenario Fallback: User + Pass + OTP

Mantido para compatibilidade e casos onde o utilizador nao tem a App.

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

### Cenario Fallback: User + Pass + Push App

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
Web --> Utilizador : Aguarda aprovacao na App
API -> App : Push notification
Utilizador -> App : Aprova acesso
App -> API : Confirmacao
API --> BFF : Callback (approved)
BFF -> BFF : Gera session_token
BFF --> Web : {session_token, user_info}
Web --> Utilizador : Acesso concedido
@enduml
```

---

## Estrategia de Tokens

### Arquitectura BFF como Intermediario

O BFF actua como intermediario de seguranca, garantindo que o token real (apiToken) nunca e exposto ao Frontend.

```plantuml
@startuml
skinparam sequenceMessageAlign center

title Gestao de Tokens via BFF

participant "Frontend" as FE
participant "BFF" as BFF
database "Cache\n(Redis)" as Cache
participant "Backend API" as API

== Apos Login Bem-Sucedido ==
BFF -> BFF : Recebe apiToken do Backend
BFF -> BFF : Gera session_token (opaco, UUID)
BFF -> Cache : SET session:{session_token}\n{apiToken, user_id, created_at, ttl}
BFF --> FE : {session_token} (apenas este)

== Requisicoes Subsequentes ==
FE -> BFF : GET /api/accounts\nHeader: X-Session-Token: {session_token}
BFF -> Cache : GET session:{session_token}
Cache --> BFF : {apiToken, ...}
BFF -> BFF : Valida TTL e integridade
BFF -> API : GET /accounts\nHeader: Authorization: OAuth {apiToken}...
API --> BFF : {accounts_data}
BFF --> FE : {accounts_data}

== Renovacao Transparente ==
note over BFF
Se apiToken proximo de expirar,
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

| Token | Localizacao | Proposito | Visibilidade |
|-------|-------------|-----------|--------------|
| session_token | Frontend (cookie/storage) | Identificar sessao no BFF | Frontend |
| apiToken | Cache do BFF | Autenticacao com Backend | Apenas BFF |

### Ciclo de Vida dos Tokens

| Evento | Accao | Responsavel |
|--------|-------|-------------|
| Login bem-sucedido | Criar session_token, armazenar tokens reais | BFF |
| Requisicao | Traduzir session_token para tokens reais | BFF |
| Proximidade de expiracao | Renovar apiToken automaticamente | BFF |
| Logout | Eliminar session_token e tokens do cache | BFF |
| Inatividade (15 min) | Invalidar sessao | BFF |

---

## Protocolo OAuth 1.1

### Tokens Anonimos (Pre-Login)

Utilizados para operacoes antes do login (ex: obter configuracoes).

| Token | Proposito | Armazenamento |
|-------|-----------|---------------|
| access_token_anonimo | Autenticacao inicial | Codigo da App/BFF |
| consumer_key | Identificacao do cliente | Codigo da App/BFF |
| secret_key | Assinatura de requests | Codigo da App/BFF |

### Estrutura do Header OAuth

```
Authorization: OAuth access_token={{access_token}},
                      oauth_consumer_key={{consumer_key}},
                      oauth_timestamp={{timestamp}},
                      oauth_version=1.1,
                      oauth_signature={{signature}},
                      oauth_guid={{GUID}}
```

### Geracao de Assinatura

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

## API Authentication_checkLogin (AUT_004)

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

| Campo | Descricao |
|-------|-----------|
| user | Username encriptado |
| pass | Password encriptada (vazio se biometria) |
| token | Token biometrico (se aplicavel) |
| encrypt | Flag de encriptacao (Y/N) |
| device_id | Identificador do dispositivo |
| app_version | Versao da aplicacao |
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

| Flag | Valor | Accao |
|------|-------|-------|
| mustChangePassword | Y | Forcar alteracao de password |
| needStrongAuthentication | Y | Solicitar OTP, usar otp_id |
| firstLogin | Y | Mostrar wizard de preferencias |

---

## Autenticacao Forte (SCA) - PSD2

### Factores de Autenticacao

| Factor | Tipo | Exemplos |
|--------|------|----------|
| Conhecimento | Algo que sabe | Password, PIN |
| Posse | Algo que tem | Telemovel, App autorizada |
| Inerencia | Algo que e | Biometria (fingerprint, face) |

### Operacoes que Requerem SCA

| Operacao | SCA Obrigatoria | Factores |
|----------|-----------------|----------|
| Login | Sim | 2 factores (QR Code + Biometria) |
| Transferencias | Sim | Confirmacao na App |
| Pagamentos | Sim | Confirmacao na App |
| Alteracao de dados sensiveis | Sim | Confirmacao na App |
| Consultas | Nao | Apos login valido |

---

## Gestao de Sessoes

### Ciclo de Vida

```plantuml
@startuml
[*] --> Anonimo : Inicio
Anonimo --> PendingQR : QR Code gerado
PendingQR --> Autenticado : App autoriza
PendingQR --> Anonimo : QR expira (120s)
Anonimo --> Autenticando : Login tradicional
Autenticando --> Autenticado : Sucesso
Autenticando --> Anonimo : Falha
Autenticado --> Ativo : Primeira requisicao
Ativo --> Ativo : Requisicoes (renova TTL)
Ativo --> Warning : 10 min inatividade
Warning --> Ativo : Utilizador activo
Warning --> Expirado : 5 min adicionais
Expirado --> Anonimo : Sessao terminada
Ativo --> Anonimo : Logout manual
@enduml
```

### Timeouts

| Evento | Tempo | Accao |
|--------|-------|-------|
| QR Code expiracao | 120 seg | Gerar novo QR |
| Inatividade warning | 10 min | Notificar utilizador |
| Inatividade logout | 15 min | Terminar sessao |
| Token expiration | Configuravel | BFF renova automaticamente |

### Sessoes Multiplas

- **Permitido:** Um utilizador pode ter multiplas sessoes simultaneas
- **Justificativa:** Browser e App coexistem naturalmente (App necessaria para autorizar Browser)
- **Rastreabilidade:** Cada sessao tem session_token unico, permitindo auditoria

---

## Anti-Automacao e Seguranca

### Mecanismos Implementados

| Mecanismo | Descricao | Responsavel |
|-----------|-----------|-------------|
| QR Code + Dispositivo autorizado | Requer App previamente vinculada | Backend |
| Biometria | Confirma identidade do utilizador | App Mobile |
| Rate Limiting | Limita tentativas por IP/utilizador | **Gateway** |
| Device fingerprint | Identifica dispositivos suspeitos | Backend |

### Dispensa de CAPTCHA

O fluxo via QR Code dispensa CAPTCHA porque:
1. Requer dispositivo fisico (App instalada)
2. Requer dispositivo previamente autorizado pelo cliente
3. Requer autenticacao biometrica na App
4. QR Code expira em 120 segundos

---

## Dependencias

| Componente | Responsabilidade | Status |
|------------|------------------|--------|
| App Mobile | Scan QR, biometria, autorizacao | Existente |
| Backend API | Gestao de tokens, validacao | Existente |
| BFF | Intermediario de tokens, session_token | A implementar |
| Cache (Redis) | Armazenamento de sessoes/tokens | A implementar |
| Gateway | Rate Limiting, WAF | **Dependencia externa** |
| WebSocket Server | Notificacao de sessao autorizada | A implementar |

---

## Questoes Pendentes de Confirmacao

### Q-07-001: Momento de Retorno do apiToken

> **Status:** Aguarda confirmacao do analista
> **Origem:** Conflito entre DEF-GEN-other-auth-flow.md e fluxos existentes

**Contexto:**
Existe divergencia entre documentos sobre quando o `apiToken` e retornado:

| Interpretacao | Descricao |
|---------------|-----------|
| A | apiToken retornado **antes** do OTP, OTP valida via API "secure" separada |
| B | apiToken retornado **apos** validacao do OTP |

**Evidencia do novo documento (DEF-GEN-other-auth-flow.md):**
```
BFF-->ApiBBest: Authentication_checkLogin
BFF<--ApiBBest: "apiToken":"914e55d8ea3b4e19b1aa63c9efbad2ba", ...
BFF-->SPA: Pede OTP
SPA-->BFF: Envia OTP
BFF-->ApiBBest: Chamar API de secure
```

**Questao para o analista:**
- O `apiToken` e retornado imediatamente no `Authentication_checkLogin`, mesmo quando `needStrongAuthentication=Y`?
- Ou o `apiToken` so e disponibilizado apos a validacao do OTP na API "secure"?

---

## Responsabilidades Geridas pelo Siebel

As seguintes funcionalidades são geridas inteiramente pelo Siebel (backend), não sendo responsabilidade do novo WebSite:

| Funcionalidade | Responsavel | Notas |
|----------------|-------------|-------|
| Recuperação de acesso (password esquecida) | Siebel | Fluxo igual à APP Mobile |
| RBAC (Autorização por perfil) | Siebel | Perfis e permissões definidos no backend |
| Políticas de Password (complexidade, expiração) | Siebel | Regras centralizadas no backend |

---

## Itens Pendentes

| Topico | Estado | Prioridade |
|--------|--------|------------|
| **Q-07-001: Momento do apiToken** | Aguarda confirmacao | **Alta** |
| Procedimento de revogacao de tokens | A definir | Media |

---

## Decisoes Relacionadas

- [DEC-001-estrategia-autenticacao-web.md](../decisions/DEC-001-estrategia-autenticacao-web.md) - Estrategia de autenticacao
- [DEC-002-gestao-sessoes-tokens.md](../decisions/DEC-002-gestao-sessoes-tokens.md) - Gestao de sessoes e tokens

## Referencias

- [SEC-07-autenticacao-autorizacao.md](../sections/SEC-07-autenticacao-autorizacao.md)
- [DEF-09-fluxo-transferencia.md](DEF-09-fluxo-transferencia.md)
- [DEF-02-restricoes.md](DEF-02-restricoes.md) - RST-CMP-001 (Autenticacao vinculada)
- PSD2 RTS on Strong Customer Authentication
