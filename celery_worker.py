from celery import Celery
import time

import services.mail as mail

celery_app = Celery(
    "worker",
    broker="redis://127.0.0.1:6379/0",
    backend="redis://127.0.0.1:6379/0",
)

celery_app.conf.imports = ("services.mail",)

@celery_app.task
def long_task(name: str):
    print(f"Started task for {name}")
    for i in range(5):
        print(f"{name}: {i+1}/5")
        time.sleep(1)
    print("Task completed")
    
