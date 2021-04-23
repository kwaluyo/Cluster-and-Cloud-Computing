#!/usr/bin/env python
# tweepy-harvester/harvester/stream_tweet.py

from __future__ import absolute_import, print_function

from tweepy import OAuthHandler, Stream, StreamListener
import logging
from config import create_api, FILTER
import json

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
        
        self.save_file = open('twitter.json','a')
        
        super().__init__()

    def on_status(self, tweet):
        logger.info(f"Processing tweet id {tweet.id}")
        
    def on_data(self, tweet):   
        self.save_file.write(str(tweet).strip("\n"))

    def on_error(self, status):
        logger.error(status)

def main():
    api = create_api()
    stream_listener = DBStreamListener(api)
    stream = Stream(api.auth, stream_listener)
    stream.filter(locations=FILTER)

if __name__ == "__main__":
    main()