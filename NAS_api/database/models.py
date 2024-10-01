from secrets import token_urlsafe

from sqlalchemy import (Column, Integer, String)
from sqlalchemy.orm import declarative_base

from .engine import db_engine

Base = declarative_base()


class User(Base):
	__tablename__ = 'users'
	id = Column(Integer, primary_key=True, autoincrement=True)
	email = Column(String)
	password = Column(String)
	token = Column(String, default=token_urlsafe(32))



Base.metadata.create_all(db_engine)
