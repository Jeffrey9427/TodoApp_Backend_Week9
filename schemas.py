from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

class UserBase(BaseModel):
    email: str
    username: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int

    class Config:
        orm_mode = True

class UserLogin(BaseModel):
    email: str
    password: str

class TodoBase(BaseModel):
    title: str
    completed: bool

class TodoCreate(TodoBase):
    pass

class Todo(TodoBase):
    id: int
    user_id: int

    class Config:
        orm_mode = True

class UserWithTodos(User):
    todos: List[Todo] = []

    class Config:
        orm_mode = True

class Session(BaseModel):
    id: str
    user_id: int
    expiry_time: datetime

    class Config:
        orm_mode = True
