from fastapi import FastAPI, Query, Path, Body
from schemas import Book, Author, BookOut
from typing import List


app = FastAPI()

@app.get('/')
def home():
    return {"key": "Hello"}

@app.get('/{pk}')
def get_item(pk: int, q: str = None):
    # указывание типов данных, происходит автоматическая валидция входящих данных
    return {"key": pk,
            "q": q}

@app.get('/user/{pk}/items/{item}')
def get_user_item(pk: int, item: str):
    return {"user": pk, "item": item}

@app.post('/book/')
def create_book(item: Book, author: Author, quantity: int = Body(...)):
    # Body валидация post запросов
    return {"item": item, "author": author, "quantity": quantity}

@app.post('/new_book')
def new_book(item: Book, response_model=Book, response_model_exclude_unset=True):
    # response_model_exclude_unset - не возвращаются пустые необязательные данные
    # response_model_exclude = {"pages", "date"} = исключение свойств
    # response_model_exclude = {"pages", "date"} = отображение только указ. свойств

    return item

@app.post('/author')
def create_author(author: Author = Body(..., embed=True)):
    # embed - указание заголовка запроса
    return {"author": author}

@app.get('/book')
def get_book(q: str = Query(..., min_length=2, max_length=5, description='Search book', regex=r'[a-z]{2,5}')):
    # Query позволяет валидировать параметры get-запроса
    # None указывает на необязательность запроса
    # ... Ellipsis указывает на обязательность параметра
    # или же явно указать default value
    # q: List(str) = Query( - можем указать список параметров /?q=some&q=another&q=some_another
    # deprecated = True - флаг указывающий, что данный парметр устарел
    return q


@app.get('/book/{pk}')
def get_single_book(pk: int = Path(..., gt=1, le=10), pages: int = Query(None, gt=10, le=500)):
    # Path - валидация пути параметра pk
    # ... - указывает на обязательность pk
    # gt=1 - great than
    # le=10 - pk не должно быть более 10
    return {"pk": pk,
            "pges": pages}

