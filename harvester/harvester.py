#!/usr/bin/python3

from tweepy import API, OAuthHandler
from multiprocessing import Process
import logging
import time

import stream_tweet
import search_tweet
from utils import load_config


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

def create_api(cfg):
    account = cfg['TWITTER']

    auth = OAuthHandler(consumer_key=account["CONSUMER_KEY"], consumer_secret=account["CONSUMER_SECRET"])
    auth.set_access_token(account["ACCESS_TOKEN"], account["ACCESS_TOKEN_SECRET"])

    api = API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

    try:
        api.verify_credentials()

    except Exception as e:
        logger.error("Error creating API:", e)

    logger.info("API created")
    return api


def main():

    configs = load_config()
    target = [stream_tweet.main, search_tweet.main]
    while True:
        api = create_api(configs[0])
        jobs = []
        try:
            for i in range(len(configs)):
                # Create threads to stream and search tweets
                stream = Process(target=stream_tweet.main, args=(api, configs[i]), daemon=True)
                search = Process(target=search_tweet.main, args=(api, configs[i]), daemon=True)
                jobs.append(stream)
                jobs.append(search)

                # Start harvesting tweets
                stream.start()
                search.start()
                
            [p.join() for p in jobs]

        except Exception as e:
            logger.error("Harvest thread stopped:", e)
            
        # reconnect after 10 seconds
        time.sleep(10)


if __name__ == "__main__":
    main()