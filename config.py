class Config:
    '''
    General configuration parent class
    '''
    NEWS_HEADLINES_API_BASE_URL ='http://newsapi.org/v2/top-headlines?country=us&apiKey=96d005f7fdeb42cc8632c9537f783ef9'


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