class ArticalAPI:
	def __init__(self):
		self.curd_obj = curd()
		# self.summ_model = MODEL()

	def summarize(self, data):
		if not self.verify_token_id(token_id=data.token_id):
			return self.response_with(
				operation=False,
				message='Token id not found.'
			)

		return self.response_with(
			operation=True,
			summary=self.generate_summary(article_id=data.article_id)
		)

	def get_articles(self, data):
		if not self.verify_token_id(token_id=data.token_id):
			return self.response_with(
				operation=False,
				message='Token id not found.'
			)

		articles = self.curd_obj.get_articles_inrange(range=(data.count, data.count+8))

		return JSONResponse({'data': [{'article_id': article.id,
		                               'headline': article.headline,
		                               'img_src': article.img_url,
		                               'site': article.site_name,
		                               'context': article.context, } for article in articles]})

	def verify_token_id(self, token_id: str):
		user_session = self.curd_obj.get_session_by_token(token_id=token_id)
		if user_session:
			return user_session
		else:
			return False

	def response_with(self, article_id: int = None, headline: str = None, img_src: str = None, context: str = None,
	                  site: str = None, message: str = None, operation: bool = None, summary: str = None,
	                  url: str = None):
		return JSONResponse({
			'article_id': article_id,
			'headline': headline,
			'site': site,
			'img_src': img_src,
			'context': context,
			'url': url,
			'message': message,
			'operation': operation,
			'summary': summary,
		})

	def generate_summary(self, article_id: int):
		article = self.curd_obj.get_articles(article_id=article_id)
		return article.context[:500]
		# return self.summ_model.get_summary(article.context)