from typing import List
from fastapi import FastAPI, Path, Query
from schemas import User

app = FastAPI()


@app.get('/')
def home():
    return {'key': 'FastAPI start'}


@app.post('/user')
def create_user(item: User):
    return item
    

@app.get('/user')
def get_user(param: str = Query(None,              # param не обязателен к заполнению
                            #...,                   # param обязателен к заполнению 
                            #'test',                # значение param по-умолчанию
                            #['test1', 'test2'],    # список значений по-умолчанию (param: List[str])
                            min_length=2,          # минимальная длина param
                            max_length=5,          # максимальная длина param
                            #description='User',    # описание param
                            #deprecated=True        # обозначение param устаревшим
                            )):
    return param


@app.get('/user/{pk}')
def get_user_id(pk: int = Path(...,   # pk обязателен к заполнению
                            gt=0, # pk должен быть > 0
                            le=6, # pk должен быть <= 6
                            ),
                            token: int = Query(None, # token не обязателен к заполнению
                                            gt=0,    # token должен быть > 0
                                            le=2000  # token должен быть <= 2000 
                                            )):
    return {
        'pk': pk,
        'token': token
    }
