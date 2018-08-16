
from rest_framework import serializers

from app.models import Student


class StudentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Student
        fields = ['id', 's_name', 's_age']

