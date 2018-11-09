from django.shortcuts import render

from rest_framework import mixins, viewsets

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

    def perform_destroy(self, instance):
        instance.is_delete = 1
        instance.save()


def list_art(request):
    if request.method == 'GET':

        return render(request, 'articles.html')
