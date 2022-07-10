from datetime import date
from typing import List
from pydantic import BaseModel


class Technologies(BaseModel):
    title: str


class User(BaseModel):
    first_name: str
    last_name: str
    birthday: date
    is_married: bool = None
    technologies: List[Technologies]
    