from .helpers import Helper


class Client:

    def __init__(self):
        self.helper = Helper()

    def get_all_tweets(self):
        all_tweets = self.helper.get_all_tweets()
        return all_tweets

    def get_tweets(self, username):
        all_tweets = self.helper.get_tweets(username)
        return all_tweets

    def create_tweet(self, username, content, tags):
        tweet_new = self.helper.create_tweet(username, content, tags)
        return tweet_new

    def remove_tweet(self, tweet_id):
        self.helper.remove_tweet(tweet_id)

    def edit_tweet(self, tweet_id, new_content, new_tags):
        self.helper.edit_tweet(tweet_id, new_content, new_tags)
