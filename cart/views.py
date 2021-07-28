from django.shortcuts import render
from django.http import HttpResponse
from shop.models import Product
from .models import Cart
# Create your views here.


def cart_init(request):
    try:
        cart = Cart.objects.get(id=request.session.get('user_cart_id'))
    except:
        cart = Cart.objects.create()
        request.session['user_cart_id'] = cart.id
    return cart


def cart_view(request):
    return render(request,'cart/cart_view.html')

import json
def addToCart(request):
    d = request.GET.get('data')
    data = json.loads(d)
    cart = cart_init(request)
    cart.add(data['product_id'],data['count'])

    return HttpResponse('Add')