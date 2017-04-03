from scripts.utility_belt import fetch_news_api_sources, poll_news_api, find_reddit_shares

import pickle
import re
import sys


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
    f.close()


def restore_dump(file_path):
    f = open(file_path)
    articles = pickle.load(f)
    return articles


def articles_to_string(articles):
    regex = r"http://www\.reddit\.com/r/(.*?)/.*"

    articles = sorted(articles, key = lambda a: -1 * a.avg_share_score())
    str_builder = ""

    for article in articles:
        if article.shares:
            str_builder += "\n" + str(article)

            for share in article.shares:
                str_builder += "\n  {0} : {1}".format(re.search(regex, share.share_url).group(1), str(share.share_rating))

    return str_builder


def dump_string(file_path):
    articles = restore_dump(file_path)
    return articles_to_string(articles)


if __name__ == "__main__":
    fetch_and_pickle(sys.argv[1])
