from pymongo import MongoClient
from exposure.scripts.utility_belt import fetch_news_api_sources, poll_news_api, find_reddit_shares
from exposure.adapters import aljazeera
from exposure.adapters import time

# ARE YOU EVEN SERIOUS TYLER, FILE WIDE DATABASE CONNECTION?
# Yes. So serious. #TODO: something better.
client = MongoClient()
mongo_db = client['exposure']
mongo_collection = mongo_db['articles']


def fetch_and_save():
    '''
    First, ask NewsAPI for all of it's current sources, then for each source
    ask NewsAPI for the most recent news from that source. Once we have the
    individual articles query reddit for the subreddits on which the article
    has been shared. Finally, persist ALL the article information into mongodb
    '''
    all_articles = []

    sources = fetch_news_api_sources()
    for source in sources:
        articles = poll_news_api(source, 'top')

        for a in articles:
            all_articles.append(a)
            shares = find_reddit_shares(a)

            for s in shares:
                a.add_share(s)

    storage_articles = [a.to_mongo() for a in all_articles]
    mongo_collection.insert_many(storage_articles)


def add_full_text():
    scrapper_map = {
        r'.*aljazeera.com/.*': aljazeera,
        r'.*time.com/.*': time
    }

    for regex, scrapper in scrapper_map.iteritems():
        alj_articles = mongo_collection.find({'source': {'$regex': regex}})
        for a in alj_articles:
            if not a.get('full_text'):
                try:
                    text = scrapper.fetch_and_extract_article_body(a['source'])
                    mongo_collection.update_one({'_id': a['_id']}, {
                        '$set': {
                            'full_text': text
                        }
                    })
                except Exception as e:
                    print 'Warning, failure for document {}: {}'.format(a, e)


if __name__ == "__main__":
    # fetch_and_save()
    # add_full_text()
