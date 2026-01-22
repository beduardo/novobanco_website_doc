# IMPLEMENTACAO_GW_DIFF

> **Tipo:** Documento de trabalho temporário
> **Objetivo:** Instruções para atualização do HLD com base no diagrama de arquitetura do cliente
> **Fonte:** Análise do ficheiro `customer_sequences/CENARIOS_API_GW.txt`
> **Data:** 2026-01-21

---

## 1. Contexto

Foi recebido do cliente um diagrama de sequência (`customer_sequences/CENARIOS_API_GW.txt`) que apresenta diferentes cenários de arquitetura para integração entre canais (App, SPA) e backend (Siebel). Após análise comparativa com o HLD atual, foram identificados gaps que necessitam de ajustes na documentação.

### 1.1 Cenário Alvo (Omni + Alternativas)

O cenário a documentar no HLD é o **cenário apigw + omni ALTERNATIVAS** do diagrama do cliente:

```
SPA → F5 → BFF → ApiGw → MS/Siebel
```

Onde:
- **SPA**: HomeBanking Web (React)
- **F5**: Componente de infraestrutura na entrada (a adicionar)
- **BFF**: Backend for Frontend (.NET 8) - Lógica de UI
- **ApiGw**: API Gateway (IBM)
- **MS**: Microservices - Lógica de Negócio (nova camada)
- **Siebel**: Backend principal existente

---

## 2. Alterações Requeridas

### 2.1 Adicionar F5 ao Diagrama de Arquitetura

**Ficheiro:** `sections/SEC-03-visao-geral-solucao.md`

**Localização:** Secção 3.2 Diagrama Conceptual (diagrama PlantUML)

**O que fazer:**
1. Adicionar o componente F5 entre o "Canal Web" e a "Camada BFF"
2. O F5 deve aparecer como componente de infraestrutura existente (cor verde)
3. O fluxo deve ser: `WEB --> F5 --> BFF`
4. Não é necessário especificar se é WAF ou Load Balancer - apenas "F5"

**Porquê:**
O F5 é um componente de infraestrutura existente no ambiente do cliente que faz parte do fluxo de comunicação. Omiti-lo do diagrama criaria uma representação incompleta da arquitetura real.

**Alteração no PlantUML:**

Adicionar após o package "Canal Web":
```plantuml
package "Infraestrutura de Entrada" #LightGreen {
    [F5] as F5
}
```

Alterar o fluxo de:
```plantuml
WEB --> BFF : Cookie Sessão\n(HTTPS/REST)
```

Para:
```plantuml
WEB --> F5 : Protocolo Omni
F5 --> BFF : Protocolo Omni
```

---

### 2.2 Substituir REST por Protocolo Omni

**Ficheiros a alterar:**
- `sections/SEC-03-visao-geral-solucao.md`
- `definitions/DEF-05-arquitetura-bff.md`
- `definitions/DEF-05-api-design.md`
- `sections/SEC-05-arquitetura-backend-servicos.md` (se existir referência)

**O que fazer:**
1. Substituir referências a "REST" ou "HTTPS/REST" por "Protocolo Omni" quando se tratar da comunicação entre SPA ↔ F5 ↔ BFF
2. Manter "REST" para comunicação BFF → API Gateway (protocolo BEST)
3. Adicionar nota explicativa sobre o Protocolo Omni

**Porquê:**
O "Protocolo Omni" é uma abstração/padronização sobre REST utilizada pelo cliente. Usar esta nomenclatura alinha o HLD com a terminologia interna do cliente.

**Nota a adicionar (sugestão de localização: DEF-05-api-design.md ou SEC-05):**

```markdown
### Protocolo Omni

O Protocolo Omni é uma padronização sobre REST utilizada para comunicação entre o canal web (SPA) e o BFF. Esta abstração permite:
- Uniformização de contratos entre canais
- Evolução controlada das interfaces
- Separação clara entre protocolo de canal (Omni) e protocolo de backend (BEST)

| Origem | Destino | Protocolo |
|--------|---------|-----------|
| SPA | F5 | Omni |
| F5 | BFF | Omni |
| BFF | API Gateway | BEST (REST) |
| API Gateway | MS/Siebel | Siebel/BEST |
```

