#  ___________________
#  Import LIBRARIES
# from datetime import date
from pydantic import BaseModel
#  Import FILES
#  ___________________


class Book(BaseModel):
    id: int
    title: str
    author: str
    publisher: str
    published_date: str
    # published_date: date
    page_count: int
    language: str


class Book_Update(BaseModel):
    title: str
    author: str
    publisher: str
    page_count: int
    language: str
