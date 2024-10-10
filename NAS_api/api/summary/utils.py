from typing import Type

from NAS_api.database import crudSession, crudArticle, UserSession
from NAS_api.summarize import MODEL


class summarizeArticle:
	def __init__(self) -> None:
		self.session_crud = crudSession()
		self.article_crud = crudArticle()
		self.model = MODEL()

	def summarize(self, data) -> dict[str, bool | str]:
		if not self.verify_token_id(token_id=data.token_id):
			return {
				'operation': False,
				'message': 'Token id not found.',
			}

		return {
			'operation': True,
			'summary': self.generate_summary(article_id=data.article_id),
		}

	def verify_token_id(self, token_id: str) -> bool | Type[UserSession]:
		user_session = self.session_crud.get_by_token(token_id=token_id)
		if user_session:
			return user_session
		else:
			return False

	def generate_summary(self, article_id: int) -> str:
		article = self.article_crud.get_by_ids(article_ids=(article_id,))
		if article:
			return self.model.get_summary(article[0].context)
