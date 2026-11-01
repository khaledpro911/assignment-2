// ILLUSTRATIVE — syntax verified, not executed in CI
var app = WebApplication.Create();
app.MapGet("/status", () => new { ok = true });
app.Run();
