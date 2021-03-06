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
from django.contrib import admin
from django.contrib.auth import views as auth_views

# LOGIN_URL = 'login'
# LOGOUT_URL = 'logout'
# LOGIN_REDIRECT_URL = 'home'

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('index.urls', namespace='index')),
    url(r'^user/',include('usermanage.urls', namespace='user')),
    url(r'^store/',include('storemanage.urls', namespace='store')),
    url(r'^customer/',include('customermanage.urls', namespace='customer')),
    url(r'^shopping/',include('market.urls', namespace='market')),
    url(r'^search/', include('haystack.urls')),
    url(r'^oauth/', include('social_django.urls', namespace='social')),

]
