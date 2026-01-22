---
aliases:
  - Autenticação e Autorização
tags:
  - nextreality-novobanco-website-sections
  - sections
  - authentication
  - authorization
  - security
approved: true
created: 2026-01-03
hubs:
  - "[[nextreality]]"
para-code: R
reviewed: true
status: in-progress
---

# 7. Autenticação & Autorização

## Definições e Decisões

> **Definições requeridas:**
> - [DEF-07-autenticacao-autorizacao.md](../definitions/DEF-07-autenticacao-autorizacao.md) - Status: completed
> - [DEF-05-arquitetura-bff.md](../definitions/DEF-05-arquitetura-bff.md) - Status: completed
>
> **Decisões relacionadas:**
> - [DEC-001-estrategia-autenticacao-web.md](../decisions/DEC-001-estrategia-autenticacao-web.md) - Status: accepted
> - [DEC-002-gestao-sessoes-tokens.md](../decisions/DEC-002-gestao-sessoes-tokens.md) - Status: accepted
> - [DEC-003-modelo-autorizacao-abac.md](../decisions/DEC-003-modelo-autorizacao-abac.md) - Status: accepted

## Propósito

Definir a estratégia completa de autenticação e autorização do HomeBanking Web, incluindo fluxos de autenticação, MFA/SCA, gestão de sessões, tokens e políticas de segurança.

## Conteúdo

### 7.1 Visão Geral de Autenticação

> **Pendência:** Esta secção necessita de validação mais detalhada com equipa de autenticação do NovoBanco.

```plantuml
@startuml
skinparam backgroundColor #FEFEFE

title Métodos de Autenticação - HomeBanking Web

rectangle "Métodos de Autenticação" {
    rectangle "Fluxo Primário" #LightGreen {
        [QR Code + Biometria App]
        note bottom : Scan QR Code\nValidação biométrica na app\nVinculação de sessão
    }

    rectangle "Fluxo Fallback" #Yellow {
        [Username/Password + 2FA]
        note bottom : Credenciais\n+ SMS OTP ou App Push
    }

    rectangle "Não Suportado" #LightCoral {
        [Certificado Digital]
    }
}

@enduml
```

| Método | Suporte | Observação |
|--------|---------|------------|
| QR Code + Biometria | Primário | Validação via app mobile |
| Username/Password | Fallback | Apenas quando QR Code falha |
| SMS OTP | Fallback | Segundo fator no fallback |
| App Push | Fallback | Segundo fator no fallback |
| Certificado Digital | Não | Não suportado |

**Login unificado:** Sim, mesmas credenciais da app mobile.

**Registo:** O utilizador pode registar-se pela Web ou pela APP. São processos semelhantes mas necessários em cada dispositivo (independentes). A validação de identidade no primeiro acesso utiliza a mesma API de Login.

### 7.2 Fluxos de Autenticação

#### 7.2.1 Fluxo Primário - QR Code

```plantuml
@startuml
skinparam backgroundColor #FEFEFE

actor "Utilizador" as USER
participant "Browser" as FE
participant "BFF" as BFF
participant "Auth Service" as AUTH
participant "App Mobile" as APP

USER -> FE : Acede ao HomeBanking
FE -> BFF : Solicita QR Code
BFF -> AUTH : Gera QR Code + Session Token
AUTH --> BFF : QR Code data
BFF --> FE : Apresenta QR Code

USER -> APP : Abre app mobile
USER -> APP : Escaneia QR Code
APP -> APP : Solicita biometria
USER -> APP : Confirma biometria
APP -> AUTH : Valida + vincula sessão
AUTH --> APP : Sessão aprovada

AUTH --> BFF : Notifica aprovação
BFF -> BFF : Cria sessão web
BFF --> FE : Set-Cookie: SessionID\n(HttpOnly, Secure, SameSite=Strict)
FE --> USER : Acesso concedido

@enduml
```

