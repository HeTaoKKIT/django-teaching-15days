from django.db.models import Avg, Count, Sum, Max, Min, Q, F
from django.shortcuts import render
from django.http import HttpResponse

# 引入学生Student模型
from app.models import Student, StuInfo, Grade, Course


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


def sel_stu(request):
    # 查询
    # 查询年龄等于18的学生信息
    # first()： 获取结果中的第一个
    # last(): 获取结果中的最后一个
    stus = Student.objects.filter(age=18)

    # 查询所有学生
    stus = Student.objects.all()

    # 查询name=xxx的学生信息
    # get(): 获取唯一的满足条件的对象，且查询的条件必须存在
    # 如果查询条件不存在，则报错
    # 如果查询的结果对于一个，则报错
    stu = Student.objects.get(name='大明')

    # 获取不叫大明的学生信息
    stus = Student.objects.exclude(name='大明')

    # 查询年龄等于18且性别为女的学生信息
    stus = Student.objects.filter(age=18).filter(gender=0)
    stus = Student.objects.filter(age=18, gender=0)

    # 排序 order_by,
    # 降序-id，在sql中 id desc
    # 升序id， 在sql中 id asc
    stus = Student.objects.all().order_by('-id')

    # 获取对象的值
    stus_value = Student.objects.all().values()

    # 判断name=妲己的学生存不存在, 存在返回True，不存在返回False
    stu = Student.objects.filter(name='妲己').exists()

    # 查询姓名中包含‘大’的学生信息，
    # contains: 大小写敏感
    # icontains: 大小写不敏感
    # 类似于 like ‘%大%’
    stus = Student.objects.filter(name__contains='大')

    # 类似于 like ‘%大’
    stus = Student.objects.filter(name__endswith='大')

    # 类似于 like ‘大%’
    stus = Student.objects.filter(name__startswith='大')

    # sql : select * from xxx where id in (1,2,3);
    stus = Student.objects.filter(id__in=[1,2,3])
    # pk代表主键
    stus = Student.objects.filter(pk__in=[1,2,3])

    # 大于: __gt__、大于等于: __gte__
    # 小于: __lt__、小于等于：__lte__
    stus = Student.objects.filter(age__lt=19)

    # 查询平均年龄
    stus = Student.objects.all()
    ages = 0
    for stu in stus:
        ages += stu.age
    avg_age = ages / len(stus)
    # 聚合aggregate
    # sql: select count(age), sum(age) from student;
    avg_age = Student.objects.all().aggregate(Avg('age'))
    print(avg_age)
    sum_age = Student.objects.all().aggregate(Sum('age'))
    print(sum_age)

    # 或者条件、非条件、并且条件
    # 查询age=18或者gender=1的学生信息
    # Q()
    # from django.db.models import Q
    stus = Student.objects.filter(Q(age=18), Q(gender=1))

    stus = Student.objects.filter(Q(age=18) & Q(gender=1))

    stus = Student.objects.filter(Q(age=18) | Q(gender=1))

    stus = Student.objects.filter(~Q(age=18) | Q(gender=1))

    # 查询语文成绩比数学成绩大的学生信息
    # F()
    # from django.db.models import F
    stus = Student.objects.filter(yuwen__gt = F('shuxue'))

    # 查询语文成绩比数学成绩大10分的学生信息
    stus = Student.objects.filter(yuwen__gt = F('shuxue') + 10)

    # 获取学生的姓名
    stus_names = [stu.name for stu in stus]

    return HttpResponse(stus_names)


def add_stu_info(request):
    s_info = StuInfo()
    s_info.phone = '13441366790'
    s_info.address = '天府新区'
    # s_info.stu_id = 1
    s_info.stu = Student.objects.get(pk=5)
    s_info.save()
    return HttpResponse('创建拓展信息')


def sel_info_by_stu(request):
    # 通过学生信息查拓展表信息
    # 查询大明的电话号码
    # sql: select stu_info.phone from student,stu_info
    # where student.id=stu_info.stu_id

    # sql2:
    # select phone from stu_info,(select id from student) as a
    # where stu_info.stu_id=a.id


    stu = Student.objects.filter(name='大明').first()
    # 第一种笨办法
    # stu_info = StuInfo.objects.filter(stu_id=stu.id).first()
    stu_info = StuInfo.objects.filter(stu=stu).first()
    phone = stu_info.phone

    # 第二种反向查询
    stu_info = stu.stuinfo
    phone = stu_info.phone
    return HttpResponse(phone)


def sel_stu_by_info(request):
    # 查询phone=13441366790的学生信息
    stu_info = StuInfo.objects.get(phone='13441366790')
    stu = stu_info.stu
    return HttpResponse('通过拓展表查询学生信息')


def add_grade(request):
    gnames = ['Python', 'Java', 'Php']
    for name in gnames:
        Grade.objects.create(g_name=name)
    return HttpResponse('创建成功')


def sel_grade_by_stu(request):
    stu = Student.objects.filter(name='大明').first()
    grade = stu.g
    return HttpResponse('通过班级查询学生成功')


def sel_stu_by_grade(request):
    g = Grade.objects.filter(g_name='python').first()
    stus = g.student_set.all()
    return HttpResponse('通过班级查询学生成功')


def add_cou(request):
    cous = ['线代', '高数', '物理', '英语']
    for c in cous:
        cou = Course()
        cou.c_name = c
        cou.save()
    return HttpResponse('创建课程成功')


def stu_cou(request):
    # 添加学生和课程的关系
    # 给大明加线代这门课
    stu = Student.objects.get(name='大明')
    cou = Course.objects.get(c_name='线代')
    # 通过人查找课程，并添加课程
    stu.course_set.add(cou)
    # 删除人的课程
    stu.course_set.remove(cou)
    return HttpResponse('添加和删除学生之间的关联关系')


def index(request):
    stus = Student.objects.all()
    return render(request, 'index.html', {'students': stus})

