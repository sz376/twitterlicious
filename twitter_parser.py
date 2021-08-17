"""
functions to fetch data from twitter
"""
import random
import os
from os.path import join, dirname
from dotenv import load_dotenv
import tweepy

dotenv_path = join(dirname(__file__), "tweepy.env")
load_dotenv(dotenv_path)
# twitter API access keys here, check README for more info
consumer_key = os.getenv("CONSUMER_KEY")
consumer_secret = os.getenv("CONSUMER_SECRET")
access_token = os.getenv("ACCESS_TOKEN")
access_token_secret = os.getenv("ACCESS_TOKEN_SECRET")


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)


def get_tweet(food_list):
    """gets a tweet given a list of foods"""
    tweet_dict = {}

    # create a random number to pull a tweet from an index
    # currently set to a low number in case of an unpopular food
    rand = random.randint(0, 6)
    for food in food_list:
        # searching API, currently set to a max return of 500.
        # Unsure of what the Twitter API rate limit is
        # but will usually pull around 25~ tweets per food item
        public_tweets = api.search(q=food, count=500)
        tempstatus = []

        for tweet in public_tweets:
            # filtering out retweets, replies, and non-english tweets
            if (
                not hasattr(tweet, "retweeted_status")
                and tweet.in_reply_to_status_id is None
                and tweet.lang == "en"
            ):
                tempstatus.append(tweet)

        # adding the list of tweet items to the dictionary
        tweet_dict[food] = tempstatus

    return food_list[rand], tweet_dict[food_list[rand]][rand]
