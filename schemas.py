from datetime import date
from typing import List
from pydantic import BaseModel, validator, Field


class Token(BaseModel):
    title: str = Field(..., max_length=6)
    amount: float
    price: float


class Case(BaseModel):
    title: str = Field(..., max_length=20)
    compound: List[Token] = []
    balance: float = 0


class User(BaseModel):
    login: str = Field(
        ..., 
        min_length=5, 
        max_length=15, 
        description='Длина логина должна быть не меньше 5 и не больше 15 символов'
        )
    password: str = Field(
        ..., 
        min_length=8, 
        max_length=20, 
        description='Длина пароля должна быть не меньше 8 и не больше 15 символов'
        )
    phone: int = Field(
        ..., 
        lt=14, 
        description='Не верный формат номера'
        )
    email: str = Field(...)
    reg: date
    case: Case = {}

    @validator('email')
    def check_email(cls, adress):
        if '@' not in adress:
            raise ValueError('Не верный формат email')
        return adress
