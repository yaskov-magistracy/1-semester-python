from pydantic import BaseModel, EmailStr, Field, ConfigDict

class User(BaseModel):
    email: EmailStr
    bio: str | None = Field(max_length=1000)
    model_config = ConfigDict(extra='forbid')

class ExtendedUser(User):
    age: int = Field(ge=0, le=130)

data = {
    "email": "e@f.r",
    "bio": None,
    "age": 100
}

print(repr(ExtendedUser(**data)))