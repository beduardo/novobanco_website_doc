---
id: DEF-02-requisitos-funcionais
aliases:
  - Novo Banco Requisitos Funcionais
tags:
  - nextreality-novobanco-website-definitions
approved: true
created: 2025-12-22
hubs:
  - "[[nextreality]]"
para-code: R
reviewed: true
---
# DEF-02: Catalogo de Requisitos Funcionais

> **Status:** em-progresso
> **Secao relacionada:** 02 - Contexto de Negocio & Requisitos

## Contexto

Este documento cataloga todos os requisitos funcionais da plataforma web de Homebanking, organizados por dominio funcional e priorizados por fase de entrega.

## Questoes a Responder

1. Quais funcionalidades existem atualmente no App Mobile que devem ser replicadas?
2. Existe documentacao das funcionalidades do App Mobile?
3. Quais funcionalidades sao obrigatorias para o MVP?
4. Quais funcionalidades podem ficar para fases posteriores?
5. Existem funcionalidades novas (que nao existem no App) a considerar?
6. Quais funcionalidades tem dependencias criticas de sistemas externos?
7. Quais funcionalidades requerem MFA/autenticacao reforçada?
8. Existem user stories ou casos de uso ja documentados?

## Arvore de Funcionalidades (Mindmaps por Categoria)

### 1. Acesso

```plantuml
@startmindmap
* Acesso
** Registo
** Login
** Recuperacao de acessos
@endmindmap
```

### 2. Home

```plantuml
@startmindmap
* Home
** Pesquisa avancada
*** Pesquisa
**** Lista de resultados
** Mensagens
*** Consultar
*** Enviar
** Store
*** Lista de funcionalidades
** Novidades/artigos
*** Lista de novidades
**** Detalhe
** Carrinho de compra de fundos
** Gestao de atalhos
** Reminders/Alertas
** Overlays
** Noticias
** Saldos & movimentos
** Patrimonio
@endmindmap
```

### 3. Área Pessoal

```plantuml
@startmindmap
* Area pessoal
** Os meus dados
*** Pessoais
**** Nacionalidade
**** Número identificação
**** Data validade
*** Profissionais
**** Habilitações
**** Profissão
**** Vive de rendimentos
*** Contactos
**** Mail
**** Residência
**** Telemóvel
*** Seguranca
**** Alteração de números de segurança
**** Limites transferências
**** Dispositivos
**** Alterar password
**** Acesso biometria
*** Outros
**** Origens
**** Destinos
**** Finalidades
**** Montantes
*** Perfil do investidor
** Personalizacoes
*** Beneficiários
*** Pagamentos frequentes
*** Agendamentos
*** Debitos diretos
*** PSD2
*** Foto de perfil
*** Fundo do ecra
*** Nome preferencial
** Comunicacao e privacidade
** Alertas e notificacoes
** Contactos Best
*** Telefonicos
*** Centros de investimento
** Spin
*** Gestao da adesao
** Logout
@endmindmap
```

### 4. Patrimonio & Operacoes

```plantuml
@startmindmap
* Patrimonio & Operacoes
** Patrimonio
** Ordens Pendentes
** Historico de operacoes
** Saldos e movimentos
** Confirmacao de operacoes
** Comprovativos e extratos
*** Comprovativos
*** Extratos
** Carteiras
@endmindmap
```

### 5. Dashboard

```plantuml
@startmindmap
* Dashboard
** Analise Rentabilidade
** Apoio a investir
@endmindmap
```

### 6. Outros Bancos

```plantuml
@startmindmap
* Outros bancos
** Adicionar conta
** Gerir
@endmindmap
```

### 7. Investimentos

```plantuml
@startmindmap
* Investimentos
** Acoes
*** Pesquisar
*** Tops
*** Consultar
*** Comprar
*** Vender
** ETF
*** Pesquisar
*** Tops
*** Consultar
*** Comprar
*** Vender
** Fundos
*** Pesquisar
*** Tops
*** Consultar
*** Comprar
*** Vender
** Obrigacoes
*** Pesquisar
*** Tops
*** Consultar
*** Comprar
*** Vender
** Warrants
*** Pesquisar
*** Tops
*** Consultar
*** Comprar
*** Vender
** Ofertas publicas
*** Consultar
*** Comprar
*** Vender
** Unit linked
*** Consultar
*** Comprar
*** Vender
** Produtos estruturados
*** Consultar
*** Comprar
** Temas investimento
*** Consulta
*** Compra
** Wishlist
** Indices
** Noticias externas
@endmindmap
```

