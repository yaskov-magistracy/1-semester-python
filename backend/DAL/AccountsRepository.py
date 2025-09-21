from .Models import AccountModel
from DAL.BaseRepository import BaseRepository

class AccountsRepository(BaseRepository[AccountModel]):
    @property
    def model(self) -> type[AccountModel]:
        return AccountModel