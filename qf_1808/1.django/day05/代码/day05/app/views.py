
import uuid

from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse


def index(request, id):
    print(type(id))
    name = '小明'
    a = [89, 76, 46, 98, 100]
    content_h2 = '<h2>天气真好</h2>'
    return render(request,
                  'index.html',
                  {'name': name, 'a': a, 'b': content_h2}
                  )


def get_name(request, name):
    print(type(name))
    return HttpResponse('name:%s' % name)


def get_float(request, num):
    return HttpResponse('float number:%s' % num)


def get_uuid(request):
    uid = str(uuid.uuid4())
    return HttpResponse(uid)


def g_uuid(request, uid):
    return HttpResponse('uuid:%s' % uid)


def get_path(request, path):
    return HttpResponse('path: %s' % path)


def params(request, month, day, year):
    return HttpResponse('%s年%s月%s日' % (year, month, day))


def hindex(request):
    if request.method == 'GET':
        # return HttpResponse('HELLO WORLD')
        # return render()
        # return JsonResponse({'code': 200, 'msg': '请求成功'})
        # return HttpResponseRedirect('/app/index/1/')
        return HttpResponseRedirect(
            reverse('app:index', kwargs={'id': 2})
        )

    if request.method == 'POST':
        pass