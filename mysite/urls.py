"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from mysite.views import here, math, meta, welcome, get_c, set_c, session_S, login, index, logout, register
#from views import here
#mysite 是指子mysite
from restaurants.views import menu, list_restaurants, foods, comment

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^here/$', here),
    #\{1,2}代表匹配 1 or 2 個數字
    #小括號中的字->參數 (2~n+1)個參數 第1個參數為HttpRequest
    url(r'^(\d{1,2})/plus/(\d{1,2})/$', math),
    url(r'^menu/$', menu),
    url(r'^meta/$', meta),
    url(r'^welcome/$', welcome),
    url(r'^restaurants_list/$', list_restaurants),
    url(r'^foods/$', foods),
    url(r'^comment/(\d{1,5})/$', comment),
    url(r'^get_cookies/$', get_c),
    url(r'^set_cookies/$', set_c),
    url(r'^session/$', session_S),
    url(r'^accounts/login/$', login),
    url(r'^accounts/logout/$', logout),
    url(r'^accounts/register/$', register),
    url(r'^index/$', index),
]
