# Exposure

Exposure hopes to become a tool to help readers find newsworthy information that is simultaneously thoughtful __and__ not aligned with the users current worldview using machine learning tactics, web API's, and web scraping tools, and more.

## State of the Union

Currently the Exposure project is little more than an API consumer + web-scraper. We use NewsAPI to fetch the daily headlines and URL's for those articles, storing these into a Mongo database. We then we use custom adapters per source to (attempt to) fetch the full text of the article. Our adapters make a best effort fetch and store ONLY the article text. In addition to the full text (for sources that have an up-to-date adapter) we also search Reddit for all the subreddits that have had that article posted to it, and the articles score on that subreddit.

## Running the Scripts

Install Mongo DB. I'm trusting you to Google that. Install the dependencies:

```
pip install -r requirements.txt
```

Signup with [NewsAPI](https://newsapi.org/) and get an API key. Create a file `exposure/config.py` that contains just this line:

```
NEWS_API_KEY = "YourKeyHere"
```

Add this directory to your PYTHONPATH (I suggest a virtual environment here but that's up to you).

Currently there are 3 scripts that simply serve as examples of how to do things and just one script that populates the database with today's news, and it's reddit shares. To populate your database with everything Exposure can currently grab, start your mongodb (assumed to be localhost at the time of this writing) and run:

```
python exposure/scripts/news_reddit_dump.py
```
