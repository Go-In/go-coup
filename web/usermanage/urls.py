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

app_name = 'user'
LOGIN_URL = 'login'
LOGOUT_URL = 'logout'
LOGIN_REDIRECT_URL = 'home'
SOCIAL_AUTH_FACEBOOK_KEY = '504951239878757'  # App ID
SOCIAL_AUTH_FACEBOOK_SECRET = 'd6e8030eb8a53f82a34c169139993bd4' # App Secret

urlpatterns = [
    url(r'^register/$', views.customerRegister, name='customer-register'),
    url(r'^store-register/$', views.storeRegister, name='store-register'),
    url(r'^login/$',views.singin, name='login'),
    url(r'^logout/$',views.signout, name='logout'),
    url(r'^tempprofile/$',views.profile, name='profile'),
    url(r'^profile/$',views.customerProfile, name='customer-profile'),
    url(r'^coupon/$',views.customerCoupon, name='customer-coupon'),
    url(r'^wallet/$',views.customerWallet, name='customer-wallet'),
    url(r'^customertest/$',views.customertest, name='customertest'),
    url(r'^storetest/$',views.storetest, name='storetest'),
    url(r'^setting/$',views.customerSetting, name='customer-setting'),
]
