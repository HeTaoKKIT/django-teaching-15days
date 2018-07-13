
from rest_framework import serializers

from stu.models import Student, Grade


class StuSerializer(serializers.ModelSerializer):

    s_name = serializers.CharField(max_length=3, error_messages={
        'blank': '姓名不能为空',
        'max_length': '长度太长'
    })

    class Meta:
        # 指定序列化的模型
        model = Student
        # 指定需要展示的字段
        fields = ['id', 's_name', 's_sex', 'g']

    def to_representation(self, instance):
        data = super().to_representation(instance)

        data['g'] = instance.g.g_name
        return data


class GradeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Grade
        fields = ['id', 'g_name']
