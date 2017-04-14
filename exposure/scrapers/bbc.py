from bs4 import BeautifulSoup
from exposure.scrapers.scraper import Scraper


class BBCScraper(Scraper):
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

        # BBC wraps the main body in a div with this class, but uses p's for the text
        individual_p_tags = soup.select('.story-body p')
        texts = [tag.text for tag in individual_p_tags]
        a_text = '\n'.join(texts)
        return a_text
