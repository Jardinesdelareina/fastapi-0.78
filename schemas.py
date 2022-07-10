from datetime import date
from typing import List
from pydantic import BaseModel


class Token(BaseModel):
    title: str
    amount: float
    price: float


class Case(BaseModel):
    title: str
    compound: List[Token]
    balance: float


class User(BaseModel):
    name: str
    reg: date
    case: Case
