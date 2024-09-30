from sqlalchemy.orm import sessionmaker

from database import User
from database import db_engine


class curd:
	def __init__(self):
		self.Session = sessionmaker(bind=db_engine)
		self.session = self.Session()

	def create_user(self, email: str, password: str) -> None:
		obj = User(email=email, password=password)
		self.session.add(obj)
		self.session.commit()

	def update_password(self, user_id: int, password: str) -> None:
		obj = self.session.query(User).filter_by(id=user_id).one_or_none()
		if obj:
			obj.password = password
			self.session.commit()

	def delete(self, user_id: int):
		obj = self.session.query(User).filter_by(id=user_id).one_or_none()
		if obj:
			self.session.delete(obj)
			self.session.commit()

	def get_user(self, user_id: int):
		return self.session.query(User).filter_by(id=user_id).one_or_none()
