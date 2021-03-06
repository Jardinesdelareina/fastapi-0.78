from typing import List
from fastapi import Body, FastAPI, Path, Query
from schemas import Case, User

app = FastAPI()


@app.get('/')
def home():
    return {'key': 'FastAPI start'}


@app.post('/user', response_model=User, response_model_exclude_unset=True)
def create_user(user: User, quantities: int = Body(...)):
    return {
        'user': user,
        'quantities': quantities,
    }
    

@app.post('/case')
def create_case(case: Case = Body(..., embed=True)):
    return {'case': case}


@app.get('/user')
def get_user(user: User, param: str = Query(None,              # param не обязателен к заполнению
                                        #...,                   # param обязателен к заполнению 
                                        #'test',                # значение param по-умолчанию
                                        #['test1', 'test2'],    # список значений по-умолчанию (param: List[str])
                                        min_length=2,          # минимальная длина param
                                        max_length=5,          # максимальная длина param
                                        #description='User',    # описание param
                                        #deprecated=True        # обозначение param устаревшим
                                        )):
    return {
        'user': user,
        'param': param,
    }


@app.get('/user/{pk}')
def get_user_id(pk: int = Path(...,   # pk обязателен к заполнению
                            gt=0,     # pk должен быть > 0
                            le=6,     # pk должен быть <= 6
                            ),
                            balance: float = Query(None,  # balance не обязателен к заполнению
                                            gt=0,       # balance должен быть > 0
                                            le=9999999.9  # balance должен быть <= 9999999.9
                                            )):
    return {
        'pk': pk,
        'balance': balance,
    }
