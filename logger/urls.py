from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^logs$', views.logs),
    url(r'^journals$', views.journals)
]
