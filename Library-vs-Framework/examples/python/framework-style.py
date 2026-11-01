// ILLUSTRATIVE — syntax verified, not executed in CI
from fastapi import FastAPI

app = FastAPI()

@app.get("/status")
def status() -> dict[str, bool]:
    return {"ok": True}
