from database.curd import crudArticle, Article
from datetime import datetime, timedelta

crud = crudArticle()

# temp = crud.session.query(Article).filter(Article.datetime>=datetime.now() - timedelta(hours=12)).order_by(Article.datetime.desc()).all()

# print(temp)

# for i in temp[:5]:
# 	print(i.datetime)

# print(datetime.now() - timedelta(hours=12))
# print(timedelta(hours=12))
# print()