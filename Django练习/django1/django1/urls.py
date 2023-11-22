"""
URL configuration for django1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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

from user.views import *
from django.contrib import admin
from django.urls import path,include



urlpatterns = [
    #路由url
    # path('index/',index),
    # path("index2/",index2),

    #使用子路由
    #一个应用对应一个子路由
    path('user/',include('user.urls')),
    path("admin/", admin.site.urls),
]