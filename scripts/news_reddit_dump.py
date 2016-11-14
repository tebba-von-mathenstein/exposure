from scripts.utility_belt import *
import re
import pickle

def fetch_and_pickle(file_path):
    all_articles = []

    sources = fetch_news_api_sources()
    for source in sources:
        print source
        articles = poll_news_api(source, 'top')

        for a in articles:
            print a
            all_articles.append(a)
            shares = find_reddit_shares(a)

            for s in shares:
                a.add_share(s)
                print "  " + str(s)

        # Overwrite the latest dump after each news source.
        # Might become slow later...
        f = open(file_path, 'w')
        pickle.dump(all_articles, f)


def restore_dump(file_path):
    f = open(file_path)
    articles = pickle.load(f)
    return articles


def pprint_articles(articles):
    regex = r"http://www\.reddit\.com/r/(.*?)/.*"

    for article in articles:
        if article.shares:
            print str(article)

            for share in article.shares:
                print "  {0} : {1}".format(re.search(regex, share.share_url).group(1), str(share.share_rating))

def print_latest_dump():
    articles = restore_dump('output/last_dump')
    pprint_articles(articles)
