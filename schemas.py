from pydantic import BaseModel, validator, Field
from datetime import date
from typing import List
#Валидация данных. Возвращает объект

class Genre(BaseModel):
    name: str

class Author(BaseModel):
    first_name: str = Field(..., max_length=25)
    last_name: str
    age: int = Field(
        ...,
        gt=15,
        lt=90,
        description='Автору не может быть менее 15 и не более 90 лет'
    )

    @validator('last_name')
    def check_age(cls, v):
        #кастомная валидация поля
        if len(v) < 3:
            raise ValueError('Не корректная фамилия')
        return

class Book(BaseModel):
    title: str
    writer: str
    duration: str
    date: date
    summary: str
    genres: List[Genre] = []
    pages: int

class BookOut(Book):
    id: int