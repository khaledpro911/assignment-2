# Structure: flexible versus rigid

A library-led design typically lets the application own the composition root and select where capabilities are called:

```text
app/
  domain/
  adapters/
  main.ts
```

A framework-led design often organizes code around the framework's routing, module, or provider conventions:

```text
app/
  modules/
  controllers/
  providers/
  bootstrap.ts
```

These are schematic text trees, not prescriptive templates. Framework conventions can improve consistency across a team; they can also increase coupling to framework lifecycle and upgrades. A library offers local choice while leaving more assembly and consistency work to maintainers.
