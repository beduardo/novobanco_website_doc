# Análise Comparativa: Diagrama de Sequência do Cliente vs HLD

> **Data:** 2026-01-21
> **Documento Analisado:** `LOGIN_TRANSFERENCIA_WEB.txt`
> **Objetivo:** Avaliar diferenças entre o diagrama de sequência do cliente e as definições actuais do HLD

---

## 1. Resumo Executivo

O diagrama de sequência do cliente fornece **detalhes de implementação específicos** que complementam o HLD, mas também revela **diferenças arquiteturais importantes** que necessitam de alinhamento. Existem pontos de convergência e divergência que devem ser discutidos com o cliente.

### Veredicto Geral

| Área | Status | Ação Necessária |
|------|--------|-----------------|
| Arquitectura BFF | Parcialmente alinhado | Clarificar nomenclatura de componentes |
| Fluxo de Autenticação | **Divergente** | Alinhar com cliente sobre método primário |
| Protocolo OAuth | **Divergente** | Clarificar versão OAuth (1.1 vs 2.0) |
| Gestão de Cache | Complementar | Incorporar no HLD |
| Integrações API | Complementar | Incorporar detalhes no HLD |
| Transferências | Complementar | Incorporar regras de negócio no HLD |
| Segurança | Alinhado | Pendências já identificadas |

---

## 2. Análise por Área

### 2.1 Arquitectura - Diagrama Conceptual (SEC-03, 3.2)

#### O que o HLD define:

```
SPA React → BFF (.NET 8) → API Gateway (IBM) → Siebel/Backend Services → Core Banking
```

#### O que o diagrama do cliente mostra:

```
SPA → BFF → ApiBBest (directo) → ...
SPA → BFF → API Backoffice → ...
```

#### Diferenças Identificadas:

| Aspecto | HLD | Cliente | Impacto |
|---------|-----|---------|---------|
| **API Gateway** | IBM (explícito) | Não mencionado | **Médio** - Verificar se existe ou se BFF comunica directo |
| **Backend Principal** | Siebel | ApiBBest | **Baixo** - Pode ser nomenclatura diferente |
| **Arquitectura** | BFF → Gateway → Backend | BFF → ApiBBest (directo) | **Alto** - Precisa clarificação |

#### Acção Requerida:
- [ ] Clarificar com cliente se "ApiBBest" é o mesmo que o backend Siebel ou se é outro componente
- [ ] Confirmar se existe API Gateway entre BFF e ApiBBest ou se a comunicação é directa
- [ ] Actualizar diagrama 3.2 se necessário

---

### 2.2 Autenticação (SEC-07, DEC-001)

#### O que o HLD define:

| Método | Prioridade |
|--------|------------|
| QR Code + Biometria App | **Primário** |
| Username/Password + SMS OTP | Fallback |
| Username/Password + App Push | Fallback |

#### O que o diagrama do cliente mostra:

| Cenário | Fluxo |
|---------|-------|
| **Cenário 1** | user + pass + OTP por SMS |
| **Cenário 2** | user + pass + OTP dentro app |

#### Diferenças Críticas:

| Aspecto | HLD | Cliente | Impacto |
|---------|-----|---------|---------|
| **Método Primário** | QR Code + Biometria | user + pass + OTP | **ALTO** |
| **QR Code** | Método principal | Não mencionado | **ALTO** |
| **Biometria na app** | Obrigatória no QR Code | Não mencionada | **ALTO** |

#### Análise:

O diagrama do cliente **não menciona o fluxo de QR Code + Biometria** que o HLD define como método primário. Isto pode indicar:

1. O cliente considera QR Code como um **fluxo separado** não detalhado neste documento
2. O cliente pretende que **username/password + OTP** seja o método primário
3. O documento do cliente é apenas um **subset** dos fluxos completos

#### Acção Requerida:
- [ ] **CRÍTICO:** Validar com cliente qual é o método de autenticação primário
- [ ] Se QR Code for primário, solicitar diagrama de sequência específico
- [ ] Actualizar DEC-001 e SEC-07 se necessário

---

### 2.3 Protocolo OAuth

#### O que o HLD assume:

- OAuth 2.0 (implícito)
- Bearer Token para comunicação BFF → Backend

#### O que o diagrama do cliente detalha:

```
Authorization: OAuth access_token={{acess_token_anonimo}},
                      oauth_consumer_key={{client_token}},
                      oauth_timestamp={{timestamp}},
                      oauth_version=1.1,            <-- OAuth 1.1
                      oauth_signature={{assinatura}},
                      oauth_guid={{GUID}}
```

#### Diferenças:

| Aspecto | HLD | Cliente |
|---------|-----|---------|
| **Versão OAuth** | 2.0 (implícito) | **1.1** (explícito) |
| **Assinatura** | Não detalhado | HMAC-SHA256 |
| **GUID** | Não mencionado | Obrigatório |
| **Timestamp** | Não detalhado | Obrigatório |

