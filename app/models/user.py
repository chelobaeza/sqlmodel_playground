

from typing import Optional
from sqlmodel import Field, SQLModel


class UserBase(SQLModel):
    display_name: str

    class Config:
        orm_mode = True


class User(UserBase, table=True):
    id: Optional[int] = Field(
        default=None,
        primary_key=True,
        index=True,
    )
