import os  #for get a env file
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail,Header #access a mail service
from dotenv import load_dotenv
from typing import Optional
from celery import shared_task
load_dotenv()

SENDGRID_API_KEY = os.getenv("MAIL_API_KEY")
FROM_EMAIL = os.getenv("SENDGRID_SENDER_MAIL")

@shared_task(name="mail.send_email")
def send_email(to_email: str, subject: str, body: str,email_header: Optional[str]=None):
    try:
        message = Mail(
            from_email=FROM_EMAIL,
            to_emails=to_email,
            subject=subject,
            plain_text_content=body
        )
        if email_header:
            message.add_header(Header("X-Mailer", email_header))
            
        sg = SendGridAPIClient(SENDGRID_API_KEY)
        response = sg.send(message=message)
        
        
    except Exception as e:
        raise Exception(f"Error: {e}")
    