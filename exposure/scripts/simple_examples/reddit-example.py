'''
An example of querying from reddit to get all the subreddits on which
some other website or URL was shared. In this case the image hosted at: https://i.imgur.com/R7R2jfZ.gifv
'''
import requests
from models.article_share import ArticleShare

url = "http://www.reddit.com/search.json?q=https://i.imgur.com/R7R2jfZ.gifv"
search_data = requests.get(url, headers={'User-agent': 'Exposure Bot 0.0.1'}).json()

for post in search_data['data']['children']:
    p = post['data']

    share_url = "http://www.reddit.com{0}".format(p['permalink'])
    share_score = p['score']

    share = ArticleShare(None, share_url, share_score)
    print share
