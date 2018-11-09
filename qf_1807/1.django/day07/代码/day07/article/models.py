from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=100)
    desc = models.CharField(max_length=150)
    content = models.TextField()
    icon = models.ImageField(upload_to='article', null=True)
    create_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'article'
