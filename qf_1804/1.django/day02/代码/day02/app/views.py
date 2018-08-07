from django.http import HttpResponse
from django.shortcuts import render

from app.models import Student


def hello(request):
    if request.method == 'GET':
        return HttpResponse('hello world')


def selStu(request):
    if request.method == 'GET':
        # sql = 'select * from student'
        stus = Student.objects.all()
        stus_list = []
        for stu in stus:
            s = {
                's_name': stu.s_name,
                's_age': stu.s_age
            }
            stus_list.append(s)
        return HttpResponse(stus_list)


def filterStu(request):
    if request.method == 'GET':
        # 查询年龄等于15的学生， filter()
        stus = Student.objects.filter(s_age=15)
        # 查询年龄不等于15的学生， exclude()
        stus = Student.objects.exclude(s_age=15)
        # 排序, 按照id降序
        stus = Student.objects.all().order_by('-id')
        # 升序
        stus = Student.objects.all().order_by('id')
        # values
        stus = Student.objects.all().values()
        # 获取id为1的信息
        stus = Student.objects.filter(id=1)
        stus = Student.objects.get(id=1)
        stus = Student.objects.get(pk=1)
        # get获取不到数据会直接报错, filter获取不到数据是返回空
        # stus = Student.objects.get(pk=5)
        stus = Student.objects.filter(id=5)
        # get只能返回一个数据，返回多个会报错
        # stus = Student.objects.get(s_age=15)
        # 获取所有学生(按照id降序)中第一个学生信息
        stus = Student.objects.all().order_by('-id')[0]
        stus = Student.objects.all().order_by('-id').first()
        # 获取所有学生(按照id降序)中最后一个学生信息
        stus = Student.objects.all().order_by('-id').last()

        # 模糊查询姓名， like '%小%'， like '小%'，like '%小'
        stus = Student.objects.filter(s_name__contains='小')
        stus = Student.objects.filter(s_name__startswith='小')
        stus = Student.objects.filter(s_name__endswith='小')

        # gt:大于 gte：大于等于   lt：小于  lte：小于等于
        stus = Student.objects.filter(s_age__gt=16)
        stus = Student.objects.filter(s_age__gte=16)

        # 查询id等于1,2的学生信息,
        # select * from student where id in (1,2)
        stus = Student.objects.filter(id__in=[1,2])

        # 查询姓名中包含小，并且年龄大于17
        stus = Student.objects.filter(s_name__contains='小',
                                      s_age__gt=17)

        # 列表推导式 [i for i in xxx]
        stus_list = [stu.to_dict() for stu in stus]
        return HttpResponse(stus_list)
        # return HttpResponse(stus)