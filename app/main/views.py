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
    latest_news = get_Source_news('category')
    print(latest_news)
    headlines = get_headlines
    print(headlines)
    
    title = 'Home - Welcome to The best News Article Website Online'

    return render_template('index.html',title = title,latest=latest_news, headlines = get_headlines)


@main.route('/news/<id>')
def article(id):
    articles = get_article(id)
    print(articles)
    return render_template('articles.html' , article = article)



