---
id: DEF-03-regras-transferencias
aliases:
  - Regras de Transferências
tags:
  - nextreality-novobanco-website-definitions
  - definitions
  - transfers
  - business-rules
approved: false
created: 2026-01-21
hubs:
  - "[[nextreality]]"
para-code: R
reviewed: false
status: draft
---

# DEF-03: Regras de Transferências

> **Secção relacionada:** [3 - Visão Geral da Solução](../sections/SEC-03-visao-geral-solucao.md)
> **Fonte:** Diagramas de sequência do cliente (`customer_sequences/`)

## Contexto

Definir as regras de negócio para roteamento e processamento de transferências no HomeBanking Web. O BFF é responsável por aplicar estas regras para determinar qual API utilizar.

## Tipos de Transferência

### Classificação por IBAN

```plantuml
@startuml
skinparam backgroundColor #FEFEFE

start
:Recebe IBAN;

if (IBAN começa com PT500065?) then (sim)
    :Transferência **Interna**;
    :API: Transferência Interna;
else (não)
    if (IBAN começa com PT50?) then (sim)
        :Transferência **Interbancária**;
        :API: Transferência Interbancária;
    else (não)
        if (País é SEPA?) then (sim)
            :Transferência **SEPA**;
            :API: Transferência SEPA;
        else (não)
            :Transferência **Internacional**;
            note right: Processo complexo\ncom múltiplos ecrãs
            :API: Transferência Internacional;
        endif
    endif
endif

stop

@enduml
```

### Tabela de Roteamento

| Condição IBAN | Tipo | API | Complexidade |
|---------------|------|-----|--------------|
| PT500065* | Interna (mesmo banco) | API Transferência Interna | Baixa |
| PT50* (não 0065) | Interbancária Nacional | API Transferência Interbancária | Média |
| País SEPA (não PT) | SEPA | API Transferência SEPA | Média |
| País não-SEPA | Internacional | API Transferência Internacional | **Alta** |

> **Nota:** PT500065 é o BIC/código do Banco Best. Transferências para este BIC são internas.

## Fluxo de Transferência

### Fluxo Geral

```plantuml
@startuml
skinparam backgroundColor #FEFEFE

actor "Utilizador" as USER
participant "SPA" as SPA
participant "BFF" as BFF
participant "ApiBBest" as API

== Selecção de Beneficiário ==
USER -> SPA : Acede a Transferências
SPA -> BFF : GET /api/beneficiaries
BFF -> API : API Beneficiários
API --> BFF : Lista de beneficiários
BFF --> SPA : Lista de beneficiários

USER -> SPA : Insere IBAN ou\nselecciona beneficiário

== Validação de IBAN ==
SPA -> BFF : Envia IBAN
BFF -> BFF : Valida formato IBAN\n(biblioteca)
BFF -> BFF : Determina logo/bandeira
BFF --> SPA : IBAN válido + logo

== Consulta COPS (se PT50) ==
BFF -> API : API COPS
API --> BFF : Nome do titular
BFF --> SPA : Nome do titular

USER -> SPA : Confirma nome
SPA -> BFF : Solicita confirmação

== Verificação VOP ==
BFF -> API : API VOP
API --> BFF : Confirmação OK/Aviso
BFF --> SPA : Resultado VOP

== Montante e Dados ==
USER -> SPA : Insere montante
USER -> SPA : Preenche dados adicionais

== Simulação ==
SPA -> BFF : Dados completos
BFF -> BFF : Aplica regras de roteamento
BFF -> API : API Simulação (conforme tipo)
API --> BFF : Valores + ID transacção
BFF --> SPA : Simulação

== Confirmação ==
USER -> SPA : Confirma operação
SPA -> BFF : Confirma + ID

== Execução ==
BFF -> API : API Transferência
API --> BFF : Requer OTP
BFF --> SPA : Solicita OTP
USER -> SPA : Insere OTP
SPA -> BFF : Envia OTP
BFF -> API : Valida OTP
API --> BFF : Operação confirmada
BFF --> SPA : Sucesso

@enduml
```

