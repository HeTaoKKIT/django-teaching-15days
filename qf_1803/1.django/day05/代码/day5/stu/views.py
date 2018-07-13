from django.shortcuts import render

from rest_framework import mixins, viewsets
from rest_framework.response import Response

from stu.models import Student, Grade
from stu.stu_filters import StuFilter
from stu.stu_serializer import StuSerializer, GradeSerializer


def s_index(request):
    if request.method == 'GET':
        return render(request, 'student.html')


def s_add(request):
    if request.method == 'GET':
        return render(request, 'addstu.html')


class StudentSource(mixins.ListModelMixin,
                    mixins.RetrieveModelMixin,
                    mixins.DestroyModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.CreateModelMixin,
                    viewsets.GenericViewSet):

    # 查询学生的数据
    queryset = Student.objects.all()
    # 序列化
    serializer_class = StuSerializer
    # 过滤
    filter_class = StuFilter

    def retrieve(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            serializer = self.get_serializer(instance)
            data =serializer.data
            data['msg'] = '请求成功哈哈哈哈哈哈'
        except:
            data = {
                'msg': '学生不存在',
                'code': 500
            }
        return Response(data)

    def perform_destroy(self, instance):
        instance.is_del = True
        instance.save()


class GradeSource(mixins.ListModelMixin,
                  viewsets.GenericViewSet):

    queryset = Grade.objects.all()

    serializer_class = GradeSerializer
