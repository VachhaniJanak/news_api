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


# for _ in range(10):
# 	obj.add_article(
# 		'Delhi doctor shot dead by 2 boys who came for treatment at hospital',
# 		'https://images.indianexpress.com/2024/10/nima-hospital-shooting.jpg?w=640',
# 		'The Indian Express',
# 		'''A doctor was shot dead in what appears to be a targeted attack at a small nursing home located in Kalindi Kunj in South East Delhi in the early hours of Thursday. According to the Delhi Police, they were alerted about the crime at around 1.45 am.
#
# 		When the police team arrived at the scene, they found Dr Javed Akhtar, a Unani practitioner, slumped over his desk with a gunshot wound to the left side of his head. Forensic teams from the District Crime Unit and Forensic Science Laboratory (FSL), Rohini, were called to the scene, and collected evidence for analysis, said the police.
#
# 		A police officer said their preliminary investigations revealed that two boys, approximately 16-17 years old, came to the hospital at around 1 am. One of the boys had an injured toe, which had been dressed the previous night at the same hospital by staff member Mohammad Kamil, the officer added.
#
# 		After the dressing, the two went to Dr Akhtar’s cabin for a prescription, and moments later, nursing staff Gajala Parveen and Kamil heard a gunshot. When Parveen went to the doctor’s cabin, she found Dr Akhtar in a pool of blood.
#
# 		“The two boys also came to the hospital the previous night, got the dressing done, and left. Prima facie it is a case of targeted killing as it is unprovoked and the assailants had done recce the previous night,” said Rajesh Deo, Deputy Commissioner of Police (South East).'''
# 	)
