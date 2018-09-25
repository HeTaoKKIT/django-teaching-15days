from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from goods.models import GoodsCategory


def goods_category_list(request):
    if request.method == 'GET':
        # 获取分类信息
        categorys = GoodsCategory.objects.all()
        # 返回类型
        category_types = GoodsCategory.CATEGORY_TYPE
        return render(request, 'goods_category_list.html',
                      {'categorys': categorys,
                       'category_types': category_types})


def goods_category_edit(request, id):
    if request.method == 'GET':
        # 获取当前选择的商品分类
        category = GoodsCategory.objects.get(pk=id)
        # 返回商品类型
        categorys_types = GoodsCategory.CATEGORY_TYPE
        return render(request, 'goods_category_detail.html',
                      {'category': category, 'categorys_types': categorys_types})

    if request.method == 'POST':
        # 获取图片
        category_front_image = request.FILES.get('category_front_image')
        if category_front_image:
            category = GoodsCategory.objects.get(pk=id)
            category.category_front_image = category_front_image
            category.save()
        return HttpResponseRedirect(reverse('goods:goods_category_list'))
