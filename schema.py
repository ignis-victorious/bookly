#  ___________________
#  Import LIBRARIES
from pydantic import BaseModel
#  Import FILES
#  ___________________


class BookCreateModel(BaseModel):
    title: str
    author: str
