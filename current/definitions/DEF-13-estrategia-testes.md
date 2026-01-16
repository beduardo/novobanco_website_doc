---
id: DEF-13-estrategia-testes
aliases:
  - Estratégia de Testes
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
status: completed
---

# DEF-13: Estratégia de Testes

> **Secção relacionada:** [SEC-13 - Estratégia de Testes](../sections/SEC-13-estrategia-testes.md)

## Contexto

Definir a estratégia de testes do HomeBanking Web, incluindo testes unitários, integração, contrato, E2E, performance, segurança, acessibilidade, test data management e matriz de responsabilidades.

---

## Pirâmide de Testes

```plantuml
@startuml
skinparam backgroundColor white

title Pirâmide de Testes - HomeBanking Web

rectangle "E2E Tests" as e2e #lightcoral {
    card "10%"
    card "Playwright"
    card "Critical flows"
}

rectangle "Integration Tests" as int #lightyellow {
    card "20%"
    card "Contract tests"
    card "API integration"
}

rectangle "Unit Tests" as unit #lightgreen {
    card "70%"
    card "Vitest / xUnit"
    card "Component logic"
}

unit -[hidden]-> int
int -[hidden]-> e2e

note right of e2e
Mais lentos
Mais custos
Mais frágeis
end note

note right of unit
Mais rápidos
Mais baratos
Mais estáveis
end note

@enduml
```

---

## Testes Unitários

### Frontend (React + TypeScript)

| Aspecto | Especificação |
|---------|---------------|
| Framework | Vitest |
| Assertions | Vitest expect |
| Component Testing | React Testing Library |
| Mocking | Vitest mocks |
| Coverage | Istanbul |

### Cobertura Mínima

| Tipo de Código | Cobertura Target |
|----------------|------------------|
| Componentes críticos | >= 90% |
| Hooks customizados | >= 90% |
| Utils/helpers | >= 80% |
| Serviços | >= 80% |
| Código geral | >= 80% |

### Exemplo de Teste Unitário (Frontend)

```typescript
// LoginForm.test.tsx
import { render, screen, fireEvent } from '@testing-library/react';
import { LoginForm } from './LoginForm';

describe('LoginForm', () => {
  it('should display validation error for empty username', async () => {
    render(<LoginForm onSubmit={jest.fn()} />);

    fireEvent.click(screen.getByRole('button', { name: /login/i }));

    expect(await screen.findByText(/username is required/i)).toBeInTheDocument();
  });

  it('should call onSubmit with credentials', async () => {
    const onSubmit = jest.fn();
    render(<LoginForm onSubmit={onSubmit} />);

    fireEvent.change(screen.getByLabelText(/username/i), {
      target: { value: 'testuser' }
    });
    fireEvent.change(screen.getByLabelText(/password/i), {
      target: { value: 'password123' }
    });
    fireEvent.click(screen.getByRole('button', { name: /login/i }));

    expect(onSubmit).toHaveBeenCalledWith({
      username: 'testuser',
      password: 'password123'
    });
  });
});
```

### BFF (.NET 8)

| Aspecto | Especificação |
|---------|---------------|
| Framework | xUnit |
| Assertions | FluentAssertions |
| Mocking | Moq / NSubstitute |
| Coverage | Coverlet |

### Exemplo de Teste Unitário (BFF)

```csharp
// TransferServiceTests.cs
public class TransferServiceTests
{
    private readonly Mock<IBackendClient> _backendClient;
    private readonly TransferService _sut;

    public TransferServiceTests()
    {
        _backendClient = new Mock<IBackendClient>();
        _sut = new TransferService(_backendClient.Object);
    }

    [Fact]
    public async Task ExecuteTransfer_ValidAmount_ShouldCallBackend()
    {
        // Arrange
        var request = new TransferRequest
        {
            Amount = 100,
            DestinationIban = "PT50000000000000000001"
        };

        _backendClient
            .Setup(x => x.PostAsync<TransferResponse>(It.IsAny<string>(), It.IsAny<object>()))
            .ReturnsAsync(new TransferResponse { Success = true });

        // Act
        var result = await _sut.ExecuteTransferAsync(request);

        // Assert
        result.Should().NotBeNull();
        result.Success.Should().BeTrue();
        _backendClient.Verify(x => x.PostAsync<TransferResponse>(
            "/transfers",
            It.Is<object>(o => o.Equals(request))
        ), Times.Once);
    }
}
```

