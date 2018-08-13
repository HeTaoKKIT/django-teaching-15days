from django.db import models

# from DjangoUeditor.models import UEditorField


class AType(models.Model):
    name = models.CharField(max_length=10)
    create_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'atype'


class Article(models.Model):
    title = models.CharField(max_length=15, null=False)
    desc = models.CharField(max_length=50, null=False)
    is_show = models.BooleanField(default=False)  # 是否展示
    is_recommend = models.BooleanField(default=False)  # 是否推荐
    image_url = models.ImageField(upload_to='upload', null=True)
    content = models.TextField()
    atype = models.ForeignKey(AType)
    create_time = models.DateTimeField(auto_now_add=True)
    oprate_time = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'article'


class User(models.Model):
    username = models.CharField(max_length=10)
    password = models.CharField(max_length=255)
    create_time = models.DateTimeField(auto_now_add=True)
    session_id = models.CharField(max_length=30, null=True)
    out_time = models.DateTimeField(null=True)

    class Meta:
        db_table = 'user'
