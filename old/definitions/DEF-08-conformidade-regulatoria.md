---
id: DEF-08-conformidade-regulatoria
aliases:
  - Novo Banco Conformidade Regulatoria
tags:
  - nextreality-novobanco-website-definitions
approved: true
created: 2025-12-22
hubs:
  - "[[nextreality]]"
para-code: R
reviewed: true
---
# DEF-08: Conformidade Regulatoria

> **Status:** estrutura
> **Secao relacionada:** 08 - Seguranca & Conformidade

## Contexto

Este documento define os requisitos de conformidade regulatoria, incluindo PSD2, RGPD, PCI-DSS e requisitos do Banco de Portugal.

## Questoes a Responder

1. Quais regulamentos aplicaveis?
R.: PSD2, RGPD (ver DEF-02-restricoes)

2. Quais requisitos PCI-DSS aplicaveis?
R.: _Pendente - depende do scope de cartoes_

3. Existem requisitos especificos do Banco de Portugal?
R.: _Pendente_

4. Como garantir conformidade continua?
R.: _Pendente_

## PSD2 - Payment Services Directive 2

### Strong Customer Authentication (SCA)

| Requisito | Implementacao |
|-----------|---------------|
| 2 de 3 fatores | Password + OTP/App |
| Conhecimento | Password, PIN |
| Posse | Telemovel (OTP/Push) |
| Inerencia | Biometria |

### Operacoes que Requerem SCA

| Operacao | SCA | Excecoes |
|----------|-----|----------|
| Login | Sim | - |
| Pagamentos | Sim | Whitelist, valores baixos |
| Transferencias | Sim | Entre contas proprias |
| Consultas | Nao | Apos SCA no login |

### Dynamic Linking

| Requisito | Implementacao |
|-----------|---------------|
| Montante no OTP | Sim |
| Beneficiario no OTP | Sim |
| Codigo unico | Sim |

### Open Banking APIs

> **NOTA IMPORTANTE:** A exposição de APIs PSD2 (Open Banking) **NÃO está no âmbito** deste projeto.
> As APIs PSD2 já estão implementadas pelo banco. O novo WebSite apenas **consome** as APIs existentes, não expõe novas.

| API | Proposito | Status |
|-----|-----------|--------|
| AIS | Account Information | **Fora do âmbito** (já implementado pelo banco) |
| PIS | Payment Initiation | **Fora do âmbito** (já implementado pelo banco) |
| CBPII | Card-based Payment | **Fora do âmbito** (já implementado pelo banco) |

## RGPD - Regulamento Geral de Protecao de Dados

### Principios

| Principio | Implementacao |
|-----------|---------------|
| Licitude | Consentimento explicito |
| Limitacao da finalidade | Dados usados apenas para fins declarados |
| Minimizacao | Apenas dados necessarios |
| Exatidao | Processos de atualizacao |
| Limitacao da conservacao | Politica de retencao |
| Integridade e confidencialidade | Encriptacao, controlos de acesso |

### Direitos dos Titulares

| Direito | Artigo | Prazo | Implementacao |
|---------|--------|-------|---------------|
| Informacao | 13-14 | Imediato | Privacy policy |
| Acesso | 15 | 30 dias | Export de dados |
| Retificacao | 16 | 30 dias | Edicao de perfil |
| Eliminacao | 17 | 30 dias | Right to be forgotten |
| Limitacao | 18 | 30 dias | Gestao de consentimentos |
| Portabilidade | 20 | 30 dias | Export JSON/CSV |
| Oposicao | 21 | 30 dias | Opt-out marketing |

### DPIA (Data Protection Impact Assessment)

| Aspecto | Descricao |
|---------|-----------|
| Necessidade | Obrigatorio (dados bancarios) |
| Responsavel | DPO |
| Frequencia | Inicial + alteracoes significativas |

## PCI-DSS

### Scope

| Componente | In Scope | Justificacao |
|------------|----------|--------------|
| Processamento de cartoes | _A avaliar_ | Depende de tokenizacao |
| Armazenamento PAN | Nao | Tokenizado |
| Transmissao PAN | _A avaliar_ | Via fornecedor |

