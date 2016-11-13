from models.article import Article

import sys
import webhose
from config import WEBHOSE_API_KEY

webhose.config(token=WEBHOSE_API_KEY)

query = "The White House"
r = webhose.search(query)

for post in r.posts:
    if post.language == 'english':
        author = post.author.encode('utf-8')
        title = post.title.encode('utf-8')
        publish_date = post.thread.published.encode('utf-8')
        text = post.text.encode('utf-8')
        site = post.thread.url.encode('utf-8')

        a = Article(author, title, site, None, publish_date, text)

        print a
