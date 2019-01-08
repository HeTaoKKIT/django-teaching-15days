from django.db.models import Avg, Max, Min, Sum, Count, Q, F
from django.shortcuts import render
from django.http import HttpResponse

from app.models import Student


def hello(request):
    # 读取数据库
    # 渲染页面
    return HttpResponse('hello world')


def add_stu(request):
    # 实现插入数据
    # 实现的第一种方式
    # Student.objects.create(s_name='小明')
    # 实现的第二种方式
    stu = Student()
    stu.s_name = '小花3'
    stu.s_gender = 1
    stu.save()
    return HttpResponse('创建学生成功')


def del_stu(request):
    # 实现删除
    # 1. 获取删除的对象， filter(条件)
    # 2. 实现删除方法， delete()
    Student.objects.filter(id=3).delete()
    return HttpResponse('删除学生成功')


def up_stu(request):
    # 实现更新
    # 1. 获取更新的数据， filter(条件)
    # 2. 实现更新方法， update()
    # 更新实现的第一种方法
    # Student.objects.filter(id=4).update(s_name='妲己')
    # 更新实现的第二中方法
    stu = Student.objects.filter(id=4).first()
    stu.s_name = '妲己2'
    stu.save()
    return HttpResponse('更新学生成功')


def sel_stu(request):
    # 查询学生信息
    # 查询所有的学生信息, all()
    stus = Student.objects.all()
    for stu in stus:
        print(stu.s_name)
    # 查询id=5的学生信息，filter()
    stu = Student.objects.filter(s_age=20).first()
    print(stu)
    # 1. get()取唯一的一个对象
    # 2. get(条件)条件必须成立
    stu = Student.objects.get(id=6)
    stu = Student.objects.filter(id=6).first()
    print(stu)

    # 过滤出不满足条件的信息
    stus = Student.objects.filter(s_gender=1)
    print(stus)
    stus = Student.objects.exclude(s_gender=0)
    print(stus)

    # 排序order_by
    stus = Student.objects.order_by('id')
    stus = Student.objects.order_by('-id')
    print(stus)

    # 取出对象中的某个字段
    stus = Student.objects.all().values('s_name', 's_age')
    stus = Student.objects.all().values()
    print(stus)

    # 判断查询结果是否存在 exists()
    a = Student.objects.filter(s_name='小张').exists()
    b = Student.objects.filter(s_gender=1).count()
    print(b)

    # 语法: 字段__运算符
    # 包含，模糊查询: contains
    stus = Student.objects.filter(s_name__contains='小明')
    print(stus)
    # like ‘小%’   ‘%明’
    # startswith   endswith
    stus = Student.objects.filter(s_name__startswith='小')
    print(stus)
    stus = Student.objects.filter(s_name__endswith='明')
    print(stus)

    #sql   where id in (1,2,3,4,5,6,7,8)
    stus = Student.objects.filter(id__in=[1,2,3,4,5,6,7,8])
    print(stus)
    stus = Student.objects.filter(pk__in=[1,2,3,4,5,6,7,8])
    print(stus)

    # gte gt lt lte
    stus = Student.objects.filter(s_age__gte=18, s_age__lt=20)
    stus = Student.objects.filter(s_age__gte=18).filter(s_age__lt=20)
    print(stus)

    # 聚合 Avg Max Min Sum Count
    age_avg = Student.objects.all().aggregate(Avg('s_age'))
    age_sum = Student.objects.all().aggregate(Sum('s_age'))
    print(age_avg)
    print(age_sum)

    # 查询年龄大于等于18且小于20
    stus = Student.objects.filter(s_age__gte=18, s_age__lt=20)
    # 查询年龄大于等于18或小于20, Q()
    stus = Student.objects.filter(Q(s_age__gte=18) | Q(s_age__lt=20))
    stus = Student.objects.filter(Q(s_age__gte=18) & Q(s_age__lt=20))
    stus = Student.objects.filter(~Q(s_age__gte=18))
    print(stus)
    # 查询物理成绩大于数学成绩的学生
    stus = Student.objects.all()
    for stu in stus:
        if(stu.wuli > stu.math):
            print(stu.s_name)

    stus = Student.objects.filter(wuli__gt=F('math') + 10)
    print(stus)
    return HttpResponse('查询所有学生信息')
