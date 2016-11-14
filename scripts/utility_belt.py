from config import NEWS_API_KEY
from models.article import Article
from models.article_share import ArticleShare

import requests

def poll_news_api(source, sort_by):
    articles = []
    url = "https://newsapi.org/v1/articles?source={0}&sortBy&apiKey={2}".format(source, sort_by, NEWS_API_KEY)
    data = requests.get(url, headers = {'User-agent': 'Exposure Bot 0.0.1'}).json()

    for post in data['articles']:
        # Map to unicode
        for k, v in post.iteritems():
            post[k] = post[k].encode('utf-8')

        # news-api doesn't give full text
        a = Article(post['author'], post['title'], post['url'], post['description'], post['publishedAt'], None)
        articles.append(a)

    return articles

def find_reddit_shares(article):
    article_shares = []

    url = "http://www.reddit.com/search.json?q={0}".format(article.source)
    search_data = requests.get(url, headers = {'User-agent': 'Exposure Bot 0.0.1'}).json()

    if not isinstance(search_data, dict):
        return article_shares

    for post in search_data['data']['children']:
        p = post['data']

        share_url = "http://www.reddit.com{0}".format(p['permalink'])
        share_score = p['score']

        share = ArticleShare(None, share_url, share_score)
        article_shares.append(share)

    return article_shares
