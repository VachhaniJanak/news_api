from bs4 import BeautifulSoup
from requests import get

urls = {
	'parent': 'https://indianexpress.com/',
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

	def __scrape_headline(self):
		self.headline = self.soup.find('h1').text

	def __scrape_description(self):
		self.description = self.soup.find('h2', class_='synopsis').text

	def __scrape_writer(self):
		self.writer = self.soup.find('div', class_="editor-details-new-change").find('a').text

	def __scrape_datetime(self):
		self.datetime = self.soup.find('div', class_="editor-details-new-change").find('span')['content']

	def __scrape_img(self):
		self.img_url = self.soup.find('span', class_='custom-caption').img['src']

	def __scrape_context(self):
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
		self.__scrape_headline()
		self.__scrape_description()
		self.__scrape_writer()
		self.__scrape_datetime()
		self.__scrape_img()
		self.__scrape_context()


class IndianExpress:
	def __init__(self):

		self.entertainments = list()
		self.sports = list()
		self.politics = list()
		self.businesses = list()
		self.techs = list()
		self.educations = list()
		self.researches = list()

		self.fetch_alldata()

	def __trending(self):
		pass

	def __get_header(self):
		return None

	def __response(self, url, headers):
		respone = get(url, headers=headers)
		return BeautifulSoup(respone.content, 'html.parser')

	def __entertainment(self):
		entertainment_articles_urls = []
		soup = self.__response(urls['entertainment'], self.__get_header())

		for tags in soup.find('div', class_='nation'):
			if tags.name == 'div' and tags['class'][0] == 'articles':
				entertainment_articles_urls.append(tags.a['href'])

		for url in entertainment_articles_urls:
			try:
				self.entertainments.append(scraper(url, headers=self.__get_header()))
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
				self.sports.append(scraper(url, headers=self.__get_header()))
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
				self.businesses.append(scraper(url, headers=self.__get_header()))
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
				self.techs.append(scraper(url, headers=self.__get_header()))
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
				self.educations.append(scraper(url, headers=self.__get_header()))
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
				self.researches.append(scraper(url, headers=self.__get_header()))
			except Exception as e:
				print(e)

	def fetch_alldata(self):
		self.__entertainment()
		self.__sport()
		self.__politics()
		self.__business()
		# self.__tech()
		self.__education()
		# self.__research()
