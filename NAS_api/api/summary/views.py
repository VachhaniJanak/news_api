from fastapi import APIRouter, Body
from fastapi.responses import JSONResponse
from pydantic import BaseModel

from .utils import summarizeArticle

router = APIRouter()
summarize_article = summarizeArticle()


class RequestBody(BaseModel):
	token_id: str
	article_id: int


class ResponseBody(BaseModel):
	operation: bool
	summary: str = None
	message: str = None
	error: str = None


@router.post('/summary', response_model=ResponseBody)
async def get_summary(data: RequestBody = Body()):
	try:
		return summarize_article.summarize(data=data)
	except Exception as e:
		return JSONResponse({
			'operation': False,
			'error': str(e)
		})
