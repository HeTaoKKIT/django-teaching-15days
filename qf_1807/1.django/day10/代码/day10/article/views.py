from django.shortcuts import render

from rest_framework import mixins, viewsets
from rest_framework.response import Response

from article.article_filter import ArticleFiler
from article.article_serializer import ArticleSerializer
from article.models import Article


class ArticleView(viewsets.GenericViewSet,
                  mixins.ListModelMixin,
                  mixins.DestroyModelMixin,
                  mixins.CreateModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.RetrieveModelMixin):
    # 查询返回的数据
    queryset = Article.objects.filter(is_delete=0)
    # 序列化返回的文章数据
    serializer_class = ArticleSerializer
    # 过滤
    filter_class = ArticleFiler

    def perform_destroy(self, instance):
        instance.is_delete = 1
        instance.save()

    def retrieve(self, request, *args, **kwargs):
        # instance = self.get_object()
        # serializer = self.get_serializer(instance)
        # Response(serializer.data)
        try:
            instance = self.get_object()
            serializer = self.get_serializer(instance)
            return Response(serializer.data)
        except:
            data = {}
            data['code'] = 500
            data['msg'] = '获取数据失败'
            return Response(data)


    # def get_queryset(self):
    #     search_title = self.request.GET.get('title')
    #     search_desc = self.request.GET.get('desc')
    #     search_content = self.request.GET.get('content')
    #     # 既要搜索title，desc，content
    #     if not search_title and not search_desc and not search_content:
    #         return self.queryset
    #     if search_title and search_desc and search_content:
    #         return self.queryset.filter(title__contains=search_title,
    #                                     desc_contains=search_desc,
    #                                     content_contains=search_content)
    #
    #     return self.queryset.filter(title__contains=search_title)


def list_art(request):
    if request.method == 'GET':

        return render(request, 'articles.html')
