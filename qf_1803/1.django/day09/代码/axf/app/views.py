from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.core.urlresolvers import reverse

from app.models import MainWheel, MainNav, MainMustBuy, \
    MainShop, MainShow, FoodType, Goods, CartModel, \
    OrderModel, OrderGoodsModel
from utils.functions import get_order_num


def Home(request):

    if request.method == 'GET':
        mainwheels = MainWheel.objects.all()
        mainnavs = MainNav.objects.all()
        mainmustbuys = MainMustBuy.objects.all()
        mainshops = MainShop.objects.all()
        mainshows = MainShow.objects.all()

        data = {
            'mainwheels': mainwheels,
            'mainnavs': mainnavs,
            'mainmustbuys': mainmustbuys,
            'mainshops': mainshops,
            'mainshows': mainshows
        }
        return render(request, 'home/home.html', data)


def Market(request):
    if request.method == 'GET':

        return HttpResponseRedirect(reverse('axf:marketparams',
                                            kwargs={'typeid': 104749,
                                                    'cid': 0,
                                                    'sid': 0}))


def MarketParams(request, typeid, cid, sid):
    if request.method == 'GET':
        foodtypes = FoodType.objects.all()
        if cid == '0':
            goods = Goods.objects.filter(categoryid=typeid)
        else:
            goods = Goods.objects.filter(categoryid=typeid,
                                         childcid=cid)

        if sid == '0':
            pass
        elif sid == '1':
            goods = goods.order_by('-productnum')
        elif sid == '2':
            goods = goods.order_by('-price')
        elif sid == '3':
            goods = goods.order_by('price')


        childtypenames = FoodType.objects.filter(typeid=typeid).first().childtypenames
        # [['国产水果',14111], ['进口水果'：13321]]
        childtypenames_list = [i.split(':') for i in childtypenames.split('#')]
        data = {
            'foodtypes': foodtypes,
            'goods': goods,
            'typeid': typeid,
            'cid': cid,
            'sid': sid,
            'childtypenames_list': childtypenames_list
        }
        return render(request, 'market/market.html', data)


def AddToCard(request):
    if request.method == 'POST':
        user = request.user
        data = {}
        data['code'] = '1001'
        if user.id:
            goods_id = request.POST.get('goods_id')
            # 验证当前登录用户是否对同一商品进行添加操作
            cart = CartModel.objects.filter(user=user, goods_id=goods_id).first()
            if cart:
                cart.c_num += 1
                cart.save()
                data['c_num'] = cart.c_num
            else:
                # 登录的当前用户没有添加商品到购物车中，则创建
                CartModel.objects.create(user=user, goods_id=goods_id)
                data['c_num'] = 1
            data['code'] = '200'
            data['msg'] = '请求成功'
            return JsonResponse(data)
        return JsonResponse(data)


def SubToCard(request):
    if request.method == 'POST':
        user = request.user
        data = {}
        data['code'] = '1001'
        data['msg'] = '请求成功'
        if user.id:
            goods_id = request.POST.get('goods_id')
            card = CartModel.objects.filter(goods_id=goods_id, user=user).first()
            if card:
                if card.c_num == 1:
                    card.delete()
                    data['c_num'] = 0
                else:
                    card.c_num -= 1
                    card.save()
                    data['c_num'] = card.c_num
                data['code'] = '200'
                return JsonResponse(data)
            else:
                data['msg'] = '请先添加商品'
                return JsonResponse(data)
        else:
            data['msg'] = '用户没有登录'
            return JsonResponse(data)


def GoodNum(request):
    if request.method == 'GET':
        user = request.user
        cart_list = []
        if user.id:
            carts = CartModel.objects.filter(user=user)
            for cart in carts:
                data = {
                    'id': cart.id,
                    'goods_id': cart.goods.id,
                    'c_num': cart.c_num,
                    'user_id': cart.user.id
                }
                cart_list.append(data)
            return JsonResponse({'carts': cart_list, 'code': '200'})
        else:
            JsonResponse({'carts': '', 'code': '1002'})


def Cart(request):
    if request.method == 'GET':
        user = request.user
        carts = CartModel.objects.filter(user=user)
        return render(request, 'cart/cart.html', {'carts': carts})


def changeCartStatus(request):
    if request.method == 'POST':
        cart_id = request.POST.get('cart_id')
        cart = CartModel.objects.get(pk=cart_id)
        if cart.is_select:
            cart.is_select = False
        else:
            cart.is_select = True
        cart.save()
        return JsonResponse({'code': '200', 'is_select': cart.is_select})


def goodsCount(request):
    if request.method == 'GET':
        user = request.user

        carts = CartModel.objects.filter(user=user, is_select=True)
        count_prices = 0
        for cart in carts:
            count_prices += cart.goods.price * cart.c_num

        count_prices = round(count_prices, 3)
        return JsonResponse({'count': count_prices, 'code': 200})


def order(request):
    if request.method == 'POST':
        user = request.user
        # 那些商品需要下单
        carts = CartModel.objects.filter(user=user, is_select=True)
        # 创建订单
        o_num = get_order_num()
        order = OrderModel.objects.create(user=user, o_num=o_num)
        # 创建订单详情信息
        for cart in carts:
            OrderGoodsModel.objects.create(order=order,
                                           goods=cart.goods,
                                           goods_num=cart.c_num)
        # 删除购物车中已经下单的商品信息
        carts.delete()

        return JsonResponse({'code': 200, 'order_id': order.id})


def orderInfo(request):
    if request.method == 'GET':
        order_id = request.GET.get('order_id')
        order_goods = OrderGoodsModel.objects.filter(order_id=order_id)
        return render(request, 'order/order_info.html', {'order_goods': order_goods})


def changeOrderStatus(request):
    if request.method == 'POST':
        order_id = request.POST.get('order_id')
        order = OrderModel.objects.filter(id=order_id).first()
        order.o_status = 1
        order.save()
        return JsonResponse({'code':200})


def Payed(request):
    if request.method == 'GET':
        user = request.user
        # 待收货
        orders = OrderModel.objects.filter(o_status=1,
                                           user=user)

        return render(request, 'order/order_list_payed.html', {'orders': orders})


def waitPay(request):
    if request.method == 'GET':
        user = request.user
        orders = OrderModel.objects.filter(o_status=0,
                                           user=user)
        return render(request, 'order/order_list_wait_pay.html', {'orders': orders})



