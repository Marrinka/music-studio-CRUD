from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field

class Request(BaseModel):
    time_from: datetime = Field(ge=datetime.now())
    time_to: datetime = Field(ge=datetime.now())
    room_id: int = Field(ge=0, le=4)