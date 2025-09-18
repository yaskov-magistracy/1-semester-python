from .Models import NotificationModel
from DAL.BaseRepository import BaseRepository

class NotificationsRepository(BaseRepository[NotificationModel]):
    @property
    def model(self) -> type[NotificationModel]:
        return NotificationModel