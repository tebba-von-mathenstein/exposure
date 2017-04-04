from bs4 import BeautifulSoup
import requests


def fetch_and_extract_article_body(url):
    page_html = fetch_page_html(url)
    article_text = extract_article_body_text(page_html)
    return article_text


def fetch_page_html(url):
    r = requests.get(url)
    page_html = r.content
    return page_html


def extract_article_body_text(site_html):
    soup = BeautifulSoup(site_html, 'html.parser')
    article_html = soup.select('.article-body')  # Id some places, class some places...
    a_text = article_html[0].text
    a_text = a_text.split()
    a_text = ' '.join(a_text)
    return a_text
