from unittest.mock import Mock
from grpc_client.proto.twitter_clone_pb2 import Tweet
from ..twitter_clone_stub import TwitterCloneStub
from ..helpers import Helper


class TestHelper:

    twitter_clone_stub = Mock(spec=TwitterCloneStub())
    tweet = Mock(spec=Tweet())

    def test_get_all_tweets(self):
        tweets = [self.tweet, self.tweet, self.tweet]
        self.twitter_clone_stub.get_all_tweets.return_value = tweets
        all_tweets = [
            {
                "id": tweet.id,
                "username": tweet.username,
                "content": tweet.content,
                "posted_at": tweet.posted_at.ToDatetime(),
                "last_edited_at": tweet.last_edited_at.ToDatetime(),
                "tags": tweet.tag,
            }
            for tweet in tweets
        ]
        helper = Helper(self.twitter_clone_stub)
        assert helper.get_all_tweets() == all_tweets

    def test_get_tweets(self):
        self.tweet.username = "test_user"
        tweets = [self.tweet, self.tweet, self.tweet]
        self.twitter_clone_stub.get_tweets.return_value = tweets
        all_tweets = [
            {
                "id": tweet.id,
                "username": tweet.username,
                "content": tweet.content,
                "posted_at": tweet.posted_at.ToDatetime(),
                "last_edited_at": tweet.last_edited_at.ToDatetime(),
                "tags": tweet.tag,
            }
            for tweet in tweets
        ]
        helper = Helper(self.twitter_clone_stub)
        assert helper.get_tweets(self.tweet.username) == all_tweets

    def test_create_tweet(self):
        username = "test_user"
        self.tweet.username = username
        content = "test content"
        self.tweet.content = content
        tags = ["tag_1", "tag_2"]
        self.tweet.tags = tags
        self.twitter_clone_stub.create_tweet.return_value = self.tweet
        tweet_new = {
            "username": self.tweet.username,
            "content": self.tweet.content,
            "posted_at": self.tweet.posted_at,
            "last_edited_at": self.tweet.last_edited_at,
            "tags": self.tweet.tag,
        }
        helper = Helper(self.twitter_clone_stub)
        assert helper.create_tweet(username, content, tags) == tweet_new
