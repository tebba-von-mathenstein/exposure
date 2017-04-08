from bs4 import BeautifulSoup
from exposure.scrapers.scraper import Scraper


class AljazeeraScraper(Scraper):
    '''
    Implements the _extract_article_body_text for content on aljazeera.com
    '''
    @classmethod
    def _extract_article_body_text(cls, site_html):
        '''
            Given the HTML for an article on this adapters main host, extract just the
            article text and return that text as a string.
        '''
        soup = BeautifulSoup(site_html, 'html.parser')
        article_html = soup.select('.article-body')  # Id some places, class some places...
        a_text = article_html[0].text
        a_text = a_text.split()
        a_text = ' '.join(a_text)
        return a_text
