from fastapi import FastAPI
import time

app = FastAPI()

def long_task(name: str):
    print(f"Started task for {name}")
    for i in range(5):
        print(f"{name}: {i+1}/5")
        time.sleep(1)
    print("Task completed")

@app.get("/no-celery/{name}")
def run_task(name: str):
    long_task(name)
    return {"message": "Task completed"}


@app.get('/')
def home():
    return {
        "data": "working..."
    }