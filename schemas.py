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
    title: str = Field(..., description="The title of the book.")
    author: str = Field(..., description="The author of the book.")
    summary: Optional[str] = Field(None, description="A brief description of the book.")
    genre: Optional[str] = Field(None, description="Book's Genre")
    published_date: Optional[str] = Field(None, description="Book's published date")


class BookCreate(BookBase):
    pass


class Book(BookBase):
    id: int

    class Config:
        from_attributes = True
