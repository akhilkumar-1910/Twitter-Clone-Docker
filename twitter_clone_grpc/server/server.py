import logging

from proto import twitter_clone_pb2_grpc
from server.helpers import Helper

logger = logging.getLogger(__name__)


class TweetServicer(twitter_clone_pb2_grpc.TweetServiceServicer):
    def GetAllTweets(self, request, context):
        logger.info("Calling GetAllTweets")
        helper = Helper()
        all_tweets = helper.get_all_tweets()
        for tweet in all_tweets:
            yield tweet

    def GetTweets(self, request, context):
        logger.info("Calling GetTweets")
        helper = Helper()
        all_tweets = helper.get_tweets(request.username)
        for tweet in all_tweets:
            yield tweet

    def CreateTweet(self, request, context):
        logger.info("Calling CreateTweet")
        helper = Helper()
        response = helper.create_tweet(
            request.username,
            request.content,
            request.tag
        )
        return response

    def RemoveTweet(self, request, context):
        logger.info("Calling RemoveTweet")
        helper = Helper()
        helper.remove_tweet(request.id)

    def EditTweet(self, request, context):
        logger.info("Calling EditTweet")
        helper = Helper()
        response = helper.edit_tweet(
            request.id,
            request.content,
            request.tag
        )
        return response