---

## Testes de Integração

### Estratégia

```plantuml
@startuml
skinparam backgroundColor white

title Testes de Integração

rectangle "BFF" as bff {
    rectangle "API Controllers" as api
    rectangle "Services" as svc
}

rectangle "Mocks" as mocks {
    rectangle "WireMock\n(Backend API)" as wire
    rectangle "Redis\n(TestContainers)" as redis
}

rectangle "Test Runner" as runner

runner -> api : HTTP Request
api -> svc : Business Logic
svc -> wire : Mocked Backend
svc -> redis : Real Redis (container)

@enduml
```

### Ferramentas

| Ferramenta | Uso |
|------------|-----|
| WireMock | Mock do Backend API |
| TestContainers | Redis container para testes |
| WebApplicationFactory | In-memory BFF para testes |

### Exemplo de Teste de Integração

```csharp
// AccountsControllerIntegrationTests.cs
public class AccountsControllerIntegrationTests : IClassFixture<WebApplicationFactory<Program>>
{
    private readonly HttpClient _client;
    private readonly WireMockServer _mockServer;

    public AccountsControllerIntegrationTests(WebApplicationFactory<Program> factory)
    {
        _mockServer = WireMockServer.Start();

        _client = factory.WithWebHostBuilder(builder =>
        {
            builder.ConfigureServices(services =>
            {
                services.Configure<BackendOptions>(opt =>
                    opt.BaseUrl = _mockServer.Url);
            });
        }).CreateClient();
    }

    [Fact]
    public async Task GetAccounts_ValidSession_ReturnsAccountList()
    {
        // Arrange
        _mockServer.Given(Request.Create()
            .WithPath("/accounts")
            .UsingGet())
            .RespondWith(Response.Create()
                .WithStatusCode(200)
                .WithBody(@"[{""iban"":""PT50..."",""balance"":1000}]"));

        // Act
        var response = await _client.GetAsync("/api/accounts");

        // Assert
        response.StatusCode.Should().Be(HttpStatusCode.OK);
        var accounts = await response.Content.ReadFromJsonAsync<List<Account>>();
        accounts.Should().HaveCount(1);
    }
}
```

---

## Testes de Contrato

### Consumer-Driven Contract Testing

```plantuml
@startuml
skinparam backgroundColor white

title Contract Testing com Pact

rectangle "Consumer (BFF)" as consumer {
    card "Define expectations"
    card "Generates Pact file"
}

rectangle "Pact Broker" as broker {
    card "Stores contracts"
    card "Tracks compatibility"
}

rectangle "Provider (Backend)" as provider {
    card "Verifies contracts"
    card "Publishes results"
}

consumer --> broker : Publish Pact
broker --> provider : Retrieve Pact
provider --> broker : Verification results

@enduml
```

### Quando Usar

| Cenário | Usar Pact? |
|---------|------------|
| BFF <-> Backend API | Sim (recomendado) |
| Frontend <-> BFF | Opcional (E2E cobre) |
| Serviços internos | Sim |

---

## Testes End-to-End (E2E)

### Framework: Playwright

| Aspecto | Especificação |
|---------|---------------|
| Framework | Playwright |
| Browsers | Chromium, Firefox, WebKit |
| Execution | CI/CD (headless) |
| Reports | HTML + Screenshots |

### Cenários Críticos (Cobertura Mínima)

| Fluxo | Prioridade | Criticidade |
|-------|------------|-------------|
| Login via QR Code | Alta | Crítico |
| Login tradicional (fallback) | Alta | Crítico |
| Consulta de saldos | Alta | Crítico |
| Transferência nacional | Alta | Crítico |
| Pagamento de serviços | Alta | Crítico |
| Logout | Média | Alto |
| Alteração de dados | Média | Alto |

### Exemplo de Teste E2E

