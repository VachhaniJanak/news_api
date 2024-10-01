import os
import sys

from fastapi import FastAPI, Body
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


class SummaryVerify(BaseModel):
	token_id: str
	article_id: int


class FetchVerify(BaseModel):
	token_id: str
	count: int


token = {'session_id': 'wejwjkej-skdjksdjdskdks'}


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

	return JSONResponse(token)


txt = '''More than 60% of S&P 500 components outperformed the index this quarter, compared to around 25% in the first half of the year. At the same time, the equal-weight version of the 500 -- a proxy for the average index stock -- gained 9% in the quarter, outperforming the index, which is more influenced by the heavily weighted shares of megacaps such as Nvidia (NASDAQ:NVDA) and Apple (NASDAQ:AAPL), according to LSEG. "Even if the megacaps aren't contributing as much, as long as the rest of the market is doing well... I think that's a healthy development," says Mark Hackett, senior investment strategist at Nationwide,

'''


@app.post('/summary')
async def get_summary(data: SummaryVerify = Body()):
	if data.token_id == token['session_id']:
		return JSONResponse({'summary': txt})
	return JSONResponse({'summary': ''})


articals = {
	'id': 1,
	'title': 'Lorem ipsum dolor sit explicabo adipisicing elit',
	'img': 'images/designer.jpg',
	'channel': 'BBC',
	'description': 'Market participants will also want to see non-tech firms deliver strong earnings in the months ahead to justify their gains. Responsive media query code for small screens.',
	'link': ''
}


@app.post('/articals')
async def get_articals(data: FetchVerify = Body()):
	if data.token_id == token['session_id']:
		return JSONResponse({'data': [articals for i in range(10)]})
	return JSONResponse({'data': []})


if '__main__' == __name__:
	run("main:app", host="127.0.0.1", port=8000, reload=True)
