from secrets import token_urlsafe

from sqlalchemy import (Column, Integer, String, ForeignKey, DateTime, UniqueConstraint)
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy.sql import func

from .engine import db_engine

Base = declarative_base()


class User(Base):
	__tablename__ = 'users'
	id = Column(Integer, primary_key=True, autoincrement=True)
	username = Column(String, nullable=False)
	email = Column(String, nullable=False, unique=True)
	password = Column(String, nullable=False)

	session = relationship('UserSession', back_populates='user', cascade="all, delete-orphan")


class UserSession(Base):
	__tablename__ = 'usersessions'
	id = Column(Integer, primary_key=True, autoincrement=True)
	user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
	token_id = Column(String, default=lambda: token_urlsafe(32), unique=True, nullable=False)
	timestamp = Column(DateTime, default=func.now(), nullable=False)

	# Relationship with User
	user = relationship('User', back_populates='session')

	# Ensure unique session per user
	__table_args__ = (UniqueConstraint('user_id', 'token_id', name='unique_user_token'),)


class Article(Base):
	__tablename__ = 'articles'

	id = Column(Integer, primary_key=True, autoincrement=True)
	headline = Column(String, unique=True, nullable=False)
	description = Column(String)
	writer = Column(String)
	datetime = Column(DateTime, nullable=False)
	img_url = Column(String)
	context = Column(String, nullable=False)
	site_name = Column(String, nullable=False)
	url = Column(String, unique=True, nullable=False)


Base.metadata.create_all(db_engine)
