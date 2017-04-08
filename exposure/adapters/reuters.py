from bs4 import BeautifulSoup
from exposure.scrapers.scraper import Scraper


class ReutersScraper(Scraper):
    '''
    Implements the _extract_article_body_text for content on Reuters.com
    '''
    @classmethod
    def _extract_article_body_text(cls, site_html):
        '''
            Given the HTML for an article on this adapters main host, extract just the
            article text and return that text as a string.
        '''
        soup = BeautifulSoup(site_html, 'html.parser')
        main_body = soup.select('#article-text')[0]  # Reuters wraps the main body in this tag
        a_text = main_body.text
        return a_text
