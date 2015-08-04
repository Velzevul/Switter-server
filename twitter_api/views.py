
from django.utils import timezone
import tweepy
import pytz
from rest_framework.decorators import api_view
from rest_framework.response import Response


# TODO: move to a config file somewhere
consumer_secret = '4GqRwgTxdH744MMAC1lIcksqAP6bbrZ9QHgAJfWH3e9Uue5Clf'
consumer_key = '3gPH91dVKQyPIviaSmi6Jy5TK'
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
api = tweepy.API(auth)


def build_user(data):
    return {
        'screen_name': data.screen_name,
        'name': data.name,
        'profile_image_url': data.profile_image_url
    }

def build_tweet(data):
    return {
        'id': data.id_str,
        'created_at': pytz\
            .timezone(timezone.get_current_timezone_name())\
                .localize(data.created_at),
        'author': build_user(data.author),
        'favorite_count': data.favorite_count,
        'text': data.text
    }


@api_view(['GET'])
def user(request, screen_name):
    api_data = api.get_user(screen_name)
    author = build_user(api_data)
    return Response(author)


@api_view(['GET'])
def tweet(request, id):
    # TODO: handle API query limitations
    api_data = api.get_status(id)
    tweet = build_tweet(api_data)

    if hasattr(api_data, 'retweeted_status'):
        retweeted_status = build_tweet(api_data.retweeted_status)
        tweet['retweet_of'] = retweeted_status
        context = api_data.retweeted_status
        target = retweeted_status
    else:
        context = api_data
        target = tweet

    retweets = context.retweets()
    target['retweeted_by'] = [build_user(rt.author) for rt in retweets]

    return Response(tweet)
