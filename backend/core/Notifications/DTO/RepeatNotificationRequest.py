from pydantic import BaseModel, UUID4
from datetime import datetime

class RepeatNotificationRequest(BaseModel):
    targetId: UUID4
    newTime: datetime