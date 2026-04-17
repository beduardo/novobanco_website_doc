---
id: "DEC-019"
title: "App Mobile acede MicroService diretamente na autenticacao QR Code"
status: "accepted"
created: 2026-04-17
context: "DEF-13"
affects-definitions:
  - "DEF-13"
  - "DEF-12"
affects-sections:
  - "SEC-07"
  - "SEC-09"
---

# DEC-019: App Mobile acede MicroService diretamente na autenticacao QR Code

## Context

O fluxo de login via QR Code envolve dois actores: o canal web (SPA + BFF) e a App Mobile nativa. Quando o utilizador confirma na App Mobile que quer autenticar a sessão web via QR Code, é necessário comunicar esse resultado ao sistema.

A arquitectura do HomeBanking Web define o BFF como ponto de entrada exclusivo para o canal web. No entanto, a App Mobile tem a sua própria arquitectura de integração e não utiliza o BFF do canal web em nenhum momento — o BFF é específico para o canal web.

## Decision

A **App Mobile não utiliza o BFF do canal web em nenhum momento**, incluindo no fluxo de autenticação QR Code.

Na confirmação do QR Code, a App Mobile faz o POST **directamente ao MicroService** (via API Gateway IBM), executando a mesma chamada que o BFF faria se fosse o canal web a confirmar. O BFF fica à escuta via polling (DEC-017/DEC-018) e detecta o resultado quando o MicroService actualiza o estado da sessão.

## Consequences

- O MicroService expõe um endpoint de confirmação de QR Code acessível pela App Mobile (via API Gateway IBM)
- A App Mobile autentica-se no API Gateway IBM com as suas próprias credenciais (não usa credenciais do BFF)
- O BFF não participa activamente na confirmação — apenas consulta o estado via polling
- O MicroService é responsável por persistir o estado da confirmação QR Code de forma consultável pelo BFF
- Esta decisão reforça que o BFF é exclusivo do canal web; a App Mobile tem o seu próprio caminho de integração
- Impacto em SEC-07 (fluxo de autenticação QR Code) e SEC-09 (interfaces e integrações)
