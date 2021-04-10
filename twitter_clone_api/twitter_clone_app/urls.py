from django.urls import path

from twitter_clone_app.views import GetAllTweets

urlpatterns = [
    path("get-all-tweets/", GetAllTweets.as_view(), name="get_all_tweets"),
]
