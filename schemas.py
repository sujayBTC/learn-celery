from pydantic import BaseModel
from typing import Optional

class EmailSchemas(BaseModel):
    name: str
    to_email: str
    subject: str
    message: str
    email_header: Optional[str] = None
