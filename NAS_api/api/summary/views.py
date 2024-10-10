from fastapi import APIRouter, Body
from pydantic import BaseModel

from .utils import summarizeArticle

router = APIRouter()
summarize_article = summarizeArticle()


class RequestFormat(BaseModel):
	token_id: str
	article_id: int


class ResponseFormat(BaseModel):
	operation: bool
	summary: str = None
	message: str = None
	error: str = None


@router.post('/summary', response_model=ResponseFormat)
async def get_summary(data: RequestFormat = Body()):
	try:
		return summarize_article.summarize(data=data)
	except Exception as e:
		return {
			'operation': False,
			'error': str(e)
		}
