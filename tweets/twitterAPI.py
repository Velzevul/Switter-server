from django.utils import timezone
import tweepy
import pytz


# TODO: move to a config file somewhere
consumer_secret = '4GqRwgTxdH744MMAC1lIcksqAP6bbrZ9QHgAJfWH3e9Uue5Clf'
consumer_key = '3gPH91dVKQyPIviaSmi6Jy5TK'
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
api = tweepy.API(auth)


def get_tweet(tweet_id):
    # TODO: handle API query limitations

    print(tweet_id)
    api_data = api.get_status(tweet_id)

    if hasattr(api_data, 'retweeted_status'):
        context = api_data.retweeted_status
        retweet = {
            'id': api_data.id_str,
            'created_at': pytz\
                .timezone(timezone.get_current_timezone_name())\
                .localize(api_data.created_at),
            'author': {
                'screen_name': api_data.author.screen_name,
                'name': api_data.author.name,
                'profile_image_url': api_data.author.profile_image_url
            }
        }
    else:
        context = api_data
        retweet = None

    tweet = {
        'id': context.id_str,
        'created_at': pytz\
            .timezone(timezone.get_current_timezone_name())\
            .localize(context.created_at),
        'author': {
            'screen_name': context.author.screen_name,
            'name': context.author.name,
            'profile_image_url': context.author.profile_image_url
        },
        'favorite_count': context.favorite_count,
        'text': context.text,
        'retweeted_by': []
    }

    retweets = context.retweets()

    for rt in retweets:
        tweet['retweeted_by'].append({
            'screen_name': rt.author.screen_name,
            'name': rt.author.name,
            'profile_image_url': rt.author.profile_image_url
        })

    return {
        'tweet': tweet,
        'retweet': retweet
    }

#
# def store_retweet(retweet_id):
#     retrieved_retweet = api.get_status(retweet_id)
#     created_at_tz = pytz.timezone(timezone.get_current_timezone_name()).localize(retrieved_retweet.created_at)
#     retweet = Tweet(
#         id=retweet_id,
#         created_at=created_at_tz
#     )
#     author_screen_name = retrieved_retweet.author.screen_name
#
#     try:
#         author = Author.objects.get(pk=author_screen_name)
#     except Author.DoesNotExist:
#         author = Author(
#             screen_name=retrieved_retweet.author.screen_name,
#             name=retrieved_retweet.author.name,
#             profile_image_url=retrieved_retweet.author.profile_image_url
#         )
#         author.save()
#
#     retweet.author = author
#     retweet.save()
#
#     return retweet
#
#
# def store(tweet_id, retweet_id=None):
#     original_tweet_exists = False;
#
#     try:
#         tweet = Tweet.objects.get(pk=tweet_id)
#         original_tweet_exists = True
#     except Tweet.DoesNotExist:
#         tweet = store_tweet(tweet_id)
#
#     if retweet_id is not None:
#         try:
#             retweet = Tweet.objects.get(pk=retweet_id)
#         except Tweet.DoesNotExist:
#             retweet = store_retweet(retweet_id)
#
#         if original_tweet_exists:
#             tweet.retweet_authors.add(retweet.author)
#             tweet.retweet_count += 1
#             tweet.save()
#
#         retweet.original_tweet = tweet
#         retweet.save()
