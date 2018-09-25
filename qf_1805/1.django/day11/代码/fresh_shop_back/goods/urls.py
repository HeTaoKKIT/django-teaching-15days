
from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from goods import views

urlpatterns = [
    # 商品分类列表
    url(r'^goods_category_list/', login_required(views.goods_category_list), name='goods_category_list'),
    # 商品分类编辑页面
    url(r'^goods_category_edit/(\d+)/', login_required(views.goods_category_edit), name='goods_category_edit'),

]
