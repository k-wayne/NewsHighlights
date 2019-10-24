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


def get_sources(category):
    '''
    Function that gets the json response to our url request
    '''
    get_sources_url = base_url.format(category, api_key)

    with urllib.request.urlopen(get_sources_url) as url:
        get_sources_data = url.read()
        get_sources_response = json.loads(get_sources_data)

        source_results = None

        if get_sources_response['sources']:
            source_results_list = get_sources_response['sources']
            source_results = process_results(source_results_list)

    return source_results


def process_results(source_list):
    '''
    Function that processes the source result and transforms them to a list of objects
    
    Args:
        source_list: A list of dictionaries that contain source details

    Returns:
        source_results: A lost of source objects
    '''

    source_results = []
    for source_item in source_list:
        id = source_item.get("id")
        name = source_item.get("name")
        description = source_item.get("description")
        url = source_item.get("url")
        category = source_item.get("category")
        language = source_item.get("language")
        country = source_item.get("country")

        source_object = Source(id, name, description, url,
                               category, language, country)
        source_results.append(source_object)

    return source_results
