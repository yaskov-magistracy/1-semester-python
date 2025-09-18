import uuid
from datetime import datetime, timezone

class Notification():
    id: uuid
    time: datetime
    text: str

    def __init__(self, id, time, text):
        self.id = id,
        self.time = time
        self.login = text