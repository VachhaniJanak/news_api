from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from uvicorn import run

from api import login_reg_router, summary_router

app = FastAPI()
app.include_router(login_reg_router)
app.include_router(summary_router)


app.add_middleware(
	CORSMiddleware,
	allow_origins=["*"],
	allow_credentials=True,
	allow_methods=["*"],
	allow_headers=["*"],
)

if '__main__' == __name__:
	run("main:app", host="127.0.0.1", port=8000, reload=True)
