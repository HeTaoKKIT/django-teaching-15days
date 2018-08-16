
from rest_framework import serializers

from app.models import Student


class StudentSerializer(serializers.ModelSerializer):

    s_name = serializers.CharField(error_messages={'blank': '姓名不能为空'})
    class Meta:
        model = Student
        fields = ['id', 's_name', 's_age']

