from django.conf.urls import url
from django.contrib import admin

from . import views

app_name = 'index'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^detail/$', views.detail, name='detail'),
    url(r'^profile/$', views.profile, name='profile'),
    url(r'^cart/$', views.cart, name='cart'),
    url(r'^coupon/$', views.coupon, name='coupon'),
    url(r'^wallet/$', views.wallet, name='wallet'),
    url(r'^setting/$', views.setting, name='setting')
]
