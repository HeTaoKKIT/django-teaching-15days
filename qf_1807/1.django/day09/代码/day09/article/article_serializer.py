
from rest_framework import serializers

from article.models import Article


class ArticleSerializer(serializers.ModelSerializer):

    class Meta:
        # 序列化的模型
        model = Article
        # 需要序列化的字段
        fields = ['title', 'desc', 'content', 'id']
