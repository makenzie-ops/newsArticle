import urllib.request,json
from .models import Article, Category, Source , Headlines


# Getting api key
api_key = '2d7e55cf5e324b4c98a4a1ee81d40ffd'
base_url= None

article_url = None

def configure_request(app):
    global api_key,base_url,article_url

    api_key = '2d7e55cf5e324b4c98a4a1ee81d40ffd' 
    
    base_url =app.config['SOURCES_API_BASE_URL']


def get_Source_news():
    '''
    Function that gets the json response to url request
    '''
    get_source_url= 'https://newsapi.org/v2/sources?apiKey={}'.format( api_key)
    # print(get_source_url)
    with urllib.request.urlopen(get_source_url) as url:
        get_sources_data = url.read()
        get_sources_response = json.loads(get_sources_data)


        if get_sources_response['sources']:
            source_results_list = get_sources_response['sources']
            source_res = process_results(source_results_list)

    return source_res

def process_results(source_list):
    '''
    function to process results and transform them to a list of objects
    Args:
        source_list:dictionary cotaining source details
    Returns:
        source_results: A list of source objects
    '''
    source_results = []
    for source_item in source_list:
        id = source_item.get('id')
        name = source_item.get('name')
        description = source_item.get('description')
        url = source_item.get('url')
        if id:
            source_object = Source(id,name,description,url)
            source_results.append(source_object)

    return source_results

def get_article(id):
    get_article_url =  'https://newsapi.org/v2/everything?q={}&apiKey={}'.format(id,api_key)
    #print(get_article_url)
    with urllib.request.urlopen(get_article_url) as url:
        get_article_data = url.read()
        get_article_response = json.loads(get_article_data)

        get_article_results = None

        if get_article_response['articles']:
            get_article_list = get_article_response['articles']
            get_article_results = process_articles_results( get_article_list)


    return   get_article_results

def process_articles_results(news):
    '''
    function that processes the json files of articles from the api key
    '''
    article_source_results = []
    for article in news:
        author = article.get('author')
        description = article.get('description')
        time = article.get('publishedAt')
        url = article.get('urlToImage')
        image = article.get('url')
        title = article.get ('title')

        if title:
            article_objects = Article(author,description,time,image,url,title)
            article_source_results.append(article_objects)

    return article_source_results

def get_category(article):
    '''
    function that gets the response to the category json
    '''
    get_category_url =  'https://newsapi.org/v2/everything?q={}&apiKey={}'.format(article, api_key)
    #print(get_category_url)
    with urllib.request.urlopen(get_category_url) as url:
        get_category_data = url.read()
        get_cartegory_response = json.loads(get_category_data)

        get_cartegory_results = None

        if get_cartegory_response['articles']:
            get_cartegory_list = get_cartegory_response['articles']
            get_cartegory_results = process_articles_results(get_cartegory_list)

    return get_cartegory_results

def get_headlines():
    '''
    function that gets the response to the category json
    '''
    get_headlines_url = 'https://newsapi.org/v2/top-headlines?country=us&apiKey={}'.format(api_key)
    #print(get_headlines_url)
    with urllib.request.urlopen(get_headlines_url) as url:
        get_headlines_data = url.read()
        get_headlines_response = json.loads(get_headlines_data)

        if get_headlines_response['articles']:
            get_headlines_list = get_headlines_response['articles']
            get_headlines_results = process_articles_results(get_headlines_list)

    return get_headlines_results