from django.urls import path

from twitter_clone_app.views import GetAllTweets, GetUserTweets, CreateEditDeleteTweet

urlpatterns = [
    path("get-all-tweets/", GetAllTweets.as_view(), name="get_all_tweets"),
    path("get-user-tweets/", GetUserTweets.as_view(), name="get_user_tweets"),
    path("create-tweet/", CreateEditDeleteTweet.as_view(), name="create_tweet"),
]
