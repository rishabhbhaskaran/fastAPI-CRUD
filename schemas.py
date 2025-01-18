from pydantic import BaseModel
from typing import Optional


class UserBase(BaseModel):
    username: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int

    class Config:
        from_attributes = True


class BookBase(BaseModel):
    title: str
    author: str
    summary: Optional[str] = None
    genre: Optional[str] = None
    published_date: Optional[str] = None


class BookCreate(BookBase):
    pass


class Book(BookBase):
    id: int

    class Config:
        from_attributes = True
