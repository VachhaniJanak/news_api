from fastapi import FastAPI, Body
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from uvicorn import run

app = FastAPI()


class Data(BaseModel):
	token: str
	artical_text: str


@app.post('/')
async def root(query: Data = Body(...)):
	pred = 'sdjskdjskjdksjdksjd'
	model_response = {'artical_summary': pred}
	return JSONResponse(model_response)


if '__main__' == __name__:
	run("main:app", host="127.0.0.1", port=8000, reload=True)
