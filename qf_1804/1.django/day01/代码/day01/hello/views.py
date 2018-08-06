from django.http import HttpResponse
from django.shortcuts import render


def hello(request):
    if request.method == 'GET':
        return HttpResponse('hello world')

