from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^tweets$', views.tweets),
    url(r'^tweets/(?P<tweet_id>[0-9]+)$', views.tweet),
    url(r'^locks$', views.locks),
    url(r'^locks/(?P<tweet_id>[0-9]+)$', views.lock),
    url(r'^users$', views.users),
    url(r'^users/(?P<screen_name>.+)$', views.user)
]
