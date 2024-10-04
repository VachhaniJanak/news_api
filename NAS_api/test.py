# from database import curd
#
# obj = curd()


from requests import get
from bs4 import BeautifulSoup

headers = {
	'User-Agent': "Mozilla/6.0 (Windows NT 11.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246"}

# respone = get('https://indianexpress.com', headers=headers)
#
# soup = BeautifulSoup(respone.content, 'html.parser')
# # print(soup.prettify())
#
# for i in soup.find_all(class_='other-article'):
# 	link = i.find('a')['href']
# 	break

link = 'https://indianexpress.com/article/entertainment/bollywood/govinda-breaks-silence-on-shooting-himself-accidentally-answers-why-he-has-a-loaded-revolver-fame-is-a-flame-and-you-have-to-be-9603604/'
respone = get(link, headers=headers)

soup = BeautifulSoup(respone.content, 'html.parser')
print(soup.find('h1', id='main-heading-article').text)
print(soup.find('h2', class_='synopsis').text)
print(soup.find('span', class_='custom-caption').img['src'])
written_by = soup.find('div', class_="editor-date-logo")
print(written_by.find('a').text)
print(written_by.find('span')['content'])


# temp = soup.find('div', class_='story_details')
#
# for i in temp:
#
# 	if i.name == 'p' and 'read more' not in i.text[:10].lower() and 'also read' not in i.text[:10].lower():
# 		print(i.text)
#
# 	if i.name == 'div':
# 		if ' '.join(i.get('class')) == 'ev-meter-content ie-premium-content-block':
# 			break
#
# for i in temp.find('div', class_='ev-meter-content ie-premium-content-block'):
#
# 	if i.name == 'p' and 'read more' not in i.text[:10].lower() and 'also read' not in i.text[:10].lower():
# 		print(i.text)
#
# 	if i.name == 'div':
# 		if i.get('id') == 'id_newsletter_subscription':
# 			break
#
#


class IndianExpress:
	def __init__(self):
		pass

	def entertainment(self):
		pass

	def sport(self):
		pass

	def politics(self):
		pass

	def business(self):
		pass

	def tech(self):
		pass

	def education(self):
		pass

	def research(self):
		pass


class Entertainment:
	def __init__(self):
		pass

	def scrape_headline(self):
		pass

	def scrape_description(self):
		pass

	def scrape_writer(self):
		pass

	def scrape_datetime(self):
		pass

	def scrape_img(self):
		pass

	def scrape_context(self):
		pass
