
import re

from django.urls import reverse
from django.utils.deprecation import  MiddlewareMixin
from django.http import HttpResponseRedirect

from carts.models import ShoppingCart
from user.models import User


class LoginStatusMiddleware(MiddlewareMixin):

    def process_request(self, request):
        # 登录状态验证
        # 设置全局user对象
        user_id = request.session.get('user_id')
        if user_id:
            user = User.objects.filter(pk=user_id).first()
            request.user = user

        # 首页配置
        if request.path == '/':
            return None

        # 过滤不需要验证的URL，比如：首页、登录、注册、购物车、media
        not_need_check = ['/goods/index/',
                          '/user/register/',
                          '/user/login/',
                          '/carts/cart/',
                          '/media/.*',
                          '/static/.*',
                          '/goods/detail/.*',
                          '/carts/add_cart/',
                          '/carts/count_cart/',
                          '/carts/change_cart/',
                          '/carts/del_cart/.*']
        path = request.path
        for not_check in not_need_check:
            if re.match(not_check, path):
                # 不需要做登录验证
                return None
        # 登录校验
        user_id = request.session.get('user_id')
        if not user_id:
            # 如果session中没有user_id字段，则跳转到登录
            return HttpResponseRedirect(reverse('user:login'))
        # 通过user_id获取user对象
        user = User.objects.filter(pk=user_id).first()
        if not user:
            # 如果获取的user不存在，则跳转到登录
            return HttpResponseRedirect(reverse('user:login'))
        # 获取到user，则设置全局用户对象
        request.user = user
        return None


class SessionSyncMiddleware(MiddlewareMixin):

    def process_response(self, request, response):
        # 没有登录就不管数据同步
        # 登录情况才做数据从session同步到数据库，且重新更新session数据

        user_id = request.session.get('user_id')
        if user_id:
            # 登录情况
            session_goods = request.session.get('goods')
            # [[goods_id, nums, is_select], [goods_id, nums, is_select]...]
            if session_goods:
                # 1. 判断session中商品是否存在于数据库中，如果存在，则更新
                # 2. 如果不存在则创建
                shop_carts = ShoppingCart.objects.filter(user_id=user_id)
                # # 更新购物车中的商品数量,记录更新商品的id值
                data = []
                for goods in shop_carts:
                    for se_goods in session_goods:
                        if se_goods[0] == goods.goods_id:
                            goods.nums = se_goods[1]
                            goods.save()
                            # 向data中添加编辑了的商品id值
                            data.append(se_goods[0])
                # 添加
                session_goods_ids = [i[0] for i in session_goods]
                add_goods_ids = list(set(session_goods_ids) - set(data))

                for add_goods_id in add_goods_ids:
                    for session_good in session_goods:
                        if add_goods_id == session_good[0]:
                            ShoppingCart.objects.create(user_id=user_id,
                                                        goods_id=add_goods_id,
                                                        nums=session_good[1])

            # 将数据库中数据同步到session中
            # [[goods_id, nums, is_select], [goods_id, nums, is_select]...]
            new_shop_carts = ShoppingCart.objects.filter(user_id=user_id)
            session_new_goods = [[i.goods_id, i.nums, i.is_select] for i in new_shop_carts]
            request.session['goods'] = session_new_goods

        return response
