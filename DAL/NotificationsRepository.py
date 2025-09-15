from .NotificationModel import NotificationModel
from DAL.BaseRepository import BaseRepository

class AccountsRepository(BaseRepository[NotificationModel]):
    @property
    def model(self) -> type[NotificationModel]:
        return NotificationModel