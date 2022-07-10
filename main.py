from typing import List
from fastapi import FastAPI, Query
from schemas import User

app = FastAPI()


@app.get('/')
def home():
    return {'key': 'FastAPI start'}


@app.get('/{pk}')
def get_item(pk: int, param: str = None):
    return {'key': pk, 'param': param}


@app.get('/user/{pk}/item/{item}')
def get_user_item(pk: int, item: str):
    return {'pk': pk,'item': item}


@app.post('/user')
def create_user(item: User):
    return item
    

@app.get('/user')
def get_user(param: List[str] = Query(#None, # param не обязателен к заполнению
                                #..., # param обязателен к заполнению 
                                #'test', # значение param по-умолчанию
                                ['test1', 'test2'], # список значений по-умолчанию
                                min_length=2, 
                                max_length=5, 
                                description='User Profile', # Описание param
                                #deprecated=True # обозначение param устаревшим
                                )):
    return param
