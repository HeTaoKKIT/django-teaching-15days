
import logging

from django.http import HttpResponse

from rest_framework import mixins, viewsets

from app.app_serializers import StudentSerializer
from app.models import Student

logger = logging.getLogger('dj')


def hello(request):
    if request.method == 'GET':
        logger.info('hello')
        return HttpResponse('hello!')


class StudentSource(mixins.ListModelMixin,
                    mixins.RetrieveModelMixin,
                    mixins.CreateModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    viewsets.GenericViewSet):
    # 查询资源的所有数据
    queryset = Student.objects.all()
    # 序列化
    serializer_class = StudentSerializer
