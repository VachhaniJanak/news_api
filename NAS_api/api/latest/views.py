from datetime import datetime

from fastapi import APIRouter, Body
from pydantic import BaseModel

from .utils import LatestArticle

router = APIRouter()
latest_article = LatestArticle()


class RequestFormat(BaseModel):
	token_id: str
	from_count: int = 0


class SiteName(BaseModel):
	name: str


class Writer(BaseModel):
	name: str


class NewsType(BaseModel):
	type: str


class Article(BaseModel):
	id: int
	headline: str
	description: str
	datetime: datetime
	img_url: str
	context: str
	url: str

	site_name: SiteName
	writer: Writer
	news_type: NewsType


class ResponseFormat(BaseModel):
	operation: bool
	articles: list[Article] = None
	message: str = None
	error: str = None


@router.post('/articles', response_model=ResponseFormat)
async def get_articles(data: RequestFormat = Body()):
	try:
		return latest_article.get_articles(data=data)
	except Exception as e:
		return {
			'operation': False,
			'error': str(e)
		}
