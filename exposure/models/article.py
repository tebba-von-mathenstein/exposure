from exposure.models.article_share import ArticleShare

class Article(object):
    """Articles are a single source of news information"""

    def __init__(self, author, title, source, url, description, publish_date, full_text):
        self.author = author
        self.title = title
        self.source = source
        self.url = url
        self.description = description
        self.publish_date = publish_date
        self.full_text = full_text

        self.shares = []

    def avg_share_score(self):
        '''
            Compute and return the average of the scores for social media shares.
        '''
        if not self.shares:
            return 0

        rating_sum = sum(share.share_rating for share in self.shares)
        return rating_sum / len(self.shares)

    def add_share(self, article_share):
        self.shares.append(article_share)


    def to_mongo(self):
        '''
            Serialize the article to a dictionary format that plays nicely with MongoDB
        '''
        d = self.__dict__
        mongo_shares = [share.to_mongo() for share in self.shares]
        d['shares'] = mongo_shares

        return d


def article_from_mongo(mongo_dict):
    a = Article(
        mongo_dict['author'],
        mongo_dict['title'],
        mongo_dict['source'],
        mongo_dict['url'],
        mongo_dict['description'],
        mongo_dict['publish_date'],
        mongo_dict['full_text']
    )

    if mongo_dict.get('shares'):
        for s in mongo_dict.get('shares'):
            a.add_share(ArticleShare(s['share_url'], s['share_rating']))

    return a
