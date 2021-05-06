#!/usr/bin/python3
# tweepy-harvester/harvester/stream_tweet.py

from __future__ import absolute_import, print_function

import json
import threading
import logging
import time

from tweepy import Stream, StreamListener

import connect_db
from processor import TweetProcessor

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()


class DBStreamListener(StreamListener):
    """ 
    A listener handles tweets that are received from the stream.
    This is a basic listener that dumps received live tweets to DB.
    """

    def __init__(self, city):
        
        # Location of live tweets
        self.city = city
        self.tweetProcessor = TweetProcessor()

        super().__init__()

    def on_data(self, data):
        """
        Save streamed tweets to DB.
        """
        try:
            # Decode the JSON from Twitter
            tweet = json.loads(data)
            logger.info(f"Stream: Processing tweet id {tweet['id']}")
            
            res = self.tweetProcessor.process(tweet, self.city)
            if not res is None:
                connect_db.dbres.save(res)
                # uncomment for debug
                # print(res)
            
            logger.info(f"Stream: Tweet saved to DB: {res}")

        except Exception as e:
            logger.error(f"Stream: Error saving to CouchDB: {e}")

    def on_error(self, status):
        """
        Handle wait times for different connection errors.
        """
        logger.error(status)

        if status == 420:
            # Rate limit reached
            logger.error("Rate limit reached. Retry in 30 seconds.")
            time.sleep(30)

        if status == 429:
            # Too many requests
            logger.error("Too many requests. Retry in 15 minutes.")
            time.sleep(15 * 60 + 1)

        else:
            logger.error("Unexpected error. Retry in 10 seconds.")
            time.sleep(10)


def start_listener(api, stream_listener, keywords, location):
    """
    Start API to listen to filtered live streams.
    """
    try:
        stream = Stream(api.auth, stream_listener, tweet_mode='extended')
        stream.filter(languages=["en"], track=keywords, is_async=True, locations=location)
        logger.info("Stream listener started.")
    except Exception as e:
        logger.error("Start stream Error:", e)


def main(api, config):
    """
    Spawn threads that will stream for live tweets from Sydney, Melbourne, Brisbane, and Adelaide.
    """

    cities = ["SYDNEY", "MELBOURNE", "BRISBANE", "ADELAIDE"]

    # read in search criteria
    keywords = config['KEYWORDS']
    location = config['LOCATION']['BBOX']

    for city in cities:
        # create instance of stream listener
        stream_listener = DBStreamListener(city)

        # start streaming tweets from each city
        threading.Thread(target=start_listener, args=(api, stream_listener, keywords, location[city],)).start()