### Requisitos Aplicaveis

| Requisito | Descricao | Status |
|-----------|-----------|--------|
| 1 | Firewall configuration | _Pendente_ |
| 2 | Default passwords | _Pendente_ |
| 3 | Protect stored data | Tokenizacao |
| 4 | Encrypt transmission | TLS 1.3 |
| 6 | Secure systems | SDLC seguro |
| 7 | Restrict access | RBAC |
| 8 | Unique IDs | Identificacao unica |
| 10 | Track access | Audit logs |
| 11 | Test security | Pentests |
| 12 | Security policy | Documentacao |

## Banco de Portugal

### Avisos Aplicaveis

| Aviso | Tema | Status |
|-------|------|--------|
| _A identificar_ | _A identificar_ | _Pendente_ |

### Requisitos de Reporting

| Report | Frequencia | Destinatario |
|--------|------------|--------------|
| Incidentes | Ad-hoc | BdP |
| Fraude | _A definir_ | BdP |

## Modelo de Ameacas (STRIDE)

### Analise STRIDE

| Ameaca | Descricao | Mitigacao |
|--------|-----------|-----------|
| **S**poofing | Identidade falsa | MFA, certificados |
| **T**ampering | Alteracao de dados | Integridade, assinaturas |
| **R**epudiation | Negar acoes | Audit logs |
| **I**nformation disclosure | Exposicao de dados | Encriptacao, controlos |
| **D**enial of service | Indisponibilidade | Rate limiting, WAF |
| **E**levation of privilege | Acesso indevido | RBAC, least privilege |

### Threat Model por Componente

| Componente | Ameacas Principais | Controlos |
|------------|-------------------|-----------|
| Login | Spoofing, Brute force | MFA, lockout |
| Transferencias | Tampering, Repudiation | SCA, audit |
| Dados pessoais | Information disclosure | Encriptacao |
| APIs | DoS | Rate limiting, WAF |

## Auditoria

### Eventos Auditados

| Evento | Dados Capturados |
|--------|------------------|
| Login | User, IP, timestamp, resultado |
| Logout | User, timestamp |
| Transferencia | User, montante, destino, timestamp |
| Alteracao dados | User, campo, antes, depois |
| Erro de autenticacao | User, IP, timestamp |

### Retencao de Audit Logs

| Tipo | Retencao |
|------|----------|
| Seguranca | 2 anos |
| Transacoes | 10 anos |
| Acessos | 1 ano |

## Resposta a Incidentes

### Classificacao de Incidentes

| Severidade | Descricao | Tempo de Resposta |
|------------|-----------|-------------------|
| Critica | Breach de dados, indisponibilidade total | 15 minutos |
| Alta | Funcionalidade critica afetada | 1 hora |
| Media | Funcionalidade secundaria afetada | 4 horas |
| Baixa | Impacto minimo | 24 horas |

### Procedimentos

| Fase | Acoes |
|------|-------|
| Detecao | Alertas, monitoring |
| Contencao | Isolar sistemas afetados |
| Erradicacao | Remover ameaca |
| Recuperacao | Restaurar servicos |
| Lessons learned | Postmortem, melhorias |

## Decisoes

### Definido

- PSD2 SCA obrigatorio
- RGPD conformidade total
- Encriptacao AES-256 / TLS 1.3

### Pendentes

- Scope PCI-DSS exato
- Requisitos especificos BdP
- DPIA completo
- Procedimentos de breach notification

## Referencias

- [SEC-08-seguranca-conformidade.md](../sections/SEC-08-seguranca-conformidade.md)
- [DEF-02-restricoes.md](DEF-02-restricoes.md)
- [DEF-08-seguranca-dados-sensiveis.md](DEF-08-seguranca-dados-sensiveis.md)
- PSD2 RTS on SCA
- RGPD - Regulamento (UE) 2016/679
- PCI-DSS v4.0
