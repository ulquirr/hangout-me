from pydantic import BaseModel

class Hangout(BaseModel):
    title: str
    content: str
    date: str

    class Config:
        orm_mode = True


class ShowHangout(BaseModel):
    id: int
    title: str
    content: str
    date: str

    class Config():
        orm_mode = True