from django.conf.urls import url, include
from django.contrib import admin

from . import views

app_name = 'index'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^detail/(?P<ticket_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^cart/$', views.cart, name='cart'),
    url(r'^catalog/$', views.catalog, name='catalog'),
    url(r'^search-demo/$', views.searchDemo, name='search-demo'),
    url(r'^get-point/(?P<store>.+)/(?P<key>.+)/$', views.getPoint, name='get-point'),
    url(r'^sw.js', views.sw, name='service-worker'),
]
