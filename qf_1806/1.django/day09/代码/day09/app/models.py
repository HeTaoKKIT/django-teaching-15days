from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=20)
    desc = models.CharField(max_length=150)
    # 上传到article文件夹里
    img = models.ImageField(upload_to='article')
    create_time = models.DateTimeField(auto_now_add=True)
    is_delete= models.BooleanField(default=0)

    class Meta:
        db_table = 'article'
