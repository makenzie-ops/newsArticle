import os
class Config:
 
    NEWS_HEADLINES_API_BASE_URL ='http://newsapi.org/v2/top-headlines?country=us&apiKey=96d005f7fdeb42cc8632c9537f783ef9'
    NEWS_API_KEY = os.environ.get('NEWS_API_KEY')

class ProdConfig(Config):
    pass


class DevConfig(Config):
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}