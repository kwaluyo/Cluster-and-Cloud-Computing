import couchdb
import re
import os,json
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from tweepy import Stream, StreamListener

couchserver = couchdb.Server("http://127.0.0.1:5984")
# Set credentials if necessary
couchserver.resource.credentials = ("admin", "admin")

dbresult = 'resulttest20k'
if dbresult in couchserver:
    dbres = couchserver[dbresult]
else:
    dbres = couchserver.create(dbresult)
# path_to_json = 'ADELAIDE/' # please change the directory name
path_to_several_json = ['ADELAIDE/','BRISBANE/','MELBOURNE/','SYDNEY/']
for path_to_json in path_to_several_json:
    json_files = [pos_json for pos_json in os.listdir(path_to_json) if pos_json.endswith('.jsonl')]
    # print(json_files)  # for me this prints ['foo.json']
    for each in json_files:
        print(each)
        with open(path_to_json+each, 'r', encoding='utf-8') as f:
            for line in f:
                data = []
                data.extend(json.loads(line))
                for eachdetail in data:
                    text = re.sub(r"(@[\w]+)|(https?://\S+)|(#+)", '', eachdetail['text'], flags=re.MULTILINE)
                    sentiment = SentimentIntensityAnalyzer().polarity_scores(text)
                    summary = 'negative'
                    if sentiment['compound'] > 0: 
                        summary = 'positive'
                    elif sentiment['compound']<0:
                        summary = 'negative'
                    else:
                        summary = 'neutral'
                    result = {
                        'id': eachdetail['id'],
                        'time':eachdetail['created_at'],
                        'text': text,
                        'location': path_to_json[0:-1],
                        'sentiment': sentiment,
                        'sentiment_summary': summary
                    }
                    dbres.save(result)
