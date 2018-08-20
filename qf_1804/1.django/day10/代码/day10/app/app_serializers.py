
from rest_framework import serializers

from app.models import Student


class StudentSerializer(serializers.ModelSerializer):

    s_name = serializers.CharField(error_messages={'blank': '姓名不能为空'})

    class Meta:
        model = Student
        fields = ['id', 's_name', 's_age']

    def to_representation(self, instance):
        # 调用父类，拿到序列化结果
        data = super().to_representation(instance)
        # 对序列化结果进行添加参数
        data['address'] = '金科南路'

        return data
