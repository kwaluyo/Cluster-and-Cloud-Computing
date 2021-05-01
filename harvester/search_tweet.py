import tweepy
from tweepy import API, OAuthHandler
import threading
import logging
import json
import os
import datetime

from utils import load_config

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()


def search_city(api, location, city, since_id):
    """
    Search tweets within a specified radius from city center (latitude and longitude).
    Depending on Twitter Developer Account type, it can search tweets from the full archive or,
    search tweets from the last 7 days.
    """
    if not os.path.isdir(city+"/"):
        os.makedirs(city)
    
    path = city + "/" + str(datetime.date.today())+".jsonl"
    save_file = open(path, 'a', encoding="utf8")

    # Scrape tweets from January 2020 or the past 7 days
    try:
        for i in range(250):
            # Returns tweets by users located within a given radius of the given latitude/longitude. 
            # The location is preferentially taking from the Geotagging API, but will fall back to their Twitter profile.
            # There are limits to the number of Tweets which can be accessed through the API. 
            # If the limit of Tweets has occurred since the since_id, the since_id will be forced to the oldest ID available.
            for tweet in api.search(lang=["en"], geocode=location, count=100, since_id=since_id):

                # Look for tweet
                logger.info(f"Search: Processing tweet id {tweet.id}")
                save_file.write("["+json.dumps(tweet._json, separators=(',', ':'))+"]\n")

    except Exception as e:
        logger.error("Tweet search error:", e)


def main(api, config):
    
    cities = ["SYDNEY", "MELBOURNE", "BRISBANE", "ADELAIDE"]
    
    # read in search criteria
    location = config['LOCATION']
    since_id = config['SINCE_ID'] # JAN2020

    # start stream listener
    for city in cities:
        threading.Thread(target=search_city, args=(api, location[city], city, since_id,)).start()