---

### 2.3 Adicionar Camada de Microservices (MS)

**Ficheiros a alterar:**
- `sections/SEC-03-visao-geral-solucao.md` (diagrama e descrição)
- `definitions/DEF-05-arquitetura-bff.md` (responsabilidades)
- `decisions/DEC-007-padrao-bff.md` (atualizar se necessário)

**O que fazer:**

#### No Diagrama (SEC-03):
1. Adicionar package "Microservices" entre API Gateway e Backend Services
2. Representar como componente novo (azul) - ainda a desenvolver
3. Indicar que a lista de MS está pendente

**Alteração no PlantUML de SEC-03:**

Adicionar após o package "Gateway":
```plantuml
package "Microservices" #LightBlue {
    [Microservices\n(Lógica de Negócio)] as MS
    note right of MS
      Containers OpenShift
      Regras de Negócio
      **PENDENTE: Identificar MS**
    end note
}
```

Adicionar fluxos:
```plantuml
BFF --> APIGW : clientid + secret\n(Protocolo BEST)
APIGW --> MS : Bearer Token
APIGW --> SIEBEL : Bearer Token
MS --> SIEBEL : Protocolo Siebel
```

#### Na descrição de responsabilidades:

**BFF - Responsabilidades (atualizar em DEF-05-arquitetura-bff.md):**
- Lógica de UI/Apresentação
- Agregação de dados para o canal web
- Transformação de formatos
- Gestão de sessão web
- Orquestração de chamadas

**MS - Responsabilidades (adicionar):**
- Lógica de Negócio
- Regras de domínio
- Operações que requerem processamento além do Siebel
- Serviços partilháveis entre canais (futuramente)

**Porquê:**
A camada de Microservices permite:
1. Implementar lógica de negócio fora do Siebel (agilidade)
2. Separar claramente lógica de UI (BFF) de lógica de negócio (MS)
3. Criar serviços reutilizáveis entre canais
4. Mesma stack tecnológica que o BFF (.NET)

---

### 2.4 Atualizar Tabela de Fluxo de Autenticação

**Ficheiro:** `sections/SEC-03-visao-geral-solucao.md`

**Localização:** Secção "Fluxo de Autenticação" (tabela)

**Alterar de:**
```markdown
| Origem | Destino | Mecanismo |
|--------|---------|-----------|
| Frontend Web | BFF | Cookie de Sessão (HttpOnly, Secure) |
| BFF | API Gateway | ClientID + ClientSecret |
| API Gateway | Backend Services | Bearer Token (propagado) |
| Siebel | - | **Validação do Token** |
```

**Para:**
```markdown
| Origem | Destino | Mecanismo | Protocolo |
|--------|---------|-----------|-----------|
| SPA | F5 | Cookie de Sessão (HttpOnly, Secure) | Omni |
| F5 | BFF | Cookie de Sessão (propagado) | Omni |
| BFF | API Gateway | ClientID + ClientSecret | BEST |
| API Gateway | MS | Bearer Token (propagado) | BEST |
| API Gateway | Siebel | Bearer Token (propagado) | Siebel |
| MS | Siebel | Protocolo Siebel | Siebel |
```

---

### 2.5 Atualizar Tabela de Componentes Principais

**Ficheiro:** `sections/SEC-03-visao-geral-solucao.md`

**Localização:** Secção 3.3 Componentes Principais

**Adicionar linha para F5 e MS:**

```markdown
| Componente | Tipo | Responsabilidade | Tecnologia |
|------------|------|------------------|------------|
| **HomeBanking Web** | Frontend SPA | Interface do utilizador, experiência web responsiva | React |
| **F5** | Infraestrutura | Entrada de tráfego web | Existente |
| **BFF Web** | Backend | Lógica de UI, agregação, transformação, orquestração | .NET 8 |
| **Microservices** | Backend | Lógica de Negócio, regras de domínio | .NET 8 |
| **API Gateway** | Infraestrutura | Roteamento, rate limiting, autenticação | IBM (Existente) |
| **Backend Services (Siebel)** | Serviços | Lógica de negócio core, integrações | Existente |
| **ELK Stack** | Observabilidade | Logs centralizados, métricas, dashboards | Existente |
```

