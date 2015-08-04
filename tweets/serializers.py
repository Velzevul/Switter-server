from rest_framework import serializers
from .models import Author, Tweet


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author


class TweetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tweet

    def create(self, validated_data):
        retweet_authors = []
        if 'retweeted_by' in validated_data.keys():
            retweet_author_ids = validated_data.pop('retweeted_by')
            retweet_authors = Author.objects.in_bulk(retweet_author_ids)

        tweet = Tweet(**validated_data)
        tweet.save()

        for retweet_author in retweet_authors:
            tweet.retweeted_by.add(retweet_author)
            tweet.save()

        return tweet


class OriginalTweetSerializer(serializers.ModelSerializer):
    author = AuthorSerializer()
    retweeted_by = AuthorSerializer(many=True)

    class Meta:
        model = Tweet


class TweetNestedSerializer(serializers.ModelSerializer):
    author = AuthorSerializer()
    retweeted_by = AuthorSerializer(many=True)
    original_tweet = OriginalTweetSerializer()

    class Meta:
        model = Tweet
