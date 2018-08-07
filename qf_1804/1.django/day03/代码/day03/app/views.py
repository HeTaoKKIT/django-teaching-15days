from django.db.models import F, Q
from django.http import HttpResponse
from django.shortcuts import render

from app.models import Student, StudentInfo, Grade, Course


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
        # 查询语文成绩最大
        stus = Student.objects.all().order_by('-yuwen').first()
        stus = Student.objects.all().order_by('yuwen').last()

        # 查询比id=1的学生的数学成绩大10分的学生的信息
        # stu = Student.objects.filter(pk=1).first()
        # stu = Student.objects.get(pk=1)
        # shuxue = stu.shuxue
        # stus = Student.objects.filter(shuxue__gt= shuxue+10)

        # 或者： 查询数学成绩比语文成绩大十分的学生信息
        # F()可以将模型的两个字段进行算数计算
        stus = Student.objects.filter(shuxue__gt = F('yuwen') + 10)

        stus = Student.objects.all()
        stus_list = []
        for stu in stus:
            if stu.shuxue > stu.yuwen + 10:
                stus_list.append(stu)

        # 查询语文成绩大于70，或者年龄小于17的学生信息
        # Q()
        stus = Student.objects.filter(yuwen__gt=70, s_age__lt=17)
        stus = Student.objects.filter(Q(yuwen__gt=70) | Q(s_age__lt=17))

        # 查询语文成绩不等于70，或者年龄小于17的学生信息
        stus = Student.objects.filter(~Q(yuwen=70) | Q(s_age__lt=17))

        # 列表推导式 [i for i in xxx]
        stus_list = [stu.to_dict() for stu in stus]
        return HttpResponse(stus_list)
        # return HttpResponse(stus)


def addStu(request):
    if request.method == 'GET':
        # 第一种
        # stu = Student()
        # stu.s_name = '大明'
        # stu.s_age = '30'
        # stu.yuwen = 59
        # stu.shuxue = 30.5
        # stu.save()
        # 第二种
        # stu = Student('小小明', 25, 90, 89.6)
        # stu.save()
        # 第三种
        Student.objects.create(s_name='妲己', yuwen=67, shuxue=56, s_age=40)
        return HttpResponse('创建成功')


def delStudent(request):
    if request.method == 'GET':
        stu = Student.objects.filter(id=3)
        stu.delete()
        return HttpResponse('删除成功')


def updateStudent(request):
    if request.method == 'GET':
        # 修改方法1
        # stu = Student.objects.filter(id=2).first()
        # stu.s_name = '小明明'
        # stu.save()
        # 修改方法2
        Student.objects.filter(id=2).update(s_name='小明明明')
        return HttpResponse('修改成功')


def oneToOneSelect(request):
    if request.method == 'GET':
        # 查询id=2的学生电话号码和学生地址，还有学生的姓名
        # 写sql
        """
        SELECT * from student as s
        JOIN app_studentinfo as a ON a.stu_id=s.id
        where s.id=2

        SELECT * from student, app_studentinfo
        where student.id=app_studentinfo.stu_id
        """
        #通过学生对象找一对一关联的表信息
        stu = Student.objects.get(pk=2)
        stuinfo = stu.studentinfo

        # 通过拓展表找学生信息，知道电话号码123455678找学生
        stuinfo = StudentInfo.objects.get(phone='123455678')
        stu = stuinfo.stu

        return HttpResponse('查询学生的拓展表信息')


def OneToManySelect(request):
    if request.method == 'GET':
        # 查询id=4的学生的班级名称
        stu = Student.objects.get(id=4)
        grade = stu.g
        # 查询id=1的班级的所有学生
        grade = Grade.objects.filter(id=1).first()
        stus = grade.student_set.all()

        return HttpResponse('班级名称:%s' % grade.g_name)


def addGrade(request):
    if request.method == 'GET':
        Grade.objects.create(g_name='Python')
        return HttpResponse('创建班级成功')


def addCourse(request):
    if request.method == 'GET':
        courses = ['高数', '线代', 'VHDL', '马克思']
        for course in courses:
            Course.objects.create(c_name=course)
        return HttpResponse('创建课程成功')


def ManyToManySelect(request):
    if request.method == 'GET':
        # id=4的学生添加两门课程(id=1,2)
        stu = Student.objects.get(id=4)
        c1 = Course.objects.get(id=1)
        c2 = Course.objects.get(id=2)
        # stu.course_set.add(c1)
        # stu.course_set.add(c2)
        # 删除id=4的学生的课程中id=1的课程
        stu.course_set.remove(c1)
        # 学生查询课程
        stu.course_set.all().filter()

        return HttpResponse('添加学生对应班级信息')
