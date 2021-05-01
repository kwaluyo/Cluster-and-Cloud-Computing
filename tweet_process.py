import json
import re
import nltk
nltk.download('vader_lexicon')
from nltk.sentiment.vader import SentimentIntensityAnalyzer

tweets = []
with open('twitter.jsonl') as f:
    for line in f:
        data = json.loads(line)
        tweets.append(data)

def process_tweet(tweet_obj):
    text = tweet_obj['text']
    # remove user mentions, URLs and '#' character in hashtags
    text = re.sub(r"(@[\w]+)|(https?://\S+)|(#+)", '', text, flags=re.MULTILINE)

    # compound -> normalized from negative & postive score
    sentiment = SentimentIntensityAnalyzer().polarity_scores(text)['compound']
    return text, sentiment

def main():
    for tweet_obj in tweets:
        # for .json -> text, sentiment = process_tweet(tweet_obj)
        text, sentiment = process_tweet(tweet_obj[0])
