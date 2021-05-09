from unittest.mock import Mock
import pytest
from database.twitter_clone_db import TwitterCloneDB
from server.helpers import Helper
from database import models
from proto.twitter_clone_pb2 import Tweet
from google.protobuf.timestamp_pb2 import Timestamp
import datetime

# import grpc


class TestHelper:

    twitter_clone_db = Mock(spec=TwitterCloneDB())
    tweet = Mock(spec=Tweet)

    @pytest.mark.skip
    def test_get_all_tweets(self):
        tweet_db = models.Tweet(
            username="test_user",
            content="Test Content",
            posted_at=datetime.datetime.now(),
            last_edited_at=datetime.datetime.now(),
        )
        for tag in ["tag_1", "tag_2"]:
            tweet_db.tags.append(models.Tag(tag=tag))
        tweets = [tweet_db, tweet_db]
        self.twitter_clone_db.get_all_tweets.return_value = tweets
        all_tweets = []
        t1 = Timestamp()
        t2 = Timestamp()
        for tweet_ in tweets:
            if tweet_.posted_at is not None:
                t1.FromDatetime(tweet_.posted_at)
            if tweet_.last_edited_at is not None:
                t2.FromDatetime(tweet_.last_edited_at)
            else:
                t2 = t1
            ret_tweet = self.tweet(
                id=tweet_.id,
                username=tweet_.username,
                content=tweet_.content,
                posted_at=t1,
                last_edited_at=t2,
            )
            for tag in tweet_.tags:
                ret_tweet.tag.append(tag.tag)
            all_tweets.append(ret_tweet)
        helper = Helper(self.twitter_clone_db)
        assert helper.get_all_tweets() == all_tweets

    def test_get_tweets(self):
        tweet_db = models.Tweet(
            username="test_user",
            content="Test Content",
            posted_at=datetime.datetime.now(),
            last_edited_at=datetime.datetime.now(),
        )
        for tag in ["tag_1", "tag_2"]:
            tweet_db.tags.append(models.Tag(tag=tag))
        tweets = [tweet_db, tweet_db]
        self.twitter_clone_db.get_tweets.return_value = tweets
        all_tweets = []
        t1 = Timestamp()
        t2 = Timestamp()
        for tweet in tweets:
            if tweet.posted_at is not None:
                t1.FromDatetime(tweet.posted_at)
            if tweet.last_edited_at is not None:
                t2.FromDatetime(tweet.last_edited_at)
            else:
                t2 = t1
            ret_tweet = Tweet(
                id=tweet.id,
                username=tweet.username,
                content=tweet.content,
                posted_at=t1,
                last_edited_at=t2,
            )
            for tag in tweet.tags:
                ret_tweet.tag.append(tag.tag)
            all_tweets.append(ret_tweet)
        helper = Helper(self.twitter_clone_db)
        assert helper.get_tweets(self.tweet) == all_tweets

    def test_get_tweets_returns_empty_list_if_username_not_present(self):
        self.twitter_clone_db.get_tweets.return_value = []
        helper = Helper(self.twitter_clone_db)
        assert helper.get_tweets(self.tweet) == []
