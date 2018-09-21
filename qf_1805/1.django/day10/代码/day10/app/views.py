from django.shortcuts import render
from rest_framework import viewsets, mixins

from app.filters import StudentFilter
from app.models import Student
from app.serializers import StudentSerializer


class StudentView(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  mixins.DestroyModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  viewsets.GenericViewSet):

    # 返回数据
    queryset = Student.objects.all()
    # 序列化结果
    serializer_class = StudentSerializer
    # 过滤
    filter_class = StudentFilter

    # def get_queryset(self):
    #     # 获取学生对象的数据
    #     queryset = self.queryset
    #     name = self.request.query_params.get('name')
    #     # 返回过滤的学生结果
    #     return queryset.filter(s_name__contains=name)


    def perform_destroy(self, instance):
        instance.is_delete = 1
        instance.save()


def index(request):
    if request.method == 'GET':
        return render(request, 'index.html')


def add(request):
    if request.method == 'GET':
        return render(request, 'add.html')
