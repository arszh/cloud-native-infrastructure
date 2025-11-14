from fastapi import FastAPI
import os, socket

app = FastAPI()

@app.get("/")
def read_root():
    return {
        "message": "Hello from DevOps portfolio project!",
        "hostname": socket.gethostname(),
        "environment": os.getenv("APP_ENV", "local"),
    }

@app.get("/healthz")
def healthz():
    return {"status": "ok"}