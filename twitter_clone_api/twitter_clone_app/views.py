from rest_framework.views import APIView
from rest_framework.response import Response

from grpc_client.client.client import Client


class GetAllTweets(APIView):
    client = Client()

    def get(self, request):
        all_tweets = self.client.get_all_tweets()
        return Response(all_tweets)
