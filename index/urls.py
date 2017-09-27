from django.conf.urls import url
from django.contrib import admin

from . import views

app_name = 'index'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^detail/$', views.detail, name='detail'),
    url(r'^profile/$', views.profile, name='profile')
]
