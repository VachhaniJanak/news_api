# import os
# import sys

from fastapi import APIRouter, Body
from fastapi.responses import JSONResponse
from pydantic import BaseModel

from NAS_api.database import curd
from NAS_api.summarize.model import MODEL

# sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

router = APIRouter()
curd_obj = curd()
summ_model = MODEL()


class SummaryVerify(BaseModel):
	token_id: str
	article_id: int


class FetchVerify(BaseModel):
	token_id: str
	count: int


token = {'session_id': 'wejwjkej-skdjksdjdskdks'}

txt = '''More than 60% of S&P 500 components outperformed the index this quarter, compared to around 25% in the first half of the year. At the same time, the equal-weight version of the 500 -- a proxy for the average index stock -- gained 9% in the quarter, outperforming the index, which is more influenced by the heavily weighted shares of megacaps such as Nvidia (NASDAQ:NVDA) and Apple (NASDAQ:AAPL), according to LSEG. "Even if the megacaps aren't contributing as much, as long as the rest of the market is doing well... I think that's a healthy development," says Mark Hackett, senior investment strategist at Nationwide,

'''

articals = {
	'id': 1,
	'title': 'Lorem ipsum dolor sit explicabo adipisicing elit',
	'img': 'images/designer.jpg',
	'channel': 'BBC',
	'description': 'Market participants will also want to see non-tech firms deliver strong earnings in the months ahead to justify their gains. Responsive media query code for small screens.',
	'link': ''
}


@app.post('/summary')
async def get_summary(data: SummaryVerify = Body()):
	if data.token_id == token['session_id']:
		# return JSONResponse({'summary': summ_model.get_summary(temp.data[0])})
		return JSONResponse({'summary': txt})
	return JSONResponse({'summary': ''})


@app.post('/articals')
async def get_articals(data: FetchVerify = Body()):
	if data.token_id == token['session_id']:
		return JSONResponse({'data': [articals for i in range(10)]})
	return JSONResponse({'data': []})

