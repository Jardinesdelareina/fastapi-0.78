from fastapi import FastAPI
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
    