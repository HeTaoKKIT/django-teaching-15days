from django.contrib.auth.models import AbstractUser, User
from django.db import models


class MyUser(AbstractUser):
    # 扩展django自带的auth_user表，可以自定义新增的字段

    class Meta:
        # django默认给每个模型初始化三个权限
        # 默认的是change、delete、add权限
        permissions = (
            ('add_my_user', '新增用户权限'),
            ('change_my_user_username', '修改用户名权限'),
            ('change_my_user_password', '修改用户密码权限'),
            ('all_my_user', '查看用户权限')
        )


