from pydantic import BaseModel, UUID4
from datetime import datetime

class Notification(BaseModel):
    id: UUID4
    time: datetime
    text: str