import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from database import curd, UserSession

obj = curd()


# from requests import post

# print(post('http://127.0.0.1:8000', data={'token':'eweiweiuwe', 'artical_text':'dksjjdksjdksd'}).json())


# temp = User()
# temp.session = [
# 	Session(), Session()
# ]

# obj.create_user(username='teack', email="wwwteackcom@gmail.com", password='123456789')


# print(obj.create_session(user=obj.get_userbyid(user_id=1)))

# print(obj.delete_session(token_id='etYj7AfgxFcQWJ5651haKOyCh5A6FpL4u666yn6nLh4'))

