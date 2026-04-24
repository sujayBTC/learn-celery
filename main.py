from fastapi import FastAPI

from celery_worker import long_task

app = FastAPI()

@app.get("/no-celery/{name}")
def run_task(name: str):
    task = long_task.delay(name)
    return {
        "message": "Task completed",
        "task_id": task.id,
        }


@app.get('/')
def home():
    return {
        "data": "working..."
    }