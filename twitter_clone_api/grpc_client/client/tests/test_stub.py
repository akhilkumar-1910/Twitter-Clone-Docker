from unittest.mock import Mock
# import pytest
import grpc
from grpc_service.proto.twitter_clone_pb2_grpc import TweetServiceStub
from grpc_service.proto.twitter_clone_pb2 import Tweet
from ..twitter_clone_stub import TwitterCloneStub


class TestTwitterCloneStub:

    stub = Mock(spec=TweetServiceStub(channel=grpc.insecure_channel("")))
    tweet = Mock(spec=Tweet())

    def test_get_all_tweets(self):
        all_tweets = [self.tweet, self.tweet, self.tweet, self.tweet]
        self.stub.GetAllTweets.return_value = all_tweets
        twitter_clone_stub = TwitterCloneStub(self.stub)
        assert twitter_clone_stub.get_all_tweets() == all_tweets

    def test_get_tweets(self):
        self.tweet.username = "test_user"
        all_tweets = [self.tweet, self.tweet]
        self.stub.GetTweets.return_value = all_tweets
        twitter_clone_stub = TwitterCloneStub(self.stub)
        assert twitter_clone_stub.get_tweets("test_user") == all_tweets

    def test_create_tweet(self):
        self.tweet.username = "test_user"
        content = "Test content for creating tweet."
        self.tweet.content = content
        tags = ["test_tag_1, test_tag_2"]
        for tag in tags:
            self.tweet.tag.append(tag)
        self.stub.CreateTweet.return_value = self.tweet
        twitter_clone_stub = TwitterCloneStub(self.stub)
        assert (
            twitter_clone_stub.create_tweet("test_user", content, tags)
            == self.tweet
        )

    def test_remove_tweet(self):
        self.tweet.id = 1
        self.stub.RemoveTweet.return_value = self.tweet
        twitter_clone_stub = TwitterCloneStub(self.stub)
        assert twitter_clone_stub.remove_tweet(1) == self.tweet

    def test_edit_tweet(self):
        self.tweet.id = 1
        edited_content = "Testing edited content."
        self.tweet.content = edited_content
        edited_tags = ["tag_1", "tag_2"]
        for tag in edited_tags:
            self.tweet.tag.append(tag)
        self.stub.EditTweet.return_value = self.tweet
        twitter_clone_stub = TwitterCloneStub(self.stub)
        assert (
            twitter_clone_stub.edit_tweet(1, edited_content, edited_tags)
            == self.tweet
        )
