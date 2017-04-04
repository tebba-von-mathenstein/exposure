class Article:
    """Articles are a single source of news information"""

    # Hate this formatting for print... just sayin
    article_format_str = """
=====================
Author: {author}
Date: {publish_date}
Source: {source}
Title: {title}
Description: {description}
"""

    def __init__(self, author, title, source, description, publish_date, full_text):
        self.author = author
        self.title = title
        self.source = source
        self.description = description
        self.publish_date = publish_date
        self.full_text = full_text

        self.shares = []

    def __str__(self):
        return Article.article_format_str.format(
            author = self.author,
            title = self.title,
            source = self.source,
            description = self.description,
            publish_date = self.publish_date,
            full_text = self.full_text)

    def avg_share_score(self):
        if not self.shares:
            return 0

        rating_sum = sum(share.share_rating for share in self.shares)
        return rating_sum / len(self.shares)

    def add_share(self, article_share):
        self.shares.append(article_share)

    def to_mongo(self):
        d = self.__dict__
        mongo_shares = [share.to_mongo() for share in self.shares]
        d['shares'] = mongo_shares

        return d
