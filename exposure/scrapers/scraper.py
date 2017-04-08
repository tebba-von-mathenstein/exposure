import requests


class Scraper(object):
    '''
    This base class sets the interface design for the article text extraction
    web scrappers. Each scrapper extends this class to provide the specific text
    extraction mechanism by implementing _extract_article_body_text
    '''

    @classmethod
    def fetch_and_extract_article_body(cls, url):
        '''
            Provided with a url to a news article on www.reuters.com extract and return the
            article's text body
        '''
        page_html = cls._fetch_page_html(url)
        article_text = cls._extract_article_body_text(page_html)
        return article_text

    @classmethod
    def _fetch_page_html(cls, url):
        '''
            Get all of the HTML for the page hosted at URL. Return that HTML as a string.
        '''
        r = requests.get(url)
        page_html = r.content
        return page_html

    @classmethod
    def _extract_article_body_text(cls, site_html):
        '''
            Given the HTML for an article on this adapters main host, extract just the
            article text and return that text as a string.
        '''
        raise NotImplementedError("Cannot call Scrapper Base Class _extract_article_body_text")