> **Nota - Arquitectura Completa:** Os diagramas de autenticação acima estão simplificados para focar no fluxo de autenticação do utilizador. Para a arquitectura completa incluindo API Gateway (IBM) e validação de token pelo Siebel, consultar [SEC-03 3.2 - Diagrama Conceptual](SEC-03-visao-geral-solucao.md#32-diagrama-conceptual) e [SEC-05 5.4 - Comunicação entre Serviços](SEC-05-arquitetura-backend-servicos.md#54-comunicacao-entre-servicos).

#### 7.2.2 Fluxo Fallback - Username/Password + 2FA

```plantuml
@startuml
skinparam backgroundColor #FEFEFE

actor "Utilizador" as USER
participant "Browser" as FE
participant "BFF" as BFF
participant "Auth Service" as AUTH

USER -> FE : Indica falha no QR Code
FE --> USER : Apresenta opções fallback

USER -> FE : Insere Username/Password
FE -> BFF : POST /auth/login (credentials)
BFF -> AUTH : Valida credenciais
AUTH --> BFF : Requer 2FA

alt SMS OTP
    BFF -> AUTH : Solicita envio OTP
    AUTH --> USER : SMS com código
    USER -> FE : Insere código OTP
    FE -> BFF : POST /auth/verify-otp
else App Push
    BFF -> AUTH : Solicita push notification
    AUTH -> APP : Envia push
    USER -> APP : Aprova notificação
end

AUTH --> BFF : 2FA validado
BFF -> BFF : Cria sessão web
BFF --> FE : Set-Cookie: SessionID
FE --> USER : Acesso concedido

@enduml
```

#### 7.2.3 Detalhes Técnicos do Fluxo Fallback (BFF ↔ ApiPsd2)

O fluxo fallback utiliza a ApiPsd2 para autenticação. O BFF encapsula toda a complexidade:

```plantuml
@startuml
skinparam backgroundColor #FEFEFE

actor "Utilizador" as USER
participant "Browser" as FE
participant "BFF" as BFF
database "Redis" as REDIS
participant "ApiPsd2" as API

USER -> FE : Insere Username/Password
FE -> BFF : POST /auth/login\nx-nb-channel: best.spa

note over BFF
  Gera: GUID, timestamp
  Calcula: assinatura SHA256
  Token: access_token_anonimo
end note

BFF -> API : AUT_004 (Authentication_checkLogin)\nOAuth Authorization header\n{user, pass, encrypt, device_id, app_version, so_id}

API --> BFF : returnCode: "0"\napiToken, mustChangePassword,\nneedStrongAuthentication, firstLogin

alt needStrongAuthentication == "Y"
    BFF -> API : AUT_001 (ReenviaOTP)
    API --> BFF : authentication, auth_seq, object_id
    BFF --> FE : Requer OTP
    USER -> FE : Insere código OTP
    FE -> BFF : POST /auth/verify-otp
    BFF -> API : DEV_005.2 (RegistarDispositivoSecure)\n{object_id, auth_type, auth_value}
    API --> BFF : Sucesso
end

BFF -> BFF : Gera token_sessao_spa (GUID)
BFF -> REDIS : SET token_sessao_spa\n{apiToken, user_context, ...}
BFF --> FE : Set-Cookie: token_sessao_spa\n(HttpOnly, Secure, SameSite=Strict)\n{mustChangePassword, firstLogin}

@enduml
```

**Códigos de Operação ApiPsd2:**

| Código | Operação | Descrição |
|--------|----------|-----------|
| AUT_004 | Authentication_checkLogin | Validação de credenciais |
| AUT_001 | ReenviaOTP | Solicita envio de OTP |
| DEV_005.2 | RegistarDispositivoSecure | Valida OTP e regista dispositivo |
| CLI_005 | ConsultaCliente | Consulta dados do cliente (pós-login) |

#### 7.2.4 Segurança na Transmissão de Credenciais

> **Nota Importante:** O ambiente web requer atenção especial na transmissão e gestão de credenciais. Ver [Secção 8.3.6](SEC-08-seguranca-conformidade.md#836-considerações-de-segurança-web-vs-mobile) para diferenças de segurança web vs mobile.

##### Transmissão de Credenciais

| Aspeto | Especificação | Observação |
|--------|---------------|------------|
| **Canal** | HTTPS (TLS 1.2+) | Obrigatório |
| **PIN/Password** | Transmitido em payload JSON | Protegido por TLS |
| **Cifra adicional** | **A avaliar** | Avaliar necessidade de cifrar PIN antes de TLS |
| **Método HTTP** | POST | Nunca em query string |

##### Dados Retornados no Login

| Dado | Destino | Formato | Observação |
|------|---------|---------|------------|
| **Session ID** | Cookie no browser | HttpOnly, Secure, SameSite=Strict | Único identificador exposto ao browser |
| **Access Token** | Cache do BFF | Nunca enviado ao browser | Isolado pelo padrão BFF |
| **Refresh Token** | Cache do BFF | Nunca enviado ao browser | Isolado pelo padrão BFF |
| **Dados do utilizador** | Response JSON | Apenas dados não sensíveis | Nome, segmento, etc. |

> **Pendência de Revisão:** Identificar exatamente quais dados são retornados pela API de login da app mobile e avaliar se todos são seguros para exposição no ambiente web. Ver comentário JGC #10.

##### Cookies de Sessão

| Atributo | Valor | Justificação |
|----------|-------|--------------|
| **HttpOnly** | `true` | Previne acesso via JavaScript (proteção XSS) |
| **Secure** | `true` | Apenas transmitido via HTTPS |
| **SameSite** | `Strict` | Previne CSRF |
| **Path** | `/` | Aplicação inteira |
| **Domain** | Domínio da aplicação | Sem subdomínios wildcard |
| **Max-Age** | Sessão ou timeout | Conforme política de sessão |

##### Pendências de Segurança de Credenciais

| Item | Descrição | Prioridade |
|------|-----------|------------|
| **Revisão de dados no login** | Identificar todos os dados retornados no login e avaliar risco em ambiente web | **Alta** |
| **Cifra de PIN** | Avaliar se PIN deve ser cifrado client-side antes de transmissão (além de TLS) | Alta |
| **Credenciais do banco** | Avaliar risco de exposição de credenciais de acesso a sistemas backend | Alta |

### 7.3 MFA/SCA (Strong Customer Authentication)

| Aspeto | Decisão |
|---------|---------|
| **SCA Obrigatório** | Sim, para todos os acessos a áreas restritas |
| **Segundo fator primário** | Biometria via app (validação QR Code) |
| **Segundo fator fallback** | SMS OTP ou App Push |
| **Isenções SCA** | Nenhuma |

**Fluxo de fallback:** Após o utilizador informar falha na leitura do QR Code, a aplicação permite login com SMS OTP ou App Push. A disponibilidade dos métodos é **uniforme** para todos os utilizadores (não configurável por utilizador) e **sem prioridade** entre os métodos.

#### 7.3.1 SCA Condicional

A ApiPsd2 retorna a flag `needStrongAuthentication` que indica se SCA é requerido:

| Valor | Significado | Ação |
|-------|-------------|------|
| "Y" | SCA obrigatório | Prosseguir com OTP |
| "N" | SCA não requerido | Login completo |

> **Pendência:** Clarificar com o cliente em que cenários `needStrongAuthentication` retorna "N". Ver PENDENCIAS.md.

### 7.4 Gestão de Sessões

```plantuml
@startuml
skinparam backgroundColor #FEFEFE

title Ciclo de Vida da Sessão

[*] --> Ativa : Login bem-sucedido

Ativa --> Ativa : Atividade do utilizador\n(reset timeout inatividade)
Ativa --> Aviso : 9 min inatividade
Aviso --> Ativa : Utilizador interage
Aviso --> Expirada : 10 min inatividade
Ativa --> Expirada : 30 min absolutos
Ativa --> Terminada : Logout manual
Expirada --> [*]
Terminada --> [*]

note right of Aviso
    Popup com temporizador
    Avisa utilizador
end note

@enduml
```

| Parâmetro | Valor | Observação |
|-----------|-------|------------|
| **Timeout por inatividade** | 10 minutos (sugestão) | Configurável |
| **Timeout absoluto** | 30 minutos (sugestão) | Configurável |
| **Sessão exclusiva** | Recomendado | Novo login invalida sessão anterior |
| **Aviso de expiração** | Popup com temporizador | - |
| **Relação sessão web/mobile** | **Independentes** | Não há relação entre sessões |
| **Limite de sessões** | _A definir_ | - |

> **Nota:** Os tempos de sessão são sugestões e devem ser configuráveis. O valor final será definido em conjunto com o cliente.

### 7.5 Estratégia de Tokens

```plantuml
@startuml
skinparam backgroundColor #FEFEFE

title Arquitetura de Tokens - Dois Níveis

package "Browser" {
    [Session Cookie] as SC
    note bottom of SC
        HttpOnly, Secure
        SameSite=Strict
    end note
}

package "BFF Cache" {
    [Access Token] as AT
    [Refresh Token] as RT
    note bottom of AT : TTL: 15 min
    note bottom of RT : TTL: 7 dias
}

package "Backend Services" {
    [OAuth Server] as OAUTH
}

[Browser] --> [BFF] : Session Cookie
[BFF] --> AT : Lookup
[BFF] --> RT : Refresh silencioso
[BFF] --> OAUTH : Bearer Token

@enduml
```

| Token | Localização | TTL | Uso |
|-------|-------------|-----|-----|
| **Session Cookie** | Browser (cookie) | 30 min | Browser -> BFF |
| **Access Token** | BFF Cache | 15 min | BFF -> Backend |
| **Refresh Token** | BFF Cache | 7 dias | Renovação silenciosa |

**Renovação:** Refresh silencioso conforme atividade do utilizador. BFF renova tokens automaticamente antes de expiração.

### 7.6 Autorização

| Aspeto | Decisão |
|---------|---------|
| **Modelo** | ABAC híbrido com RBAC |
| **Responsabilidade** | Backend Services (Siebel) |
| **Role** | Atributo do sujeito (quando necessário) |
| **Atributos** | Sujeito, Recurso, Ação, Ambiente |
| **Permissões por operação** | Sim (consulta vs transação) |

> **Nota - Responsabilidade:** A validação de autorização (ABAC/RBAC) é responsabilidade dos Backend Services (Siebel). O BFF propaga os tokens e não implementa lógica de autorização própria.

**Atributos considerados:**

| Categoria | Atributos |
|-----------|-----------|
| **Sujeito** | Utilizador, role, tipo de cliente, segmento |
| **Recurso** | Tipo de conta, produto, limite |
| **Ação** | Consulta, transação, configuração |
| **Ambiente** | Canal (web), horário, localização, dispositivo |

**Nota:** Roles e perfis específicos serão definidos no assessment inicial do projeto.

### 7.7 Políticas de Password

> **Nota do Cliente:** Todo o processo de políticas de password é gerido pela API. O frontend apenas apresenta os formulários; a validação e lógica são responsabilidade do backend.

| Aspeto | Decisão |
|---------|---------|
| Requisitos mínimos | **Gerido pela API** |
| Expiração | **Gerido pela API** |
| Recuperação | **Gerido pela API** |
| Bloqueio por tentativas | **Gerido pela API** |

### 7.8 Anti-automation

| Aspeto | Status |
|---------|--------|
| CAPTCHA | _A definir_ |
| Rate limiting login | _A definir_ |
| Deteção de bots | _A definir_ |

### 7.9 Revogação

| Aspeto | Status |
|---------|--------|
| Revogação por comprometimento | _A definir_ |
| Logout de todos os dispositivos | _A definir_ |
| Revogação ao mudar password | _A definir_ |

## Entregáveis

- [x] Diagramas de fluxo de autenticação
- [x] Especificação de MFA/SCA
- [x] Política de gestão de sessões
- [x] Estratégia de tokens documentada
- [x] Modelo de autorização
- [ ] Políticas de password - Parcial
- [ ] Controlos anti-automation - Pendente
- [ ] Procedimentos de revogação - Pendente

## Definições Utilizadas

- [x] [DEF-07-autenticacao-autorizacao.md](../definitions/DEF-07-autenticacao-autorizacao.md) - Status: completed
- [x] [DEF-05-arquitetura-bff.md](../definitions/DEF-05-arquitetura-bff.md) - Status: completed

## Decisões Referenciadas

- [x] [DEC-001-estrategia-autenticacao-web.md](../decisions/DEC-001-estrategia-autenticacao-web.md) - Status: accepted
- [x] [DEC-002-gestao-sessoes-tokens.md](../decisions/DEC-002-gestao-sessoes-tokens.md) - Status: accepted
- [x] [DEC-003-modelo-autorizacao-abac.md](../decisions/DEC-003-modelo-autorizacao-abac.md) - Status: accepted

## Itens Pendentes

| Item | Documento | Responsável | Status |
|------|-----------|-------------|--------|
| ~~Fluxo de primeiro acesso/registo web~~ | ~~DEF-07~~ | ~~Arquitetura~~ | **Decidido: Web ou APP independentes** |
| ~~Validação fluxos fallback (SMS/Push)~~ | ~~DEF-07~~ | ~~Produto~~ | **Decidido: Uniforme, sem prioridade** |
| ~~Sessão web/mobile~~ | ~~DEF-07~~ | ~~Produto~~ | **Decidido: Independentes** |
| ~~Políticas de password~~ | ~~DEF-07~~ | ~~Segurança~~ | **Decidido: Gerido pela API** |
| **Revisão dados retornados no login** | SEC-07 / SEC-08 | Segurança + Arquitetura | **Pendente - Alta prioridade** |
| **Cifra de PIN (além de TLS)** | SEC-07 / SEC-08 | Segurança | **Pendente - Alta prioridade** |
| **Credenciais do banco em ambiente web** | SEC-07 / SEC-08 | Segurança | **Pendente - Alta prioridade** |
| Sessão exclusiva (aprovação cliente) | DEF-07-autenticacao-autorizacao | Produto | Pendente |
| Limite de sessões ativas | DEF-07-autenticacao-autorizacao | Segurança | Pendente |
| Logout automático outras sessões | DEF-07-autenticacao-autorizacao | Segurança | Pendente |
| Estratégia CAPTCHA | DEF-07-autenticacao-autorizacao | Segurança | Pendente |
| Rate limiting login | DEF-07-autenticacao-autorizacao | Arquitetura | Pendente |
| Deteção de bots | DEF-07-autenticacao-autorizacao | Segurança | Pendente |
| Logout de todos dispositivos | DEF-07-autenticacao-autorizacao | Segurança | Pendente |
| Revogação de tokens | DEF-07-autenticacao-autorizacao | Segurança | Pendente |
