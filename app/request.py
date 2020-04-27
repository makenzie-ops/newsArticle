import urllib.request,json
from .models import Article,Source


# Getting api key
api_key = None
# Getting the movie base url
base_url = None

def configure_request(app):
    global api_key,base_url
    api_key = app.config['MOVIE_API_KEY']
    base_url = app.config['MOVIE_API_BASE_URL']

def get_Source_news(category):
    '''
    Function that gets the json response to our url request
    '''
    get_news_url = base_url.format(category,api_key)

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
        Function  that processes the news result and transform them to a list of Objects

    Args:
        news_list: A list of dictionaries that contain news details

    Returns :
        news_results: A list of news objects
    '''
    
    news_results = []
    for news_item in news_list:
        id = news_item.get('id')
        title = news_item.get('original_title')
        description = news_item.get('description')
        published_at = news_item.get('published_at')
        content= news_item.get('content')

        if description:
            news_object = Article(id,title,description,published_at,content)
            news_results.append(news_object)

    return news_results

def get_news(id):
    get_news_details_url = base_url.format(id,api_key)

    with urllib.request.urlopen(get_news_details_url) as url:
        news_details_data = url.read()
        news_details_response = json.loads(news_details_data)

        news_object = None
        if news_details_response:
            id = news_details_response.get('id')
            title = news_details_response.get('original_title')
            description= news_details_response.get(' description')
            poster = news_details_response.get('poster_path')
            published_at= news_details_response.get('published_at')
            content= news_details_response.get('content')

            news_object = Article(id,title,description,poster,published_at,content)

    return news_object