import logging

import grpc

from grpc_client.proto.twitter_clone_pb2 import Tweet
from grpc_client.proto.twitter_clone_pb2_grpc import TweetServiceStub

logger = logging.getLogger(__name__)


class TwitterCloneStub:

    def __init__(self, stub=None):
        self.channel = grpc.insecure_channel("grpc:50051")
        self.stub = stub or TweetServiceStub(self.channel)
        self.all_tweets = []

    def get_all_tweets(self):
        tweet = Tweet()
        try:
            tweets = self.stub.GetAllTweets(tweet)
            self.all_tweets = [tweet for tweet in tweets]
            logger.info("stub: get_all_tweets: success")
            return self.all_tweets
        except grpc.RpcError as e:
            if e.code() == grpc.StatusCode.UNAVAILABLE:
                logger.error("grpc server unavailable")
                return self.all_tweets

    def get_tweets(self, username):
        tweet = Tweet(username=username)
        try:
            tweets = self.stub.GetTweets(tweet)
            self.all_tweets = [tweet for tweet in tweets]
            logger.info("stub: get_tweets: success")
            return self.all_tweets
        except grpc.RpcError as e:
            if e.code() == grpc.StatusCode.UNAVAILABLE:
                logger.error("grpc server unavailable")
            else:
                logger.error(f"{e.code()}: {e.details()}")

    def create_tweet(self, username, content, tags):
        tweet = Tweet(
            username=username,
            content=content,
        )
        for tag in tags:
            tweet.tag.append(tag)
        try:
            tweet_new = self.stub.CreateTweet(tweet)
            logger.info("stub: create_tweet: success")
            return tweet_new
        except grpc.RpcError as e:
            if e.code() == grpc.StatusCode.UNAVAILABLE:
                logger.error("grpc server unavailable")
            else:
                logger.error(f"{e.code()}: {e.details()}")

    def remove_tweet(self, tweet_id):
        tweet = Tweet(
            id=tweet_id
        )
        try:
            tweet_to_remove = self.stub.RemoveTweet(tweet)
            logger.info("stub: remove_tweet: success")
            return tweet_to_remove
        except grpc.RpcError as e:
            if e.code() == grpc.StatusCode.UNAVAILABLE:
                logger.error("grpc server unavailable")
            else:
                logger.error(f"{e.code()}: {e.details()}")

    def edit_tweet(self, tweet_id, new_content, new_tags):
        tweet = Tweet(
            id=tweet_id,
            content=new_content,
        )
        for tag in new_tags:
            tweet.tag.append(tag)
        try:
            tweet_to_edit = self.stub.EditTweet(tweet)
            logger.info("stub: edit_tweet: success")
            return tweet_to_edit
        except grpc.RpcError as e:
            if e.code() == grpc.StatusCode.UNAVAILABLE:
                logger.error("grpc server unavailable")
            else:
                logger.error(f"{e.code()}: {e.details()}")

    def __del__(self):
        self.channel.close()
