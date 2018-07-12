
from rest_framework import serializers

from stu.models import Student


class StuSerializer(serializers.ModelSerializer):

    class Meta:
        # 指定序列化的模型
        model = Student
        # 指定需要展示的字段
        fields = ['id', 's_name', 's_sex', 'g']
