import os
class Config:
 
    NEWS_API_BASE_URL = 'http://newsapi.org/v2/everything?q=Apple&from=2020-04-28&sortBy=popularity&apiKey=2d7e55cf5e324b4c98a4a1ee81d40ffd'
    ARTICLE_BASE_URL = 'https://newsapi.org/v2/top-headlines?country=us&apiKey=2d7e55cf5e324b4c98a4a1ee81d40ffd'
    NEWS_API_KEY = os.environ.get('NEWS_API_KEY')

class ProdConfig(Config):
    pass


class DevConfig(Config):
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}