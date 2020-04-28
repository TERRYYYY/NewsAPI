import os
class Config:
    '''
    General configuration parent class
    '''
    NEWS_API_BASE_URL = 'https://newsapi.org/v2/sources?apiKey=12d688c8a85c4864ba3c8dac4ee62038'
    ARTICLE_BASE_URL = 'https://newsapi.org/v2/top-headlines?sources={}&apiKey=12d688c8a85c4864ba3c8dac4ee62038'
    NEWS_API_KEY = os.environ.get('NEWS_API_KEY')    

class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass


class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}