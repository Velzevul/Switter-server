from django.utils import timezone
from datetime import datetime
from random import random
import os
import sys

PROJECT_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__)))
sys.path += [PROJECT_PATH]
os.environ['DJANGO_SETTINGS_MODULE'] = 'Switter.settings'

from api.models import Tweet


def task():
    now = datetime.now()
    t = Tweet.objects.filter(is_deployed__exact=False).order_by('?').first()
    non_deployed_tweets_left = Tweet.objects.filter(is_deployed__exact=False).count()
    if t is None:
        print('{0}: No more tweets to deploy!'.format(now.ctime()))
    else:
        if now.hour < 8:
            threshold = 0.85
        elif now.hour < 12:
            threshold = 0.75
        elif now.hour < 16:
            threshold = 0.65
        elif now.hour < 21:
            threshold = 0.75
        else:
            threshold = 0.85

        chance = random()
        if chance > threshold:
            t.created_at = timezone.now()
            t.is_deployed = True
            t.save()
            non_deployed_tweets_left -= 1
            print('{0}: (chance - {1}%) Tweet {2} has been deployed. Non-deployed tweets left: {3}'
                  .format(now.ctime(), threshold*100, t.id, non_deployed_tweets_left))
            # for JSON return, that's how to get the time in the current (correct) timezone:
            # t.created_at.astimezone(timezone.get_current_timezone()).ctime()
        else:
            print('{0}: (chance - {1}%) Chance check failed, not deploying. Non-deployed tweets left: {2}'
                  .format(now.ctime(), threshold*100, non_deployed_tweets_left))


if __name__ == '__main__':
    task()
