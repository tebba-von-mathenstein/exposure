from scripts.utility_belt import *
articles = poll_news_api('the-new-york-times', 'top')

for a in articles:
    print a
    shares = find_reddit_shares(a)


    for s in shares:
        print "  " + str(s)
