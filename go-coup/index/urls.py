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
    url(r'^pfai/(?P<store_id>[0-9]+)/$', views.store, name='store'),
    url(r'^brand-list/$', views.brand_list, name='brand_list'),
]