from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()

# Place your database schema code here

# Example code:
class Company(Base):
    __tablename__ = "company"
    id = Column(Integer, primary_key = True)
    name = Column(String)
    info = Column(String)
    link = Column(String)
    kind = Column(String)

    def __repr__(self):
        return ("organization name: {}, info:{}, link: {}, what do they take: {}".format(self.name, self.info, self.link, self.kind))

class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key = True)
    username = Column(String, unique=True)
    password = Column(String)
    def __repr__(self):
        return("username: {}, password: {}".format(self.username,self.password))
