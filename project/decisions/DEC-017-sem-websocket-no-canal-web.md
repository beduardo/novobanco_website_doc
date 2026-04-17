---
id: "DEC-017"
title: "Sem WebSocket no Canal Web"
status: "accepted"
created: 2026-04-17
context: "DEF-19"
affects-definitions:
  - "DEF-19"
affects-sections:
  - "SEC-09"
  - "SEC-12"
---

# DEC-017: Sem WebSocket no Canal Web

## Context

O canal HomeBanking Web necessita de comunicação em tempo real para algumas funcionalidades (ex: notificação de estado do login via QR Code). WebSocket é uma tecnologia comum para este tipo de comunicação bidirecional persistente, mas a sua viabilidade depende da infraestrutura de rede e dos componentes intermediários (F5, proxies, firewalls) que nem sempre suportam conexões WebSocket de longa duração em ambientes bancários.

## Decision

**Não será utilizado WebSocket** em nenhuma funcionalidade do canal HomeBanking Web.

Toda a comunicação em tempo real ou quasi-real-time deverá ser implementada através de **polling HTTP** (pedidos periódicos do cliente ao BFF). O intervalo de polling e a estratégia de timeout são definidos por funcionalidade.

## Consequences

- Funcionalidades que dependam de notificações em tempo real (ex: resultado do login QR Code) usam polling HTTP
- O BFF expõe endpoints de estado consultáveis pelo SPA a intervalos regulares
- A infraestrutura existente (F5, API Gateway IBM) não necessita de configuração adicional para WebSocket
- Maior simplicidade de implementação e debugging
- Trade-off: maior número de pedidos HTTP em funcionalidades com polling; a frequência deve ser calibrada para minimizar carga
- O fallback de verificação manual (DEC-018) existe precisamente para cenários onde o polling não seja viável
