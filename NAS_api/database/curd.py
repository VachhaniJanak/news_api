from sqlalchemy.orm import sessionmaker

from .engine import db_engine
from .models import User, UserSession, Article


def display_warn(message: str, l=10):
	print('\033[93m' + '[' + "@" * l, message, "@" * l + ']' + '\033[0m')


class curd:
	def __init__(self) -> None:
		self.Session = sessionmaker(bind=db_engine)
		self.session = self.Session()

	def create_user(self, username: str, email: str, password: str) -> any:
		try:
			obj = User(username=username, email=email, password=password)
			self.session.add(obj)
			self.session.commit()
			return obj
		except Exception as e:
			display_warn(message=str(e) + ' class: crud -> function: create_user')
			return False

	def update_password(self, user_id: int, password: str) -> any:
		try:
			obj = self.session.query(User).filter_by(id=user_id).one_or_none()
			obj.password = password
			self.session.commit()
			return obj
		except Exception as e:
			display_warn(message=str(e) + ' class: crud -> function: update_password')
			return False

	def delete_user(self, user_id: int) -> any:
		try:
			obj = self.session.query(User).filter_by(id=user_id).one_or_none()
			self.session.delete(obj)
			self.session.commit()
			return obj
		except Exception as e:
			display_warn(message=str(e) + ' class: crud -> function: delete_user')
			return False

	def get_user(self, user_id: int = None, user_email: str = None) -> any:
		if user_id:
			return self.session.query(User).filter_by(id=user_id).one_or_none()
		if user_email:
			return self.session.query(User).filter_by(email=user_email).one_or_none()

	def get_userbylogin(self, email: str, password: str) -> any:
		return self.session.query(User).filter_by(email=email, password=password).one_or_none()

	def create_session(self, user: any) -> any:
		try:
			session_obj = UserSession(user=user)
			self.session.add(session_obj)
			self.session.commit()
			return session_obj.token_id
		except Exception as e:
			display_warn(message=str(e) + ' class: crud -> function: create_session')
			return False

	def delete_all_sessions(self, user: any) -> any:
		try:
			sessions_obj = self.session.query(UserSession).filter_by(user=user).all()
			for session_obj in sessions_obj:
				self.session.delete(session_obj)
			self.session.commit()
			return True
		except Exception as e:
			display_warn(message=str(e) + ' class: crud -> function: delete_all_session')
			return False

	def delete_session(self, token_id: str):
		try:
			session_obj = self.session.query(UserSession).filter_by(token_id=token_id).one_or_none()
			self.session.delete(session_obj)
			self.session.commit()
			return True
		except Exception as e:
			display_warn(message=str(e) + ' class: crud -> function: delete_session')
			return False

	def get_session_by_token(self, token_id: str):
		return self.session.query(UserSession).filter_by(token_id=token_id).one_or_none()

	def add_article(self, headline: str, img_url: str, site_name: str, context: str):
		try:
			article = Article(
				headline=headline,
				img_url=img_url,
				site_name=site_name,
				context=context
			)
			self.session.add(article)
			self.session.commit()
			return article
		except Exception as e:
			display_warn(message=str(e) + ' class: crud -> function: add_article')
			return False

	def get_articles(self, article_id: int):
		return self.session.query(Article).filter_by(id=article_id).one_or_none()