from bs4 import BeautifulSoup
from requests import get
from datetime import datetime

urls = {
	'parent': 'https://indianexpress.com',
	'political': 'https://indianexpress.com/section/political-pulse/',
	'business': 'https://indianexpress.com/section/business/',
	'entertainment': 'https://indianexpress.com/section/entertainment/',
	'sports': 'https://indianexpress.com/section/sports/',
	'education': 'https://indianexpress.com/section/education/',
	'research': 'https://indianexpress.com/section/research/',
	'technology': 'https://indianexpress.com/section/technology/',
}


class scraper:
	def __init__(self, url, headers):
		self.__soup = BeautifulSoup(get(url, headers=headers).content, 'html.parser')

		self.headline = ''
		self.description = ''
		self.writer = ''
		self.datetime = ''
		self.img_url = ''
		self.context = ''
		self.site_name = 'IndianExpress'
		self.url = url

		self.fetch_alldata()

	def __scrape_headline(self):
		self.headline = self.__soup.find('h1').text

	def __scrape_description(self):
		self.description = self.__soup.find('h2', class_='synopsis').text

	def __scrape_writer(self):
		self.writer = self.__soup.find('div', class_="editor-details-new-change").find('a').text

	def __scrape_datetime(self):
		self.datetime = self.__soup.find('div', class_="editor-details-new-change").find('span')['content']
		self.datetime = datetime.fromisoformat(self.datetime)

	def __scrape_img(self):
		self.img_url = self.__soup.find('span', class_='custom-caption').img['src']

	def __scrape_context(self):
		raw_context = self.__soup.find('div', class_='story_details').find_all('p')
		lenght = len(raw_context)
		for i, html_tag in enumerate(raw_context):
			temp = html_tag.text[:20].lower()
			if 'read more' not in temp and 'also read' not in temp:
				if lenght == i + 1:
					self.context += '\n' + html_tag.text.lower().split('click')[0].title()
				else:
					self.context += '\n' + html_tag.text

	def fetch_alldata(self):
		self.__scrape_headline()
		self.__scrape_description()
		self.__scrape_writer()
		self.__scrape_datetime()
		self.__scrape_img()
		self.__scrape_context()

		del self.__soup


class IndianExpress:
	def __init__(self):

		self.top_news = list()
		self.entertainment = list()
		self.sport = list()
		self.politics = list()
		self.business = list()
		self.technology = list()
		self.education = list()
		self.research = list()

	def __get_header(self):
		return None

	def __response(self, url, headers):
		respone = get(url, headers=headers)
		return BeautifulSoup(respone.content, 'html.parser')

	def __top_news(self):
		top_news_articles_urls = []
		soup = self.__response(urls['parent'], self.__get_header())

		for tags in soup.find_all('div', class_='other-article'):
			top_news_articles_urls.append(tags.a['href'])

		for url in top_news_articles_urls:
			try:
				self.top_news.append(scraper(url, headers=self.__get_header()))
			except Exception as e:
				print(e)

	def __entertainment(self):
		entertainment_articles_urls = []
		soup = self.__response(urls['entertainment'], self.__get_header())

		for tags in soup.find('div', class_='nation'):
			if tags.name == 'div' and tags['class'][0] == 'articles':
				entertainment_articles_urls.append(tags.a['href'])

		for url in entertainment_articles_urls:
			try:
				self.entertainment.append(scraper(url, headers=self.__get_header()))
			except Exception as e:
				print(e)

	def __sport(self):
		sport_articles_urls = []
		soup = self.__response(urls['sports'], self.__get_header())

		for tags in soup.find('div', class_='nation'):
			if tags.name == 'div' and tags['class'][0] == 'articles':
				sport_articles_urls.append(tags.a['href'])

		for url in sport_articles_urls:
			try:
				self.sport.append(scraper(url, headers=self.__get_header()))
			except Exception as e:
				print(e)

	def __politics(self):
		politics_articles_urls = []
		soup = self.__response(urls['political'], self.__get_header())

		for tags in soup.find('div', class_='nation'):
			if tags.name == 'div' and tags['class'][0] == 'articles':
				politics_articles_urls.append(tags.a['href'])

		for url in politics_articles_urls:
			try:
				self.politics.append(scraper(url, headers=self.__get_header()))
			except Exception as e:
				print(e)

	def __business(self):
		business_articles_urls = []
		soup = self.__response(urls['business'], self.__get_header())

		for tags in soup.find('div', class_='nation'):
			if tags.name == 'div' and tags['class'][0] == 'articles':
				business_articles_urls.append(tags.a['href'])

		for url in business_articles_urls:
			try:
				self.business.append(scraper(url, headers=self.__get_header()))
			except Exception as e:
				print(e)

	def __tech(self):
		tech_articles_urls = []
		soup = self.__response(urls['technology'], self.__get_header())

		for tags in soup.find('div', class_='nation'):
			if tags.name == 'div' and tags['class'][0] == 'articles':
				tech_articles_urls.append(tags.a['href'])

		for url in tech_articles_urls:
			try:
				self.technology.append(scraper(url, headers=self.__get_header()))
			except Exception as e:
				print(e)

	def __education(self):
		education_articles_urls = []
		soup = self.__response(urls['education'], self.__get_header())

		for tags in soup.find('div', class_='nation'):
			if tags.name == 'div' and tags['class'][0] == 'articles':
				education_articles_urls.append(tags.a['href'])

		for url in education_articles_urls:
			try:
				self.education.append(scraper(url, headers=self.__get_header()))
			except Exception as e:
				print(e)

	def __research(self):
		entertainment_articles_urls = []
		soup = self.__response(urls['research'], self.__get_header())

		for tags in soup.find('div', class_='nation'):
			if tags.name == 'div' and tags['class'][0] == 'articles':
				entertainment_articles_urls.append(tags.a['href'])

		for url in entertainment_articles_urls:
			try:
				self.research.append(scraper(url, headers=self.__get_header()))
			except Exception as e:
				print(e)

	def fetch_alldata(self):
		self.__top_news()
		self.__entertainment()
		self.__sport()
		self.__politics()
		self.__business()
		self.__education()
		# self.__tech()
		# self.__research()

