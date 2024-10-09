from NAS_api.database import curdUser, crudSession


class UserAPI:
	def __init__(self):
		self.user_curd = curdUser()
		self.session_curd = crudSession()

	def create(self, data):
		if self.is_email_exist(email=data.email):
			return {
				'operation': False,
				'message': 'Email already exists.'
			}

		user = self.user_curd.create(
			username=data.username,
			email=data.email,
			password=data.password,
		)
		return {
			'operation': True,
			'username': user.username,
			'message': 'Account create successfully.'
		}

	def is_email_exist(self, email: str) -> any:
		user = self.user_curd.get_id_or_email(user_email=email)
		if user:
			return user
		else:
			return False

	def login(self, data):
		user = self.is_email_exist(email=data.email)
		if user:
			return self.check_password(user=user, data=data)
		else:
			return {
				'operation': False,
				'message': 'Email does not exists.'
			}

	def check_password(self, user, data):
		if user.password == data.password:
			self.session_curd.delete_all(user=user)
			token_id = self.session_curd.create(user=user)
			return {
				'operation': True,
				'token_id': token_id,
				'username': user.username,
				'message': 'Login successfully.'
			}
		else:
			return {
				'operation': False,
				'message': 'Invalid password.'
			}
