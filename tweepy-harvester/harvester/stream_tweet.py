#!/usr/bin/env python
# tweepy-harvester/harvester/stream_tweet.py

from __future__ import absolute_import, print_function

from tweepy import OAuthHandler, Stream, StreamListener
import logging
import threading
from config import create_api, FILTER_GEOLOCATION
import json
import time

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()


class DBStreamListener(StreamListener):
    """ 
    A listener handles tweets that are received from the stream.
    This is a basic listener that dumps received tweets to json file.
    """
    
    def __init__(self, api):
        self.api = api
        self.me = api.me()
        
        super().__init__()

    def on_status(self, tweet):
        logger.info(f"Processing tweet id {tweet.id}")
        save_file = open('twitter.jsonl', 'a', encoding="utf8")
        save_file.write("["+json.dumps(tweet._json, separators=(',', ':'))+"]\n")
        save_file.close()

    def on_error(self, status):
        logger.error(status)
        if status == 420:

            # Rate limit reached, wait 15 minutes
            time.sleep(900)
            return False

        # Reconnect to server
        return True


def main():
    api = create_api()
    stream_listener = DBStreamListener(api)
    
    while True:
        try:
            # Listen for tweet
            stream = Stream(api.auth, stream_listener)
            stream.filter(locations=FILTER_GEOLOCATION)
            
        except KeyboardInterrupt: 
            break

        except Exception as e:
            logger.error(e)
            continue


if __name__ == "__main__":
    main()