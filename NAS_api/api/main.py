from fastapi import FastAPI
from uvicorn import run

app = FastAPI()


@app.get('/')
def root():
	return {'message': 'Hello, Wolrd'}


if '__main__' == __name__:
	run("main:app", host="127.0.0.1", port=8000, reload=True)
