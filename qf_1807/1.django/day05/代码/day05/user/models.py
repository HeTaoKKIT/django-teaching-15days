from django.db import models


class MyUser(models.Model):
    username = models.CharField(max_length=10, unique=True)
    password = models.CharField(max_length=100)
    create_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'my_user'


class TokenUser(models.Model):
    token = models.CharField(max_length=30)
    user = models.OneToOneField(MyUser)

    class Meta:
        db_table = 'token_user'



