from typing import Type

from database import crudArticle, crudSession, UserSession, Article
from database.engine import vectordb_engine


class SimilaritySearch:

	def __init__(self) -> None:
		self.article_crud = crudArticle()
		self.session_crud = crudSession()

	def get_articles(self, data) -> dict[str, bool | str | list[Type[Article]]]:
		if not self.verify_token_id(token_id=data.token_id):
			return {
				'operation': False,
				'message': 'Token id not found.'
			}

		if data.article_id:
			return {
				'operation': True,
				'articles': self.article_crud.get_by_ids(
					article_ids=vectordb_engine.get_by_id(
						article_id=data.article_id,
						top_n=data.upto
					)
				)}

		if data.query:
			return {
				'operation': True,
				'articles': self.article_crud.get_by_ids(
					article_ids=vectordb_engine.get_by_query(
						query=data.query,
						top_n=data.upto
					)
				)
			}
		return {
			'operation': False,
			'message': 'Articles Not Found'
		}

	def verify_token_id(self, token_id: str) -> Type[UserSession] | bool:
		user_session = self.session_crud.get_by_token(token_id=token_id)
		if user_session:
			return user_session
		else:
			return False