```typescript
// login.spec.ts
import { test, expect } from '@playwright/test';

test.describe('Login Flow', () => {
  test('should login successfully with valid credentials', async ({ page }) => {
    await page.goto('/login');

    // Simular scan de QR Code (ambiente de teste)
    await page.click('[data-testid="qr-login-button"]');

    // Aguardar redirect após autenticação simulada
    await page.waitForURL('/dashboard');

    // Verificar elementos da página inicial
    await expect(page.locator('[data-testid="welcome-message"]')).toBeVisible();
    await expect(page.locator('[data-testid="account-summary"]')).toBeVisible();
  });

  test('should display error for invalid session', async ({ page }) => {
    await page.goto('/login');

    // Forçar erro de sessão
    await page.evaluate(() => localStorage.clear());
    await page.goto('/dashboard');

    // Deve redirecionar para login
    await expect(page).toHaveURL('/login');
    await expect(page.locator('[data-testid="session-expired-message"]')).toBeVisible();
  });
});
```

### Configuração CI/CD

```yaml
# azure-pipelines.yml (E2E stage)
- stage: E2E
  jobs:
  - job: PlaywrightTests
    pool:
      vmImage: 'ubuntu-latest'
    steps:
    - task: NodeTool@0
      inputs:
        versionSpec: '20.x'

    - script: npm ci
    - script: npx playwright install --with-deps

    - script: npx playwright test
      env:
        BASE_URL: $(E2E_BASE_URL)

    - task: PublishTestResults@2
      inputs:
        testResultsFormat: 'JUnit'
        testResultsFiles: 'test-results/*.xml'

    - publish: playwright-report
      artifact: playwright-report
```

---

## Testes de Segurança

### Tipos de Testes

| Tipo | Ferramenta | Quando |
|------|------------|--------|
| SAST | SonarQube / Checkmarx | Cada commit |
| DAST | OWASP ZAP | Pre-release |
| Dependency Scan | Snyk / Dependabot | Diário |
| Penetration Test | Manual (externo) | Antes go-live |

### OWASP Top 10 Coverage

| Vulnerabilidade | Teste |
|-----------------|-------|
| A01 Broken Access Control | DAST + Manual |
| A02 Cryptographic Failures | SAST + Code Review |
| A03 Injection | SAST + DAST |
| A04 Insecure Design | Code Review + Threat Model |
| A05 Security Misconfiguration | DAST + Infra Scan |
| A06 Vulnerable Components | Dependency Scan |
| A07 Auth Failures | DAST + Pentest |
| A08 Integrity Failures | SAST + DAST |
| A09 Logging Failures | Code Review |
| A10 SSRF | DAST |

---

## Testes de Acessibilidade

### Framework: axe-core

| Aspecto | Especificação |
|---------|---------------|
| Standard | WCAG 2.1 AA |
| Tool | axe-core |
| Integration | Playwright + axe |
| Reports | HTML |

### Exemplo de Teste

```typescript
// accessibility.spec.ts
import { test, expect } from '@playwright/test';
import AxeBuilder from '@axe-core/playwright';

test.describe('Accessibility', () => {
  test('login page should not have accessibility violations', async ({ page }) => {
    await page.goto('/login');

    const results = await new AxeBuilder({ page })
      .withTags(['wcag2a', 'wcag2aa'])
      .analyze();

    expect(results.violations).toEqual([]);
  });

  test('dashboard should be keyboard navigable', async ({ page }) => {
    await page.goto('/dashboard');

    // Tab through main elements
    await page.keyboard.press('Tab');
    await expect(page.locator(':focus')).toHaveAttribute('data-testid', 'main-menu');

    await page.keyboard.press('Tab');
    await expect(page.locator(':focus')).toHaveAttribute('data-testid', 'account-summary');
  });
});
```

---

## Test Data Management

### Estratégia

| Ambiente | Dados |
|----------|-------|
| dev | Dados sintéticos (fixtures) |
| qa | Dados anonimizados de produção |
| prod | N/A (não testar em prod) |

### Fixtures

```typescript
// fixtures/users.ts
export const testUsers = {
  standard: {
    username: 'test_user_001',
    accounts: ['PT50000000000000000001'],
    balance: 10000
  },
  premium: {
    username: 'test_user_premium',
    accounts: ['PT50000000000000000002', 'PT50000000000000000003'],
    balance: 50000
  }
};
```

