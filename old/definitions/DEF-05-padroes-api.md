---
id: DEF-05-padroes-api
aliases:
  - Novo Banco Padroes API
tags:
  - nextreality-novobanco-website-definitions
approved: true
created: 2025-12-22
hubs:
  - "[[nextreality]]"
para-code: R
reviewed: true
---
# DEF-05: Padroes e Convencoes de API

> **Status:** em-progresso
> **Secao relacionada:** 05 - Arquitetura Backend & Servicos

## Contexto

Este documento define os padroes e convencoes para APIs, formatacao de dados e estruturas de referencia utilizados na plataforma.

## Questoes a Responder

1. Qual o formato padrao para datas nas APIs?
R.: yyyy-MM-dd'T'HH:mm:ss.SSSZ (ISO 8601)

2. Qual o formato padrao para montantes nas APIs?
R.: String (para evitar problemas de precisao com floating point)

3. Existem listas de referencia partilhadas (paises, moedas)?
R.: Sim, JSONs com listas de paises e country codes

4. Como sao geridos os deeplinks?
R.: Links criados para ligacao aos ecras

5. Quais constantes de configuracao existem?
R.: Ver seccao de Constantes

## Padroes de Formatacao

### Datas

| Aspecto | Especificacao |
|---------|---------------|
| Formato | `yyyy-MM-dd'T'HH:mm:ss.SSSZ` |
| Padrao | ISO 8601 |
| Tipo retornado | String |
| Timezone | UTC (Z suffix) ou offset explicito |
| Exemplo | `2024-01-15T14:30:00.000Z` |

**Nota:** A API devolve sempre string para datas.

### Montantes/Valores Monetarios

| Aspecto | Especificacao |
|---------|---------------|
| Tipo retornado | String |
| Separador decimal | Ponto (.) |
| Casas decimais | 2 (para EUR) |
| Exemplo | `"1234.56"` |

**Nota:** A API devolve sempre string para evitar problemas de precisao com numeros de virgula flutuante.

## Dados de Referencia

### Listas de Paises e Country Codes

JSONs utilizados para popular listas na aplicacao:

```json
{
  "countryCode": "AD",
  "countryName": "Andorra",
  "dialCode": "+376",
  "flagResource": "flag_ad",
  "currency": "EUR"
}
```

| Campo | Descricao |
|-------|-----------|
| countryCode | Codigo ISO 3166-1 alpha-2 |
| countryName | Nome do pais |
| dialCode | Codigo telefonico internacional |
| flagResource | Identificador do recurso de imagem da bandeira |
| currency | Moeda principal (ISO 4217) |

### Logos de Bancos

Correspondencia entre IBAN e logo/bandeira:

| Cenario | Fonte do Logo |
|---------|---------------|
| IBAN nacional (PT) | Link para logo do banco (via codigo banco) |
| IBAN internacional | Lista interna com logos por country code |

## Deeplinks

Links para navegacao directa a ecras especificos:

| Aspecto | Descricao |
|---------|-----------|
| Proposito | Ligacao aos ecras da aplicacao |
| Formato | _Pendente documentacao detalhada_ |
| Exemplos | _Pendente_ |

## Constantes de Configuracao

### Constantes Registadas

| Constante | Proposito | Categoria |
|-----------|-----------|-----------|
| SIBS Client ID | Identificador do parceiro SIBS | Integracao |
| Consumer Key | Chave de API BEST | Autenticacao |
| Consumer Secret | Segredo de API BEST | Autenticacao |
| Guest Token | Token para acesso guest | Autenticacao |
| PSD2 Redirect | Link para pagina PSD2 | Open Banking |
| Unit Link Constants | Pares de valores para unit linked | Investimentos |

### Constantes de Seguros Viagem

| Constante | Proposito |
|-----------|-----------|
| Insurance_travel_ensurer | Dados da seguradora |
| Insurance_travel_product | Identificador do produto |
| Insurance_travel_integration_id | ID de integracao |
| Insurance_banned_country_codes | Paises excluidos |

## Decisoes

### Padroes Definidos

- Datas em formato ISO 8601 como string
- Montantes como string para precisao
- Dados de referencia em JSON

### Pendentes de Documentacao

- Estrutura completa de deeplinks
- Lista completa de constantes e seus valores
- Endpoints de dados de referencia

## Referencias

- [SEC-05-arquitetura-backend-servicos.md](../sections/SEC-05-arquitetura-backend-servicos.md)
- ISO 8601 - Date and time format
- ISO 3166-1 - Country codes
- ISO 4217 - Currency codes
