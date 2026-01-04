---
id: DEF-02-requisitos-nao-funcionais
aliases:
  - Novo Banco Requisitos Nao Funcionais
tags:
  - nextreality-novobanco-website-definitions
approved: true
created: 2025-12-22
hubs:
  - "[[nextreality]]"
para-code: R
reviewed: true
---
# DEF-02: Requisitos Nao-Funcionais (NFRs)

> **Status:** estrutura
> **Secao relacionada:** 02 - Contexto de Negocio & Requisitos

## Contexto

Este documento especifica os requisitos nao-funcionais da plataforma, incluindo disponibilidade, desempenho, seguranca, escalabilidade e conformidade, com metricas quantificaveis.

## Questoes a Responder

1. Qual a disponibilidade esperada (SLA)? 99.9%? 99.95%?
R.: 99.95%

2. Qual a latencia maxima aceitavel para operacoes criticas?
R.: Menos de 1seg.

3. Quantos utilizadores simultaneos sao esperados?
_A definir_

4. Qual o volume de transacoes esperado (TPS)?
_A definir_

5. Quais os requisitos de seguranca alem de PSD2/RGPD?
Somente PSD2 e RGPD no momento

6. Qual o tempo maximo de recuperacao em caso de falha (RTO)?
_A definir_

7. Qual a perda maxima de dados aceitavel (RPO)?
_A definir_

8. Existem requisitos especificos do Banco de Portugal?
_A definir_

9. Quais browsers e dispositivos devem ser suportados?
Chrome, Safari, Edge

10. Quais os requisitos de acessibilidade (WCAG level)?
R.: WCAG 2.2 nível AA

## Requisitos por Categoria

### Disponibilidade

| ID | Requisito | Metrica | Target | Prioridade |
|----|-----------|---------|--------|------------|
| NFR-AVL-001 | Disponibilidade geral | Uptime % | 99.95% (ex: 99.9%) | Alta |
| NFR-AVL-002 | Janela de manutencao | Horas/mes | _Pendente_ | Media |
| NFR-AVL-003 | MTTR (Mean Time to Recovery) | Minutos | _Pendente_ | Alta |
| NFR-AVL-004 | MTBF (Mean Time Between Failures) | Horas | _Pendente_ | Media |

### Desempenho

| ID | Requisito | Metrica | Target | Prioridade |
|----|-----------|---------|--------|------------|
| NFR-PRF-001 | Tempo de carregamento inicial | Segundos | _Pendente_ (ex: < 3s) | Alta |
| NFR-PRF-002 | Latencia API (p95) | Milissegundos | _Pendente_ (ex: < 500ms) | Alta |
| NFR-PRF-003 | Latencia API (p99) | Milissegundos | _Pendente_ (ex: < 1000ms) | Alta |
| NFR-PRF-004 | Tempo de login | Segundos | _Pendente_ | Alta |
| NFR-PRF-005 | Tempo de transferencia | Segundos | _Pendente_ | Alta |

### Escalabilidade

| ID | Requisito | Metrica | Target | Prioridade |
|----|-----------|---------|--------|------------|
| NFR-SCL-001 | Utilizadores simultaneos | Numero | _Pendente_ | Alta |
| NFR-SCL-002 | Transacoes por segundo (TPS) | TPS | _Pendente_ | Alta |
| NFR-SCL-003 | Pico de carga | Multiplicador | _Pendente_ (ex: 3x normal) | Media |
| NFR-SCL-004 | Crescimento anual | % | _Pendente_ | Media |

### Seguranca

| ID | Requisito | Metrica | Target | Prioridade |
|----|-----------|---------|--------|------------|
| NFR-SEC-001 | Encriptacao em transito | Protocolo | TLS 1.3 | Alta |
| NFR-SEC-002 | Encriptacao em repouso | Algoritmo | AES-256 | Alta |
| NFR-SEC-003 | Conformidade PSD2 SCA | % conformidade | 100% | Alta |
| NFR-SEC-004 | Conformidade RGPD | % conformidade | 100% | Alta |
| NFR-SEC-005 | Penetration testing | Frequencia | _Pendente_ (ex: anual) | Alta |
| NFR-SEC-006 | Vulnerability scanning | Frequencia | _Pendente_ (ex: continuo) | Alta |
| NFR-SEC-007 | Tempo de sessao inativo | Minutos | _Pendente_ (ex: 10min) | Alta |

### Recuperacao (DR)

| ID | Requisito | Metrica | Target | Prioridade |
|----|-----------|---------|--------|------------|
| NFR-DR-001 | RTO (Recovery Time Objective) | Horas | _Pendente_ (ex: 4h) | Alta |
| NFR-DR-002 | RPO (Recovery Point Objective) | Minutos | _Pendente_ (ex: 15min) | Alta |
| NFR-DR-003 | Backup frequency | Frequencia | _Pendente_ | Alta |
| NFR-DR-004 | DR test frequency | Frequencia | _Pendente_ (ex: trimestral) | Media |

### Compatibilidade

| ID | Requisito | Metrica | Target | Prioridade |
|----|-----------|---------|--------|------------|
| NFR-CMP-001 | Browsers suportados | Lista | _Pendente_ | Alta |
| NFR-CMP-002 | Versoes minimas browsers | Versao | _Pendente_ | Alta |
| NFR-CMP-003 | Dispositivos moveis (responsive) | Breakpoints | _Pendente_ | Alta |
| NFR-CMP-004 | Resolucoes de ecra | Lista | _Pendente_ | Media |

### Acessibilidade

| ID | Requisito | Metrica | Target | Prioridade |
|----|-----------|---------|--------|------------|
| NFR-ACC-001 | Conformidade WCAG | Level | **2.2 AA** | Alta |
| NFR-ACC-002 | Screen reader support | % paginas | 100% | Alta |
| NFR-ACC-003 | Keyboard navigation | % paginas | 100% | Alta |

### Observabilidade

| ID | Requisito | Metrica | Target | Prioridade |
|----|-----------|---------|--------|------------|
| NFR-OBS-001 | Log retention | Dias | _Pendente_ | Media |
| NFR-OBS-002 | Metrics granularity | Segundos | _Pendente_ | Media |
| NFR-OBS-003 | Alerting response | Minutos | _Pendente_ | Alta |

## Decisoes

### SLAs Definidos
_A preencher apos respostas_

### Trade-offs Aceites
_A preencher apos respostas_

## Restricoes Conhecidas

- Conformidade PSD2 SCA obrigatoria
- Conformidade RGPD obrigatoria
- Requisitos Banco de Portugal aplicaveis

## Referencias

- [SEC-02-contexto-negocio-requisitos.md](../sections/SEC-02-contexto-negocio-requisitos.md)
- PSD2 RTS
- RGPD
- Banco de Portugal - Avisos aplicaveis
