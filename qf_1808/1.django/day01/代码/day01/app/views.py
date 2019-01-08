from django.shortcuts import render
from django.http import HttpResponse


def hello(request):
    # 读取数据库
    # 渲染页面
    return HttpResponse('hello world')
