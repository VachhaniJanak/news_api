import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from database import curd

obj = curd()
# print(obj.get_user(user_id=1).email)
# print(obj.update_password(user_id=1, password='9876543221'))
# print(obj.create_user(email='abc@gmail.com', password='203920323'))
# print(obj.delete_user(user_id=2))


# from requests import post
#
# 
# print(post('http://127.0.0.1:8000', data={'token':'eweiweiuwe', 'artical_text':'dksjjdksjdksd'}).json())