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


# temp = {
# 	'headline': 'Lorem ipsum dolor sit explicabo adipisicing elit',
# 	'img_src': 'images/designer.jpg',
# 	'site': 'BBC',
# 	'context': 'Market participants will also want to see non-tech firms deliver strong earnings in the months ahead to justify their gains. Responsive media query code for small screens.',
# 	'url': 'https://www.google.com'
# },

# obj.add_article(
# 'Lorem ipsum dolor sit explicabo adipisicing elit',
# 'images/designer.jpg',
# 'BBC',
# 'Market participants will also want to see non-tech firms deliver strong earnings in the months ahead to justify their gains. Responsive media query code for small screens.'
# )
