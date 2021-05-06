import threading
import logging
import json

from utils import load_config
from processor import TweetProcessor
import connect_db

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()


class SearchTweet():
    """
    Handles an API for searching tweets for a given city location from a given twitter since ID.
    The location is preferentially taking from the Geotagging API, but will fall back to their Twitter profile.
    There are limits to the number of Tweets which can be accessed through the API. 
    If the limit of Tweets has occurred since the since_id, the since_id will be forced to the oldest ID available.
    """

    def __init__(self, api, location, city, since_id):

        self.tweetProcessor = TweetProcessor()
        self.api = api
        self.location = location
        self.city = city
        self.since_id = since_id


    def search_city(self):
        """
        Search tweets within a specified radius from city center (latitude and longitude).
        Depending on Twitter Developer Account type, it can search tweets from the full archive or,
        search tweets from the last 7 days.
        """
        
        # Scrape tweets from January 2020 or the past 7 days
        try:
            while True:
                
                # Returns tweets by users located within a given radius of the given latitude/longitude. 
                for tweet in self.api.search(lang=["en"], geocode=self.location, count=100, since_id=self.since_id):
                    # Look for tweet
                    logger.info(f"Search: Processing tweet id {tweet.id}")
                    tweet_data = tweet._json

                    res = self.tweetProcessor.process(tweet_data, self.city)
                    if not res is None:
                        connect_db.dbres.save(res)
                        # uncomment for debug
                        # print(res)
                    
                        logger.info(f"Search: Tweet saved to DB: {res}")

        except Exception as e:
            logger.error(f"Search: Error searching tweets: {e}")


def main(api, config):
    """
    Spawn threads that will search for old and new (mixed) tweets from Sydney, Melbourne, Brisbane, and Adelaide.
    """

    cities = ["SYDNEY", "MELBOURNE", "BRISBANE", "ADELAIDE"]

    # read in search criteria
    location = config['LOCATION']
    since_id = config['SINCE_ID'] # JAN2020

    # start searching tweets on each city
    for city in cities:
        search = SearchTweet(api, location[city], city, since_id)
        threading.Thread(target=search.search_city).start()
