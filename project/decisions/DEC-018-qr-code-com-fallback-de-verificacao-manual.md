---
id: "DEC-018"
title: "QR Code com Fallback de Verificacao Manual"
status: "accepted"
created: 2026-04-17
context: "DEF-13"
affects-definitions:
  - "DEF-13"
affects-sections:
  - "SEC-07"
---

# DEC-018: QR Code com Fallback de Verificacao Manual

## Context

O login via QR Code no HomeBanking Web depende de o utilizador digitalizar o QR Code com a App Mobile, que confirma a autenticação. O canal web fica a aguardar esta confirmação via polling HTTP (DEC-017 — sem WebSocket disponível).

Em cenários onde o polling automático não seja viável (ex: limitações de infraestrutura, bloqueio de pedidos periódicos), o utilizador ficaria bloqueado a aguardar indefinidamente sem feedback accionável.

## Decision

O ecrã de login QR Code inclui um **botão "Verificar"** que dispara exactamente o mesmo pedido HTTP que o polling automático dispararia.

- O botão aciona o mesmo endpoint e com a mesma lógica do ciclo de polling
- Não existe mecanismo adicional, código de verificação separado, nem fluxo alternativo — é apenas a forma manual de acionar o mesmo pedido
- O polling automático e o botão coexistem: se o polling estiver activo, o botão é redundante mas inofensivo; se o polling não funcionar, o botão é o fallback

## Consequences

- Não há impacto no BFF nem no backend — o endpoint de verificação de estado do QR Code já existe para o polling
- Implementação frontend minimal: um botão que chama a mesma função do polling
- O utilizador tem controlo manual sobre a verificação, eliminando a dependência total do polling automático
- O botão deve estar visível mas não proeminente, para não confundir utilizadores em fluxo normal
