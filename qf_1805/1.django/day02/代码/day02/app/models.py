
from datetime import datetime

from django.db import models


class Student(models.Model):
    s_name = models.CharField(max_length=10, unique=True, verbose_name='姓名')
    s_age = models.IntegerField(default=19, verbose_name='年龄')
    s_sex = models.BooleanField(default=1, verbose_name='性别')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    operate_time = models.DateTimeField(auto_now=True, verbose_name='修改时间')

    class Meta:
        db_table = 'app_student'
    #
    # def __init__(self, name, age=None, sex=None):
    #     super().__init__()
    #     self.s_name = name
    #     self.s_age = age if age else self.s_age
    #     self.s_sex = sex if sex else self.s_sex
    #     self.create_time = datetime.now()
    #     self.operate_time = datetime.now()
