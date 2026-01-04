---
aliases:
  - Seguranca e Conformidade
tags:
  - nextreality-novobanco-website-sections
  - sections
  - security
  - compliance
  - psd2
  - gdpr
approved: true
created: 2026-01-03
hubs:
  - "[[nextreality]]"
para-code: R
reviewed: true
status: in-progress
---

# 8. Seguranca & Conformidade

> **Definicoes requeridas:**
> - [DEF-08-seguranca-conformidade.md](../definitions/DEF-08-seguranca-conformidade.md) - Status: completed
>
> **Decisoes relacionadas:**
> - [DEC-004-controlos-seguranca-frontend.md](../decisions/DEC-004-controlos-seguranca-frontend.md) - Status: accepted

## Proposito

Definir os requisitos de seguranca e conformidade regulatoria do HomeBanking Web, incluindo modelo de ameacas, controlos de seguranca, e conformidade com PSD2, RGPD, PCI-DSS e regulamentacao do Banco de Portugal.

## Conteudo

### 8.1 Visao Geral de Seguranca

```plantuml
@startuml
skinparam backgroundColor #FEFEFE

title Camadas de Seguranca - HomeBanking Web

rectangle "Seguranca em Camadas" {
    rectangle "Frontend" #LightBlue {
        [Security Headers]
        [XSS Protection]
        [SRI]
    }

    rectangle "BFF" #LightGreen {
        [CSRF Tokens]
        [Input Validation]
        [Session Management]
    }

    rectangle "Infraestrutura" #Yellow {
        [WAF]
        [TLS]
        [Rate Limiting]
    }

    rectangle "Conformidade" #LightCoral {
        [PSD2]
        [RGPD]
        [PCI-DSS]
        [BdP]
    }
}

@enduml
```

### 8.2 Modelo de Ameacas

| Aspecto | Status |
|---------|--------|
| **Threat modeling realizado** | Nao (acao pendente) |
| **Principais ameacas identificadas** | _A definir_ |
| **Metodologia** | _A definir_ (STRIDE ou PASTA) |

### 8.3 Controlos de Seguranca

#### 8.3.1 Security Headers HTTP

| Header | Valor | Justificacao |
|--------|-------|--------------|
| **Content-Security-Policy** | `self` (inicial) | Prevencao XSS, expandir conforme necessario |
| **X-Frame-Options** | `SAMEORIGIN` | Prevencao Clickjacking |
| **X-Content-Type-Options** | `nosniff` | Prevencao MIME sniffing |
| **Strict-Transport-Security** | `max-age` a definir | Forca HTTPS |

#### 8.3.2 Subresource Integrity (SRI)

| Aspecto | Decisao |
|---------|---------|
| **Estrategia** | Bibliotecas servidas localmente |
| **Atributos** | `integrity` e `crossorigin` em recursos externos |
| **CDN** | Evitar; se necessario, atencao a atualizacoes de terceiros |

#### 8.3.3 Protecao XSS

```plantuml
@startuml
skinparam backgroundColor #FEFEFE

title Controlos XSS - Por Camada

rectangle "SSR/BFF" #LightGreen {
    [Escape de saida HTML]
    [Validacao de entrada]
    [Sanitizacao de entrada]
}

rectangle "Frontend React" #LightBlue {
    [React auto-escape]
    [innerHTML proibido]
    [eval proibido]
}

rectangle "Ferramentas" #Yellow {
    [ESLint rules]
    [SonarQube]
}

@enduml
```

| Camada | Controlo |
|--------|----------|
| **SSR/BFF** | Escape de saida HTML, validacao e sanitizacao de entrada |
| **React** | Escape automatico em JSX |
| **Lint/SAST** | `innerHTML` e `eval` proibidos via lint e SonarQube |

#### 8.3.4 Protecao CSRF

| Controlo | Implementacao |
|----------|---------------|
| **Tokens CSRF** | Rotacionados por request |
| **Cookie de sessao** | `SameSite=Strict`, `Secure`, `HttpOnly` |
| **CORS** | Configurado restritivamente |
| **Metodos seguros** | GET somente idempotentes |

#### 8.3.5 Controlos Backend/BFF

| Aspecto | Status |
|---------|--------|
| Input validation | Detalhes no assessment inicial |
| WAF | _A definir_ com equipa de infraestrutura |

### 8.4 OWASP Top 10

| Categoria | Status |
|-----------|--------|
| Controlos especificos | _A definir_ |
| SAST/DAST no pipeline | _A definir_ |
| Frequencia de scans | _A definir_ |

### 8.5 Conformidade PSD2

