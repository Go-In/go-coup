"""go_coup URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from . import views

app_name = 'store'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^currency/add/$', views.currencyRegister, name='currency-register'),
    url(r'^add/$', views.ticketRegister, name='ticket-register'),
    url(r'^create-qr/$', views.createQr, name='create-qr'),
    url(r'^(?P<ticket_id>[0-9]+)/edit/$', views.ticketEdit, name='ticket-edit'),
    url(r'^(?P<ticket_id>[0-9]+)/delete/$', views.ticketDelete, name='ticket-delete'),
    url(r'^(?P<ticket_id>[0-9]+)/dashboard/$', views.ticketDashboard, name='ticket-dashboard'),
    url(r'^dashboard/$', views.dashboard, name='dashboard'),
    url(r'^get-coupon/(?P<customer>.+)/(?P<key>.+)/$', views.getCoupon, name='get-coupon'),
]
