from fastapi import APIRouter, Body
from fastapi.responses import JSONResponse
from pydantic import BaseModel

from NAS_api.database import curd


router = APIRouter()
curd_obj = curd()


class LoginData(BaseModel):
	email: str
	password: str


class RegData(BaseModel):
	username: str
	email: str
	password: str


token = {'session_id': 'wejwjkej-skdjksdjdskdks'}


@router.post('/create')
async def create(data: RegData = Body()):
	print(data.username)
	print(data.email)
	print(data.password)
	return {'message': "done"}


@router.post('/login')
async def login(data: LoginData = Body(), ):
	print(data.email)
	print(data.password)

	return JSONResponse(token)
