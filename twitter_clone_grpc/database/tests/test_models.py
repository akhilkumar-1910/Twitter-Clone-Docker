from .. import models


class TestModels:

    def test_tweet_object_id_content(self, db_session):
        tweet = models.Tweet(content="Test content")
        db_session.add(tweet)
        db_session.commit()
        assert str(tweet) == "{0}. {1}".format(1, "Test content")

    def test_tag_object_id_tagname(self, db_session):
        tag = models.Tag(tag="test_tag")
        db_session.add(tag)
        db_session.commit()
        assert str(tag) == "{0}. {1}".format(1, "test_tag")
