from django.db import models


class Grade(models.Model):
    g_name = models.CharField(max_length=10, unique=True)

    class Meta:
        db_table = 'grade'


class Student(models.Model):
    s_name = models.CharField(max_length=10, unique=True)
    s_age = models.IntegerField(default=20)
    s_gender = models.BooleanField(default=0)
    # auto_now_add: 创建时，默认字段赋值为最新的时间
    create_time = models.DateTimeField(auto_now_add=True)
    # auto_now: 修改数据时，自动赋值为更新字段时的时间
    update_time = models.DateTimeField(auto_now=True)
    math = models.DecimalField(max_digits=3, decimal_places=1, null=True)
    wuli = models.DecimalField(max_digits=3, decimal_places=1, null=True)
    # 一对多的外键定义
    g = models.ForeignKey(Grade, null=True,
                          on_delete=models.CASCADE,
                          related_name='stu')

    class Meta:
        db_table = 'student'


class StudentInfo(models.Model):
    s_no = models.CharField(max_length=10, null=False)
    phone = models.CharField(max_length=11, null=True)
    name = models.CharField(max_length=10, null=True)
    # 定义一对一的关联关系
    # on_delete:
    # models.CASCADE 删除主表，从表也会被删
    # models.PROTECT 不让删除主表
    # models.SET_NULL 删除主表，从表的关联字段设置为空
    stu = models.OneToOneField(Student,
                               on_delete=models.SET_NULL,
                               related_name='info',
                               null=True)


class Course(models.Model):
    c_name = models.CharField(max_length=10, unique=True)
    # ManyToManyField字段定义在任何一个模型都可以
    stu = models.ManyToManyField(Student, null=True, related_name='cou')

    class Meta:
        db_table = 'course'
