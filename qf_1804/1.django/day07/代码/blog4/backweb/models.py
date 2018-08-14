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


class Permission(models.Model):
    """
    权限表
    文章列表权限----> LISTARTICLE
    文章添加权限----> ADDARTICEL
    文章编辑权限----> EDITARTICLE
    文章删除权限----> DELETEARTICLE
    """
    p_name = models.CharField(max_length=15)

    class Meta:
        db_table = 'permission'


class Role(models.Model):
    """
    角色表
    """
    r_name = models.CharField(max_length=10)
    r_p = models.ManyToManyField(Permission)

    class Meta:
        db_table = 'role'


class User(models.Model):
    username = models.CharField(max_length=10)
    password = models.CharField(max_length=255)
    is_superuser = models.BooleanField(default=False)
    create_time = models.DateTimeField(auto_now_add=True)
    session_id = models.CharField(max_length=30, null=True)
    out_time = models.DateTimeField(null=True)
    u_r = models.ForeignKey(Role, null=True)

    class Meta:
        db_table = 'user'