from fastapi import APIRouter, Body
from fastapi.responses import JSONResponse
from pydantic import BaseModel

from NAS_api.database import curd

router = APIRouter()


class LoginData(BaseModel):
	email: str
	password: str


class RegData(BaseModel):
	username: str
	email: str
	password: str


class UserAPI:
	def __init__(self):
		self.curd_obj = curd()

	def create(self, data):
		if self.is_emailexist(email=data.email):
			return self.response_with(
				operation=False,
				message='Email already exists.'
			)

		user = self.curd_obj.create_user(
			username=data.username,
			email=data.email,
			password=data.password,
		)
		return self.response_with(
			operation=True,
			username=user.username,
			email=user.email,
			password=user.password,
			message='Account create successfully.'
		)

	def is_emailexist(self, email: str) -> any:
		user = self.curd_obj.get_user(user_email=email)
		if user:
			return user
		else:
			return False

	def response_with(self, operation: bool = None,
	                  token_id: str = None, username: str = None,
	                  email: str = None, password: str = None,
	                  message: str = None):

		return JSONResponse({
			'operation': operation,
			'token_id': token_id,
			'username': username,
			'email': email,
			'password': password,
			'message': message
		})

	def login(self, data):
		user = self.is_emailexist(email=data.email)
		if user:
			return self.check_password(user=user, data=data)
		else:
			return self.response_with(
				operation=False,
				message='Email does not exists.'
			)

	def check_password(self, user, data):
		if user.password == data.password:
			self.curd_obj.delete_all_sessions(user=user)
			token_id = self.curd_obj.create_session(user=user)
			return self.response_with(
				operation=True,
				token_id=token_id,
				username=user.username,
				email=user.email,
				password=user.password,
				message='Login successfully.'
			)
		else:
			return self.response_with(
				operation=False,
				message='Invalid password.'
			)


user_api = UserAPI()


@router.post('/create')
async def create(data: RegData = Body()):
	try:
		return user_api.create(data=data)
	except Exception as e:
		return JSONResponse({
			'operation': False,
			'error': str(e),
		})


@router.post('/login')
async def login(data: LoginData = Body(), ):
	try:
		return user_api.login(data=data)
	except Exception as e:
		return JSONResponse({
			'operation': False,
			'error': str(e)
		})
