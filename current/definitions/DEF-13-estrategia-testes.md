---
id: DEF-13-estrategia-testes
aliases:
  - Estrategia de Testes
tags:
  - nextreality-novobanco-website-definitions
  - definitions
  - testing
  - quality-assurance
  - automation
approved: true
created: 2026-01-08
hubs:
  - "[[nextreality]]"
para-code: R
reviewed: true
status: structure
---

# DEF-13: Estrategia de Testes

> **Related section:** [13 - Estrategia de Testes](../sections/SEC-13-estrategia-testes.md)

## Context

Definir a estrategia de testes do HomeBanking Web, incluindo testes unitarios, integracao, contrato, E2E, performance, seguranca, acessibilidade, test data management e matriz de responsabilidades.

## Questions to Answer

### Testes Unitarios

> **Nota:** Frameworks definidos em [DEF-04-stack-frontend.md](DEF-04-stack-frontend.md): Vitest (frontend), .NET xUnit (BFF)

1. Qual a cobertura de codigo minima requerida?
    Necessita aprofundamento. Sugestao: 80% para codigo critico

2. Os testes unitarios bloqueiam o pipeline se falharem?
    Sim (quality gate em DEF-10)

### Testes de Integracao

3. Como sao mockados os servicos externos?
    Necessita aprofundamento. Opcoes: WireMock, TestContainers

4. Ha ambiente dedicado para testes de integracao?
    Ambiente QA (DEF-10)

### Testes de Contrato

5. Sera utilizado contract testing (ex: Pact)?
    Necessita aprofundamento. Recomendado para BFF<->Backend

### Testes E2E

> **Nota:** Framework definido em [DEF-04-stack-frontend.md](DEF-04-stack-frontend.md): Playwright

6. Quais cenarios criticos serao cobertos?
    Necessita aprofundamento. Minimo: login, transferencias, consultas

7. Os testes E2E bloqueiam o pipeline?
    Necessita aprofundamento

### Testes de Performance

> **Nota:** Ver [DEF-12-desempenho-fiabilidade.md](DEF-12-desempenho-fiabilidade.md) para load testing

8. Quando sao executados os testes de performance?
    Necessita aprofundamento. Sugestao: antes de cada release major

### Testes de Seguranca

> **Nota:** SAST definido em [DEF-10-arquitetura-operacional.md](DEF-10-arquitetura-operacional.md)

9. Ha penetration testing periodico?
    Necessita aprofundamento. Minimo: antes do go-live

### Testes de Acessibilidade

> **Nota:** WCAG definido em [DEF-04-design-system.md](DEF-04-design-system.md)

10. Ha testes automatizados de acessibilidade?
    Necessita aprofundamento. Opcoes: axe-core, Lighthouse

### Test Data Management (Simplificado)

11. Ha ambiente com dados anonimizados de producao?
    Necessita aprofundamento

### Testes de Aceitacao (Simplificado)

12. Ha ambiente UAT dedicado?
    Ambiente QA (DEF-10)

13. Quais os criterios de aceitacao?
    Necessita aprofundamento

## Decisions

### Unit Testing Framework
- **Decision:** _Pending_
- **Justification:** _Pending_
- **Alternatives considered:** _Pending_

### E2E Testing Framework
- **Decision:** _Pending_
- **Justification:** _Pending_
- **Alternatives considered:** _Pending_

### Contract Testing
- **Decision:** _Pending_
- **Justification:** _Pending_
- **Alternatives considered:** _Pending_

### Security Testing
- **Decision:** _Pending_
- **Justification:** _Pending_
- **Alternatives considered:** _Pending_

## Known Constraints

- Quality gates definidos (Coverage + SAST) - DEF-10
- Pipeline CI/CD em Azure DevOps - DEF-10
- Ambientes: dev, qa, prod - DEF-10
- Requisitos de seguranca bancaria

## Related Decisions

- [DEC-009-stack-tecnologica-frontend.md](../decisions/DEC-009-stack-tecnologica-frontend.md) - Stack frontend (framework de testes)
- [DEC-010-stack-tecnologica-backend.md](../decisions/DEC-010-stack-tecnologica-backend.md) - Stack backend (framework de testes)

## References

- [DEF-10-arquitetura-operacional.md](DEF-10-arquitetura-operacional.md) - CI/CD e Quality Gates
- [DEF-08-seguranca-conformidade.md](DEF-08-seguranca-conformidade.md) - Requisitos de seguranca
- [DEF-02-requisitos-nao-funcionais.md](DEF-02-requisitos-nao-funcionais.md) - NFRs
- Testing Trophy (Kent C. Dodds)
- OWASP Testing Guide
- WCAG 2.1 Guidelines
