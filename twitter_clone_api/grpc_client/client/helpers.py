from .twitter_clone_stub import TwitterCloneStub


class Helper():

    def __init__(self, stub=None):
        self.stub = stub or TwitterCloneStub()

    def get_all_tweets(self):
        tweets = self.stub.get_all_tweets()
        if tweets is not None:
            all_tweets = [
                {
                    "id": tweet.id,
                    "username": tweet.username,
                    "content": tweet.content,
                    "posted_at": tweet.posted_at.ToDatetime(),
                    "last_edited_at": tweet.last_edited_at.ToDatetime(),
                    "tags": list(tweet.tag),
                }
                for tweet in tweets
            ]
            return all_tweets

    def get_tweets(self, username):
        tweets = self.stub.get_tweets(username)
        if tweets is not None:
            all_tweets = [
                {
                    "id": tweet.id,
                    "username": tweet.username,
                    "content": tweet.content,
                    "posted_at": tweet.posted_at.ToDatetime(),
                    "last_edited_at": tweet.last_edited_at.ToDatetime(),
                    "tags": list(tweet.tag),
                }
                for tweet in tweets
            ]
            return all_tweets

    def create_tweet(self, username, content, tags):
        tweet = self.stub.create_tweet(username, content, tags)
        tweet_new = {
            "username": tweet.username,
            "content": tweet.content,
            "posted_at": tweet.posted_at,
            "last_edited_at": tweet.last_edited_at,
            "tags": list(tweet.tag),
        }
        return tweet_new

    def remove_tweet(self, tweet_id):
        self.stub.remove_tweet(tweet_id)

    def edit_tweet(self, tweet_id, new_content, new_tags):
        self.stub.edit_tweet(tweet_id, new_content, new_tags)