---

### 2.6 Atualizar Legenda do Diagrama

**Ficheiro:** `sections/SEC-03-visao-geral-solucao.md`

**Adicionar na legenda:**

```markdown
| Cor | Significado |
|-----|-------------|
| Azul | Componentes novos (a desenvolver): SPA, BFF, MS |
| Verde | Componentes existentes (reutilizar): F5, API Gateway, Siebel |
| Amarelo | Componentes a detalhar (pendente) |
| Cinza | Infraestrutura transversal |
```

---

### 2.7 Adicionar Pendência para Lista de MS

**Ficheiro:** `sections/SEC-03-visao-geral-solucao.md`

**Localização:** Secção "Pendências de Detalhe"

**Adicionar:**

```markdown
| Item | Descrição | Responsável |
|------|-----------|-------------|
| Serviços Azure | Identificar quais serviços Azure são acedidos diretamente pelo BFF | NovoBanco |
| Outros Backend Services | Identificar serviços além do Siebel | NovoBanco |
| **Lista de Microservices** | **Identificar quais MS serão desenvolvidos e suas responsabilidades** | **NovoBanco/NextReality** |
```

---

## 3. Resumo de Ficheiros a Alterar

| Ficheiro | Alterações |
|----------|------------|
| `sections/SEC-03-visao-geral-solucao.md` | Diagrama PlantUML, tabelas de fluxo e componentes, legenda, pendências |
| `definitions/DEF-05-arquitetura-bff.md` | Responsabilidades BFF (apenas UI), adicionar referência a MS |
| `definitions/DEF-05-api-design.md` | Adicionar secção sobre Protocolo Omni |
| `decisions/DEC-007-padrao-bff.md` | Revisar para incluir separação BFF (UI) vs MS (Negócio) se necessário |

---

## 4. Diagrama Alvo (Referência Visual)

O diagrama final deve representar:

```
┌─────────────────────────────────────────────────────────────────────┐
│                                                                     │
│   ┌─────────┐     ┌─────┐     ┌─────────┐     ┌─────────────┐      │
│   │   SPA   │────▶│ F5  │────▶│   BFF   │────▶│ API Gateway │      │
│   │ (React) │     │     │     │ (.NET)  │     │    (IBM)    │      │
│   └─────────┘     └─────┘     └─────────┘     └──────┬──────┘      │
│       │              │             │                  │             │
│       │   Protocolo  │  Protocolo  │    Protocolo     │             │
│       │     Omni     │    Omni     │      BEST        │             │
│                                                       │             │
│                                          ┌────────────┴─────────┐   │
│                                          │                      │   │
│                                          ▼                      ▼   │
│                                    ┌──────────┐          ┌────────┐ │
│                                    │    MS    │─────────▶│ Siebel │ │
│                                    │ (.NET)   │          │        │ │
│                                    └──────────┘          └────────┘ │
│                                          │                    │     │
│                                    Lógica de            Lógica de   │
│                                     Negócio              Negócio    │
│                                                           Core      │
│                                                                     │
│   ═══════════════════════════════════════════════════════════════   │
│   AZUL = Novo (SPA, BFF, MS)    VERDE = Existente (F5, GW, Siebel)  │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

---

## 5. Validações Após Implementação

Após aplicar as alterações, verificar:

1. [ ] O diagrama PlantUML renderiza corretamente
2. [ ] Todas as referências a "REST" na comunicação SPA↔BFF foram substituídas por "Protocolo Omni"
3. [ ] F5 aparece no fluxo entre SPA e BFF
4. [ ] MS aparece como camada entre API Gateway e Siebel
5. [ ] Tabelas de componentes e fluxos estão atualizadas
6. [ ] Pendência de "Lista de Microservices" foi adicionada

---

## 6. Notas Adicionais

- **Não documentar:** A estratégia de migração gradual da App para o BFF não deve ser mencionada no HLD
- **Protocolo BEST:** Manter referência ao "protocolo BEST" para comunicação BFF → API Gateway (é o protocolo existente do banco)
- **Protocolo Siebel:** Manter referência ao "protocolo Siebel" para comunicação API Gateway/MS → Siebel

---

**Fim do documento de instruções**
