# Library vs Framework

**Student:** Khaled Abdulhabib  
**Course:** A1 Cybersecurity Bootcamp capstone  
**Supervisors:** Professor Mahmoud and Sufyan Al-Ba'adani

A concise, security-aware comparison of libraries and frameworks, with five cross-language illustrations. The repository favors sourced qualitative trade-offs over unsourced performance claims.

## Definitions

- **Library:** Reusable code that application code calls when it needs a capability.
- **Framework:** A reusable application structure that invokes user-provided code at defined extension points.
- **Inversion of Control (IoC):** Control of application flow or object creation is delegated to a host/container instead of being directed entirely by user code.
- **Dependency Injection (DI):** A form of IoC in which dependencies are supplied from outside a consuming object, commonly through its constructor.
- **Hollywood Principle:** “Don't call us, we'll call you.” The framework calls application code at agreed lifecycle points. The phrase is a mnemonic, not a formal specification. [1] [2]

## Trade-off matrix

| Ecosystem | IoC Mechanism | Resolution Time | Core Engine | Trade-offs |
| --- | --- | --- | --- | --- |
| Spring | ApplicationContext/BeanFactory; constructor or other DI | Container bootstrap and bean creation; some facilities may be lazy | Spring IoC container | Broad ecosystem and integration; more conventions, configuration, and runtime machinery. [3] |
| .NET | IServiceCollection registrations and IServiceProvider | Host/container build and service resolution; lifetime affects reuse | Generic Host plus built-in DI abstractions | Familiar integrated services; registration and lifetime mistakes remain application risks. [4] |
| NestJS | Module provider keys and constructor DI | Application bootstrap resolves provider graph | Nest runtime container | Structured modules and scopes; runtime key/configuration complexity. [5] |
| Symfony | Service container with autowiring/configuration | Container compilation/build, with lazy options available | Symfony DependencyInjection component | Strong integration and autowiring; container conventions can feel prescriptive. [6] |
| FastAPI | `Depends` callables and dependency graph | Per-request dependency execution, with caching within a request by default | FastAPI dependency resolver | Lightweight composability; dependency behavior is coupled to request handling. [7] |

Resolution-time descriptions are architectural, not benchmark claims. Actual behavior depends on version, configuration, scope, and deployment.

## Code examples

These compact illustrations contrast direct library calls with framework-managed callbacks. They are explanatory fragments, not complete applications. The same file examples are under `examples/`.

### TypeScript

```typescript
// ILLUSTRATIVE — syntax verified, not executed in CI
import { format } from "date-fns";
const label = format(new Date(), "yyyy-MM-dd");
```

```typescript
// ILLUSTRATIVE — syntax verified, not executed in CI
import { Controller, Get } from "@nestjs/common";
@Controller("status")
class StatusController {
  @Get() read() { return { ok: true }; }
}
```

### Python

```python
// ILLUSTRATIVE — syntax verified, not executed in CI
from pathlib import Path
text = Path("message.txt").read_text(encoding="utf-8")
```

```python
// ILLUSTRATIVE — syntax verified, not executed in CI
from fastapi import FastAPI
app = FastAPI()
@app.get("/status")
def status(): return {"ok": True}
```

### PHP

```php
// ILLUSTRATIVE — syntax verified, not executed in CI
$slug = strtolower(str_replace(" ", "-", $title));
```

```php
// ILLUSTRATIVE — syntax verified, not executed in CI
use Symfony\Component\Routing\Attribute\Route;
final class StatusController {
    #[Route('/status')]
    public function read(): array { return ['ok' => true]; }
}
```

### Java

```java
// ILLUSTRATIVE — syntax verified, not executed in CI
String label = java.time.LocalDate.now().toString();
```

```java
// ILLUSTRATIVE — syntax verified, not executed in CI
@RestController
class StatusController {
    @GetMapping("/status")
    Map<String, Boolean> read() { return Map.of("ok", true); }
}
```

### C Sharp

```csharp
// ILLUSTRATIVE — syntax verified, not executed in CI
var label = DateTimeOffset.UtcNow.ToString("yyyy-MM-dd");
```

```csharp
// ILLUSTRATIVE — syntax verified, not executed in CI
var app = WebApplication.Create();
app.MapGet("/status", () => new { ok = true });
```

## Project structure: flexible vs. rigid

A **flexible library-led** design leaves composition to the application:

```text
src/
  features/
  adapters/
  composition-root.ts
```

A **rigid framework-led** design follows framework-defined boundaries:

```text
src/
  modules/
  controllers/
  providers/
  main.ts
```

Neither structure is inherently safer; review boundaries, configuration, and dependencies.

## Security and attack surface

See [Security notes](docs/05-security.md). Key considerations:

- Framework defaults can reduce repetitive mistakes, but misconfiguration can widen exposure.
- Transitive components expand the update and vulnerability-monitoring surface.
- IoC containers and reflection add resolution paths that deserve strict configuration and review.
- Store secrets outside source control and grant runtime identities least privilege.

## References

See [the reference list](docs/06-references.md) for IEEE-style entries and APA-style citations. Sources are official framework documentation, OWASP guidance, NIST NVD, and Martin Fowler's design article.
