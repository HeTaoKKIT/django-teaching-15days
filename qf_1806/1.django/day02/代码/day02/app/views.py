from django.shortcuts import render
from django.http import HttpResponse

from app.models import Student


def hello(request):
    return HttpResponse('你好，千锋')


def create_stu(request):
    # 第一种方式: 创建学生
    # stu = Student()
    # stu.s_name = '小李'
    # stu.s_age = 20
    # # 保存到数据库中
    # stu.save()
    # 第二种方式:
    # Student.objects.create(s_name='小明')
    Student.objects.create(s_name='小花')
    Student.objects.create(s_name='莉哥')
    Student.objects.create(s_name='大锤')
    Student.objects.create(s_name='小锤')
    Student.objects.create(s_name='温婉')
    Student.objects.create(s_name='张三')

    return HttpResponse('创建成功')


def sel_stu(request):
    # 实现查询
    # all()查询所有对象信息
    stus = Student.objects.all()
    # filter() 过滤
    stus = Student.objects.filter(s_name='小明')
    # first() 获取第一个
    # last() 获取最后一个
    stus = Student.objects.filter(s_age=20).first()
    # get() 获取对象，容易出错
    # stus = Student.objects.get(s_age=20)
    # 查询年龄等于20，性别是女的学生信息
    stus = Student.objects.filter(s_age=20).filter(s_gender=0)
    stus = Student.objects.filter(s_age=20, s_gender=0)

    # 模糊查询 like '%xxx%' 'x%'  '%x'
    stus = Student.objects.filter(s_name__contains='锤')
    stus = Student.objects.filter(s_name__startswith='小')
    stus = Student.objects.filter(s_name__endswith='小')

    # 大于 gt/gte  小于 lt/lte
    stus = Student.objects.filter(s_age__gt=18)
    stus = Student.objects.filter(s_age__gte=18)
    stus = Student.objects.filter(s_age__lte=18)

    # 排序 order_by()
    # 升序
    stus = Student.objects.order_by('id')
    # 降序
    stus = Student.objects.order_by('-id')

    # 查询不满足条件的数据 exclude()
    stus = Student.objects.exclude(s_age=18)

    # 计算统计的个数: count()， len()
    stus_count = stus.count()
    print(stus_count)

    # values()
    stus_values = stus.values()

    # id=pk
    stus = Student.objects.filter(id=2)
    stus = Student.objects.filter(pk=2)

    stu_names = [stu.s_name for stu in stus]
    print(stu_names)
    return HttpResponse('查询成功')