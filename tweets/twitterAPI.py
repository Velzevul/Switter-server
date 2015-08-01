from django.utils import timezone
import tweepy
import pytz


# TODO: move to a config file somewhere
consumer_secret = '4GqRwgTxdH744MMAC1lIcksqAP6bbrZ9QHgAJfWH3e9Uue5Clf'
consumer_key = '3gPH91dVKQyPIviaSmi6Jy5TK'
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
api = tweepy.API(auth)


def get_tweet(tweet_id):
    def build_author(data):
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
            'author': build_author(data.author),
            'favorite_count': data.favorite_count,
            'text': data.text
        }

    # TODO: handle API query limitations
    api_data = api.get_status(tweet_id)

    if hasattr(api_data, 'retweeted_status'):
        context = api_data.retweeted_status
        retweet = build_tweet(api_data)
        retweet['retweet_of_id'] = context.id_str
    else:
        context = api_data
        retweet = None

    tweet = build_tweet(context)
    tweet['retweeted_by'] = []

    retweets = context.retweets()

    for rt in retweets:
        rt_author = build_author(rt.author)
        tweet['retweeted_by'].append(rt_author)

    return {
        'tweet': tweet,
        'retweet': retweet
    }
