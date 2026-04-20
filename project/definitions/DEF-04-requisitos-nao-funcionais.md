---
id: "DEF-04"
title: "Requisitos Não Funcionais"
status: "completed"
created: "2026-01-01"
updated: "2026-04-18"
related-decisions:
  - "DEC-006"
  - "DEC-012"
  - "DEC-015"
  - "DEC-025"
affects-sections:
  - "SEC-02"
---

# DEF-04: Requisitos Não Funcionais

> **Secção relacionada:** [2 - Contexto de Negócio & Requisitos](../sections/SEC-02-contexto-negocio-requisitos.md)

## Contexto

Os requisitos não funcionais definem os atributos de qualidade da solução HomeBanking web, incluindo performance, segurança, disponibilidade e escalabilidade. Estes requisitos são críticos para um sistema bancário.

Os valores concretos de cada requisito, bem como os parâmetros operacionais associados (auto-scaling, capacity planning, resiliência, testes de carga), serão fornecidos pelo Novo Banco através da sua documentação interna.

## Categorias de Requisitos

### Performance
Valores a constar de documentação do banco.

### Disponibilidade
Valores a constar de documentação do banco.

### Escalabilidade
Valores a constar de documentação do banco.

### Segurança
Certificações, requisitos de encriptação e política de retenção de logs a constar de documentação do banco.

### Compatibilidade
Browsers suportados e requisitos de responsividade a constar de documentação do banco.

## Restrições Conhecidas

- Parâmetros operacionais concretos (HPA, resource limits, PDB, ferramenta de load testing) serão fornecidos pelo banco — ver DEC-025
- Infraestrutura de segurança (WAF, SIEM, DR, backup) é responsabilidade do banco — ver DEC-015

## Referências

- [DEF-22-desempenho-fiabilidade.md](DEF-22-desempenho-fiabilidade.md) — Implementação técnica dos requisitos de performance
- [DEC-006-estrategia-containers-openshift.md](../decisions/DEC-006-estrategia-containers-openshift.md) — OpenShift e suporte a disponibilidade
- [DEC-012-comunicacao-de-janelas-de-manutencao-ao-cliente.md](../decisions/DEC-012-comunicacao-de-janelas-de-manutencao-ao-cliente.md) — Janelas de manutenção
- [DEC-015-reutilizacao-infraestrutura-operacional-existente-novo-banco.md](../decisions/DEC-015-reutilizacao-infraestrutura-operacional-existente-novo-banco.md) — Responsabilidade de infraestrutura e segurança
- [DEC-025-parametros-operacionais-de-plataforma-definidos-pelo-banco.md](../decisions/DEC-025-parametros-operacionais-de-plataforma-definidos-pelo-banco.md) — Parâmetros operacionais definidos pelo banco