---

## Matriz de Responsabilidades

| Tipo de Teste | Quem Escreve | Quem Executa | Quando |
|---------------|--------------|--------------|--------|
| Unit Tests | Developers | CI Pipeline | Cada commit |
| Integration | Developers | CI Pipeline | Cada commit |
| Contract | Developers | CI Pipeline | Cada commit |
| E2E | QA + Developers | CI Pipeline | Cada PR |
| Performance | QA | Manual + CI | Pre-release |
| Security (SAST) | Automated | CI Pipeline | Cada commit |
| Security (DAST) | SecOps | Manual | Pre-release |
| Accessibility | QA | CI Pipeline | Cada PR |
| UAT | QA + PO | Manual | Pre-release |

---

## Quality Gates

### Pipeline Blocking

| Gate | Threshold | Bloqueante? |
|------|-----------|-------------|
| Unit Tests | 100% pass | Sim |
| Coverage | >= 80% | Sim |
| SAST | 0 Critical, 0 High | Sim |
| E2E Critical | 100% pass | Sim |
| E2E Non-critical | >= 95% pass | Não |
| Accessibility | 0 Critical | Sim |

```plantuml
@startuml
skinparam backgroundColor white

title Quality Gates no Pipeline

start
:Commit;
:Build;
:Unit Tests;
if (Pass?) then (sim)
    :Coverage Check;
    if (>= 80%?) then (sim)
        :SAST Scan;
        if (0 Critical?) then (sim)
            :E2E Tests;
            if (Critical pass?) then (sim)
                :Deploy to DEV;
            else (não)
                :BLOCK;
                stop
            endif
        else (não)
            :BLOCK;
            stop
        endif
    else (não)
        :BLOCK;
        stop
    endif
else (não)
    :BLOCK;
    stop
endif

stop

@enduml
```

---

## Questões Pendentes de Confirmação

| ID | Questão | Responsável | Prioridade |
|----|---------|-------------|------------|
| Q-13-001 | Cobertura mínima aprovada (80%) | Tech Lead | Alta |
| Q-13-002 | Ferramenta de contract testing (Pact) | Arquitetura | Média |
| Q-13-003 | Dados de teste anonimizados disponíveis | DBA / QA | Média |
| Q-13-004 | Fornecedor de pentest | SecOps | Alta |

---

## Decisões

### Unit Testing Framework
- **Decisão:** Vitest (Frontend), xUnit (BFF)
- **Justificação:** Alinhamento com stack definida (DEC-009, DEC-010)
- **Alternativas consideradas:** Jest (frontend), NUnit (backend)

### E2E Testing Framework
- **Decisão:** Playwright
- **Justificação:** Multi-browser, moderno, boa integração CI/CD
- **Alternativas consideradas:** Cypress, Selenium

### Contract Testing
- **Decisão:** Pact (se necessário para BFF<->Backend)
- **Justificação:** Consumer-driven, ampla adoção
- **Alternativas consideradas:** Spring Cloud Contract

### Security Testing
- **Decisão:** SAST no pipeline + DAST pre-release + Pentest antes go-live
- **Justificação:** Cobertura completa do SDLC
- **Alternativas consideradas:** Apenas SAST

---

## Decisões Relacionadas

- [DEC-009-stack-tecnologica-frontend.md](../decisions/DEC-009-stack-tecnologica-frontend.md) - Stack frontend (framework de testes)
- [DEC-010-stack-tecnologica-backend.md](../decisions/DEC-010-stack-tecnologica-backend.md) - Stack backend (framework de testes)

## Referências

- [DEF-10-arquitetura-operacional.md](DEF-10-arquitetura-operacional.md) - CI/CD e Quality Gates
- [DEF-08-seguranca-conformidade.md](DEF-08-seguranca-conformidade.md) - Requisitos de segurança
- [DEF-04-design-system.md](DEF-04-design-system.md) - WCAG requirements
- Testing Trophy (Kent C. Dodds)
- OWASP Testing Guide
- WCAG 2.1 Guidelines
- Playwright Documentation
