import unnitest
from models import news

Article = article.article

class Article:
  '''
  article class to define article objects
  '''
  def __init__(self,author,title,publishedAt,content,url):
    self.author=author
    self.title=title
    self.publishedAt=publishedAt
    self.content=content
    self.url=url