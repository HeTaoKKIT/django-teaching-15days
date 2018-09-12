from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from app.models import Student


def index(request):
    if request.method == 'GET':
        stus = Student.objects.all()

        return render(request, 'stus.html', {'students': stus})
        # return render(request, 'index.html', {'students': stus})
        # return HttpResponse('hello')


def del_stu(request, s_id):
    if request.method == 'GET':
        # 删除方法
        # 1. 获取url中的id值
        # id = request.GET.get('id')
        # 2. 获取id对应的学生对象
        stu = Student.objects.get(pk=s_id)
        # 3. 对象.delete()
        stu.delete()
        return HttpResponseRedirect(reverse('app:index'))
        # return HttpResponseRedirect('/app/stu/')

