from pydantic import BaseModel

class BlockRequest(BaseModel):
    targetLogin: str
    blockReason: str