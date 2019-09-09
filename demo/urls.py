"""demo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# 路由匹配的规则，从上到下
from django.contrib import admin
from django.urls import path,re_path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.about),
    path('index/', views.index),
    path('about/', views.about),
    re_path(r'^$', views.index),
    re_path(r'urltest/(\d)', views.urltest),
    # re_path(r'urltestnew/(\d{4})/(\w+)', views.urltestnew),
    re_path(r'urltestnew/(?P<year>\d{4})/(?P<city>\w+)', views.urltestnew),
    path('gethtml/',views.gethtml),

    path('indextmp/',views.indextmp),
    path('abc/',views.abc),
    path('hello/',views.hello),
    path('tpltest/',views.tpltest),
    re_path('tpltest/(\d+)',views.tpltest),
    path('statictest/',views.statictest),
    path('staticdemo/',views.staticdemo),
]