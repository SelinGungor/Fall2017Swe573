from django.conf.urls import url, include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^contact', views.contact, name='contact'),
    url(r'^deepyou', views.analyse, name='analyse'),
    url(r'^settings.STATIC_URL + "deepyou.png"', views.show_graph, name='show_graph'),
]
