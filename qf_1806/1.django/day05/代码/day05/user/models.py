from django.db import models


class User(models.Model):
    name = models.CharField(unique=True, max_length=10, verbose_name='姓名')
    password = models.CharField(max_length=200)
    email = models.CharField(max_length=30, null=True)
    create_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'user'


class UserToken(models.Model):
    # 标识符，用于用户访问需要登录验证页面的时候使用，校验标识符是否正确
    token = models.CharField(max_length=30, verbose_name='标识符')
    user = models.OneToOneField(User)

    class Meta:
        db_table = 'user_token'
