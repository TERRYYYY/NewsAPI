from app import app
import urllib.request,json
from .models import news 
from .config import Config

News = news.News

#Getting api key
api_key = app.config ['NEWS_API_KEY']

#Getting news base url
base_url =app.config["NEWS_API_BASE_URL"]


def get_news(category):

    '''
    Function that gets json response to our url request
    '''
    get_news_url = 'http://newsapi.org/v2/everything?q={}&apiKey={}'.format(category,api_key)
    # https://newsapi.org/v2/everything?q={}&apiKey=12d688c8a85c4864ba3c8dac4ee62038
    # 'https://newsapi.org/v2/everything?q={}&apiKey={}'
    # 'https://api.themoviedb.org/3/movie/{}?api_key={}'

    with urllib.request.urlopen(get_news_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)

        news_results = None

        if get_news_response['results']:
            news_results_list = get_news_response['results']
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
        description = news_item('description')
        publishedAt = news_item('publishedAt')
        author = news_item('author')
        urlToImage = news_item('urlToImage')
        url = news_item('url')

        if urlToImage:
            news_object = News(id,name,description,publishedAt,author,urlToImage,url)
            news_results.append(news_object)

        return news_results

def get_mynews(id):
    get_mynews_details_url = base_url.format(id,api_key)

    with urllib.request.urlopen(get_mynews_url) as url:
        mynews_details_data = url.read()
        mynews_details_response = json.loads(mynews_details_data)

        mynews_details = None
        if mynews_details_response:
            id = mynews_details_response.get('id')
            name = mynews_details_response.get('name')
            description = mynews_details_response.get('description')
            publishedAt = mynews_details_response.get('publishedAt')
            author = mynews_details_response.get('author')
            urlToImage = mynews_details_response.get('urlToImage')
            url = mynews_details_response.get('url')
       

            mynews_object = News(id,name,description,publishedAt,author,urlToImage,url)
    

        return mynews_object