from django.db import models


class Atype(models.Model):
    t_name = models.CharField(max_length=10)

    class Meta:
        db_table = 'a_type'


class Article(models.Model):
    title = models.CharField(max_length=10)
    desc = models.CharField(max_length=100)
    content = models.TextField()
    is_delete = models.BooleanField(default=0)
    create_time = models.DateTimeField(auto_now_add=True)
    atype = models.ForeignKey(Atype, null=True)

    class Meta:
        db_table = 'article'
