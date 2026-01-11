from fastapi import FastAPI

app = FastAPI(title="FastAPI on EKS")

@app.get("/")
def read_root():
    return {"message": "Hello from FastAPI running on EKS 🚀"}

@app.get("/health")
def health():
    return {"status": "ok"}
