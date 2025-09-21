from pydantic import BaseModel
from datetime import datetime

class AddNotificationRequest(BaseModel):
    time: datetime
    text: str