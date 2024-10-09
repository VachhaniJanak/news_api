from fastapi import APIRouter, Body
from fastapi.responses import JSONResponse
from pydantic import BaseModel


router = APIRouter()

class RequestData(BaseModel):
	token_id: str
	count: int = 0



@router.post('/get_articles')
async def get_articles(data: RequestData = Body()):
	try:
		return articles_api.get_articles(data=data)
	except Exception as e:
		return JSONResponse({
			'operation': False,
			'message': str(e)
		})