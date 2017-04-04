from bs4 import BeautifulSoup
import requests


def fetch_and_extract_article_body(url):
    '''
        Provided with a url to a news article on www.aljazeera.com extract and return the
        article's text body
    '''
    page_html = _fetch_page_html(url)
    article_text = _extract_article_body_text(page_html)
    return article_text


def _fetch_page_html(url):
    '''
        Get all of the HTML for the page hosted at URL. Return that HTML as a string.
    '''
    r = requests.get(url)
    page_html = r.content
    return page_html


def _extract_article_body_text(site_html):
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
