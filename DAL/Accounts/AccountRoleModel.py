from enum import Enum

class AccountRoleModel(str, Enum):
    Admin = "Admin"
    User = "User"