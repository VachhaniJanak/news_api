from datetime import datetime, timedelta
from threading import Thread

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from uvicorn import run

from api import login_reg_router, summary_router, similar_router, latest_router
from database import crudArticle
from newscraper import IndianExpress, TheTimesOfIndian

flag = True

app = FastAPI()
news_site_objs = (IndianExpress(), TheTimesOfIndian())
article_crud = crudArticle()
old_datetime = datetime.now()

app.include_router(login_reg_router)
app.include_router(summary_router)
app.include_router(similar_router)
app.include_router(latest_router)


def fetch_news():
	global flag
	global old_datetime
	if flag and (datetime.now() - old_datetime >= timedelta(hours=1)):
		flag = False

		for news_site_obj in news_site_objs:
			news_site_obj.fetch_alldata()
			news_site_dict = news_site_obj.__dict__
			for news_type in list(news_site_dict.keys()):
				for article in news_site_dict[news_type]:
					article.news_type = news_type
					article.datetime = datetime.fromisoformat(article.datetime)
					article_crud.add_article(**article.__dict__)

		old_datetime = datetime.now()
		flag = True


app.add_middleware(
	CORSMiddleware,
	allow_origins=["*"],
	allow_credentials=True,
	allow_methods=["*"],
	allow_headers=["*"],
)


@app.middleware("http")
async def addmiddleware(request: Request, call_next):
	Thread(target=fetch_news, args=()).start()
	response = await call_next(request)
	return response


if '__main__' == __name__:
	run("main:app", host="127.0.0.1", port=8000, reload=True)
