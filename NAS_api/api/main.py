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

@app.post('/summary')
async def get_summary():
	txt = '''More than 60% of S&P 500 components outperformed the index this quarter, compared to around 25% in the first half of the year. At the same time, the equal-weight version of the 500 -- a proxy for the average index stock -- gained 9% in the quarter, outperforming the index, which is more influenced by the heavily weighted shares of megacaps such as Nvidia (NASDAQ:NVDA) and Apple (NASDAQ:AAPL), according to LSEG. "Even if the megacaps aren't contributing as much, as long as the rest of the market is doing well... I think that's a healthy development," says Mark Hackett, senior investment strategist at Nationwide,

'''
	return JSONResponse({'summary': txt})


if '__main__' == __name__:
	run("main:app", host="127.0.0.1", port=8000, reload=True)
