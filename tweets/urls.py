from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^tweets$', views.tweets),
    url(r'^tweets/fetch$', views.fetch_tweet),
    url(r'^authors$', views.authors),
    url(r'^authors/fetch$', views.fetch_author),
    url(r'^test$', views.test)
]
