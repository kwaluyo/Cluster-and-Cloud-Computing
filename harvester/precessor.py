import json
import re
import nltk
nltk.download('vader_lexicon')
from nltk.sentiment.vader import SentimentIntensityAnalyzer

cities = ["SYDNEY", "MELBOURNE", "BRISBANE", "ADELAIDE"]

class tweet_processor():
    def __init__(self, tweet_obj):
        self.tweet_obj = tweet_obj

    def process(self) -> {}:
        result = {}

        try:
            text = re.sub(r"(@[\w]+)|(https?://\S+)|(#+)", '', self.tweet_obj['text'], flags=re.MULTILINE)
            sentiment = SentimentIntensityAnalyzer().polarity_scores(text)

            for city in cities:
                if city in self.tweet_obj['user']['location'].upper():
                    location = city

            result['id'] = self.tweet_obj['id_str']
            result['text'] = text
            result['location'] = location
            result['sentiment'] = sentiment
            result['sentiment_summary'] = 'positive' if sentiment['compound'] > 0 else 'neagtive'

            return result

        except Exception as err:
            print(err)
            return {}
