---
id: SEC-07-autenticacao-autorizacao
aliases:
  - Novo Banco Autenticacao Autorizacao
tags:
  - nextreality-novobanco-website-sections
approved: true
created: 2025-12-22
hubs:
  - "[[nextreality]]"
para-code: R
reviewed: true
---
# 07. Autenticacao & Autorizacao

> **Status:** em-progresso
> **Definicoes utilizadas:** DEF-07-autenticacao-oauth.md
> **Ultima atualizacao:** 2025-12-22

## Proposito

Definir os mecanismos de autenticacao, autorizacao, gestao de sessoes e estrategias de seguranca da plataforma de Homebanking do Novo Banco.

---

## 7.1 Visao Geral

A autenticacao na plataforma segue o modelo de **Strong Customer Authentication (SCA)** exigido pela PSD2, utilizando dois ou mais factores de autenticacao. O fluxo principal utiliza a App Mobile autorizada como dispositivo de confianca para validacao biometrica.

### Principios de Seguranca

| Principio | Implementacao |
|-----------|---------------|
| Defense in depth | Multiplas camadas (Gateway, BFF, Backend) |
| Zero trust | Tokens opacos no frontend, validacao em cada camada |
| Least privilege | Sessoes com scope limitado |
| Fail secure | Fallback para fluxos mais restritivos |

---

## 7.2 Fluxos de Autenticacao

### Cenarios Suportados

| Cenario | Descricao | Recomendacao |
|---------|-----------|--------------|
| **QR Code Especifico** | QR dinamico por sessao, vinculacao automatica via WebSocket | **Principal** |
| QR Code Generico | QR fixo, codigo manual introduzido pelo utilizador | Alternativo |
| User + Pass + OTP SMS | Login tradicional com OTP via SMS | Fallback legacy |
| User + Pass + Push App | Login tradicional com aprovacao na App | Fallback |

### Fluxo Principal: QR Code Especifico de Sessao

Este fluxo oferece a melhor experiencia de utilizador mantendo elevados padroes de seguranca.

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

== Fase 2: Scan e Autorizacao na App ==
User -> App : Scan QR Code
App -> App : Extrai pending_session_id
App -> App : Solicita biometria/PIN
User -> App : Confirma biometria
App -> API : POST /auth/authorize-session\n{pending_session_id, device_id, biometric_token}
API -> API : Valida dispositivo autorizado
API -> API : Gera tokens (apiToken, sasToken)
API --> App : {status: "authorized"}

== Fase 3: Browser recebe autorizacao ==
API -> BFF : Callback (session authorized)
BFF -> Cache : Atualiza sessao (AUTHORIZED)
BFF -> Browser : WebSocket: session_authorized
Browser -> BFF : POST /auth/complete-session
BFF -> BFF : Gera session_token
BFF -> Cache : Armazena mapeamento
BFF --> Browser : {session_token, user_info}
Browser --> User : Login concluido

@enduml
```

### Fluxo Alternativo: QR Code Generico

```plantuml
@startuml
skinparam sequenceMessageAlign center

title Autenticacao via QR Code Generico

actor "Utilizador" as User
participant "Browser" as Browser
participant "App Mobile" as App
participant "BFF" as BFF
participant "Backend API" as API

User -> Browser : Acede pagina de login
Browser -> Browser : Exibe QR Code generico
User -> App : Scan QR Code
App -> App : Solicita biometria
User -> App : Confirma biometria
App -> API : POST /auth/web-session
API --> App : {session_code: "A7X9K2"}
App --> User : Exibe codigo
User -> Browser : Introduz codigo
Browser -> BFF : POST /auth/link-session
BFF -> API : Valida session_code
API --> BFF : {apiToken, sasToken}
BFF -> BFF : Gera session_token
BFF --> Browser : {session_token}
Browser --> User : Login concluido

@enduml
```

---

## 7.3 Estrategia de Tokens

### Arquitectura BFF como Intermediario

O BFF actua como camada de seguranca, garantindo que os tokens reais nunca sao expostos ao Frontend.

```plantuml
@startuml
skinparam sequenceMessageAlign center

title Gestao de Tokens via BFF

