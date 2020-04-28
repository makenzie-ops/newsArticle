from flask import render_template,request,redirect,url_for
from . import main
from ..request import get_Source_news,get_article ,get_category,get_headlines
from ..models import Source


# Views
@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    # Getting latest news
    latest_news = get_Source_news()
    print(latest_news)
    headlines = get_headlines
    print(headlines)
    
    title = 'Welcome to The best News Article Website Online'

    return render_template('index.html',title = title,latest=latest_news, headlines = get_headlines)


@main.route('/news/<id>')
def article(id):
    articles = get_article(id)
    print(articles)
    return render_template('articles.html' , article = article)


@main.route('/categories/<cat_name>')
def category(cat_name):
    '''
    function to return the categories.html page and its content
    '''
    category = get_category(cat_name)
    title = f'{cat_name}'
    cat = cat_name
    print(cat)

    return render_template('categories.html',title = title,category = category, cat= cat_name)



