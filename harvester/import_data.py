'''
COMP90024
Team 17
Jeanelle Abanto: 1133815
Kartika Waluyo: 1000555
Radhimas Djan: 1146240
Zi Jin: 987771  
'''

import os
import json

from processor import TweetProcessor
import connect_db


class ImportTweets():
    """
    Import locally saved search tweet results to db.
    """

    def __init__(self) -> None:
        self.tweetProcessor = TweetProcessor()

    def populate_db(self):
        # path_to_json = 'ADELAIDE/' # please change the directory name
        path_to_several_json = ['ADELAIDE/','BRISBANE/','MELBOURNE/','SYDNEY/']
        for path_to_json in path_to_several_json:
            json_files = [pos_json for pos_json in os.listdir(path_to_json) if pos_json.endswith('.jsonl')]

            for file in json_files:
                print(f"Importing tweets from {path_to_json+file}")

                with open(path_to_json+file, 'r', encoding='utf-8') as f:
                    for line in f:
                        data = []
                        data.extend(json.loads(line))

                        for tweet in data:
                            city = path_to_json.strip('/')
                            res = self.tweetProcessor.process(tweet, city)
                            if not res is None:
                                connect_db.save_to_db(tweet=res)


if __name__ == "__main__":
    ImportTweets().populate_db()