
from django.db import models

# ORM


class Student(models.Model):

    s_name = models.CharField(max_length=10, unique=True)
    s_age = models.IntegerField(default=16)
    s_sex = models.BooleanField(default=1)
    operator_time = models.DateTimeField(auto_now=True)
    create_time = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        db_table = 'student'

    def to_dict(self):
        return {
            'id': self.id,
            's_name': self.s_name,
            's_age': self.s_age,
            's_sex': self.s_sex
        }
