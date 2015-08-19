from django.utils import timezone
from datetime import datetime
from random import random
import os, sys

PROJECT_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__)))
sys.path += [PROJECT_PATH]
os.environ['DJANGO_SETTINGS_MODULE'] = 'Switter.settings'

from api.models import Tweet


def task():
    t = Tweet.objects.filter(is_deployed__exact=False).first()
    non_deployed_tweets_left = Tweet.objects.filter(is_deployed__exact=False).count()
    if t is None:
        print('{0}: No more tweets to deploy!'.format(datetime.now().ctime()))
    else:
        chance = random()
        threshold = 0.6
        if chance > threshold:
            t.created_at = timezone.now()
            t.is_deployed = True
            t.save()
            non_deployed_tweets_left -= 1
            print('{0}: Tweet {1} has been deployed. Non-deployed tweets left: {2}'.format(datetime.now().ctime(), t.id, non_deployed_tweets_left))
            # for JSON return, that's how to get the time in the current (correct) timezone:
            # t.created_at.astimezone(timezone.get_current_timezone()).ctime()
        else:
            print('{0}: Chance check failed, not deploying. Non-deployed tweets left: {1}'.format(datetime.now().ctime(), non_deployed_tweets_left))



if __name__ == '__main__':
    task()