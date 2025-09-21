from enum import Enum

class AccountRole(str, Enum):
    Admin = "Admin"
    User = "User"