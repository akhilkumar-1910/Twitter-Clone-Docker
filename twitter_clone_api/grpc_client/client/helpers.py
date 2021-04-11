class Helper():

    def __init__(self):
        pass

    def get_all_tweets(self, tweets):
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

    def get_tweets(self, tweets):
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

    def create_tweet(self, tweet):
        tweet_new = {
            "username": tweet.username,
            "content": tweet.content,
            "posted_at": tweet.posted_at.ToDatetime(),
            "last_edited_at": tweet.last_edited_at.ToDatetime(),
            "tags": list(tweet.tag),
        }
        return tweet_new

    def remove_tweet(self, tweet_id):
        pass

    def edit_tweet(self, tweet_id, new_content, new_tags):
        pass
