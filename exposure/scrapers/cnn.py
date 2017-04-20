from bs4 import BeautifulSoup
from exposure.scrapers.scraper import Scraper


class CNNScraper(Scraper):
    '''
    Implements the _extract_article_body_text for content on CNN.com
    '''
    @classmethod
    def _extract_article_body_text(cls, site_html):
        '''
            Given the HTML for an article on this adapters main host, extract just the
            article text and return that text as a string.
        '''
        soup = BeautifulSoup(site_html, 'html.parser')
        individual_p_tags = soup.select('.zn-body__paragraph')  # CNN seems to give all the p's this class
        texts = [tag.text for tag in individual_p_tags]
        a_text = '\n'.join(texts)
        return a_text
