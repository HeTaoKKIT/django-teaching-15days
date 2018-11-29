from django.db import models


class Grade(models.Model):
    g_name = models.CharField(max_length=10)
    create_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'grade'


class Student(models.Model):
    name = models.CharField(max_length=10, unique=True)
    age = models.IntegerField(default=18)
    gender = models.BooleanField(default=1)
    # auto_now_add: 创建数据时，默认create_time字段为当前时间
    create_time = models.DateTimeField(auto_now_add=True, null=True)
    # auto_now: 修改时间，每次update学生信息时，修改该字段的时间为当前时间
    operate_time = models.DateTimeField(auto_now=True, null=True)
    yuwen = models.DecimalField(max_digits=3, decimal_places=1, null=True)
    shuxue = models.DecimalField(max_digits=3, decimal_places=1, null=True)
    # 指定学生和班级的关联关系, foreignkey定义在多的一方
    g = models.ForeignKey(Grade, null=True)

    class Meta:
        # 指定Student模型映射到数据库中时，对应的表名。
        db_table = 'student'


class StuInfo(models.Model):
    phone = models.CharField(max_length=11)
    address = models.CharField(max_length=100)
    # OneToOneField等价于ForeignKey, 且约束unique=True
    stu = models.OneToOneField(Student)

    class Meta:
        db_table = 'stu_info'


class Course(models.Model):
    c_name = models.CharField(max_length=10)
    # ManyToManyField字段定义在关联的任何一个模型中都可以
    stu = models.ManyToManyField(Student)

    class Meta:
        db_table = 'course'


