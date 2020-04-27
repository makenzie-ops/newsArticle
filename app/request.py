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