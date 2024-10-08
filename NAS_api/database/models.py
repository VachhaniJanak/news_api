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

	headline = Column(String, nullable=False, unique=True)
	description = Column(String)
	datetime = Column(DateTime, nullable=False)
	img_url = Column(String)
	context = Column(String, nullable=False)
	url = Column(String, nullable=False)

	site_id = Column(Integer, ForeignKey('sites.id'), nullable=True)
	writer_id = Column(Integer, ForeignKey('writers.id'), nullable=True)
	newstype_id = Column(Integer, ForeignKey('newstypes.id'), nullable=True)

	site_name = relationship('SiteName', back_populates='article')
	writer = relationship('Writer', back_populates='article')
	news_type = relationship('NewsType', back_populates='article')


class SiteName(Base):
	__tablename__ = 'sites'
	id = Column(Integer, primary_key=True, autoincrement=True)
	name = Column(String, nullable=False, unique=True)

	# Relationship with Article
	article = relationship('Article', back_populates='site_name')


class Writer(Base):
	__tablename__ = 'writers'
	id = Column(Integer, primary_key=True, autoincrement=True)
	name = Column(String, nullable=False, unique=True)

	# Relationship with Article
	article = relationship('Article', back_populates='writer')


class NewsType(Base):
	__tablename__ = 'newstypes'
	id = Column(Integer, primary_key=True, autoincrement=True)
	type = Column(String, unique=True)

	# Relationship with Article
	article = relationship('Article', back_populates='news_type')


Base.metadata.create_all(db_engine)
