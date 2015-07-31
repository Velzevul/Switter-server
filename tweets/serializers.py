from rest_framework import serializers
from .models import Author, Tweet


class AuthorSerializer(serializers.Serializer):
    screen_name = serializers.CharField()
    name = serializers.CharField()
    profile_image_url = serializers.URLField()

    def create(self, validated_data):
        return Author.objects.create(**validated_data)


class TweetSerializer(serializers.Serializer):
    id = serializers.CharField()
    created_at = serializers.DateTimeField()
    favorite_count = serializers.IntegerField(allow_null=True)
    retweet_count = serializers.IntegerField(allow_null=True)
    text = serializers.CharField(allow_null=True)

    def create(self, validated_data):
        return Tweet.objects.create(**validated_data)