```plantuml
@startuml
skinparam backgroundColor #FEFEFE

title Conformidade PSD2 - HomeBanking Web

rectangle "Requisitos PSD2" {
    rectangle "SCA" #LightGreen {
        [Todas as operacoes]
        note bottom : Sem isencoes
    }

    rectangle "Dynamic Linking" #Yellow {
        [Valor + Beneficiario]
        note bottom : Estrutura app\nja segue PSD2\n(a aprofundar)
    }

    rectangle "Comunicacao Segura" #LightGreen {
        [TLS 1.2+]
    }
}

@enduml
```

| Requisito | Decisao |
|-----------|---------|
| **SCA obrigatorio** | Sim, todas as operacoes |
| **Isencoes SCA** | Nenhuma |
| **Dynamic Linking** | Estrutura app ja segue PSD2 (a aprofundar) |
| **TLS** | 1.2+ (versao especifica a definir) |

### 8.6 Conformidade RGPD

| Aspecto | Status |
|---------|--------|
| Base legal para tratamento | _A definir_ |
| Consentimento | _A definir_ |
| DPO designado | _A definir_ |
| ROPA | _A definir_ |

### 8.7 PCI-DSS

| Aspecto | Status |
|---------|--------|
| Processamento de PAN | _A definir_ |
| Nivel de conformidade | _A definir_ |
| Tokenizacao de cartoes | _A definir_ |

### 8.8 Banco de Portugal

| Aspecto | Status |
|---------|--------|
| Requisitos regulatorios BdP | _A definir_ |
| Requisitos de reporte | _A definir_ |

### 8.9 Registo de Auditoria

| Aspecto | Status |
|---------|--------|
| Eventos a registar | _A definir_ |
| Formato de logs | _A definir_ |
| Periodo de retencao | _A definir_ |
| Imutabilidade | _A definir_ |

### 8.10 Resposta a Incidentes

| Aspecto | Status |
|---------|--------|
| Plano de resposta | _A definir_ |
| SLAs de resposta | _A definir_ |
| CSIRT | _A definir_ |

### 8.11 Gestao de Vulnerabilidades

| Aspecto | Status |
|---------|--------|
| Processo de gestao | _A definir_ |
| SLAs de correcao | _A definir_ |
| Bug bounty | _A definir_ |

### 8.12 Segregacao de Ambientes

| Aspecto | Status |
|---------|--------|
| Segregacao (dev/staging/prod) | _A definir_ |
| Segregacao de dados | _A definir_ |

## Entregaveis

- [ ] Modelo de ameacas documentado - Pendente
- [x] Matriz de controlos de seguranca - Parcial
- [ ] Checklist OWASP Top 10 - Pendente
- [x] Matriz de conformidade PSD2 - Parcial
- [ ] Matriz de conformidade RGPD - Pendente
- [ ] Avaliacao PCI-DSS - Pendente
- [ ] Requisitos Banco de Portugal - Pendente
- [ ] Especificacao de audit logging - Pendente
- [ ] Plano de resposta a incidentes - Pendente
- [ ] Processo de gestao de vulnerabilidades - Pendente

## Definicoes Utilizadas

- [x] [DEF-08-seguranca-conformidade.md](../definitions/DEF-08-seguranca-conformidade.md) - Status: completed

## Decisoes Referenciadas

- [x] [DEC-004-controlos-seguranca-frontend.md](../decisions/DEC-004-controlos-seguranca-frontend.md) - Status: accepted

## Itens Pendentes

| Item | Documento | Responsavel |
|------|-----------|-------------|
| Threat modeling | DEF-08-seguranca-conformidade | Seguranca |
| Metodologia threat modeling | DEF-08-seguranca-conformidade | Seguranca |
| max-age HSTS | DEF-08-seguranca-conformidade | Seguranca |
| WAF (definicao) | DEF-08-seguranca-conformidade | Infraestrutura |
| Controlos OWASP Top 10 | DEF-08-seguranca-conformidade | Seguranca |
| SAST/DAST no pipeline | DEF-08-seguranca-conformidade | DevOps |
| Frequencia de scans | DEF-08-seguranca-conformidade | Seguranca |
| Dynamic Linking (aprofundar) | DEF-08-seguranca-conformidade | Arquitetura |
| Base legal RGPD | DEF-08-seguranca-conformidade | DPO |
| Consentimento RGPD | DEF-08-seguranca-conformidade | DPO |
| DPO designado | DEF-08-seguranca-conformidade | Legal |
| ROPA | DEF-08-seguranca-conformidade | DPO |
| PCI-DSS avaliacao | DEF-08-seguranca-conformidade | Compliance |
| Requisitos BdP | DEF-08-seguranca-conformidade | Compliance |
| Audit logging | DEF-08-seguranca-conformidade | Arquitetura |
| Resposta a incidentes | DEF-08-seguranca-conformidade | Seguranca |
| Gestao de vulnerabilidades | DEF-08-seguranca-conformidade | Seguranca |
| Segregacao de ambientes | DEF-08-seguranca-conformidade | Infraestrutura |
