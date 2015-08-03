from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.get),
    url(r'^create$', views.create),
    url(r'^fetch$', views.fetch),
    url(r'^test$', views.test)
]
