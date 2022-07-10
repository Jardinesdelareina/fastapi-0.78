from datetime import date
from typing import List
from pydantic import BaseModel, validator


class Token(BaseModel):
    title: str
    amount: float
    price: float

    @validator('amount', 'price')
    def check_num(cls, num):
        if num < 0:
            raise ValueError('Значение не может быть меньше 0')
        return num


class Case(BaseModel):
    title: str
    compound: List[Token]
    balance: float


class User(BaseModel):
    name: str
    phone: int
    email: str
    reg: date
    case: Case

    @validator('phone')
    def check_phone(cls, num):
        if len(str(num)) < 11:
            raise ValueError('Не верный формат номера')
        return num