### 8. Poupanca

```plantuml
@startmindmap
* Poupanca
** Depositos a prazo
*** Subscricao
*** Gestao
** Leiloes
*** Leiloes de DP
*** Licitar DP
** Produtos poupanca reforma
*** Consultar
*** Comprar
*** Simular
*** Gerir
** BTP
*** Consultar
*** Encerrar
*** Login
*** Reforcar
*** Levantar
** Objetivos
*** Criar Objetivo
*** Gerir Objetivos
** Robot Advisor
@endmindmap
```

### 9. Credito

```plantuml
@startmindmap
* Credito
** Credito habitacao
*** Detalhe
*** Simular
*** Lista
** Credito Pessoal
*** Detalhe
*** Lista de creditos
** Conta margem
*** Simular
*** Contratar
@endmindmap
```

### 10. Transferencias

```plantuml
@startmindmap
* Transferencias
** Intra
** Inter
** Internacionais
@endmindmap
```

### 11. Pagamentos

```plantuml
@startmindmap
* Pagamentos
** Servicos
** Compras
** Estado
** Jogos Santa Casa
@endmindmap
```

### 12. Carregamentos

```plantuml
@startmindmap
* Carregamentos
** WOO
** NOS
** Vodafone
** Meo
** WTF
** UZO
@endmindmap
```

### 13. MBWay

```plantuml
@startmindmap
* MBWay
** Criar Mbnet
** Gerir Mbnet
** Dividir conta
** Pedir dinheiro
** Enviar dinheiro
@endmindmap
```

### 14. Cartoes

```plantuml
@startmindmap
* Cartoes
** Pedido de Cartao
** Gestao de Cartoes
** Bloquear Cartao
** Gerir plafond
** Gerir modalidade
** Pagar Cartao
** Cash Advance
** Compras Especiais
** Gerar Mbnet
@endmindmap
```

### 15. Eventos Corporativos

```plantuml
@startmindmap
* Eventos corporativos
** Lista
*** A decorrer
*** Passados
** Resposta
@endmindmap
```

### 16. Outros

```plantuml
@startmindmap
* Outros
** Seguros de protecao (externo)
** Area do viajante
*** Cambios
*** Ligacoes internas
** Bea (ligacao externa)
** Avaliacao de cliente
@endmindmap
```		


## Catalogo de Requisitos por Dominio

### Autenticacao e Seguranca

| ID | Requisito | Descricao | Prioridade | Fase |
|----|-----------|-----------|------------|------|
| RF-AUTH-001 | Login com credenciais | _Pendente_ | _Pendente_ | _Pendente_ |
| RF-AUTH-002 | Autenticacao MFA | _Pendente_ | _Pendente_ | _Pendente_ |
| RF-AUTH-003 | Recuperacao de password | _Pendente_ | _Pendente_ | _Pendente_ |
| RF-AUTH-004 | Gestao de sessoes | _Pendente_ | _Pendente_ | _Pendente_ |
| RF-AUTH-005 | Logout | _Pendente_ | _Pendente_ | _Pendente_ |

### Contas e Saldos

| ID | Requisito | Descricao | Prioridade | Fase |
|----|-----------|-----------|------------|------|
| RF-ACC-001 | Consulta de saldos | _Pendente_ | _Pendente_ | _Pendente_ |
| RF-ACC-002 | Lista de contas | _Pendente_ | _Pendente_ | _Pendente_ |
| RF-ACC-003 | Detalhes de conta | _Pendente_ | _Pendente_ | _Pendente_ |
| RF-ACC-004 | Extrato de movimentos | _Pendente_ | _Pendente_ | _Pendente_ |
| RF-ACC-005 | Filtros e pesquisa | _Pendente_ | _Pendente_ | _Pendente_ |
| RF-ACC-006 | Export de extrato (PDF) | _Pendente_ | _Pendente_ | _Pendente_ |

### Transferencias

| ID | Requisito | Descricao | Prioridade | Fase |
|----|-----------|-----------|------------|------|
| RF-TRF-001 | Transferencia entre contas proprias | _Pendente_ | _Pendente_ | _Pendente_ |
| RF-TRF-002 | Transferencia nacional | _Pendente_ | _Pendente_ | _Pendente_ |
| RF-TRF-003 | Transferencia SEPA | _Pendente_ | _Pendente_ | _Pendente_ |
| RF-TRF-004 | Transferencia internacional | _Pendente_ | _Pendente_ | _Pendente_ |
| RF-TRF-005 | Agendamento de transferencia | _Pendente_ | _Pendente_ | _Pendente_ |
| RF-TRF-006 | Transferencias recorrentes | _Pendente_ | _Pendente_ | _Pendente_ |