#### Análise:

O diagrama do cliente utiliza **OAuth 1.1** com assinaturas HMAC, que é mais complexo que OAuth 2.0. Isto tem implicações em:

- Complexidade de implementação do BFF
- Gestão de chaves (consumer_key, secret_key)
- Segurança (assinatura de requests)

#### Acção Requerida:
- [ ] Confirmar versão OAuth utilizada pela ApiBBest
- [ ] Actualizar DEF-05-autenticacao-oauth.md com detalhes
- [ ] Documentar chaves necessárias (consumer_key, secret_key, etc.)

---

### 2.4 Gestão de Cache (Informação Nova)

#### O que o diagrama do cliente adiciona:

```
modelo de gestão de cache: Cache or API
Valida se tem dados na cache e se não pede à API e guarda na cache
Para este cliente há dados em cache?
- Se sim, devolve os dados ao SPA
- Se não, pede dados às APIs
```

#### Impacto no HLD:

O HLD menciona cache de sessão (tokens) mas **não detalha** estratégia de cache de dados. O cliente define um padrão **"Cache or API"** que deve ser incorporado.

#### Acção Requerida:
- [ ] Adicionar secção sobre estratégia de cache de dados no DEF-05-arquitetura-bff.md
- [ ] Definir políticas de invalidação de cache
- [ ] Especificar que dados são cacheáveis (dados para home, beneficiários, etc.)

---

### 2.5 APIs de Integração (Informação Nova)

#### O que o diagrama do cliente detalha:

##### APIs para Home (após login):

| API | Descrição |
|-----|-----------|
| Client_getClientInformation | Nome e dados do cliente |
| Client_getClientContact | Contactos |
| SIBS_getConsentStatus | PSD2 |
| SIBS_getConsentAccount | PSD2 |
| Objective_getClientObjectives | Avisos de objectivos |
| Devices_getDevices | Dispositivos registados |
| MIFID_getInvestorProfile | Perfil do investidor |
| Schedule_getSchedules | Agendamentos |
| Permanent_getPermanentOrders | Ordens permanentes |
| CorpAction_getOngoingClosedCA | Operações corporativas |
| Operation_getOperationConfirmation | Operações |
| Account_getMovements | Movimentos de contas |
| Account_getAccounts | Contas |
| CCards_getCreditCards | Cartões de crédito |
| DCards_getDebitCards | Cartões de débito |
| Statement_getUserStatement | Património |
| Message_getInboxMessage | Mensagens |

##### APIs de Transferência:

| API | Propósito |
|-----|-----------|
| API de beneficiários | Lista de beneficiários |
| API COPS | Nome do titular (IBAN nacional) |
| API VOP | Validação/confirmação de nome |
| API Simulação | Simulação de transferência |
| API Transferência | Execução da transferência |
| API Secure | Validação OTP |

#### Acção Requerida:
- [ ] Incorporar catálogo de APIs no DEF-09-integracao-interfaces.md
- [ ] Documentar contratos de cada API
- [ ] Solicitar documentação detalhada das APIs ao cliente

---

### 2.6 Regras de Negócio - Transferências (Informação Nova)

#### O que o diagrama do cliente detalha:

##### Validação de IBAN:

```
BFF valida qual o tipo de IBAN e se é válido.
Confirmação se o IBAN é válido por biblioteca a escolher

Logo/bandeira:
- Correspondência entre IBAN e logo/bandeira
- Se nacional: logo do banco
- Se internacional: lista interna com todos os logos
  Exemplo: ("AD", "Andorra", "+376", flag_ad, "EUR")
```

##### Regras de Roteamento de Transferência:

| Condição | Tipo de Transferência |
|----------|----------------------|
| PT500065 (IBAN do BEST) | Transferência Interna |
| PT50 (não BEST) | Transferência Interbancária |
| Internacional SEPA | SEPA |
| Internacional não SEPA | Processo complexo com vários ecrãs |

##### Fluxo de Transferência:

1. Selecção tipo (IBAN/Conta ou SPIN)
2. Validação IBAN
3. COPS → Nome do titular
4. VOP → Confirmação do nome
5. Simulação → Valores e ID transacção
6. Confirmação + OTP
7. Execução

#### Acção Requerida:
- [ ] Documentar regras de roteamento no DEF-03-casos-uso-principais.md
- [ ] Especificar biblioteca de validação de IBAN
- [ ] Documentar fluxo completo de transferências não-SEPA (complexo)

---

### 2.7 Segurança

#### Alinhamento Verificado:

