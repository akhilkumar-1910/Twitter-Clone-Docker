import grpc
from grpc_client.proto.twitter_clone_pb2 import Tweet
from grpc_client.proto.twitter_clone_pb2_grpc import TweetServiceStub


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
            return self.all_tweets
        except grpc.RpcError as e:
            if e.code() == grpc.StatusCode.UNAVAILABLE:
                print("grpc server unavailable")
                return self.all_tweets

    def get_tweets(self, username):
        tweet = Tweet(username=username)
        try:
            tweets = self.stub.GetTweets(tweet)
            self.all_tweets = [tweet for tweet in tweets]
            return self.all_tweets
        except grpc.RpcError as e:
            if e.code() == grpc.StatusCode.UNAVAILABLE:
                print("grpc server unavailable")
                return self.all_tweets

    def create_tweet(self, username, content, tags):
        tweet = Tweet(
            username=username,
            content=content,
        )
        for tag in tags:
            tweet.tag.append(tag)
        try:
            tweet_new = self.stub.CreateTweet(tweet)
            return tweet_new
        except grpc.RpcError as e:
            if e.code() == grpc.StatusCode.UNAVAILABLE:
                print("grpc server unavailable")
                return tweet
            else:
                print("Here in else")
                print(e.code())
                print(e.details())
                return tweet

    def remove_tweet(self, tweet_id):
        tweet = Tweet(
            id=tweet_id
        )
        try:
            tweet_to_remove = self.stub.RemoveTweet(tweet)
            return tweet_to_remove
        except grpc.RpcError as e:
            if e.code() == grpc.StatusCode.UNAVAILABLE:
                print("grpc server unavailable")
                return tweet
            else:
                print(e.code())
                print(e.details())
                return tweet

    def edit_tweet(self, tweet_id, new_content, new_tags):
        tweet = Tweet(
            id=tweet_id,
            content=new_content,
        )
        for tag in new_tags:
            tweet.tag.append(tag)
        try:
            tweet_to_edit = self.stub.EditTweet(tweet)
            return tweet_to_edit
        except grpc.RpcError as e:
            if e.code() == grpc.StatusCode.UNAVAILABLE:
                print("grpc server unavailable")
                return tweet
            else:
                print(e.code())
                print(e.details())
                return tweet

    def __del__(self):
        self.channel.close()
