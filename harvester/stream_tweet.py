#!/usr/bin/python3
# tweepy-harvester/harvester/stream_tweet.py

from __future__ import absolute_import, print_function

from tweepy import API, OAuthHandler, Stream, StreamListener
import threading
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
        logger.info(f"Stream: Processing tweet id {tweet.id}")
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


def start_listener(api, stream_listener, keywords, location):
    try:
        stream = Stream(api.auth, stream_listener, tweet_mode='extended')
        stream.filter(languages=["en"], track=keywords, is_async=True, locations=location['ALL'])
        logger.info("Stream listener started.")
    except Exception as e:
        logger.error("Start stream Error:", e)


def main(api, config):

    # read in search criteria
    keywords = config['KEYWORDS']
    location = config['LOCATION']

    # create instance of stream listener
    stream_listener = DBStreamListener()
    
    # start stream listener
    try:
        stream = Stream(api.auth, stream_listener, tweet_mode='extended')
        stream.filter(languages=["en"], track=keywords, is_async=True, locations=location['ALL'])
        logger.info("Stream listener started.")
    except Exception as e:
        logger.error("Start stream Error:", e)