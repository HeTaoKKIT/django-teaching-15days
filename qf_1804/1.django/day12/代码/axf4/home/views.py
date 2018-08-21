from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.urls import reverse

from home.models import MainWheel, MainNav, MainMustBuy, \
    MainShop, MainShow, FoodType, Goods, CartModel


def index(request):
    if request.method == 'GET':

        mainwheels = MainWheel.objects.all()
        mainnavs = MainNav.objects.all()
        mainmustbuys = MainMustBuy.objects.all()
        mainshops = MainShop.objects.all()
        mainshows = MainShow.objects.all()

        data = {
            'mainwheels':  mainwheels,
            'mainnavs': mainnavs,
            'mainmustbuys': mainmustbuys,
            'mainshops': mainshops,
            'mainshows': mainshows
        }
        return render(request, 'home/home.html', data)


def market(request):
    if request.method == 'GET':

        return HttpResponseRedirect(reverse('home:market_params',
                                            kwargs={'typeid': 104749,
                                                    'cid': 0,
                                                    'sid':0
                                                    }))


def marketParms(request, typeid, cid, sid):
    if request.method == 'GET':
        # 分类
        foodtypes = FoodType.objects.all()
        # 分类对应的商品信息
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

        # 获取某个分类的全部类型
        types = FoodType.objects.filter(typeid=typeid).first()
        childtypes = [i.split(':') for i in types.childtypenames.split('#')]

        data = {
            'foodtypes': foodtypes,
            'goods': goods,
            'typeid': typeid,
            'cid': cid,
            'childtypes': childtypes,
        }
        return render(request, 'market/market.html', data)


def add_to_card(request):
    if request.method == 'POST':
        user = request.user
        if user.id:
            goods_id = request.POST.get('goods_id')
            cart = CartModel.objects.filter(user=user,
                                            goods_id=goods_id).first()
            if cart:
                cart.c_num += 1
                cart.save()
                c_data={'c_num': cart.c_num}
            else:
                CartModel.objects.create(user=user,
                                         goods_id=goods_id)
                c_data = {'c_num': 1}
            data = {
                'code': 200,
                'msg': '请求成功',
                'data': c_data
            }
            return JsonResponse(data)
        else:
            data = {
                'code': 200,
                'msg': '用户没有登录',
                'data': ''
            }
            return JsonResponse(data)
