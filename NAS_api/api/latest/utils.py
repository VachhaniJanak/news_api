from typing import Type

from NAS_api.database import crudArticle, crudSession, UserSession, Article


class LatestArticle:
	def __init__(self) -> None:
		self.article_crud = crudArticle()
		self.session_crud = crudSession()

	def get_articles(self, data) -> dict[str, bool | str | list[Type[Article]]]:
		if not self.verify_token_id(token_id=data.token_id):
			return {
				'operation': False,
				'message': 'Token id not found.'
			}

		return {
			'operation': True,
			'articles': self.article_crud.get_in_range(
				minmax=(data.from_count, data.from_count + 16)
			)
		}

	def verify_token_id(self, token_id: str) -> Type[UserSession] | bool:
		user_session = self.session_crud.get_by_token(token_id=token_id)
		if user_session:
			return user_session
		else:
			return False
