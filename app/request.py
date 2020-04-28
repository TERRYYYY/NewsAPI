import urllib.request,json
from .models import News
from .models import Article

# News = news.News
# Article = article.Article

#Getting api key
api_key = None

#Getting news base url
base_url =None
article_url = None

def configure_request(app):
    global api_key,base_url,article_url
    api_key = app.config['NEWS_API_KEY']
    base_url =app.config['NEWS_API_BASE_URL']
    article_url = app.config['ARTICLE_BASE_URL']
def get_news(category):

    '''
    Function that gets json response to our url request
    '''

    get_news_url = base_url.format(category,api_key)
    # https://newsapi.org/v2/{}?q={}&apiKey={}
    # https://newsapi.org/v2/everything?q={}&apiKey=12d688c8a85c4864ba3c8dac4ee62038
    # 'https://newsapi.org/v2/everything?q={}&apiKey={}'
    # 'https://api.themoviedb.org/3/movie/{}?api_key={}'
    print(get_news_url)

    with urllib.request.urlopen(get_news_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)

        news_results = None

        if get_news_response['sources']:
            news_results_list = get_news_response['sources']
            news_results = process_results(news_results_list)

        return news_results

def process_results(news_list):
    '''
    Function that processes the news result and transform them to a list of object
    '''
    news_results = []
    for news_item in news_list:
        id = news_item.get('id')
        name = news_item.get('name')
        description = news_item.get('description')
        url = news_item.get('url')
        category = news_item.get('category')
        language = news_item.get('language')
        country = news_item.get('country')
        
        news_object = News(id,name,description,url,category,language,country)
        news_results.append(news_object)

    return news_results

def get_article(source):


    get_article_url=article_url.format(source,api_key)
    print (get_article_url)


    # get_article_url=article_url.format(id,api_key)
    # print(get_article_url)

    with urllib.request.urlopen(get_article_url) as url:

        get_article_data=url.read()
        get_article_response= json.loads(get_article_data)

    article_results=None
    if get_article_response['articles']:
      article_results_list = get_article_response['articles']
      article_results = process_articles(article_results_list)
    return article_results

def process_articles(article_list):
  
    article_results = []
    for article_item in article_list:
        id=article_item.get('id')
        name=article_item.get('name')
        author=article_item.get('author')
        description=article_item.get('description')
        title= article_item.get('title')
        url=article_item.get('url')
        urlToImage=article_item.get('urlToImage')
        publishedAt= article_item.get('publishedAt')
        content = article_item.get('content')
        
        article_object = Article(id,name,author,title,description,url,urlToImage,publishedAt,content)
        article_results.append(article_object)
    return article_results


# def get_article(id):
#     get_article_details_url = article_url.format(id,api_key)

#     with urllib.request.urlopen(get_article_url) as url:
#         article_details_data = url.read()
#         article_details_response = json.loads(article_details_data)

#         article_details = None
#         if article_details_response:
#             id = mynews_details_response.get('id')
#             name = mynews_details_response.get('name')
#             description = mynews_details_response.get('description')
#             publishedAt = mynews_details_response.get('publishedAt')
#             author = mynews_details_response.get('author')
#             urlToImage = mynews_details_response.get('urlToImage')
#             url = mynews_details_response.get('url')
       

#             mynews_object = News(id,name,description,publishedAt,author,urlToImage,url)
    

#         return mynews_object