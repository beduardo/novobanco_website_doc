---
id: DEC-011
title: Diagrama de Arquitetura Único
status: accepted
date: 2026-01-20
decision-makers:
  - NextReality
  - NovoBanco DSI
consulted:
  - Jorge Gomes Costa
tags:
  - nextreality-novobanco-website-decisions
  - decisions
  - arquitetura
  - diagramas
---

# DEC-011: Diagrama de Arquitetura Único

## Contexto

O documento HLD contém múltiplos diagramas de arquitetura em diferentes seções (SEC-01, SEC-03, SEC-05, SEC-09) que apresentam visões semelhantes da arquitetura do sistema. Conforme feedback do cliente (JGC), estes diagramas:

1. Não estavam consistentes entre si
2. Não refletiam corretamente o modelo discutido nas sessões
3. Tornavam a manutenção difícil (alterações requeriam atualização em múltiplos locais)

## Decisão

**Utilizar apenas um diagrama de arquitetura de referência, localizado na Seção 3.2 (Diagrama Conceptual).**

Todas as outras seções que necessitem referenciar a arquitetura devem apontar para o diagrama da seção 3.2, em vez de duplicar o diagrama.

## Justificação

1. **Manutenção simplificada** - Alterações à arquitetura requerem atualização em apenas um local
2. **Consistência garantida** - Elimina risco de diagramas ficarem dessincronizados
3. **Alinhamento com feedback do cliente** - JGC sugeriu "fazer um boneco com isto e referenciar"
4. **Clareza** - Um único diagrama de referência evita confusão sobre qual é a versão correta

## Consequências

### Positivas

- Documento mais fácil de manter
- Consistência garantida entre seções
- Redução de erros por divergência de diagramas

### Negativas

- Seções específicas perdem contexto visual imediato
- Leitores precisam navegar até seção 3.2 para ver a arquitetura

### Mitigação

- Incluir referência clara ao diagrama 3.2 em cada seção relevante
- Manter diagramas de detalhe específicos quando necessário (ex: fluxos de autenticação, sequências)

## Seções Afetadas

| Seção | Diagrama Atual | Ação |
|-------|----------------|------|
| SEC-01 (1.4) | Diagrama 1 - Visão Geral | Remover, referenciar SEC-03 3.2 |
| SEC-03 (3.2) | Diagrama 3 - Conceptual C4 | **MANTER como referência principal** |
| SEC-03 (3.5) | Diagrama 5 - Integração | Avaliar se é detalhe ou duplicação |
| SEC-05 (5.1) | Diagrama 10 - Decomposição | Avaliar se é detalhe ou duplicação |
| SEC-05 (5.2) | Diagrama 11 - BFF | Manter como detalhe do BFF |
| SEC-09 (9.1) | Diagrama 25 - Integração | Remover, referenciar SEC-03 3.2 |
| SEC-09 (9.2) | Diagrama 26 - Core Banking | Manter como detalhe de integração |

## Diagramas a Manter (Detalhes Específicos)

Os seguintes diagramas de **detalhe** devem ser mantidos pois mostram aspectos específicos não cobertos pelo diagrama principal:

1. Diagramas de fluxo/sequência (autenticação, operações)
2. Diagramas de componentes internos (BFF, Frontend)
3. Diagramas de infraestrutura (CI/CD, containers)

## Referências

- Comentário JGC #40 (reply): "A minha sugestão seria fazer um boneco com isto e referenciar"
- Comentário JGC #1 (reply 2): "Já vi que mais abaixo têm um boneco mais fiel ao que falámos. Porquê de aqui estar diferente?"
- Comentário JGC #12 (reply): "O 3.2 já está alinhado. Porque a diferença?"
