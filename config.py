import os


class Config:
    '''
    General configuration parent class
    '''

    NEWS_API_BASE_URL = 'https://newsapi.org/v2/sources?language=en&category={}&apiKey={}'
    NEWS_ARTICLE_URL = 'https://newsapi.org/v2/everything?language=en&sources={}&apiKey={}'
    NEWS_API_KEY = os.environ.get('NEWS_API_KEY')
