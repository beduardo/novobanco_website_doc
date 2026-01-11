# Questoes para Reuniao com Cliente

**Data:** 2026-01-11
**Projeto:** HomeBanking Web - HLD
**Objetivo:** Esclarecer questoes de escopo e requisitos pendentes

---

## 1. Escopo do Projeto

### Canais e Aplicacoes

- O canal web deve suportar apenas browser desktop/mobile ou tambem aplicacoes hibridas (React Native)?
- As aplicacoes nativas iOS e Android estao no escopo deste projeto?
- O CMS e backoffice estao no escopo ou sao projetos separados?
- Qual o sistema legado existente que sera substituido ou coexistira com o novo HomeBanking?

### Funcionalidades

- Quais funcionalidades fazem parte do MVP (Minimum Viable Product)?
- Existe priorizacao das funcionalidades por fase de implementacao?
- O HomeBanking web tera paridade funcional com a app mobile ou apenas um subconjunto?
- PWA (Progressive Web App) com funcionamento offline e necessario?

---

## 2. Infraestrutura e Ferramentas

### Repositorio de Codigo

- O repositorio sera Azure Repos ou GitHub? (ha mencao a ambos nos documentos)
- Qual a estrategia de branching preferida (GitFlow, trunk-based)?

### Ambiente e Deploy

- Confirmar que Azure Kubernetes Service (AKS) sera a plataforma inicial
- Qual o timeline previsto para migracao para OpenShift?
- Quantos ambientes serao necessarios (Dev, QA, Staging, Prod)?
- Existe site de Disaster Recovery? Qual o RTO/RPO esperado?

### Ferramentas de Observabilidade

- Confirmar reutilizacao do ELK Stack existente
- Qual a ferramenta de alerting em uso (ElastAlert, Watcher, outra)?

---

## 3. Seguranca e Conformidade

### RGPD

- Qual a base legal para tratamento de dados dos utilizadores?
- Existe DPO (Data Protection Officer) designado?
- Como sao tratados os pedidos de Subject Access Request (SAR)?
- Qual o processo para exercicio do direito ao esquecimento?

### PCI-DSS

- O canal web processa dados de cartao (PAN) diretamente?
- Qual o nivel de conformidade PCI-DSS necessario?
- A tokenizacao de cartoes e feita onde (frontend, backend, terceiro)?

### Banco de Portugal

- Quais os requisitos regulatorios especificos do Banco de Portugal aplicaveis?
- Existem requisitos de reporte obrigatorio?

### Auditoria

- Quais eventos devem ser registados para auditoria?
- Qual o periodo de retencao de logs de auditoria?
- Os logs devem ser imutaveis (write-once)?

### Resposta a Incidentes

- Existe plano de resposta a incidentes de seguranca?
- Quais os SLAs de resposta por severidade?
- Existe CSIRT (Computer Security Incident Response Team)?

---

## 4. Integracoes

### Core Banking

- Quais os SLAs de disponibilidade do Backend API existente?
- Qual o tempo de resposta esperado das APIs do Core Banking?

### Notificacoes

- Qual o provider de SMS em uso?
- Qual o provider de Push Notifications?
- Qual o provider de Email Transacional?

### Cartoes

- Qual o provider de emissao/processamento de cartoes?
- Como funciona a integracao 3D Secure?
- A alteracao de PIN sera suportada no canal web?

### Open Banking / PSD2

- O banco expoe APIs como ASPSP (Account Servicing Payment Service Provider)?
- O banco consome APIs de terceiros como TPP (Third Party Provider)?
- Qual o modelo de gestao de consentimentos PSD2?

### Message Broker

- Existe message broker em uso (RabbitMQ, Kafka, Azure Service Bus)?
- Quais eventos sao publicados/consumidos?
- Qual a estrategia de dead-letter para mensagens falhadas?

---

## 5. Implementacao e Go-Live

### Timeline

- Qual a data prevista para go-live?
- O lancamento sera faseado (pilot/beta) ou big-bang?
- Qual a duracao prevista do periodo de hypercare?

### Cutover

- Qual a estrategia de cutover preferida (big-bang, phased, parallel)?
- Existe janela de cutover definida (ex: fim de semana)?
- Qual o tempo maximo aceitavel para rollback?

### Migracao de Dados

- Existem dados a migrar do sistema legado (preferencias, configuracoes)?
- Como sera feita a validacao pos-migracao?

### Criterios Go/No-Go

- Quem sao os aprovadores para decisao de go-live?
- Quais os criterios minimos obrigatorios (alem dos tecnicos)?

---

## 6. Governacao e Equipas

### Modelo de Trabalho

- Qual a metodologia de projeto (Agile, SAFe, tradicional)?
- Equipas externas participam do desenvolvimento? Se sim, quais?
- Qual a frequencia de steering committee?
- Quem sao os stakeholders principais e sponsors?

### Papeis

- Quem sera o Product Owner?
- Quem sera o Tech Lead?
- Existe equipa de QA dedicada?

### Processo de Decisao

- Quem aprova decisoes tecnicas/arquiteturais?
- Existe processo de Change Advisory Board (CAB)?
- Qual o lead time minimo para mudancas em producao?

### Roadmap

- Qual a cadencia de releases prevista (semanal, quinzenal, mensal)?
- Existem datas fixas de release ou e continuo?
- Qual a percentagem de capacidade alocada para divida tecnica?

---

## 7. Performance e Disponibilidade

### Requisitos Confirmados (DEF-02)

- 400 utilizadores concorrentes
- 10 TPS (transacoes por segundo)
- Tempo de resposta P95 < 3 segundos
- Disponibilidade 99.9%

### A Confirmar

- Os valores acima estao corretos e aprovados?
- Qual o crescimento esperado para os proximos 3-5 anos?
- Existem periodos de pico conhecidos (fim de mes, pagamentos)?

---

## Proximos Passos

Apos esta reuniao:

1. Atualizar o HLD com as respostas obtidas
2. Remover itens "A definir" que foram esclarecidos
3. Identificar questoes que requerem sessoes adicionais de levantamento
4. Definir data alvo para entrega do HLD

---

## Notas da Reuniao

_Espaco para anotacoes durante a reuniao_

**Data da reuniao:**
**Participantes:**

### Respostas e Decisoes

_(preencher durante a reuniao)_
