#!/usr/bin/python3
# tweepy-harvester/harvester/stream_tweet.py

from __future__ import absolute_import, print_function

import json
import threading
import logging
import re
import time

# nltk.download('vader_lexicon')
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from tweepy import Stream, StreamListener

import connect_db

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()


class DBStreamListener(StreamListener):
    """ 
    A listener handles tweets that are received from the stream.
    This is a basic listener that dumps received tweets to json file.
    """

    def __init__(self, city):
        
        # Location of live tweets
        self.city = city

        super().__init__()

    def on_status(self, tweet):
        logger.info(f"Stream: Processing tweet id {tweet.id}")
        # save_file = open('twitter.jsonl', 'a', encoding="utf8")
        # save_file.write("[" + json.dumps(tweet._json, separators=(',', ':')) + "]\n")
        # save_file.close()

    def on_error(self, status):
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

    def on_data(self, data):
        try:

            # Decode the JSON from Twitter
            datajson = json.loads(data)
            result = []

            text = re.sub(r"(@[\w]+)|(https?://\S+)|(#+)", '', datajson['text'], flags=re.MULTILINE)
            sentiment = SentimentIntensityAnalyzer().polarity_scores(text)
            summary = 'negative'
            if sentiment['compound'] > 0: 
                summary = 'positive'
            elif sentiment['compound']<0:
                summary = 'negative'
            else:
                summary = 'neutral'

            result = {
                'id': datajson['id'],
                'time':datajson['created_at'],
                'text': text,
                # change location based on bounding box
                'location': self.city,
                'sentiment': sentiment,
                'sentiment_summary': summary
            }

            connect_db.dbres.save(result)
            logger.info(result)
        except Exception as e:
            logger.error("Error saving to CouchDB", e)


def start_listener(api, stream_listener, keywords, location):
    try:
        stream = Stream(api.auth, stream_listener, tweet_mode='extended')
        stream.filter(languages=["en"], track=keywords, is_async=True, locations=location)
        logger.info("Stream listener started.")
    except Exception as e:
        logger.error("Start stream Error:", e)


def main(api, config):

    cities = ["SYDNEY", "MELBOURNE", "BRISBANE", "ADELAIDE"]

    # read in search criteria
    keywords = config['KEYWORDS']
    location = config['LOCATION']['BBOX']

    for city in cities:
        # create instance of stream listener
        stream_listener = DBStreamListener(city)

        # start stream listener
        threading.Thread(target=start_listener, args=(api, stream_listener, keywords, location[city],)).start()