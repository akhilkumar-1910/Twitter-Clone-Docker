from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from grpc_client.client.client import Client
from twitter_clone_app.serializers import TweetSerializer


class GetAllTweets(APIView):
    client = Client()

    def get(self, request):
        all_tweets = self.client.get_all_tweets()
        return Response(all_tweets)


class GetUserTweets(APIView):
    client = Client()

    def get(self, request):
        try:
            username = request.query_params["username"]
        except KeyError:
            return Response(
                {"detail": "username query param is required"},
                status=status.HTTP_400_BAD_REQUEST
            )

        user_tweets = self.client.get_tweets(username)
        return Response(user_tweets)


class CreateEditDeleteTweet(APIView):
    client = Client()

    def post(self, request):
        serializer = TweetSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        data = serializer.data
        tweet = self.client.create_tweet(
            data["username"],
            data["content"],
            data["tags"]
        )
        return Response(tweet, status=status.HTTP_201_CREATED)
