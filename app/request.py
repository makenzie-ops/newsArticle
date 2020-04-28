# from app import app
import urllib.request,json
from .models import Article
from .models import Source

# Getting api key
api_key = '2d7e55cf5e324b4c98a4a1ee81d40ffd'
# Getting the movie base url
base_url = None
article_url = None

def configure_request(app):
    global api_key,base_url,article_url
    api_key = app.config['NEWS_API_KEY']
    base_url =app.config['NEWS_API_BASE_URL']
    article_url = app.config['ARTICLE_BASE_URL']

def get_Source_news(category):
    get_Source_news = base_url.format(category, api_key)
    print(get_Source_news)
    with urllib.request.urlopen(get_Source_news) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)

        news_results =None

        if get_news_response.get('results'):
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
        title = news_item.get('title')
        description = news_item('description')
        publishedAt = news_item('publishedAt')
        author = news_item('author')
        urlToImage = news_item('urlToImage')
        url = news_item('url')

        if urlToImage:
            news_object = Source(id,title,description,publishedAt,author,urlToImage,url)
            news_results.append(news_object)

        return news_results

def get_article(id):


    get_article_url= article_url.format(id,api_key)


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

        author=article_item.get('author')
        title= article_item.get('title')
        publishedAt= article_item.get('publishedAt')
        content = article_item.get('content')
        url=article_item.get('url')

        if title:
            article_object = Article(author,title,publishedAt,content,url)
            article_results.append(article_object)
        return article_results

def get_category(categ_head):
    '''
    function that gets the response to the category json
    '''
    get_category_url = article_url.format(categ_head,api_key)
    print(get_category_url)
    with urllib.request.urlopen(get_category_url) as url:
        get_category_data = url.read()
        get_cartegory_response = json.loads(get_category_data)

        get_cartegory_results = None

        if get_cartegory_response['articles']:
            get_cartegory_list = get_cartegory_response['articles']
            get_cartegory_results =article_resultss(get_cartegory_list)

    return get_cartegory_results

def get_headlines():
    '''
    function that gets the response to the category json
    '''
    get_headlines_url = 'https://newsapi.org/v2/top-headlines?country=us&apiKey={}'.format(api_key)
    print(get_headlines_url)
    with urllib.request.urlopen(get_headlines_url) as url:
        get_headlines_data = url.read()
        get_headlines_response = json.loads(get_headlines_data)

        get_headlines_results = None

        if get_headlines_response['articles']:
            get_headlines_list = get_headlines_response['articles']
            get_headlines_results = article_results(get_headlines_list)

    return get_headlines_results