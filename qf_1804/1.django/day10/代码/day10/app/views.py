

from django.http import HttpResponse
from django.shortcuts import render

from rest_framework import mixins, viewsets
from rest_framework.response import Response

from app.app_filter import StudentFilter
from app.app_serializers import StudentSerializer
from app.models import Student
from utils.functions import print_log


@print_log
def hello(request):
    if request.method == 'GET':

        return HttpResponse('hello!')


class StudentSource(mixins.ListModelMixin,
                    mixins.RetrieveModelMixin,
                    mixins.CreateModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    viewsets.GenericViewSet):
    # 查询资源的所有数据
    queryset = Student.objects.filter(is_delete=False)
    # 序列化
    serializer_class = StudentSerializer
    # 过滤
    # filter_class = StudentFilter

    def get_queryset(self):
        queryset = self.queryset
        # return queryset.filter(s_name__contains='李')
        return queryset


    def perform_destroy(self, instance):
        instance.is_delete = True
        instance.save()

    def retrieve(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            serializer = self.get_serializer(instance)
            return Response(serializer.data)
        except:
            data = {
                'code': 1001,
                'msg': '学生不存在'
            }
        return Response(data)


def students(request):
    if request.method == 'GET':
        return render(request, 'students.html')


def add_students(request):
    if request.method == 'GET':
        return render(request, 'addStudent.html')
