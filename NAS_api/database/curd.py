from sqlalchemy.orm import sessionmaker

from .engine import db_engine
from .models import User


def display_warn(message: str, l=10):
	print('\033[93m' + '[' + "@" * l, message, "@" * l + ']' + '\033[0m')


class curd:
	def __init__(self) -> None:
		self.Session = sessionmaker(bind=db_engine)
		self.session = self.Session()

	def create_user(self, email: str, password: str) -> bool:
		try:
			obj = User(email=email, password=password)
			self.session.add(obj)
			self.session.commit()
			return True
		except Exception as e:
			display_warn(message=str(e)+' class: crud -> function: create_user')
			return False

	def update_password(self, user_id: int, password: str) -> bool:
		try:
			obj = self.session.query(User).filter_by(id=user_id).one_or_none()
			obj.password = password
			self.session.commit()
			return True
		except Exception as e:
			display_warn(message=str(e)+' class: crud -> function: update_password')
			return False

	def delete_user(self, user_id: int) -> bool:
		try:
			obj = self.session.query(User).filter_by(id=user_id).one_or_none()
			self.session.delete(obj)
			self.session.commit()
			return True
		except Exception as e:
			display_warn(message=str(e)+' class: crud -> function: delete_user')
			return False

	def get_user(self, user_id: int = None, user_token: str = None) -> any:
		if user_id:
			return self.session.query(User).filter_by(id=user_id).one_or_none()

		if user_token:
			return self.session.query(User).filter_by(token=user_token).one_or_none()

