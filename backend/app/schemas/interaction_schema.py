from pydantic import BaseModel
from typing import Optional

class InteractionBase(BaseModel):
    hcp_name: str
    topic: str
    follow_up: Optional[str] = None
    summary: Optional[str] = None


class InteractionCreate(InteractionBase):
    pass


class InteractionResponse(InteractionBase):
    id: int

    class Config:
        orm_mode = True
