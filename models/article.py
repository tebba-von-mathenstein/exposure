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

    def __str__(self):
        return Article.article_format_str.format(
            author = self.author,
            title = self.title,
            source = self.source,
            description = self.description,
            publish_date = self.publish_date,
            full_text = self.full_text,
        )