participant "Frontend" as FE
participant "BFF" as BFF
database "Cache\n(Redis)" as Cache
participant "Backend API" as API

== Apos Login ==
BFF -> BFF : Recebe apiToken, sasToken
BFF -> BFF : Gera session_token (opaco)
BFF -> Cache : Armazena tokens reais
BFF --> FE : {session_token}

== Requisicoes ==
FE -> BFF : Request + session_token
BFF -> Cache : Recupera tokens reais
BFF -> API : Request + apiToken
API --> BFF : Response
BFF --> FE : Response

== Logout ==
FE -> BFF : POST /auth/logout
BFF -> Cache : Remove sessao
BFF --> FE : {logged_out}

@enduml
```

### Tipos de Tokens

| Token | Localizacao | Proposito | Visibilidade |
|-------|-------------|-----------|--------------|
| session_token | Frontend | Identificar sessao no BFF | Frontend |
| apiToken | Cache BFF | Autenticacao com Backend | Apenas BFF |
| sasToken | Cache BFF | Acesso ao cofre de chaves | Apenas BFF |

### Ciclo de Vida

| Evento | Accao | Responsavel |
|--------|-------|-------------|
| Login bem-sucedido | Criar session_token, armazenar tokens reais | BFF |
| Requisicao | Traduzir session_token para tokens reais | BFF |
| Proximidade de expiracao | Renovar apiToken automaticamente | BFF |
| Logout | Eliminar session_token e tokens do cache | BFF |
| Inatividade (15 min) | Invalidar sessao | BFF |

---

## 7.4 Autenticacao Forte (SCA) - PSD2

### Factores de Autenticacao

| Factor | Tipo | Implementacao |
|--------|------|---------------|
| Conhecimento | Algo que sabe | Password, PIN |
| Posse | Algo que tem | App Mobile autorizada |
| Inerencia | Algo que e | Biometria (fingerprint, face) |

### Operacoes que Requerem SCA

| Operacao | SCA | Metodo |
|----------|-----|--------|
| Login | Sim | QR Code + Biometria |
| Transferencias | Sim | Confirmacao na App |
| Pagamentos | Sim | Confirmacao na App |
| Alteracao de dados sensiveis | Sim | Confirmacao na App |
| Consultas | Nao | Sessao activa valida |

---

## 7.5 Gestao de Sessoes

### Estados da Sessao

```plantuml
@startuml
[*] --> Anonimo : Inicio
Anonimo --> PendingQR : QR Code gerado
PendingQR --> Autenticado : App autoriza
PendingQR --> Anonimo : QR expira (120s)
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

### Sessoes Multiplas

- **Politica:** Permitidas
- **Justificativa:** Browser e App coexistem (App necessaria para autorizar Browser)
- **Rastreabilidade:** Cada sessao tem session_token unico

---

## 7.6 MFA (Multi-Factor Authentication)

### Metodos Suportados

| Metodo | Descricao | Uso |
|--------|-----------|-----|
| Biometria na App | Fingerprint ou Face ID | **Principal** |
| PIN na App | Codigo numerico de 6 digitos | Fallback |
| OTP SMS | Codigo enviado por SMS | Legacy |
| Push Notification | Aprovacao na App | Alternativo |

### Fluxo de Step-up Authentication

Para operacoes sensiveis (transferencias, pagamentos), e solicitada confirmacao adicional na App.

```plantuml
@startuml
actor Utilizador
participant Browser
participant BFF
participant "Backend API" as API
participant "App Mobile" as App

Utilizador -> Browser : Solicita transferencia
Browser -> BFF : POST /transfers\n{session_token, dados}
BFF -> API : POST /transfers\n{apiToken, dados}
API --> BFF : {requires_sca: true, operation_id}
BFF --> Browser : {pending_approval, operation_id}
Browser --> Utilizador : Aguarde aprovacao na App
API -> App : Push notification
Utilizador -> App : Confirma com biometria
App -> API : POST /confirm\n{operation_id, biometric}
API --> BFF : Callback (approved)
BFF -> API : Executa transferencia
API --> BFF : {success}
BFF --> Browser : {transfer_completed}
Browser --> Utilizador : Transferencia concluida

@enduml
```

---

