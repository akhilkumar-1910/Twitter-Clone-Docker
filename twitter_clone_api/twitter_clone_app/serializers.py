from rest_framework import serializers


class TweetSerializer(serializers.Serializer):
    username = serializers.CharField()
    content = serializers.CharField()
    tags = serializers.ListField(
        child=serializers.CharField()
    )
