import os
import sys

from fastapi import FastAPI, Body, Request, Response, Cookie
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from uvicorn import run

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from database import curd

app = FastAPI()
curd_obj = curd()

app.add_middleware(
	CORSMiddleware,
	allow_origins=["*"],
	allow_credentials=True,
	allow_methods=["*"],
	allow_headers=["*"],
)


class LoginData(BaseModel):
	email: str
	password: str


class RegData(BaseModel):
	username: str
	email: str
	password: str


@app.post('/create')
async def create(data: RegData = Body()):
	print(data.username)
	print(data.email)
	print(data.password)
	return {'message': "done"}


@app.post('/')
async def login(data: LoginData = Body(), ):
	print(data.email)
	print(data.password)

	return JSONResponse({'session_id': 'wejwjkej-skdjksdjdskdks'})


@app.post('/forgot-password')
async def reset():
	pass


if '__main__' == __name__:
	run("main:app", host="127.0.0.1", port=8000, reload=True)
