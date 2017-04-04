from pymongo import MongoClient
from scripts.utility_belt import fetch_news_api_sources, poll_news_api, find_reddit_shares
from adapters import aljazeera

# ARE YOU EVEN SERIOUS TYLER, FILE WIDE DATABASE CONNECTION?
# Yes. So serious.
client = MongoClient()
mongo_db = client['exposure']
mongo_collection = mongo_db['articles']


def fetch_and_save():
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


def add_aljazeera_article_text():
    alj_articles = mongo_collection.find({'source': {'$regex': '.*www.aljazeera.com/.*'}})
    for a in alj_articles:
        if not a.get('full_text'):
            text = aljazeera.fetch_and_extract_article_body(a['source'])
            print text
            mongo_collection.update_one({'_id': a['_id']}, {
                '$set': {
                    'full_text': text
                }
            })


if __name__ == "__main__":
    # fetch_and_save()
    add_aljazeera_article_text()
