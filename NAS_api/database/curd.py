from datetime import datetime, timedelta
from typing import Type

from sqlalchemy.orm import sessionmaker

from .engine import db_engine, vectordb_engine
from .models import User, UserSession, Article, Writer, NewsType, SiteName


def display_warn(message: str, l=10):
	print('\033[93m' + '[' + "@" * l, message, "@" * l + ']' + '\033[0m')


class curdUser:
	def __init__(self) -> None:
		self.Session = sessionmaker(bind=db_engine)
		self.session = self.Session()

	def create(self, username: str, email: str, password: str) -> bool | Type[User]:
		try:
			obj = User(username=username, email=email, password=password)
			self.session.add(obj)
			self.session.commit()
			return obj
		except Exception as e:
			self.session.rollback()
			display_warn(message=str(e) + ' class: crudUser -> function: create')
			return False

	def update_password(self, user_id: int, password: str) -> bool | Type[User]:
		try:
			obj = self.session.query(User).filter_by(id=user_id).one_or_none()
			obj.password = password
			self.session.commit()
			return obj
		except Exception as e:
			self.session.rollback()
			display_warn(message=str(e) + ' class: crudUser -> function: update_password')
			return False

	def delete(self, user_id: int) -> bool | Type[User]:
		try:
			obj = self.session.query(User).filter_by(id=user_id).one_or_none()
			self.session.delete(obj)
			self.session.commit()
			return obj
		except Exception as e:
			self.session.rollback()
			display_warn(message=str(e) + ' class: crudUser -> function: delete')
			return False

	def get_id_or_email(self, user_id: int = None, user_email: str = None) -> Type[User]:
		if user_id:
			return self.session.query(User).filter_by(id=user_id).one_or_none()
		if user_email:
			return self.session.query(User).filter_by(email=user_email).one_or_none()


class crudSession:
	def __init__(self) -> None:
		self.Session = sessionmaker(bind=db_engine)
		self.session = self.Session()

	def create(self, user: any) -> int | bool:
		try:
			session_obj = UserSession(user=user)
			self.session.add(session_obj)
			self.session.commit()
			return session_obj.token_id
		except Exception as e:
			self.session.rollback()
			display_warn(message=str(e) + ' class: crudSession -> function: create')
			return False

	def delete_all(self, user: any) -> bool:
		try:
			self.session.query(UserSession).filter_by(user=user).delete()
			self.session.commit()
			return True
		except Exception as e:
			self.session.rollback()
			display_warn(message=str(e) + ' class: crudSession -> function: delete_all')
			return False

	def delete(self, token_id: str) -> bool:
		try:
			self.session.query(UserSession).filter_by(token_id=token_id).delete()
			self.session.commit()
			return True
		except Exception as e:
			self.session.rollback()
			display_warn(message=str(e) + ' class: crudSession -> function: delete')
			return False

	def get_by_token(self, token_id: str) -> Type[UserSession]:
		return self.session.query(UserSession).filter_by(token_id=token_id).one_or_none()


class crudArticle:
	def __init__(self) -> None:
		self.Session = sessionmaker(bind=db_engine)
		self.session = self.Session()

	def add_article(self, headline: str, description: str, datetime, img_url: str, context: str, url: str,
	                site_name: str, writer: str, news_type: str) -> Type[Article] | bool:
		try:
			article = Article(
				headline=headline,
				description=description,
				datetime=datetime,
				img_url=img_url,
				context=context,
				url=url,
			)

			article.site_name = self.add_site_name(name=site_name)
			article.writer = self.add_writer(name=writer)
			article.news_type = self.add_news_type(news_type=news_type)

			self.session.add(article)
			self.session.commit()

			vectordb_engine.create(
				article_id=article.id,
				document=article.description,
			)
			return article

		except Exception as e:
			self.session.rollback()
			display_warn(message=str(e) + ' class: crudArticle -> function: add_article')
			return False

	def add_site_name(self, name: str) -> Type[SiteName] | SiteName:
		obj = self.session.query(SiteName).filter_by(name=name.lower()).one_or_none()
		if obj:
			return obj
		obj = SiteName(name=name.lower())
		return obj

	def add_writer(self, name: str) -> Type[SiteName] | Writer:
		obj = self.session.query(Writer).filter_by(name=name.lower()).one_or_none()
		if obj:
			return obj
		obj = Writer(name=name.lower())
		return obj

	def add_news_type(self, news_type: str) -> Type[NewsType] | NewsType:
		obj = self.session.query(NewsType).filter_by(type=news_type.lower()).one_or_none()
		if obj:
			return obj
		obj = NewsType(type=news_type.lower())
		return obj

	def get_by_ids(self, article_ids: tuple[int]) -> list[Type[Article]]:
		return self.session.query(Article).filter(Article.id.in_(article_ids)).all()

	def get_in_range(self, minmax: tuple) -> list[Type[Article]]:
		return self.session.query(Article).order_by(Article.datetime.desc()).offset(minmax[0]).limit(
			minmax[1] - minmax[0]).all()

	def delete_old(self, days: int = 1) -> bool:
		try:
			time_diff = datetime.now() - timedelta(days=days)
			self.session.query(Article).filter(Article.datetime <= time_diff).delete()
			self.session.commit()
			return True
		except Exception as e:
			self.session.rollback()
			display_warn(message=str(e) + ' class: crudArticle -> function: delete_old')
			return False
