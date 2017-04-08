from bs4 import BeautifulSoup
from exposure.scrapers.scraper import Scraper


class NYTimesScraper(Scraper):
    '''
    Implements the _extract_article_body_text for content on nytimes.com
    '''
    @classmethod
    def _extract_article_body_text(cls, site_html):
        '''
            Given the HTML for an article on this adapters main host, extract just the
            article text and return that text as a string.
        '''
        soup = BeautifulSoup(site_html, 'html.parser')
        individual_p_tags = soup.select('.story-body-text')  # NYTimes seems to give all the p's this class
        texts = [tag.text for tag in individual_p_tags]
        a_text = ' '.join(texts)
        return a_text