### Pagamentos

| ID | Requisito | Descricao | Prioridade | Fase |
|----|-----------|-----------|------------|------|
| RF-PAY-001 | Pagamento de servicos | _Pendente_ | _Pendente_ | _Pendente_ |
| RF-PAY-002 | Pagamento por referencia | _Pendente_ | _Pendente_ | _Pendente_ |
| RF-PAY-003 | Pagamento ao Estado | _Pendente_ | _Pendente_ | _Pendente_ |
| RF-PAY-004 | Debitos diretos | _Pendente_ | _Pendente_ | _Pendente_ |
| RF-PAY-005 | Pagamentos agendados | _Pendente_ | _Pendente_ | _Pendente_ |

### Cartoes

| ID | Requisito | Descricao | Prioridade | Fase |
|----|-----------|-----------|------------|------|
| RF-CRD-001 | Lista de cartoes | _Pendente_ | _Pendente_ | _Pendente_ |
| RF-CRD-002 | Detalhes do cartao | _Pendente_ | _Pendente_ | _Pendente_ |
| RF-CRD-003 | Movimentos do cartao | _Pendente_ | _Pendente_ | _Pendente_ |
| RF-CRD-004 | Bloqueio/desbloqueio | _Pendente_ | _Pendente_ | _Pendente_ |
| RF-CRD-005 | Alteracao de limites | _Pendente_ | _Pendente_ | _Pendente_ |
| RF-CRD-006 | Consulta/alteracao PIN | _Pendente_ | _Pendente_ | _Pendente_ |
| RF-CRD-007 | MBWay | _Pendente_ | _Pendente_ | _Pendente_ |

### Beneficiarios

| ID | Requisito | Descricao | Prioridade | Fase |
|----|-----------|-----------|------------|------|
| RF-BEN-001 | Lista de beneficiarios | _Pendente_ | _Pendente_ | _Pendente_ |
| RF-BEN-002 | Adicionar beneficiario | _Pendente_ | _Pendente_ | _Pendente_ |
| RF-BEN-003 | Editar beneficiario | _Pendente_ | _Pendente_ | _Pendente_ |
| RF-BEN-004 | Remover beneficiario | _Pendente_ | _Pendente_ | _Pendente_ |

### Notificacoes

| ID | Requisito | Descricao | Prioridade | Fase |
|----|-----------|-----------|------------|------|
| RF-NOT-001 | Centro de notificacoes | _Pendente_ | _Pendente_ | _Pendente_ |
| RF-NOT-002 | Configuracao de alertas | _Pendente_ | _Pendente_ | _Pendente_ |
| RF-NOT-003 | Historico de notificacoes | _Pendente_ | _Pendente_ | _Pendente_ |

### Definicoes e Perfil

| ID | Requisito | Descricao | Prioridade | Fase |
|----|-----------|-----------|------------|------|
| RF-SET-001 | Dados pessoais | _Pendente_ | _Pendente_ | _Pendente_ |
| RF-SET-002 | Alteracao de contactos | _Pendente_ | _Pendente_ | _Pendente_ |
| RF-SET-003 | Preferencias de notificacao | _Pendente_ | _Pendente_ | _Pendente_ |
| RF-SET-004 | Seguranca (alterar password) | _Pendente_ | _Pendente_ | _Pendente_ |
| RF-SET-005 | Gestao de dispositivos | _Pendente_ | _Pendente_ | _Pendente_ |

### Outros Dominios

| ID | Requisito | Descricao | Prioridade | Fase |
|----|-----------|-----------|------------|------|
| RF-OTH-001 | _A identificar_ | _Pendente_ | _Pendente_ | _Pendente_ |

## Decisoes

### Fases de Entrega
- **MVP:** _Lista de IDs_
- **Fase 1:** _Lista de IDs_
- **Fase 2:** _Lista de IDs_
- **Backlog:** _Lista de IDs_

### Funcionalidades Excluidas
_Lista de funcionalidades que NAO serao implementadas e justificativa_

## Restricoes Conhecidas

- Paridade total com App Mobile e requisito
- Autenticacao deve seguir mesmo fluxo OAuth do App

## Referencias

- [SEC-02-contexto-negocio-requisitos.md](../sections/SEC-02-contexto-negocio-requisitos.md)
- [DEF-01-business-objectives.md](DEF-01-business-objectives.md)
- Documentacao do App Mobile (se existir)
