
from rest_framework import serializers

from app.models import Article


class ArticleSerializer(serializers.ModelSerializer):

    class Meta:
        # 指定序列化的模型
        model = Article
        # 序列化字段
        fields = ['id', 'title', 'desc']
