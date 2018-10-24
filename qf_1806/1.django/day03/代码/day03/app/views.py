from django.db.models import Q, F
from django.shortcuts import render
from django.http import HttpResponse

from app.models import Student, StudentInfo, Grade


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

    # 或条件
    # == ===
    # Q()， alt+enter
    stus = Student.objects.filter(Q(s_age=20) | Q(s_gender=0))
    # 且条件
    stus = Student.objects.filter(Q(s_age=20) & Q(s_gender=0))
    # 非条件 ~
    stus = Student.objects.filter(~Q(s_age=20))

    # 查询语文成绩比数学成绩大的学生信息
    stus = Student.objects.filter(yuwen__gt=F('shuxue') + 10)

    stu_names = [stu.s_name for stu in stus]
    print(stu_names)
    return HttpResponse('查询成功')


def del_stu(request):
    # 实现删除
    Student.objects.filter(s_name='小明').delete()
    return HttpResponse('删除成功')


def update_stu(request):
    # 实现更新
    # 第一种
    # stu = Student.objects.filter(s_name='莉哥').first()
    # Student.objects.get(s_name='莉哥')
    # stu.s_name = '王五'
    # stu.save()
    # 第二种
    Student.objects.filter(s_name='王五').update(s_name='莉哥')

    return HttpResponse('修改成功')


def all_stu(request):
    # 获取所有学生信息
    stus = Student.objects.all()
    # 返回页面
    data = {'students':stus}
    return render(request, 'stus.html', data)


def add_info(request):
    # method 获取请求HTTP方式
    if request.method == 'GET':
        return render(request, 'info.html')

    if request.method == 'POST':
        # 获取页面中提交的手机号码和地址，并保存
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        stu_id = request.GET.get('stu_id')
        # 保存
        StudentInfo.objects.create(phone=phone,
                                   address=address,
                                   stu_id=stu_id)
        return HttpResponse('创建扩展表信息成功')


def sel_info_by_stu(request):
    if request.method == 'GET':
        # 通过学生查询扩展表信息
        stu = Student.objects.get(s_name='小明')
        # 第一种
        info = StudentInfo.objects.filter(stu_id=stu.id)
        info = StudentInfo.objects.filter(stu=stu)

        # 第二种, 学生对象.关联的模型名的小写
        info = stu.studentinfo

        return HttpResponse('通过学生查找拓展表信息')


def sel_stu_by_info(request):
    if request.method == 'GET':
        # 知道手机号码1388009453，找人
        info = StudentInfo.objects.get(phone='1388009453')
        student = info.stu
        print(student)
        return HttpResponse('通过手机号码查找学生的信息')


def add_grade(request):
    if request.method == 'GET':
        names = ['物联网', '计科', '外语']
        for name in names:
            Grade.objects.create(g_name=name)
        return HttpResponse('创建班级成功')


def sel_stu_grade(request):
    if request.method == 'GET':
        # 1. 通过学生查找班级
        stu = Student.objects.filter(s_name='小明').first()
        grade = stu.grade
        # 2. 通过班级查找学生
        grade = Grade.objects.get(g_name='外语')
        students = grade.student_set.filter(s_gender=0).all()
        return HttpResponse('查询学生和班级信息')
