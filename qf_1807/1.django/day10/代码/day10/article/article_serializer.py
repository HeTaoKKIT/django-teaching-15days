
from rest_framework import serializers

from article.models import Article


class ArticleSerializer(serializers.ModelSerializer):
    desc = serializers.CharField(min_length=10,
                                 max_length=100,
                                 error_messages={
                                     'required': '描述必填',
                                     'max_length': '描述不超过100字符',
                                     'min_length': '描述不少于10字符'
                                 })
    title = serializers.CharField(max_length=10,
                                  error_messages={
                                      'required': '标题必填',
                                  })
    content = serializers.CharField(min_length=10,
                                    error_messages={
                                      'required': '内容必填',
                                    })

    class Meta:
        # 序列化的模型
        model = Article
        # 需要序列化的字段
        fields = ['title', 'desc', 'content', 'id', 'atype']

    def to_representation(self, instance):
        # 序列化是会默认调用该方法，返回的结果为当前instance对象的序列化结果
        data = super().to_representation(instance)
        if instance.atype:
            data['atype'] = instance.atype.t_name
        return data
