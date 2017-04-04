from exposure.config import NEWS_API_KEY
from exposure.models.article import Article
from exposure.models.article_share import ArticleShare

import requests


def fetch_news_api_sources():
    '''
        Using NewsAPI fetch their current source list from the provided endpoint.
        return a list of strings with the names of the news sources.
    '''
    url = "https://newsapi.org/v1/sources?apiKey={0}".format(NEWS_API_KEY)
    data = requests.get(url, headers={'User-agent': 'Exposure Bot 0.0.1'}).json()
    sources = [source['id'] for source in data['sources']]

    return sources


def poll_news_api(source, sort_by):
    '''
        Given a valid NewsAPI news source (source) and a valid NewsAPI sort_by parameter, fetch
        the first n news articles sorted by that parameter (where n is whatever the current default
        number of returned values for NewsAPI is).

        return a list of exposure.model.Articles
    '''
    articles = []
    url = "https://newsapi.org/v1/articles?source={0}&sortBy={1}&apiKey={2}".format(source, sort_by, NEWS_API_KEY)
    data = requests.get(url, headers={'User-agent': 'Exposure Bot 0.0.1'}).json()

    raw_article_data = data.get('articles')
    if not raw_article_data:
        return articles

    for article_dict in raw_article_data:
        # Map to unicode
        for k, v in article_dict.iteritems():
            if v is None:
                article_dict[k] = None
            else:
                article_dict[k] = v.encode('utf-8')

        # news-api doesn't give full text
        article = Article(
            article_dict['author'],
            article_dict['title'],
            article_dict['url'],
            article_dict['description'],
            article_dict['publishedAt'],
            None
        )
        articles.append(article)

    return articles


def find_reddit_shares(article):
    '''
    Given an exposure.models.Article query reddit for it's 'source' field, which is a URL. Create
    ArticleShare objects for each instance of a share of this article on a subreddit return a list
    of these ArticleShares.
    '''
    article_shares = []

    url = "http://www.reddit.com/search.json?q={0}".format(article.source)
    search_data = requests.get(url, headers={'User-agent': 'Exposure Bot 0.0.1'}).json()

    if not isinstance(search_data, dict):
        return article_shares

    for post in search_data['data']['children']:
        p = post['data']
        permalink = p['permalink'].encode('utf-8')

        share_url = "http://www.reddit.com{0}".format(permalink)
        share_score = p['score']

        share = ArticleShare(share_url, share_score)
        article_shares.append(share)

    return article_shares
