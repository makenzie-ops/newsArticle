from flask import render_template
from app import app
from .request import get_Source_news, get_news

# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
      # Getting latest news
    latest_news = get_Source_news('latest')
    print(latest_news)
   
    title = 'Home - Welcome to The best News Article Website Online'

    return render_template('index.html',title = title,latest=latest_news)

@app.route('/news/<int:id>')
def news(id):

    '''
    View movie page function that returns the movie details page and its data
    '''
    news = get_news(id)
    title = f'{news.title}'

    return render_template('news.html',title = title, news =news)