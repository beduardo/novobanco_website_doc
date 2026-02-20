# Pendências - HomeBanking Web HLD

**Última atualização:** 2026-01-21
**Documento de referência:** [COMENTARIOS-JGC-ANALISE.md](COMENTARIOS-JGC-ANALISE.md)

Este documento consolida todas as questões pendentes que requerem resposta ou validação do NovoBanco para completar o documento HLD.

---

## Legenda de Status

| Status | Significado |
|--------|-------------|
| [ ] | Pendente |
| [~] | Em discussão |
| [x] | Resolvido |

---

## 1. Pendências de Arquitetura (Cliente)

### 1.1 Serviços Azure

| # | Questão | Origem | Prioridade | Status |
|---|---------|--------|------------|--------|
| A1 | Quais serviços Azure são acedidos diretamente pelo BFF (fora do middleware BEST)? | Tema A, Comentário #1 | Alta | [ ] |
| A2 | Como esses serviços Azure transitam para a nova realidade do canal web? | Tema A, Comentário #1 | Alta | [ ] |

**Contexto:** O diagrama de arquitetura (SEC-03 3.2) inclui "Serviços Azure" como componente genérico. É necessário identificar especificamente quais serviços são utilizados.

### 1.2 Organização de Containers

| # | Questão | Origem | Prioridade | Status |
|---|---------|--------|------------|--------|
| A3 | Preferência por 1 container por layer "banco BEST" ou segregação diferente (por domínio, etc.)? | Tema A, Comentário #16 | Média | [ ] |

**Contexto:** Comentário JGC: "Uma coisa que era importante era tentar avaliar se queremos 1 container por layer 'banco best' ou se vamos segregar de alguma forma."

---

## 2. Pendências de Segurança

### 2.1 Credenciais e Login

| # | Questão | Origem | Prioridade | Status |
|---|---------|--------|------------|--------|
| S1 | Quais dados/credenciais são retornados no login da app mobile atualmente? | Tema E, Comentário #10 | **Crítica** | [ ] |
| S2 | Esses dados são seguros para exposição em ambiente web (menos protegido que nativo)? | Tema E, Comentário #10 | **Crítica** | [ ] |
| S3 | O PIN/password deve ser cifrado antes da transmissão (além de TLS)? | Tema E, Comentário #17 | Alta | [ ] |

**Contexto:** O ambiente web é menos protegido que o ambiente mobile nativo. Comentário JGC: "Um dos pontos que me parece que tem de ser mesmo revisto é o tema das credenciais retornadas no login."

**Ação Requerida:** Revisão de segurança específica para o canal web antes do go-live.

### 2.2 Controlos Anti-automation

| # | Questão | Origem | Prioridade | Status |
|---|---------|--------|------------|--------|
| S4 | Estratégia de CAPTCHA para o canal web? | SEC-07 | Média | [ ] |
| S5 | Rate limiting específico para login? | SEC-07 | Média | [ ] |
| S6 | Deteção de bots? | SEC-07 | Média | [ ] |

---

## 3. Pendências de Infraestrutura

### 3.1 Plataforma OpenShift

| # | Questão | Origem | Prioridade | Status |
|---|---------|--------|------------|--------|
| I1 | Qual a situação atual da plataforma OpenShift ("atual" vs "em homologação")? | Tema H, Comentário #48 | Média | [ ] |
| I2 | O projeto HomeBanking Web entra no cluster NB existente? | Tema H, Comentário #50 | Média | [ ] |
| I3 | Existe F5 em todos os ambientes (dev, qa, prod)? | Tema H, Comentário #50 | Média | [ ] |

### 3.2 Ambientes

| # | Questão | Origem | Prioridade | Status |
|---|---------|--------|------------|--------|
| I4 | Confirmar nomenclatura dos namespaces: `best-web-dev`, `best-web-qa`, `best-web-prod`? | Tema H, Comentário #50 | Média | [ ] |
| I5 | Descrição detalhada dos ambientes produtivos vs não produtivos? | Tema H, Comentário #50 | Baixa | [ ] |

### 3.3 CI/CD e Serviços Partilhados

| # | Questão | Origem | Prioridade | Status |
|---|---------|--------|------------|--------|
| I6 | Qual Container Registry será utilizado? Políticas de scanning? | SEC-10 | Alta | [ ] |
| I7 | Qual ferramenta de Secrets Management? Como injetar secrets nos pods? | SEC-10 | Alta | [ ] |
| I8 | Integração com pipeline CI/CD existente - validação necessária? | Tema I, Comentário #51 | Alta | [ ] |

