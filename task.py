from django.utils import timezone
import datetime
import os, sys

PROJECT_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__)))
sys.path += [PROJECT_PATH]
os.environ['DJANGO_SETTINGS_MODULE'] = 'Switter.settings'

from api.models import Tweet

def task():
    t = Tweet.objects.filter(is_deployed__exact=False).first()
    t.created_at = timezone.now()
    t.is_deployed = True
    t.save()
    print('Tweet has been deployed')
    print(t.created_at.astimezone(timezone.get_current_timezone()).ctime())


if __name__ == '__main__':
    task()