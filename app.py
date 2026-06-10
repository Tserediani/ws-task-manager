from fastapi import FastAPI
from routes.tasks import router as tasks_router

app = FastAPI()
app.include_router(tasks_router)


@app.get("/")
def health_check():
    return {"status": "ok"}