**Ação Requerida:** Agendar sessão com equipa de infraestrutura do NovoBanco.

---

## 4. Pendências de Negócio/Produto

### 4.1 Estratégia de Cutover

| # | Questão | Origem | Prioridade | Status |
|---|---------|--------|------------|--------|
| N1 | Estratégia de switch do canal atual para o novo: big bang ou incremental? | Tema C, Comentário #4 | Alta | [ ] |
| N2 | Haverá coexistência temporária de canais? | Tema C | Média | [ ] |

**Contexto:** Comentário JGC: "Era relevante ver como fazemos o switch. Na realidade não existe MVP mas deveríamos definir se teremos uma estratégia de bigbang ou outra porque isto pode influenciar o desenho e a infraestrutura."

### 4.2 Performance

| # | Questão | Origem | Prioridade | Status |
|---|---------|--------|------------|--------|
| N3 | Valores reais de throughput da app mobile (pedidos/segundo normal e em pico)? | Tema D, Comentário #5 | Alta | [ ] |
| N4 | Projeção de crescimento para o canal web? | Tema D | Média | [ ] |
| N5 | Padrões de sazonalidade (fim de mês, períodos fiscais)? | Tema D | Média | [ ] |

**Contexto:** Comentário JGC: "É importante calibrar este valor. Pedidos/segundo normal e em pico." Os valores atuais (10 TPS, 400 utilizadores) são estimativas provisórias.

### 4.3 Sessões

| # | Questão | Origem | Prioridade | Status |
|---|---------|--------|------------|--------|
| N6 | Aprovar sessão exclusiva (novo login invalida sessão anterior)? | SEC-07 | Média | [ ] |
| N7 | Limite de sessões ativas por utilizador? | SEC-07 | Baixa | [ ] |

---

## 5. Pendências de Terceiros/Integrações

| # | Questão | Origem | Prioridade | Status |
|---|---------|--------|------------|--------|
| T1 | Lista completa de serviços fora do middleware BEST necessários para a solução? | Tema F, Comentário #11 | Alta | [ ] |
| T2 | Abertura de conta tem interações com terceiros? | Tema F, Comentário #11 | Média | [ ] |
| T3 | Notificações de confirmação de transferência existem na app mobile? | Tema F, Comentário #42 | Baixa | [ ] |

---

## 6. Pendências de Observabilidade

| # | Questão | Origem | Prioridade | Status |
|---|---------|--------|------------|--------|
| O1 | Confirmar que ELK Stack é a stack de logging a utilizar? | Tema J, Comentário #14 | Média | [ ] |
| O2 | Logging do frontend: implementar ou não? (custo/benefício vs desafios de segurança) | Tema J, Comentário #22 | Média | [ ] |
| O3 | Mascaramento vs cifragem de dados sensíveis nos logs (para auditoria/diagnóstico)? | Tema J, Comentário #54 | Média | [ ] |
| O4 | NB pode partilhar estrutura de logs existente para alinhar? | Tema J, Comentário #53 | Baixa | [ ] |

**Ação Requerida:** Agendar sessão com equipa de infraestrutura para observabilidade (Tema N).

---

## 7. Pendências de Design/Frontend

| # | Questão | Origem | Prioridade | Status |
|---|---------|--------|------------|--------|
| D1 | Agendar sessão específica de React para alinhar stack frontend? | Tema L, Comentário #20 | Média | [ ] |
| D2 | Quais alternativas existem na framework do NB para componentes? | Tema L, Comentário #20 | Média | [ ] |
| ~~D3~~ | ~~O que é a "Havas"?~~ | Tema L | - | [x] **Resolvido: Havas é a empresa responsável pelo design** |
| D4 | O que já foi alinhado com a Havas relativamente a componentes? | Tema L, Comentário #21 | Média | [ ] |

---

## 8. Pendências da Análise do Fluxo ApiPsd2

> **Origem:** Análise dos diagramas `customer_sequences/`
> **Data:** 2026-01-21

### 8.1 Autenticação e SCA

