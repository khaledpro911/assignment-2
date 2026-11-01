# Definitions and decision guide

## Terms

A **library** is a reusable component whose functions are normally invoked by the application. A **framework** supplies a reusable structure and calls application code through defined extension points. Products can combine both models; the label describes a usage relationship, not an absolute category.

**Inversion of Control (IoC)** means that some control—such as lifecycle, dispatch, or dependency construction—moves from application code to a host or container. **Dependency Injection (DI)** is one IoC technique: an object receives dependencies rather than constructing or locating them itself. Constructor injection makes required dependencies explicit. [1] [3]

The **Hollywood Principle** is the shorthand “Don't call us, we'll call you”: the framework invokes user code at a callback, route, or lifecycle boundary. It helps explain framework flow but does not imply a particular security property. [2]

## Practical choice

Prefer a library when local control, small integration surface, or independent composition matters. Prefer a framework when shared lifecycle, routing, or standard application structure provides enough value to offset conventions and additional dependencies. Evaluate the actual version, extension points, security support, and team's ability to maintain it. These are qualitative criteria, not measured performance rankings.
