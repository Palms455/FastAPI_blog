from pydantic import BaseModel
from datetime import date
from typing import List
#Валидация данных. Возвращает объект

class Genre(BaseModel):
    name:str


class Book(BaseModel):
    title: str
    writer: str
    duration: str
    date: date
    summary: str
    genres: List[Genre]
    pages: int
