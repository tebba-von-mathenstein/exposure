class ArticleShare:
    """A instance of an article being shared on a Social Media site"""

    def __init__(self, article, share_url, share_rating):
            self.article = article
            self.share_url = share_url
            self.share_rating = share_rating

    def __str__(self):
        return "{0} : {1}".format(self.share_url, self.share_rating)
