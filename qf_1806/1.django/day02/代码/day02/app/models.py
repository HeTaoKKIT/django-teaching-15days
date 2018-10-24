from django.db import models


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

    class Meta:
        # 定义模型迁移到数据库中的表名
        db_table = 'student'


