---
id: "DEC-012"
title: "Comunicacao de Janelas de Manutencao ao Cliente"
status: "proposed"
created: 2026-03-26
context: "DEF-25"
affects-definitions:
  - "DEF-10"
  - "DEF-20"
  - "DEF-25"
affects-sections:
  - "SEC-04"
  - "SEC-10"
  - "SEC-12"
  - "SEC-15"
---

# DEC-012: Comunicacao de Janelas de Manutencao ao Cliente

## Context

O HomeBanking Web tem janelas de manutencao definidas (DEF-25): deploys standard em dias uteis (9h-18h) e deploys major aos sabados (6h-10h). A estrategia de deploy e rolling update com zero downtime (DEF-20), mas em cenarios de manutencao major ou indisponibilidade, o cliente precisa de informacao clara sobre o estado do servico.

Existem tres cenarios de comunicacao:

1. **Pre-manutencao** -- Avisar antecipadamente que havera uma janela de manutencao programada
2. **Durante manutencao (site operacional)** -- Informar que funcionalidades podem estar degradadas
3. **Site indisponivel** -- Apresentar pagina informativa quando o site nao esta acessivel

Esta decisao origina-se da necessidade de garantir transparencia com o cliente, alinhada com os padroes de feedback definidos em DEF-10 (toasts e modais) e com a meta de disponibilidade de 99.9% (DEF-22).

## Decision

### Pagina de Manutencao (Site Indisponivel)

Quando o site estiver completamente indisponivel durante uma janela de manutencao, o **F5 BIG-IP (Load Balancer)** sera responsavel por servir uma pagina estatica de manutencao. Esta pagina sera apresentada automaticamente quando os pods do frontend nao estiverem a responder aos health checks.

- O F5 redireciona o trafego para uma pagina estatica alojada externamente ao cluster
- A pagina nao depende da infraestrutura do HomeBanking Web (cluster, BFF, backend)
- O conteudo e apresentacao da pagina estatica serao definidos durante o desenvolvimento

### Questoes a Definir Durante o Desenvolvimento

As seguintes questoes devem ser respondidas pela equipa de negocio e desenvolvimento durante a fase de implementacao:

**Q1: Estrategia de aviso pre-manutencao**
- Como e quando avisar o cliente antecipadamente sobre manutencoes programadas?
- Com quantas horas/dias de antecedencia?
- Formato do aviso (banner, toast, modal, email)?
- **Responsavel:** Equipa de Negocio

**Q2: Fonte de informacao das janelas de manutencao**
- As janelas de manutencao devem ser geridas por API, feature flags, CMS ou configuracao estatica?
- Como o frontend obtem a informacao de manutencao programada?
- **Responsavel:** Equipa de Desenvolvimento

**Q3: Conteudo da mensagem de manutencao**
- Deve incluir previsao de retorno (horario estimado)?
- Deve indicar canais alternativos (app mobile, telefone, balcao)?
- Que informacao apresentar na pagina estatica do F5?
- **Responsavel:** Equipa de Negocio

## Consequences

### Positivas

- **Independencia da infraestrutura**: A pagina de manutencao servida pelo F5 garante que o cliente ve informacao mesmo com o cluster completamente indisponivel
- **Transparencia**: O cliente e informado sobre o estado do servico, reduzindo frustacao e contactos ao suporte
- **Flexibilidade**: As questoes em aberto permitem que as decisoes de UX e negocio sejam tomadas com mais contexto durante o desenvolvimento

### Negativas / Trade-offs

- **Dependencia do F5**: A configuracao da pagina de manutencao depende da equipa de infraestrutura/rede
- **Questoes em aberto**: Tres aspectos importantes ficam para a fase de desenvolvimento, o que pode atrasar a implementacao se nao forem priorizados
- **Coordenacao necessaria**: A ativacao da pagina de manutencao requer coordenacao entre DevOps (deploy) e Infra (F5)

### Implicacoes

- DEF-20 (Arquitetura Operacional) deve incluir o procedimento de ativacao da pagina de manutencao no F5 como parte dos runbooks
- DEF-10 (UX Guidelines) devera ser atualizada com os padroes de comunicacao de manutencao quando Q1 e Q3 forem respondidas
- DEF-25 (Governacao) deve referenciar esta decisao no processo de gestao de mudanca
