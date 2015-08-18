from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^tweets/(?P<id>[0-9]+)$', views.tweet),
    url(r'^users/(?P<screen_name>.+)$', views.user)
]
