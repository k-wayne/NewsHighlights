import urllib.request
import json
from .models import Source, Article

# Getting api key
api_key = None
# Getting the news base url
base_url = None

article_url = None


def configure_request(app):
    global api_key, base_url, article_url
    api_key = app.config['NEWS_API_KEY']
    base_url = app.config['NEWS_API_BASE_URL']
    article_url = app.config['NEWS_ARTICLE_URL']
