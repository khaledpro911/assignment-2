# Security and attack surface

A framework is not inherently more or less secure than a library. Defaults can make secure patterns easier, but application configuration and dependency maintenance remain essential.

## Risks and controls

- **Dependency confusion:** A public package with a trusted-looking name can compete with an internal package. Use explicit registry scopes and trusted sources, protect names, and review lockfiles and package provenance.
- **Transitive dependencies:** Nested dependencies can introduce vulnerable, unmaintained, or unexpected code. Inventory the dependency graph, use software composition analysis, remove unused components, and patch by risk. [8]
- **Reflection-based RCE:** Reflection and data binding can expose dangerous property paths if unsafe inputs and deployment conditions align. Spring4Shell (CVE-2022-22965) was a conditional Spring Framework remote-code-execution vulnerability; applicability depended on conditions including JDK and deployment mode. Follow vendor remediation and assess the actual deployment rather than generalizing the exploit. [9]
- **IoC container misconfiguration:** Ambiguous bindings, unsafe scopes, unintended provider exposure, or overly broad component scanning can resolve the wrong implementation or expose privileged services. Review registrations, lifetimes, module boundaries, and runtime configuration.
- **Secrets management:** Do not commit credentials. Obtain secrets from an approved secret store or protected runtime configuration, restrict access, rotate when needed, and avoid logging secret values. [10]

## STRIDE review table

| Threat | Example in this context | Mitigation |
| --- | --- | --- |
| Spoofing | Attacker publishes a look-alike dependency or registry package | Scope registries, verify provenance, and restrict package sources |
| Tampering | Dependency or container configuration is changed in a build | Protect review and release permissions; verify lockfiles and artifacts |
| Repudiation | A service binding or release change lacks attributable history | Record reviewed changes and preserve CI/release audit logs |
| Information disclosure | Secret is injected into logs or exposed through a provider | Minimize secret access, redact logs, and test configuration boundaries |
| Denial of service | Vulnerable or expensive dependency path is reachable | Patch, limit resource use, and monitor exposed routes and components |

STRIDE entries are review prompts, not proof of coverage. Apply threat modeling to the specific application and deployment.
