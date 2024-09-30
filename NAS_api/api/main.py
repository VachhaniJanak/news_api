import os
import sys

from fastapi import FastAPI, Body
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from uvicorn import run

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from database import curd

app = FastAPI()
curd_obj = curd()


class Data(BaseModel):
	token: str
	artical_text: str


@app.post('/')
async def root(query: Data = Body(...)):
	user_obj = curd_obj.get_user(user_token=query.token)
	if user_obj:
		print(user_obj.email)
		print(user_obj.password)
		pred = 'sdjskdjskjdksjdksjd'
		model_response = {'artical_summary': pred}
		return JSONResponse(model_response)


if '__main__' == __name__:
	run("main:app", host="127.0.0.1", port=8000, reload=True)
