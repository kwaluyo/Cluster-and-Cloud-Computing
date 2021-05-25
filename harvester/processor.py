'''
COMP90024
Team 17
Jeanelle Abanto: 1133815
Kartika Waluyo: 1000555
Radhimas Djan: 1146240
Zi Jin: 987771  
'''

import logging
import re
import nltk
nltk.download('vader_lexicon')
from nltk.sentiment.vader import SentimentIntensityAnalyzer

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

class TweetProcessor():
    """
    A simple tweet processing module that cleans tweets and computes for the sentiments
    using Vader Sentiment Analyser module.
    """

    def __init__(self):
        self.sentimentAnalyser = SentimentIntensityAnalyzer()

    def process(self, tweet_obj, city) -> dict:
        """
        Preprocess tweets, compute sentiment analysis of tweets and identify whether tweet
        sentiment is positive, negative, or neutral.
        """
        result = None

        try:
            text = re.sub(r"(@[\w]+)|(https?://\S+)|(#+)", '', tweet_obj['text'], flags=re.MULTILINE)

            # compute sentiment analysis
            sentiment = self.sentimentAnalyser.polarity_scores(text)

            summary = 'negative'
            if sentiment['compound'] > 0: 
                summary = 'positive'
            elif sentiment['compound'] < 0:
                summary = 'negative'
            else:
                summary = 'neutral'

            result = {
                'id': tweet_obj['id_str'],
                'time': tweet_obj['created_at'],
                'text': text,
                'location': city,
                'sentiment': sentiment,
                'sentiment_summary': summary
            }

            return result

        except Exception as e:
            logger.error(f"Error processing tweets: {e}")
            return None