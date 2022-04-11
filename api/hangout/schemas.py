from pydantic import BaseModel

class Hangout(BaseModel):
    title: str
    content: str
    date: str

    class Config:
        orm_mode = True

class User(BaseModel):
    login: str
    password: str

    class Config:
        orm_mode = True



class ShowHangout(BaseModel):
    id: int
    title: str
    content: str
    date: str

    class Config():
        orm_mode = True


class ShowUser(BaseModel):
    id: int
    login: str
    password: str


    class Config():
        orm_mode = True