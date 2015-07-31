from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^test$', views.test),
    url(r'^add$', views.add),
    url(r'^fetch$', views.fetch)
]