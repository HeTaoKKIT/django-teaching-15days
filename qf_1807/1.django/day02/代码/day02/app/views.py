from django.shortcuts import render
from django.http import HttpResponse

# 引入学生Student模型
from app.models import Student


def add_stu(request):
    # 向数据库中的student表中插入数据
    # 第一种方式进行创建: save()
    # stu = Student()
    # stu.name = '小明'
    # 向数据库中插入一条数据
    # stu.save()

    # 第二种方式
    Student.objects.create(name='美女', age=19)

    return HttpResponse('创建成功')


def del_stu(request):
    # 实现删除
    # sql: delete from student where name='大锤';
    # 1. 查询name=‘大锤’的信息
    # Student.objects.filter(name='大锤').delete()
    stus = Student.objects.filter(name='大锤')
    stus.delete()

    return HttpResponse('删除成功')


def up_stu(request):
    # 实现更新
    # 第一种方式
    # stus = Student.objects.filter(name='小明')
    # # # 获取小明对象
    # stu = stus[0]
    stu = Student.objects.filter(name='小明').first()
    # # 获取小明对象
    stu.name = '大明'
    stu.save()
    # 第二种方式
    # Student.objects.filter(name='大明').update(name='莉哥')


    return HttpResponse('更新成功')





