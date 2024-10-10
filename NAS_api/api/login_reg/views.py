from fastapi import APIRouter, Body
from pydantic import BaseModel

from .utils import UserAPI

router = APIRouter()
user_api = UserAPI()


class LoginData(BaseModel):
	email: str
	password: str


class RegData(BaseModel):
	username: str
	email: str
	password: str


class ResponseFormat(BaseModel):
	operation: bool
	token_id: str = None
	username: str = None
	message: str = None
	error: str = None


@router.post('/create', response_model=ResponseFormat)
async def create(data: RegData = Body()):
	try:
		return user_api.create(data=data)
	except Exception as e:
		return {
			'operation': False,
			'error': str(e),
		}


@router.post('/login', response_model=ResponseFormat)
async def login(data: LoginData = Body(), ):
	try:
		return user_api.login(data=data)
	except Exception as e:
		return {
			'operation': False,
			'error': str(e)
		}