| Aspecto | HLD (SEC-08) | Cliente |
|---------|--------------|---------|
| Cifra de credenciais | Pendente (item documentado) | "Ver se faz sentido encriptar o user e pass(?)" |
| TLS | Definido (TLS 1.2+) | Implícito |

#### Observação:

Ambos os documentos identificam a mesma dúvida sobre cifrar credenciais além do TLS. Isto confirma que a pendência no HLD é real e deve ser discutida.

---

## 3. Informação Nova a Incorporar

### 3.1 Detalhes Técnicos de Autenticação

O cliente fornece detalhes sobre:

- **Token anónimo** para primeira chamada
- **Chaves necessárias:** access_token_anonimo, consumer_key, secret_key, Token_Endpoint, clientid, client_secret, ClientScopes, authorizationpoint
- **Formato Authorization header** com OAuth 1.1
- **API AUT_004** (Authentication_checkLogin)

### 3.2 Dados Retornados no Login

```json
{
    "returnCode": "0",
    "returnMsg": "Sucesso",
    "outputData": {
        "apiToken": "...",
        "mustChangePassword": "N",
        "needStrongAuthentication": "N",
        "firstLogin": "N",
        "otp_id": null,
        "sasToken": ""
    }
}
```

**Nota do cliente:** "sasToken não é necessário para o SPA"

### 3.3 API Backoffice

Fornece dados de CMS:
- Notícias
- Novidades
- Alertas
- Publicidades (estrutura JSON detalhada no documento)

---

## 4. Questões para Discussão com Cliente

### 4.1 Arquitectura

1. O componente "ApiBBest" corresponde ao API Gateway IBM ou é um backend diferente?
2. Existe API Gateway entre BFF e ApiBBest ou a comunicação é directa?
3. Onde se encaixa o Siebel na arquitectura descrita?

### 4.2 Autenticação

4. **CRÍTICO:** O método QR Code + Biometria está planeado para o canal web? Se sim, é o método primário?
5. O documento descreve apenas o fluxo de fallback (user+pass+OTP)?
6. Qual a versão OAuth utilizada (1.1 ou 2.0)?

### 4.3 Transferências

7. Qual biblioteca será utilizada para validação de IBAN?
8. Existe documentação das APIs COPS e VOP?
9. Qual o fluxo completo para transferências internacionais não-SEPA?

### 4.4 Cache

10. Qual a estratégia de invalidação de cache?
11. Qual o TTL recomendado para dados da home?
12. Redis ou outra tecnologia para cache de dados?

---

## 5. Acções Recomendadas

### Prioridade Alta

| # | Acção | Responsável |
|---|-------|-------------|
| 1 | Clarificar método de autenticação primário (QR Code vs user+pass) | NextReality + Cliente |
| 2 | Confirmar arquitectura (API Gateway, ApiBBest, Siebel) | NextReality + Cliente |
| 3 | Validar versão OAuth (1.1 vs 2.0) | NextReality + Cliente |

### Prioridade Média

| # | Acção | Responsável |
|---|-------|-------------|
| 4 | Incorporar catálogo de APIs no DEF-09 | NextReality |
| 5 | Documentar regras de roteamento de transferências | NextReality |
| 6 | Adicionar estratégia de cache de dados | NextReality |

### Prioridade Baixa

| # | Acção | Responsável |
|---|-------|-------------|
| 7 | Documentar formato OAuth 1.1 se confirmado | NextReality |
| 8 | Especificar biblioteca de validação IBAN | Cliente |
| 9 | Documentar fluxo não-SEPA completo | Cliente |

---

## 6. Conclusão

O diagrama de sequência do cliente é **valioso** pois fornece detalhes de implementação específicos que complementam o HLD. No entanto, existem **divergências arquitecturais e de autenticação** que devem ser resolvidas antes de prosseguir.

A principal divergência é o **método de autenticação primário** - o HLD define QR Code + Biometria, mas o cliente detalha apenas user+pass+OTP. Esta questão é **crítica** e deve ser resolvida com prioridade.

O documento do cliente também revela que a integração utiliza **OAuth 1.1** com assinaturas, o que é mais complexo que o OAuth 2.0 assumido no HLD. Isto tem impacto na implementação do BFF.

### Recomendação Final

Agendar reunião com cliente para:
1. Esclarecer divergências de autenticação
2. Confirmar arquitectura de integração
3. Obter documentação das APIs mencionadas

Após este alinhamento, o diagrama de sequência pode ser incorporado como referência técnica no HLD.

---

## Apêndice: Referências do HLD Consultadas

- SEC-03-visao-geral-solucao.md (Diagrama 3.2)
- SEC-07-autenticacao-autorizacao.md
- SEC-08-seguranca-conformidade.md
- DEC-001-estrategia-autenticacao-web.md
- DEC-007-padrao-bff.md
- DEF-05-arquitetura-bff.md
- DEF-09-integracao-interfaces.md
