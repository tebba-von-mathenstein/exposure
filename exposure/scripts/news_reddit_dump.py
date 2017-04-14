from pymongo import MongoClient
from exposure.scripts.utility_belt import fetch_news_api_sources, poll_news_api, find_reddit_shares

# TODO: this is going to get out of hand... we need to think of a better strategy for importing all these...
from exposure.scrapers.aljazeera import AljazeeraScraper
from exposure.scrapers.nytimes import NYTimesScraper
from exposure.scrapers.reuters import ReutersScraper
from exposure.scrapers.time import TimeMagazineScraper
from exposure.scrapers.bbc import BBCScraper
from exposure.scrapers.breitbart import BreitbartScraper

from exposure.models.article import article_from_mongo


def fetch_and_save():
    '''
    First, ask NewsAPI for all of it's current sources, then for each source
    ask NewsAPI for the most recent news from that source. Once we have the
    individual articles query reddit for the subreddits on which the article
    has been shared. Finally, persist ALL the article information into mongodb
    '''
    client = MongoClient()
    mongo_db = client['exposure']
    mongo_collection = mongo_db['articles']

    all_articles = []

    sources = fetch_news_api_sources()
    for source in sources:
        print "fetching articles for source: {}".format(source)
        all_articles += poll_news_api(source, 'top')

    storage_articles = [a.to_mongo() for a in all_articles]
    mongo_collection.insert_many(storage_articles)
    client.close()


def add_reddit_shares():
    client = MongoClient()
    mongo_db = client['exposure']
    mongo_collection = mongo_db['articles']
    articles = mongo_collection.find()

    for a_dict in articles:
        a = article_from_mongo(a_dict)
        print u"Fetching reddit shares for article: {}".format(a.url)
        shares = find_reddit_shares(a)
        print "  Shares were: {}".format(shares)

        for s in shares:
            a.add_share(s)

        mongo_collection.replace_one({'_id': a_dict['_id']}, a.to_mongo())

    client.close()


def add_full_text():
    client = MongoClient()
    mongo_db = client['exposure']
    mongo_collection = mongo_db['articles']

    scrapper_map = {
        r'.*aljazeera.com/.*': AljazeeraScraper,
        r'.*nytimes.com/.*': NYTimesScraper,
        r'.*reuters.com/.*': ReutersScraper,
        r'.*time.com/.*': TimeMagazineScraper,
        r'.*bbc.co.*': BBCScraper,
        r'.*breitbart.com.*': BreitbartScraper
    }

    for regex, scrapper in scrapper_map.iteritems():
        articles = mongo_collection.find({'url': {'$regex': regex}})
        for a in articles:
            if not a.get('full_text'):
                print u"Fetching full text for {}".format(a['url'])
                try:
                    text = scrapper.fetch_and_extract_article_body(a['url'])
                    mongo_collection.update_one({'_id': a['_id']}, {
                        '$set': {
                            'full_text': text
                        }
                    })
                except Exception as e:
                    print 'Warning, failure for document {}: {}'.format(a['url'], e)
    client.close()


if __name__ == "__main__":
    # fetch_and_save()
    # add_reddit_shares()
    add_full_text()
