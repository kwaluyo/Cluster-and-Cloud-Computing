#!/usr/bin/python3
# tweepy-harvester/harvester/stream_tweet.py

from __future__ import absolute_import, print_function

from tweepy import API, OAuthHandler, Stream, StreamListener
import logging
import json
import time

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()


class DBStreamListener(StreamListener):
    """ 
    A listener handles tweets that are received from the stream.
    This is a basic listener that dumps received tweets to json file.
    """
    
    def on_status(self, tweet):
        logger.info(f"Processing tweet id {tweet.id}")
        save_file = open('twitter.jsonl', 'a', encoding="utf8")
        save_file.write("["+json.dumps(tweet._json, separators=(',', ':'))+"]\n")
        save_file.close()

    def on_error(self, status):
        logger.error(status)

        if status == 420:
            # Rate limit reached
            logger.error("Rate limit reached. Retry in 30 seconds.")
            time.sleep(30)

        if status == 429:
            # Too many requests
            logger.error("Too many requests. Retry in 15 minutes.")
            time.sleep(15*60 + 1)

        else:
            logger.error("Unexpected error. Retry in 10 seconds.")
            time.sleep(10)


def main():

    # read in Twitter credentials and search criteria
    try:
        with open('config.json', "r") as f:
            config = json.load(f)
            
            if not 'TWITTER' in config:
                logger.error("Twitter account not found.") 
                exit(1)
            
            if not 'KEYWORDS' in config:
                logger.error("Search keywords not found.")
                exit(1)

            if not 'LOCATION' in config:
                logger.error("Search location not found.")

            account = config['TWITTER']
            keywords = config['KEYWORDS']
            location = config['LOCATION']

    except IOError:
        logger.error("A config file was not found.")
        exit(1)

    # create instance of stream listener
    stream_listener = DBStreamListener()
    auth = OAuthHandler(consumer_key=account["CONSUMER_KEY"], consumer_secret=account["CONSUMER_SECRET"])
    auth.set_access_token(account["ACCESS_TOKEN"], account["ACCESS_TOKEN_SECRET"])

    api = API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

    # verify Twitter credentials
    try:
        api.verify_credentials()

    except Exception as e:
        logger.error("Failed to verify Twitter credentials.", exc_info=True)
        exit(1)

    logger.info("Twitter credentials verified.")

    # start stream listener
    stream = Stream(auth, stream_listener, tweet_mode='extended')
    stream.filter(track=keywords, is_async=True, locations=location)

    logger.info("Stream listener started.")


if __name__ == "__main__":
    main()