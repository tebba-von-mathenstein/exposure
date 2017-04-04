class ArticleShare:
    """A instance of an article being shared on a Social Media site"""

    def __init__(self, share_url, share_rating):
            self.share_url = share_url
            self.share_rating = share_rating

    def to_mongo(self):
        '''
            Serialize the article to a dictionary format that plays nicely with MongoDB
        '''
        return {
            'share_url': self.share_url,
            'share_rating': self.share_rating
        }

    def __str__(self):
        return "{0}:{1}".format(self.share_url, self.share_rating)
