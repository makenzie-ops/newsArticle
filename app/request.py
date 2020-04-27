from app import app
import urllib.request,json
from .models import news

News = news.News


# Getting api key
api_key = app.config['NEWS_API_KEY']


# Getting the news headlines base url
base_url = app.config["NEWS_HEADLINES_API_BASE_URL"]

# Getting the news sources base url
base_url = app.config["NEWS_SOURCES_API_BASE_URL"]

def get_news(category):
    '''
    Function that gets the json response to our url request
    '''
    get_news_url = base_url.format(category,api_key)

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
        Function  that processes the news result and transform them to a list of Objects

    Args:
        news_list: A list of dictionaries that contain movie details

    Returns :
        news_results: A list of movie objects
    '''
    
    news_results = []
    for news_item in news_list:
        id = news_item.get('id')
        title = news_item.get('original_title')
        destcription = news_item.get('description')
        poster = news_item.get('poster_path')
        published_at = news_item.get('published_at')
        content= news_item.get('content')

        if poster:
            news_object = News(id,title,destcription,poster,published_at,content)
            news_results.append(news_object)

    return news_results