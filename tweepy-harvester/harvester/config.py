# tweepy-harvester/harvester/config.py
import tweepy
import logging
import os

logger = logging.getLogger()


# CouchDB credentials
# NODE_ID = os.getenv("NODE_ID")
# COUCHDB_USER = os.getenv("COUCHDB_USER")
# COUCHDB_PASSWORD = os.getenv("COUCHDB_PASSWORD")

# Twitter credentials
TWITTER_CONSUMER_KEY = os.getenv("TWITTER_CONSUMER_KEY")
TWITTER_CONSUMER_SECRET = os.getenv("TWITTER_CONSUMER_SECRET")
TWITTER_ACCESS_TOKEN = os.getenv("TWITTER_ACCESS_TOKEN")
TWITTER_ACCESS_TOKEN_SECRET = os.getenv("TWITTER_ACCESS_TOKEN_SECRET")

# Change value to filter out tweets intended for analysis
# FILTER = [140.928224, -39.449811, 150.024903, -33.959390] # filter tweets from VICTORIA
FILTER = [113.338953078, -43.6345972634, 153.569469029, -10.6681857235] # filter tweets from AUSTRALIA

def create_api():
    consumer_key = TWITTER_CONSUMER_KEY
    consumer_secret = TWITTER_CONSUMER_SECRET
    access_token = TWITTER_ACCESS_TOKEN
    access_token_secret = TWITTER_ACCESS_TOKEN_SECRET
    
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    api = tweepy.API(auth, wait_on_rate_limit=True, 
        wait_on_rate_limit_notify=True)

    try:
        api.verify_credentials()

    except Exception as e:
        logger.error("Error creating API", exc_info=True)
        raise e

    logger.info("API created")

    return api