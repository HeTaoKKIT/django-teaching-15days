from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render

from app.models import Student


def create_stu(request):
    # 创建学生信息
    # 引入ORM概念：对象关系映射
    # 第一种方式
    # Student.objects.create(s_name='小花1')
    # 第二种
    # stu = Student()
    # stu.s_name = '小龙'
    # stu.save()
    # 第三种
    stu = Student('小草', 18, 1)
    stu.save()

    return HttpResponse('创建学生方法')


def select_stu(request):
    """
    all：所有
    filter: 获取的结果为queryset，可以返回空，或一条或多条数据
    get：获取的结果是object对象，如果获取不成功，会报错，如果获取的参数超多一条，也会报错
    exclude：不包含
    """
    # 查询数据
    # select * from app_student;
    stus = Student.objects.all()
    # select * from xxx where s_name='小花';
    stus = Student.objects.filter(s_name='小花')
    # filter(): 查询年龄等于19的学生
    stus = Student.objects.filter(s_age=28)
    # get(): 查询年龄等于19的学生
    # stus = Student.objects.get(s_age=19)
    stus = Student.objects.filter(id=100)
    # 多条件查询
    # 年龄等于19，姓名等于小花
    stus = Student.objects.filter(s_age=19).filter(s_name='小花')
    stus = Student.objects.filter(s_age=19, s_name='小花')
    # 查询姓名不等于小花的学生信息
    stus = Student.objects.exclude(s_name='小花')
    # 排序，按照id升序/降序===> asc/desc
    stus = Student.objects.all().order_by('id')
    stus = Student.objects.all().order_by('-id')

    # values()
    stus = Student.objects.all().values('id', 's_name', 's_age')
    # get(),first()
    # stus = Student.objects.get(id=100)
    stus = Student.objects.filter(id=100).first()
    # first()/last()
    stus = Student.objects.all().order_by('id').last()
    stus = Student.objects.all().order_by('-id').first()
    stus = Student.objects.all().order_by('-id')[10:]
    # return HttpResponse(stus.id)
    # 查询名字中带有花的学生的信息
    # select * from xxx where name like '%花%'
    stus = Student.objects.filter(s_name__contains='花')
    # select * from xxx where name like '花%'
    stus = Student.objects.filter(s_name__startswith='花')
    # select * from xxx where name like '%花'
    stus = Student.objects.filter(s_name__endswith='花')
    # in
    stus = Student.objects.filter(id__in=[1,2,3])
    # 年龄大于18
    stus = Student.objects.filter(s_age__gt=18)
    # pk
    stus = Student.objects.filter(id=1)
    stus = Student.objects.filter(pk=1)

    # Q(),查询姓名叫小花的，或者年龄等于18.或使用 |
    stus = Student.objects.filter(Q(s_name='小花') | Q(s_age=18))
    stus = Student.objects.filter(Q(s_name='小花') & Q(s_age=18))
    # 非，姓名不叫小花的，或者年龄等于18的
    stus = Student.objects.filter(~Q(s_name='小花') | Q(s_age=18))


    # 获取学生的姓名
    stu_names = [(stu.s_name,stu.id) for stu in stus]
    print(stu_names)
    names = []
    for i in stus:
        names.append(i.s_name)
    print(names)
    return HttpResponse(stu_names)


def delete_stu(request):
    # 删除
    # stu = Student.objects.get(pk=5)
    # stu = Student.objects.filter(pk=3).first()
    # stu.delete()

    Student.objects.filter(id=2).first().delete()
    return HttpResponse('删除')


def update_stu(request):
    # 更新
    # 第一种
    stu = Student.objects.get(pk=1)
    stu.s_name = '帅哥'
    stu.save()
    # 第二种
    Student.objects.filter(id=1).update(s_name='哈哈')
    return HttpResponse('修改')
