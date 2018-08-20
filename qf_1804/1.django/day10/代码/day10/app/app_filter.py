
import django_filters

from rest_framework import filters

from app.models import Student


class StudentFilter(filters.FilterSet):
    # 过滤s_name参数，精确过滤
    s_name = django_filters.CharFilter('s_name', lookup_expr='icontains')
    s_age_min = django_filters.NumberFilter('s_age', lookup_expr='gte')
    s_age_max = django_filters.NumberFilter('s_age', lookup_expr='lte')


    class Meta:
        model = Student
        fields = ['s_name',]

