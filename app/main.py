from fastapi import FastAPI
from app.api.routes import router

app = FastAPI(
    title="Quora Duplicate Question Detection API"
)

app.include_router(router)

@app.get("/")
def home():
    return {
        "message": "API Running Successfully"
    }

