'''
An example of how to fetch and print all the recent techcruch articles from NewsAPI
'''
from exposure.config import NEWS_API_KEY
from exposure.models.article import Article
import requests

# techcruch is one of many sources
url = "https://newsapi.org/v1/articles?source=techcrunch&apiKey=" + NEWS_API_KEY
data = requests.get(url, headers = {'User-agent': 'Exposure Bot 0.0.1'}).json()

for post in data['articles']:
    # Map to unicode
    for k, v in post.iteritems():
        post[k] = post[k].encode('utf-8')

    # news-api doesn't give full text
    a = Article(post['author'], post['title'], post['url'], post['description'], post['publishedAt'], None)
    print a
