from datetime import datetime

from bs4 import BeautifulSoup
from requests import get

urls = {
	'parent': 'https://timesofindia.indiatimes.com',
	'political': 'https://timesofindia.indiatimes.com/politics/politics-specials',
	'business': 'https://timesofindia.indiatimes.com/business',
	'entertainment': 'https://timesofindia.indiatimes.com/entertainment',
	'sports': 'https://timesofindia.indiatimes.com/sports',
	'education': 'https://timesofindia.indiatimes.com/education',
	'technology': 'https://timesofindia.indiatimes.com/technology',
}


class scraper:
	def __init__(self, url=None, headers=None, soup=None):
		self.__soup = soup
		if url:
			self.__soup = BeautifulSoup(get(url, headers=headers).content, 'html.parser')

		self.headline = ''
		self.description = ''
		self.writer = ''
		self.datetime = ''
		self.img_url = ''
		self.context = ''
		self.site_name = 'TheTimesOfIndian'
		self.url = url

		self.fetch_alldata()

	def __scrape_headline(self):
		self.headline = self.__soup.find('h1').text

	def __scrape_description(self):
		try:
			self.description = self.__soup.find('div', class_='M1rHh undefined').text
		except Exception as e:
			print(str(e), 'File -> TheTimeOfIndia : class ->  Scraper : Func -> __scrape_description')

	def __scrape_writer(self):
		try:
			self.writer = self.__soup.find('div', class_='xf8Pm byline').a.text
		except:
			self.writer = 'ANI'

	def __scrape_datetime(self):
		date = self.__soup.find('div', class_='xf8Pm byline').span.text.split('Updated:')
		if len(date) > 1:
			self.datetime = datetime.strptime(date[1].strip(), "%b %d, %Y, %H:%M %Z")
		else:
			self.datetime = datetime.strptime(date[0].strip(), "%b %d, %Y, %H:%M %Z")

	def __scrape_img(self):
		self.img_url = self.__soup.find('div', class_='wJnIp').img['src']

	def __scrape_context(self):

		dis = self.__soup.find('div', class_='wJnIp').img.get('title', '')
		self.context = self.__soup.find('div', class_='_s30J clearfix').text.replace(dis, '')

	def fetch_alldata(self):
		self.__scrape_headline()
		self.__scrape_description()
		self.__scrape_writer()
		self.__scrape_datetime()
		self.__scrape_img()
		self.__scrape_context()

		del self.__soup


class TheTimesOfIndian:
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

		for tags in soup.find_all('div', class_='col_l_6'):
			try:
				top_news_articles_urls.append(tags.find('a').get('href'))
			except Exception as e:
				print(e)

		for url in top_news_articles_urls:
			try:
				self.top_news.append(scraper(url, headers=self.__get_header()))
			except Exception as e:
				print(e)

	def __entertainment(self):
		entertainment_articles_urls = []
		soup = self.__response(urls['entertainment'], self.__get_header())

		for tags in soup.find_all('div', class_='slick-slide'):
			try:
				entertainment_articles_urls.append(tags.find('a').get('href'))
			except Exception as e:
				print(e)

		for url in entertainment_articles_urls:
			try:
				self.entertainment.append(scraper(url, headers=self.__get_header()))
			except Exception as e:
				print(e)

	def __sport(self):
		all_sport_articles = []
		sport_articles_urls = []
		soup = self.__response(urls['sports'], self.__get_header())

		for tags in soup.find_all('li', class_='sBgUN')[1:]:
			url = tags.find('a').get('href')
			all_sport_articles.append(self.__response(url=url, headers=self.__get_header()))

		for obj in all_sport_articles:
			for item in obj.find_all('div', class_='col_l_4 col_m_4'):
				sport_articles_urls.append(item.a.get('href'))

		for url in sport_articles_urls:
			try:
				self.sport.append(scraper(url, headers=self.__get_header()))
			except Exception as e:
				print(e)

	def __politics(self):
		politics_articles_urls = []
		soup = self.__response(urls['political'], self.__get_header())

		for tags in soup.find('ul', class_='top-newslist').find_all('a', class_='w_img'):
			politics_articles_urls.append(f'{urls['parent']}{tags.get('href')}')

		for url in politics_articles_urls:
			try:
				self.politics.append(scraper(url, headers=self.__get_header()))
			except Exception as e:
				print(e)

	def __business(self):
		all_business_articles = []
		business_articles_urls = []
		soup = self.__response(urls['business'], self.__get_header())

		for tags in soup.find_all('li', class_='sBgUN')[1:]:
			url = tags.find('a').get('href')
			all_business_articles.append(self.__response(url=url, headers=self.__get_header()))

		for obj in all_business_articles:
			try:
				for a in soup.find('div', class_='row').find_all('a'):
					business_articles_urls.append(a.get('href'))
			except Exception as e:
				try:
					self.business.append(scraper(headers=self.__get_header(), soup=obj))
				except Exception as e:
					print(e)

		for url in business_articles_urls:
			try:
				self.business.append(scraper(url=url, headers=self.__get_header()))
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
		all_education_articles = []
		education_articles_urls = []
		soup = self.__response(urls['education'], self.__get_header())

		for tags in soup.find_all('li', class_='sBgUN')[1:]:
			url = tags.find('a').get('href')
			all_education_articles.append(self.__response(url=url, headers=self.__get_header()))

		for obj in all_education_articles:
			try:
				for a in soup.find('div', class_='row').find_all('a'):
					education_articles_urls.append(a.get('href'))
			except Exception as e:
				try:
					self.education.append(scraper(headers=self.__get_header(), soup=obj))
				except Exception as e:
					print(e)

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
