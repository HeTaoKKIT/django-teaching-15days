
from rest_framework import filters
import django_filters

from article.models import Article


class ArticleFiler(filters.FilterSet):
    # 过滤URL中title参数
    title = django_filters.CharFilter('title', lookup_expr='contains')
    # 过滤URL中的desc参数
    desc = django_filters.CharFilter('desc', lookup_expr='contains')
    # 过滤URL中的content参数
    content = django_filters.CharFilter('content', lookup_expr='contains')
    # 过滤URL中时间最小值min_time
    min_time = django_filters.DateTimeFilter('create_time', lookup_expr='gt')
    # 过滤URL中时间最大值max_time
    max_time = django_filters.DateTimeFilter('create_time', lookup_expr='lt')

    class Meta:
        model = Article
        fields = ['title', 'desc', 'content', 'min_time', 'max_time']