### Dados do Pedido de Transferência

| Campo | Descrição | Obrigatório |
|-------|-----------|-------------|
| home_account_number | Conta de origem | Sim |
| destination_iban | IBAN de destino | Sim |
| destination_name | Nome do beneficiário | Sim |
| amount | Montante | Sim |
| description | Descrição/motivo | Não |
| destination_email | Email do beneficiário | Não |
| destination_phone | Telefone do beneficiário | Não |
| transfer_type | Tipo de transferência | Sim (calculado) |
| beneficiary_id | ID do beneficiário (se existente) | Não |

## Validação de IBAN

### Biblioteca de Validação

O BFF deve utilizar uma biblioteca para:
1. Validar formato do IBAN
2. Validar dígitos de controlo
3. Identificar país de origem

> **Pendência:** Definir biblioteca a utilizar (sugestões: IbanNet para .NET)

### Logo/Bandeira por País

O BFF mantém mapeamento entre código de país do IBAN e recursos visuais:

| Código País | País | Moeda | Logo/Bandeira |
|-------------|------|-------|---------------|
| PT | Portugal | EUR | Logo do banco (se nacional) |
| ES | Espanha | EUR | flag_es |
| FR | França | EUR | flag_fr |
| DE | Alemanha | EUR | flag_de |
| ... | ... | ... | ... |

**Regra:**
- Se IBAN nacional (PT): mostrar logo do banco destino
- Se IBAN internacional: mostrar bandeira do país

## APIs COPS e VOP

### COPS (Confirmation of Payee Service)

| Aspecto | Descrição |
|---------|-----------|
| **Propósito** | Obter nome do titular de conta nacional |
| **Aplicável a** | IBANs PT50 (nacionais) |
| **Retorno** | Nome do titular |

### VOP (Verification of Payee)

| Aspecto | Descrição |
|---------|-----------|
| **Propósito** | Confirmar se nome inserido corresponde ao titular |
| **Input** | IBAN + Nome |
| **Retorno** | OK ou Aviso de discrepância |

### Fluxo COPS/VOP

```plantuml
@startuml
skinparam backgroundColor #FEFEFE

start
:Utilizador insere IBAN;

if (IBAN é nacional (PT50)?) then (sim)
    :Chama API COPS;
    :Obtém nome do titular;
    :Mostra nome ao utilizador;
    :Utilizador confirma nome;
    :Chama API VOP;
    if (VOP confirma?) then (sim)
        :Continua fluxo;
    else (não)
        :Mostra aviso;
        :Utilizador decide continuar;
    endif
else (não)
    :Nome inserido manualmente;
    :Sem validação COPS/VOP;
endif

:Prossegue para montante;
stop

@enduml
```

## Transferências Internacionais Não-SEPA

> **Nota:** O processo para transferências internacionais não-SEPA é significativamente mais complexo.

| Aspecto | Descrição |
|---------|-----------|
| **Complexidade** | Alta - múltiplos ecrãs e validações |
| **Dados adicionais** | Código SWIFT, taxas, câmbio |
| **Tempo** | Mais demorado |

> **Pendência:** Solicitar ao cliente diagrama de sequência específico para transferências não-SEPA.

## Decisões

### Biblioteca de Validação IBAN
- **Decisão:** _A definir_
- **Alternativas:** IbanNet (.NET), implementação própria

### Cache de Beneficiários
- **Decisão:** Cache em Redis
- **TTL:** _A definir_

### Cache de Mapeamento País/Bandeira
- **Decisão:** Estático no BFF (não volátil)

## Restrições

- COPS/VOP apenas para IBANs nacionais
- Transferências não-SEPA requerem fluxo específico
- OTP obrigatório para todas as transferências

## Referências

- Diagramas de sequência: `customer_sequences/`
- [DEF-09-integracao-interfaces.md](DEF-09-integracao-interfaces.md) - APIs de transferência
