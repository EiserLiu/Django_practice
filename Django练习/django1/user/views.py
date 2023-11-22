from django.shortcuts import render
from django.http import HttpResponse

from user.models import *


def index(request):
    pass
    # 返回响应
    # 返回对应response
    # return HttpResponse('Hello Django!')
    # 渲染模版
    return render(request, 'index.html')


def index2(request):
    return HttpResponse("index2")


def get_user(request):
    # 获取所有的用户
    users = UserModel.objects.all()
    return render(request, 'users.html', {'users': users})
