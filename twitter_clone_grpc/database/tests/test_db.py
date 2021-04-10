from .. import models
from ..twitter_clone_db import TwitterCloneDB
from sqlalchemy.orm.exc import NoResultFound
import pytest


class TestTwitterCloneDB:

    def test_get_all_tweets(self, db_session):
        tweet_1 = models.Tweet(content="Test tweet one")
        tweet_2 = models.Tweet(content="Test tweet two")
        db_session.add(tweet_1)
        db_session.add(tweet_2)
        db_session.commit()
        twitter_clone_db = TwitterCloneDB(db_session)
        assert twitter_clone_db.get_all_tweets() == [tweet_2, tweet_1]

    def test_get_tweets(self, db_session):
        tweet_1 = models.Tweet(username="test_user_1", content="Tweet one")
        tweet_2 = models.Tweet(username="test_user_1", content="Tweet two")
        tweet_3 = models.Tweet(username="test_user_2", content="Tweet three")
        db_session.add(tweet_1)
        db_session.add(tweet_2)
        db_session.add(tweet_3)
        db_session.commit()
        twitter_clone_db = TwitterCloneDB(db_session)
        assert twitter_clone_db.get_tweets("test_user_1") == [tweet_2, tweet_1]
        assert twitter_clone_db.get_tweets("test_user_2") == [tweet_3]
        assert twitter_clone_db.get_tweets("test_user_3") == []

    def test_create_tweet(self, db_session):
        tweet_1 = models.Tweet(username="test_user_1", content="Tweet one")
        tags = ["tag_1", "tag_2"]
        for tag in tags:
            tweet_1.tags.append(models.Tag(tag=tag))
        twitter_clone_db = TwitterCloneDB(db_session)
        tweet_2 = twitter_clone_db.create_tweet("test_user_1", "Tweet one", tags)
        assert tweet_1.username == tweet_2.username
        assert tweet_1.content == tweet_2.content
        assert tweet_1.tags[0].tag == tweet_2.tags[0].tag
        assert tweet_1.tags[1].tag == tweet_2.tags[1].tag

    def test_remove_tweet(self, db_session):
        tweet_1 = models.Tweet(username="test_user_1", content="Tweet one")
        tags = ["tag_1", "tag_2"]
        for tag in tags:
            tweet_1.tags.append(models.Tag(tag=tag))
        db_session.add(tweet_1)
        db_session.commit()
        twitter_clone_db = TwitterCloneDB(db_session)
        twitter_clone_db.remove_tweet(1)
        with pytest.raises(NoResultFound):
            db_session.query(models.Tweet).filter(models.Tweet.id == 1).one()

    def test_remove_tweet_returns_none(self, db_session):
        twitter_clone_db = TwitterCloneDB(db_session)
        assert twitter_clone_db.remove_tweet(1) is None

    def test_edit_tweet(self, db_session):
        tweet_1 = models.Tweet(username="test_user_1", content="Tweet one")
        tags = ["tag_1", "tag_2"]
        for tag in tags:
            tweet_1.tags.append(models.Tag(tag=tag))
        db_session.add(tweet_1)
        db_session.commit()
        edited_content = "New content"
        edited_tags = ["tag_3", "tag_4"]
        twitter_clone_db = TwitterCloneDB(db_session)
        tweet_edited = twitter_clone_db.edit_tweet(1, edited_content, edited_tags)
        assert tweet_1.content == tweet_edited.content
        assert tweet_1.tags[0].tag == tweet_edited.tags[0].tag
        assert tweet_1.tags[1].tag == tweet_edited.tags[1].tag

    def test_edit_tweet_returns_none(self, db_session):
        twitter_clone_db = TwitterCloneDB(db_session)
        edited_content = "New"
        tags = []
        assert twitter_clone_db.edit_tweet(1, edited_content, tags) is None
