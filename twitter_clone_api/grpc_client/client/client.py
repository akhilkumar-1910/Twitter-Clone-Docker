import logging

from .helpers import Helper
from .twitter_clone_stub import TwitterCloneStub

logger = logging.getLogger(__name__)


class Client:

    def __init__(self, stub=None):
        self.stub = stub or TwitterCloneStub()
        self.helper = Helper()

    def get_all_tweets(self):
        all_tweets = self.stub.get_all_tweets()
        all_tweets = self.helper.get_all_tweets(all_tweets)
        logger.info(f"all_tweets: {all_tweets}")
        return all_tweets

    def get_tweets(self, username):
        user_tweets = self.stub.get_tweets(username)
        user_tweets = self.helper.get_tweets(user_tweets)
        logger.info(f"user_tweets: {user_tweets}")
        return user_tweets

    def create_tweet(self, username, content, tags):
        tweet = self.stub.create_tweet(username, content, tags)
        tweet_new = self.helper.create_tweet(tweet)
        logger.info(f"tweet_new: {tweet_new}")
        return tweet_new

    def remove_tweet(self, tweet_id):
        self.stub.remove_tweet(tweet_id)

    def edit_tweet(self, tweet_id, new_content, new_tags):
        self.stub.edit_tweet(tweet_id, new_content, new_tags)
