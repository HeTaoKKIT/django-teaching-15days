
from django.contrib.auth.models import User, Group, Permission



from django.db.models import Avg, Max, Min, Sum, Count, Q, F
from django.shortcuts import render
from django.http import HttpResponse

from app.models import Student, StudentInfo, Grade, Course


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


def add_stu_info(request):
    # 添加小明的紧急联系人的信息，学号
    stu_info = StudentInfo()
    stu_info.s_no = '123456'
    stu_info.phone = '13551366543'
    stu_info.name = '大明'
    # stu_info.stu = Student.objects.get(id=1)
    stu_info.stu_id = 1
    stu_info.save()
    return HttpResponse('创建拓展信息成功')


def sel_phone_by_stu(request):
    # 1. 查询学生对象
    stu = Student.objects.filter(s_name='小明').first()
    # 2. 通过学生对象查询拓展表信息
    # stu_info = StudentInfo.objects.filter(stu=stu).first()
    stu_info = StudentInfo.objects.filter(stu_id=stu.id).first()
    phone = stu_info.phone
    print(phone)
    return HttpResponse('查询成功')


def sel_phone_by_stu2(request):
    # 1. 查询学生对象
    stu = Student.objects.filter(s_name='小明').first()
    # 2. 反向查询。关联模型对象.关联另外一个模型的名称的小写
    # stu_info = stu.studentinfo
    stu_info = stu.info
    phone = stu_info.phone
    print(phone)
    return HttpResponse('查询成功')


def sel_stu_by_info(request):
    # 1. 查询拓展表信息
    stu_info = StudentInfo.objects.filter(s_no='123456').first()
    # 2. 查询学生对象
    stu = stu_info.stu
    print(stu.s_name)
    return HttpResponse('查询成功')


def on_delete_stu(request):
    # 删除小明的学生信息
    # 效果: 删除主表时，从表是否被删除
    Student.objects.filter(s_name='小花').delete()
    # StudentInfo.objects.filter(stu_id=4).delete()
    return HttpResponse('删除成功')


def add_grade(request):
    # 添加班级信息
    g_names = ['Python1801', 'Python1802', 'Python1803','Python1804']
    for name in g_names:
        Grade.objects.create(g_name=name)
    return HttpResponse('创建班级成功')


def stu_grade(request):
    # 1. 查询id=4的学生对象
    stu = Student.objects.get(pk=4)
    # 2. 设置学生的班级字段
    # stu.g = Grade.objects.get(pk=1)
    stu.g_id = 1
    stu.save()
    return HttpResponse('分配学生班级成功')


def sel_grade_by_stu(request):
    # 1. 查询姓名叫小明22的对象
    stu = Student.objects.filter(s_name='小明22').first()
    grade = stu.g
    print(grade.g_name)
    return HttpResponse('查询成功')


def sel_stu_by_grade(request):
    # 1. 查询班级python1801对象
    grade = Grade.objects.filter(g_name='python1801').first()
    # stus = grade.student_set.all()
    stus = grade.stu.all()
    print(stus)
    return HttpResponse('查询成功')


def add_course(request):
    c_names = ['大学英语', '商务英语', '线代', '高数']
    for name in c_names:
        c = Course()
        c.c_name = name
        c.save()
    return HttpResponse('创建课程成功')


def add_s_c(request):
    # 将大学英语分配给小明22这个学生
    # 1. 查询课程对象
    cou = Course.objects.filter(c_name='大学英语').first()
    # 2. 查询学生对象
    stu = Student.objects.filter(s_name='小明22').first()
    # 3. 加入关联关系
    # stu.course_set.add(cou)
    # stu.cou.add(cou)
    # cou.stu.add(stu)
    stu.cou.remove(cou)

    return HttpResponse('添加中间表信息成功')


def index(request):
    stus = Student.objects.all()
    return render(request, 'index.html', {'a': stus})