## 7.7 Autorizacao (RBAC)

> **Status:** A definir

### Estrutura Prevista

| Componente | Descricao |
|------------|-----------|
| Perfis | Tipos de utilizador (Particular, Empresa, etc.) |
| Permissoes | Accoes permitidas por recurso |
| Recursos | Contas, Transferencias, Pagamentos, etc. |

### Questoes Pendentes

- Quais perfis de utilizador existem?
- Ha niveis de permissao diferentes por tipo de conta?
- Existe delegacao de poderes (procuradores)?

---

## 7.8 Anti-Automacao

### Mecanismos Implementados

| Mecanismo | Descricao | Responsavel |
|-----------|-----------|-------------|
| QR Code + Dispositivo autorizado | Requer App previamente vinculada | Backend |
| Biometria | Confirma identidade fisica | App Mobile |
| Rate Limiting | Limita tentativas por IP/utilizador | Gateway |
| Device fingerprint | Identifica dispositivos suspeitos | Backend |

### Dispensa de CAPTCHA

O fluxo via QR Code dispensa CAPTCHA porque:
1. Requer dispositivo fisico (App instalada)
2. Requer dispositivo previamente autorizado pelo cliente
3. Requer autenticacao biometrica na App
4. QR Code expira em 120 segundos

---

## 7.9 Revogacao

> **Status:** A definir

### Cenarios de Revogacao

| Cenario | Accao Esperada |
|---------|----------------|
| Logout voluntario | Invalidar session_token e tokens no cache |
| Suspeita de comprometimento | Invalidar todas as sessoes do utilizador |
| Alteracao de password | Invalidar todas as sessoes |
| Dispositivo removido | Invalidar sessoes desse dispositivo |

---

## 7.10 Politicas de Password

> **Status:** A definir

### Requisitos Previstos

| Aspecto | Requisito |
|---------|-----------|
| Comprimento minimo | A definir |
| Complexidade | A definir |
| Expiracao | A definir |
| Historico | A definir |
| Bloqueio por tentativas | A definir |

---

## Diagramas

### Diagrama de Componentes - Autenticacao

```plantuml
@startuml
skinparam componentStyle rectangle

package "Frontend" {
    [SPA React] as SPA
}

package "BFF Layer" {
    [Auth Controller] as AuthCtrl
    [Token Manager] as TokenMgr
    [WebSocket Handler] as WSHandler
}

package "Infrastructure" {
    database "Redis Cache" as Redis
    [API Gateway] as Gateway
}

package "Backend" {
    [Auth API] as AuthAPI
    [OTP Service] as OTPSvc
}

package "Mobile" {
    [App Mobile] as App
}

SPA --> Gateway : HTTPS
Gateway --> AuthCtrl : Rate Limited
AuthCtrl --> TokenMgr
TokenMgr --> Redis
AuthCtrl --> AuthAPI
AuthAPI --> OTPSvc
App --> AuthAPI : Biometria
WSHandler --> SPA : Session Status

@enduml
```

---

## Entregaveis

- [x] Diagrama de sequencia: Fluxo de autenticacao QR Code Especifico
- [x] Diagrama de sequencia: Fluxo de autenticacao QR Code Generico
- [x] Diagrama de sequencia: Gestao de tokens via BFF
- [x] Diagrama de sequencia: Step-up authentication
- [x] Diagrama de estados: Ciclo de vida da sessao
- [x] Politica de gestao de sessoes (timeouts, concorrencia)
- [ ] Matriz RBAC (roles, permissions, resources) - **A definir**
- [ ] Password policy document - **A definir**
- [ ] Procedimentos de revogacao e logout - **A definir**
- [x] Estrategia anti-bot (dispensa CAPTCHA justificada)
- [x] Configuracao de rate limiting (delegado ao Gateway)

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

## Definicoes Utilizadas

- [x] [DEF-07-autenticacao-oauth.md](../definitions/DEF-07-autenticacao-oauth.md) - Status: em-progresso

---

## Navegacao

| Anterior | Proximo |
|----------|---------|
| [06. Arquitetura de Dados](SEC-06-arquitetura-dados.md) | [08. Seguranca & Conformidade](SEC-08-seguranca-conformidade.md) |
