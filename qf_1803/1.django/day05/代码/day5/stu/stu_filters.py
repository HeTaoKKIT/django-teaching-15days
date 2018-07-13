
import django_filters
from rest_framework.filters import FilterSet

from stu.models import Student


class StuFilter(FilterSet):

    s_name = django_filters.CharFilter('s_name', lookup_expr='icontains')
    create_min = django_filters.DateTimeFilter('s_create_time', lookup_expr='gt')
    create_max = django_filters.DateTimeFilter('s_create_time', lookup_expr='lt')

    class Meta:
        model = Student
        fields = ['s_name',]
