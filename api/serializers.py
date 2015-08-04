from rest_framework import serializers
from .models import Author, Tweet


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author


class TweetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tweet


class OriginalTweetSerializer(serializers.ModelSerializer):
    author = AuthorSerializer()
    retweeted_by = AuthorSerializer(many=True)

    class Meta:
        model = Tweet


class TweetNestedSerializer(serializers.ModelSerializer):
    author = AuthorSerializer()
    retweeted_by = AuthorSerializer(many=True)
    retweeted_status = OriginalTweetSerializer()

    class Meta:
        model = Tweet
