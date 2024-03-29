from sqlalchemy import Column,Integer,String,create_engine,Text
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
class User(Base):
    __tablename__ = 'user'

    id = Column(Integer,primary_key=True)
    username = Column(String(20),nullable=False)
    password = Column(String(100),nullable=False)
    password3 = Column(String(100),nullable=False)

class Article(Base):
    __tablename__ = 'article'

    id = Column(Integer,primary_key=True)
    title = Column(String(100),nullable=False)
    content = Column(Text, nullable=False)
