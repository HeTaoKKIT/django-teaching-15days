from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=20)
    desc = models.CharField(max_length=150)
    img = models.ImageField(upload_to='article')
    create_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'article'
