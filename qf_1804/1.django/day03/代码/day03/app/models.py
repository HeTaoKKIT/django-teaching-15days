
from django.db import models

# ORM


class Grade(models.Model):
    g_name = models.CharField(max_length=10)

    class Meta:
        db_table = 'grade'

class Student(models.Model):

    s_name = models.CharField(max_length=10, unique=True)
    s_age = models.IntegerField(default=16)
    s_sex = models.BooleanField(default=1)
    operator_time = models.DateTimeField(auto_now=True)
    create_time = models.DateTimeField(auto_now_add=True, null=True)
    yuwen = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    shuxue = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    g = models.ForeignKey(Grade, on_delete=models.CASCADE, null=True)

    class Meta:
        db_table = 'student'

    # def __init__(self, s_name, s_age, yuwen, shuxue):
    #     super(Student, self).__init__()
    #     self.s_name = s_name
    #     self.s_age = s_age
    #     self.yuwen = yuwen
    #     self.shuxue = shuxue

    def to_dict(self):
        return {
            'id': self.id,
            's_name': self.s_name,
            's_age': self.s_age,
            's_sex': self.s_sex,
            'yuwen': self.yuwen,
            'shuxue': self.shuxue
        }


class StudentInfo(models.Model):
    address = models.CharField(max_length=20, null=True)
    phone = models.IntegerField()
    stu = models.OneToOneField(Student, on_delete=models.SET_NULL, null=True)


class Course(models.Model):
    c_name = models.CharField(max_length=10)
    stu = models.ManyToManyField(Student)

    class Meta:
        db_table = 'course'
