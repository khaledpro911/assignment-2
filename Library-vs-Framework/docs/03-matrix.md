# Comparison matrix

| Ecosystem | Typical IoC mechanism | Resolution timing | Architectural core | Qualitative trade-off |
| --- | --- | --- | --- | --- |
| Spring | BeanFactory/ApplicationContext and DI | Container startup or bean access, depending on configuration | Spring container | Deep integration versus larger conceptual surface. [3] |
| .NET | Service registrations and provider | Host/service-provider build and resolution | Built-in DI abstractions | Integrated conventions versus registration/lifetime responsibility. [4] |
| NestJS | Module keys and providers | Bootstrap dependency graph | Nest runtime | Strong modularity versus key and scope configuration. [5] |
| Symfony | Autowiring and compiled service container | Container build/compilation; lazy services can vary | DependencyInjection component | Convenient wiring versus convention dependence. [6] |
| FastAPI | Dependency callables | Request dependency resolution | Request and dependency resolver | Composable request dependencies versus request-coupled lifecycle. [7] |

Timings are broad descriptions of when wiring generally occurs. No measured latency or universal ranking is asserted. Version, settings, scopes, and deployment can change details.
