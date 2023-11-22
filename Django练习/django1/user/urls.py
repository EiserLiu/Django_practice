from django.urls import *
from user.views import *

#子路由


urlpatterns = [
    #路由url
    path('index/',index,name='index'),
    path('index/',index2),
    path('users/',get_user,name = 'users')
]