from django.shortcuts import render
from rest_framework import mixins, viewsets

from app.models import Article
from app.serializers import ArticleSerializer


class ArticleView(viewsets.GenericViewSet,
                  mixins.ListModelMixin,
                  mixins.DestroyModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.CreateModelMixin):

    # 查询数据
    queryset = Article.objects.filter(is_delete=0)
    # 序列化
    serializer_class = ArticleSerializer

    def perform_destroy(self, instance):
        instance.is_delete = 1
        instance.save()


def all_article(request):
    if request.method == 'GET':
        # articels = Article.objects.all()
        return render(request, 'articles.html')
