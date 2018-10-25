from django.db import models


class Grade(models.Model):
    g_name = models.CharField(max_length=10, unique=True)

    class Meta:
        db_table = 'grade'


class Student(models.Model):
    # 定义s_name字段，varchar类型，最长不超过6字符，唯一
    s_name = models.CharField(max_length=6, unique=True)
    # 定义s_age字段，int类型
    s_age = models.IntegerField(default=18)
    # 定义s_gender字段，int类型
    s_gender = models.BooleanField(default=1)
    # 定义create_time字段，创建时间
    create_time = models.DateTimeField(auto_now_add=True, null=True)
    # 定义operate_time字段，修改时间
    operate_time = models.DateTimeField(auto_now=True, null=True)
    # 定义yuwen字段，语文成绩
    yuwen = models.DecimalField(decimal_places=1,max_digits=4, null=True)
    # 定义shuxue字段，数学成绩
    shuxue = models.DecimalField(decimal_places=1, max_digits=4, null=True)

    grade = models.ForeignKey(Grade, null=True)

    class Meta:
        # 定义模型迁移到数据库中的表名
        db_table = 'student'

# 一对一
class StudentInfo(models.Model):
    phone = models.CharField(max_length=11, null=True)
    address = models.CharField(max_length=100)
    # OneToOneField 指定一对一关联关系, 该字段定义在任何一个模型都可以
    stu = models.OneToOneField(Student)

    class Meta:
        db_table = 'student_info'

# 多对多
class Course(models.Model):
    c_name = models.CharField(max_length=10)
    # 多对多关联字段
    stu = models.ManyToManyField(Student)

    class Meta:
        db_table = 'course'
