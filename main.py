from fastapi import FastAPI

from celery_worker import long_task
from services.mail import send_email
from schemas import EmailSchemas

app = FastAPI()

@app.get("/no-celery/{name}")
def run_task(name: str):
    task = long_task.delay(name)
    return {
        "message": "Task completed",
        "task_id": task.id,
        }

@app.post('/send-mail')
def send_mail(request: EmailSchemas):
    try:
        send_email.delay(
            request.to_email,
            request.subject,
            request.message,
            request.email_header
            )
        return {
            "status": "200",
            "message": "Email sent successfully!"
        }
    except Exception as e:
        raise Exception(f"Error: {e}")                                     

@app.get('/')
def home():
    return {
        "data": "working..."
    }