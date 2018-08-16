from django.db import models


class Student(models.Model):

    s_name = models.CharField(max_length=10, unique=True)
    s_age = models.IntegerField(default=18)
    s_sex = models.BooleanField(default=0)
    is_delete = models.BooleanField(default=0)

    class Meta:
        db_table = 'student'
