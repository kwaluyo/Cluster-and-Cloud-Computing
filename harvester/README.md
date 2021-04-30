# COMP90024 - Cluster and Cloud Computing - 2021 S1 - Project 2, team 17

## Harvesting tweets using Tweepy
Create your own config.json with your Twitter account credentials and search words, and search coordinates.
 - Coordinates listed under "ALL" are bounding box coordinates of the cities you are interested in streaming tweets from.
 - You can replace SYDNEY, MELBOURNE, BRISBANE, and ADELAIDE with cities you want to search tweets from.
    - Note that the value is specified by “latitide,longitude,radius”, where radius units must be specified as either “mi” (miles) or “km” (kilometers).

The config file should looks like this:

```json
{
    "TWITTER":
    {
        "CONSUMER_KEY":"",
        "CONSUMER_SECRET":"",
        "ACCESS_TOKEN":"",
        "ACCESS_TOKEN_SECRET":""
    },
    "KEYWORDS":[],
    "LOCATION":
    {
        "ALL":
        [
            149.971885992, -34.33117400499998, 151.63054702400007, -32.99606922499993,
            144.33363404800002, -38.50298801599996, 145.8784120140001, -37.17509899299995,
            152.07339276400012, -28.363962911999977, 153.54670756200005, -26.452339004999942,
            138.435645001, -35.350296029999974, 139.04403010400003, -34.50022530299998
        ],
        "SYDNEY":"-33.865143,151.209900,1000mi",
        "MELBOURNE":"-37.840935,144.946457,1000mi",
        "BRISBANE":"-27.470125,153.021072,1000mi",
        "ADELAIDE":"-34.921230,138.599503,1000mi"
    },
    "SINCE_ID":1219755883690774529
}
```
