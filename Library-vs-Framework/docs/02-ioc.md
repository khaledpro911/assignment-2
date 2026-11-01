# Inversion of Control

The user object declares what it needs; a container resolves dependencies and the host drives application lifecycle. Constructor injection is a common DI form. Framework-managed callbacks extend the same broad inversion of control beyond object construction. This simplified graph is conceptual, not a runtime trace. [1] [3]

```mermaid
flowchart LR
    App[Application configuration] -->|registers provider keys| Container[IoC container]
    Consumer[Consumer] -->|declares dependency| Container
    Container -->|constructs and injects| Consumer
    Host[Framework host] -->|dispatches lifecycle or request| Consumer
    Consumer -->|uses capability| Service[Service or library]
```
