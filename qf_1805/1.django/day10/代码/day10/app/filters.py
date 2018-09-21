
import django_filters
from rest_framework import filters

from app.models import Student


class StudentFilter(filters.FilterSet):
    # 定义过滤的字段
    name = django_filters.CharFilter('s_name', lookup_expr='contains')
    # 开始时间
    sd = django_filters.DateTimeFilter('create_time', lookup_expr='gt')
    # 结束时间
    ed = django_filters.DateTimeFilter('create_time', lookup_expr='lt')

    class Meta:
        # 过滤的模型
        model = Student
        # 过滤的字段
        fields = ['s_name', ]
