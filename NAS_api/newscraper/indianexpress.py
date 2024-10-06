from bs4 import BeautifulSoup
from requests import get


class scraper:
	def __init__(self, url, headers):
		self.respone = get(url, headers=headers)
		self.soup = BeautifulSoup(self.respone.content, 'html.parser')
		self.written_by = self.soup.find('div', class_="editor-date-logo")

		self.headline = ''
		self.description = ''
		self.writer = ''
		self.datetime = ''
		self.img_url = ''
		self.context = ''

		self.fetch_alldata()

	def scrape_headline(self):
		self.headline = self.soup.find('h1', id='main-heading-article').text

	def scrape_description(self):
		self.description = self.soup.find('h2', class_='synopsis').text

	def scrape_writer(self):
		self.writer = self.written_by.find('a').text

	def scrape_datetime(self):
		self.datetime = self.written_by.find('span')['content']

	def scrape_img(self):
		self.img_url = self.soup.find('span', class_='custom-caption').img['src']

	def scrape_context(self):
		raw_context = self.soup.find('div', class_='story_details')

		for html_tag in raw_context:
			if html_tag.name == 'p' and 'read more' not in html_tag.text[
			                                               :10].lower() and 'also read' not in html_tag.text[
			                                                                                   :10].lower():
				self.context += '\n' + html_tag.text

			if html_tag.name == 'div':
				if ' '.join(html_tag.get('class')) == 'ev-meter-content ie-premium-content-block':
					break

		for html_tag in raw_context.find('div', class_='ev-meter-content ie-premium-content-block'):

			if html_tag.name == 'p' and 'read more' not in html_tag.text[
			                                               :10].lower() and 'also read' not in html_tag.text[
			                                                                                   :10].lower():
				self.context += '\n' + html_tag.text

			if html_tag.name == 'div':
				if html_tag.get('id') == 'id_newsletter_subscription':
					break

	def fetch_alldata(self):
		self.scrape_headline()
		self.scrape_description()
		self.scrape_writer()
		self.scrape_datetime()
		self.scrape_img()
		self.scrape_context()


class IndianExpress:
	def __init__(self, url, headers):
		self.respone = get(url, headers=headers)
		self.headers = headers
		self.soup = BeautifulSoup(self.respone.content, 'html.parser')

		self.entertainments = list()
		self.sports = list()
		self.politics = list()
		self.businesses = list()
		self.techs = list()
		self.educations = list()
		self.researches = list()

	def __entertainment(self):
		entertainment_articles_urls = []
		for tags in self.soup.find('div', class_='nation'):
			if tags.name == 'div' and tags['class'][0] == 'articles':
				entertainment_articles_urls.append(tags.a['href'])

		for url in entertainment_articles_urls:
			self.entertainments.append(scraper(url, headers=self.headers))

	def __sport(self):
		sport_articles_urls = []
		for tags in self.soup.find('div', class_='nation'):
			if tags.name == 'div' and tags['class'][0] == 'articles':
				sport_articles_urls.append(tags.a['href'])

		for url in sport_articles_urls:
			self.sports.append(scraper(url, headers=self.headers))

	def __politics(self):
		politics_articles_urls = []
		for tags in self.soup.find('div', class_='nation'):
			if tags.name == 'div' and tags['class'][0] == 'articles':
				politics_articles_urls.append(tags.a['href'])

		for url in politics_articles_urls:
			self.politics.append(scraper(url, headers=self.headers))

	def __business(self):
		business_articles_urls = []
		for tags in self.soup.find('div', class_='nation'):
			if tags.name == 'div' and tags['class'][0] == 'articles':
				business_articles_urls.append(tags.a['href'])

		for url in business_articles_urls:
			self.businesses.append(scraper(url, headers=self.headers))

	def __tech(self):
		tech_articles_urls = []
		for tags in self.soup.find('div', class_='nation'):
			if tags.name == 'div' and tags['class'][0] == 'articles':
				tech_articles_urls.append(tags.a['href'])

		for url in tech_articles_urls:
			self.techs.append(scraper(url, headers=self.headers))

	def __education(self):
		education_articles_urls = []
		for tags in self.soup.find('div', class_='nation'):
			if tags.name == 'div' and tags['class'][0] == 'articles':
				education_articles_urls.append(tags.a['href'])

		for url in education_articles_urls:
			self.educations.append(scraper(url, headers=self.headers))

	def __research(self):
		entertainment_articles_urls = []
		for tags in self.soup.find('div', class_='nation'):
			if tags.name == 'div' and tags['class'][0] == 'articles':
				entertainment_articles_urls.append(tags.a['href'])

		for url in entertainment_articles_urls:
			self.researches.append(scraper(url, headers=self.headers))

	def fetch_alldata(self):
		self.__entertainment()
		self.__sport()
		self.__politics()
		self.__business()
		self.__tech()
		self.__education()
		self.__research()


obj = IndianExpress('https://indianexpress.com/section/entertainment/', headers)
print(obj)


headers = {
	'User-Agent': "Mozilla/6.0 (Windows NT 11.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246"}

