from sqlalchemy.schema import Column
from sqlalchemy.dialects.mysql import LONGTEXT
from sqlalchemy.types import String, Integer, Text
from hangout.database import Base

class Hangout(Base):
    __tablename__ = "hangouts"
    id = Column(Integer, primary_key=True, index=True)
    
    title = Column(String(20), unique=True)
    content = Column(String(20), unique=True)
    date = Column(String(20), unique=True)


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    
    login = Column(String(20), unique=True)
    password = LONGTEXT()
      