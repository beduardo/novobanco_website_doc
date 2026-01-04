---
id: DEF-10-deployment-infrastructure
aliases:
  - Novo Banco Deployment Infrastructure
tags:
  - nextreality-novobanco-website-definitions
approved: true
created: 2025-12-22
hubs:
  - "[[nextreality]]"
para-code: R
reviewed: true
---

---
# Project Definitions
## Deployment Infrasctructure
Cloud: Azure
Hosting: Kubernetes 

Pending Questions:
- Where will be hosted? AKS? Local? 
- Who will create and manage the cluster?
- If created by us:
    - Service Mesh? Istio, Linkerd?
    - Ingress controller? NGINX, Traefik, Cloud Native?
    - Integration with legacy apps (Siebel)

## Authentication
Authentication Flow:

Pending Questions:
- Preferível Client ID/Client Secret?
- External Authentication

## API Scenarios
```mermaid
sequenceDiagram
    participant App
    participant SPA
    participant F5
    participant BFF
    participant AppGkw
```

