from django.utils.dateparse import parse_datetime
from django.views.decorators.http import require_POST, require_GET
from django.views.decorators.csrf import csrf_exempt
from jsonview.decorators import json_view
from json import loads
from .twitterAPI import get_tweet
from .models import Tweet, Author


@json_view
def test(request):
    return {'status': 'OK'}


@json_view
@require_GET
def get(request):
    tweets = Tweet.objects.all()
    return [tweet.serialize() for tweet in tweets]


@csrf_exempt
@require_POST
@json_view
def fetch(request):
    tweet_id = request.POST['tweet_id']
    return get_tweet(tweet_id)


@csrf_exempt
@require_POST
@json_view
def create(request):
    def store_author(data):
        try:
            author = Author.objects.get(pk=data['screen_name'])
        except Author.DoesNotExist:
            author = Author.objects.create(
                screen_name=data['screen_name'],
                name=data['name'],
                profile_image_url=data['profile_image_url']
            )

        return author

    def store_tweet(data):
        try:
            tweet = Tweet.objects.get(pk=data['id'])
        except Tweet.DoesNotExist:
            tweet = Tweet(
                id=data['id'],
                created_at=parse_datetime(tweet_data['created_at']),
                favorite_count=data['favorite_count'],
                text=data['text']
            )

            author = store_author(data['author'])
            tweet.author = author
            tweet.save()

        return tweet

    tweet_data = loads(request.POST['tweet_data'])
    tweet = store_tweet(tweet_data)

    if 'retweeted_by' in tweet_data.keys():
        for rt_author_data in tweet_data['retweeted_by']:
            rt_author = store_author(rt_author_data)
            tweet.retweeted_by.add(rt_author)

        tweet.save()

    if 'retweet_of_id' in tweet_data.keys():
        try:
            original_tweet = Tweet.objects.get(pk=tweet_data['retweet_of_id'])
            tweet.original_tweet = original_tweet
            tweet.save()

            retweet_author_names = [author.screen_name for author in original_tweet.retweeted_by.all()]
            if tweet.author.screen_name not in retweet_author_names:
                original_tweet.retweeted_by.add(tweet.author)
                original_tweet.save()
        except Tweet.DoesNotExist:
            return {'status': 'Cannot find original tweet for the retweet. Please, save the original tweet before saving retweet'}, 500

    return {'status': 'OK'}
