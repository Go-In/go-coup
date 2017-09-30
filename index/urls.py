from django.conf.urls import url
from django.contrib import admin

from . import views

app_name = 'index'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^detail/(?P<ticket_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^cart/$', views.cart, name='cart'),
    url(r'^login/$', views.login, name='login'),
    url(r'^profile/coupon/$', views.coupon, name='coupon'),
    url(r'^profile/wallet/$', views.wallet, name='wallet'),
    url(r'^profile/setting/$', views.setting, name='setting'),
    url(r'^catalog/$', views.catalog, name='catalog')
]
