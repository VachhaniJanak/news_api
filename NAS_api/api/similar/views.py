from datetime import datetime
from typing import Type

from fastapi import APIRouter, Body
from pydantic import BaseModel

from .utils import SimilaritySearch

router = APIRouter()
similar = SimilaritySearch()


class RequestFormat(BaseModel):
	token_id: str
	article_id: int
	query: str
	upto: int


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
	datetime: Type[datetime]
	img_url: str
	context: str
	url: str

	site_name: Type[SiteName]
	writer: Type[Writer]
	news_type: Type[NewsType]


class ResponseFormat(BaseModel):
	operation: bool
	articles: list[Type[Article]]
	message: str
	error: str


@router.post('/similar', response_model=ResponseFormat)
async def get_articles(data: RequestFormat = Body()):
	try:
		return similar.get_articles(data=data)
	except Exception as e:
		return {
			'operation': False,
			'error': str(e)
		}