| # | Questão | Contexto | Prioridade | Status |
|---|---------|----------|------------|--------|
| P1 | Em que cenários `needStrongAuthentication` retorna "N"? | Diagrama mostra resposta com "N" - contradiz SCA obrigatório? | **Alta** | [ ] |
| P2 | O parâmetro `encrypt` indica que a password deve ser cifrada antes de enviar? Qual algoritmo? | AUT_004 tem `encrypt: "Y"` | Alta | [ ] |
| P3 | O `device_id` para web deve ser o User-Agent, um GUID persistente, ou outro valor? | Diagrama questiona isto | Média | [ ] |
| P4 | O `so_id` para web é "SPA"? Qual o mapeamento completo? | Diagrama usa "2" para mobile | Baixa | [ ] |

### 8.2 ApiPsd2 e Integração

| # | Questão | Contexto | Prioridade | Status |
|---|---------|----------|------------|--------|
| P5 | Existe documentação oficial da ApiPsd2? Podemos obter? | Necessário para implementação | **Alta** | [ ] |
| P6 | Lista completa de operações (AUT_*, DEV_*, CLI_*) necessárias para o canal web? | Diagrama mostra algumas | Alta | [ ] |
| P7 | Como funciona a renovação/refresh do apiToken? | Não documentado no diagrama | Alta | [ ] |

### 8.3 Segurança e Sessão

| # | Questão | Contexto | Prioridade | Status |
|---|---------|----------|------------|--------|
| P8 | O `sasToken` pode ser completamente ignorado no canal web? | Cliente nota que não faz sentido para web | Média | [ ] |
| P9 | A assinatura SHA256 usa exatamente a fórmula documentada? | Confirmar algoritmo | Alta | [ ] |

### 8.4 Transferências

| # | Questão | Contexto | Prioridade | Status |
|---|---------|----------|------------|--------|
| P10 | Documentação detalhada das APIs COPS e VOP? | Validação de titular | Alta | [ ] |
| P11 | Diagrama de sequência para transferências não-SEPA? | Processo complexo | Média | [ ] |
| P12 | Biblioteca de validação de IBAN preferida? | IbanNet (.NET) sugerido | Baixa | [ ] |

---

## Resumo por Prioridade

### Críticas (resolver antes de avançar)
- S1, S2 - Revisão de credenciais no login
- P1 - SCA condicional (needStrongAuthentication)

### Altas (resolver em breve)
- A1, A2 - Serviços Azure
- S3 - Cifra de PIN
- N1 - Estratégia de cutover
- N3 - Throughput
- T1 - Serviços fora do BEST
- I6, I7, I8 - CI/CD e infra
- P2, P5, P6, P7, P9, P10 - Documentação ApiPsd2 e APIs

### Médias (resolver durante o projeto)
- A3 - Organização de containers
- S4, S5, S6 - Anti-automation
- I1-I5 - Plataforma e ambientes
- N2, N5, N6 - Sessões e coexistência
- T2 - Abertura de conta
- O1-O3 - Observabilidade
- D1-D4 - Design/Frontend

### Baixas (podem aguardar)
- T3 - Notificações existentes
- O4 - Estrutura de logs

---

## Sessões Requeridas

| Sessão | Participantes | Temas a Abordar |
|--------|---------------|-----------------|
| **Infraestrutura** | Equipa Infra NB | I1-I8, O1-O4 |
| **Segurança** | Equipa Segurança NB | S1-S6 |
| **React/Frontend** | Equipa Dev NB + Havas | D1-D4 |
| **Arquitetura** | Arquitetura NB | A1-A3, T1-T2 |
| **Produto** | PO + Negócio | N1-N7 |

---

## Histórico de Atualizações

| Data | Ação |
|------|------|
| 2026-01-21 | Criação do documento com pendências dos temas A, B, E, G, H, I |
| 2026-01-21 | Adicionada pendência N5 (sazonalidade) do Tema D |
| 2026-01-21 | Tema J (Observabilidade) processado - questões O1-O4 já documentadas |
| 2026-01-21 | Tema L (Design System) processado - questões D1-D3 já documentadas |
| 2026-01-21 | Tema N (Observabilidade) processado - sessão com infra já documentada |
| 2026-01-21 | **Todos os 14 temas dos comentários JGC processados** |
| 2026-01-21 | **Secção 8 adicionada** - Pendências da análise dos diagramas de sequência (ApiPsd2, ApiBBest, Transferências) |
