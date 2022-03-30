# Page Redirect , Request Page , Response Page
from itertools import product
import json
from math import prod
from django.shortcuts import render, HttpResponse, redirect
# Showing Message alert on Main Page
from django.contrib import messages
# Create account
from django.contrib.auth.models import User, auth
# import Tables
from .models import *
# Login account
from django.contrib.auth import authenticate, login, logout
# Change Password
from django.contrib.auth.forms import PasswordChangeForm
# Gmail Request Add
from django.core.mail import send_mail
# Import json
from django.http import JsonResponse
# For Search Query
from django.db.models import Q
# Store User Image
from django.core.files.storage import FileSystemStorage
# CSRF Token
from django.views.decorators.csrf import csrf_exempt, csrf_protect
# Paytm Gateway
# from PayTm import Checksum
# Date Time
from django.utils.timezone import datetime
from datetime import date
import uuid
from django.conf import settings


def index(request):
    prod = Product.objects.all()[:8]
    return render(request, 'index.html', context={'prod': prod})


def shop(request):
    prod = Product.objects.all()
    return render(request, 'shop.html', context={'prod': prod})


def single_product(request, id):
    prod = Product.objects.get(id=id)
    return render(request, 'single_product.html', context={'prod': prod, })


def add_wishlist(request):
    pid = request.GET['product']
    product = Product.objects.get(id=pid)
    data = {}
    checkw = Wishlist.objects.filter(
        product=product, user=request.user).count()
    if checkw > 0:
        data = {
            'bool': False
        }
    else:
        wishlist = Wishlist.objects.create(
            product=product,
            user=request.user
        )
        data = {
            'bool': True
        }
    return JsonResponse(data)


def removeFromWishlist(request, id):
    i = Wishlist.objects.filter(product=id)
    i.delete()
    return redirect('/my_wishlist')


def my_wishlist(request):
    orders = Wishlist.objects.filter(user=request.user).order_by('-id')
    return render(request, 'wishlist.html', {'orders': orders})


def add_cart(request):
    pid = request.GET['product']
    item = request.GET['cartItem']
    product = Product.objects.get(id=pid)
    data = {}
    checkw = Cart.objects.filter(
        product=product, user=request.user).count()
    if checkw > 0:
        data = {
            'bool': False
        }
        cart = Cart.objects.filter(product=product, user=request.user)
        item = int(cart[0].itemLen) + int(item)
        cart = Cart.objects.filter(
            product=product, user=request.user).update(itemLen=item)
    else:
        cart = Cart.objects.create(
            product=product,
            user=request.user, itemLen=item
        )
        data = {
            'bool': True
        }
    return JsonResponse(data)


def removeFromCart(request, id):
    i = Cart.objects.filter(product=id)
    i.delete()
    return redirect('/cart')


def cart(request):
    orders = Cart.objects.filter(user=request.user).order_by('-id')
    totalPrice = 0
    for i in orders:
        new = i.product.price * i.itemLen
        totalPrice = int(totalPrice) + int(new)
    return render(request, 'cart.html', context={'orders': orders, 'totalPrice': totalPrice})



def checkout(request):
    if request.method == "POST":
        order_Items = Cart.objects.filter(user=request.user)
        items = []
        price = []
        itemLen = []
        for i in order_Items:
            items.append(i.product.title)
            price.append(i.product.price)
            itemLen.append(i.itemLen)
        amount = 0
        for i in order_Items:
            new = i.product.price * i.itemLen
            amount = int(amount) + int(new)
        email = request.POST['email']
        mobile = request.POST['mobile']
        address1 = request.POST['address1']
        address2 = request.POST['address2']
        city = request.POST['city']
        state = request.POST['state']
        zip = request.POST['zip']
        Order.objects.create(user=request.user, mobile=mobile , email=email, order_Items=items, price=price, itemLen=itemLen, amount=amount,
                             address1=address1, address2=address2, city=city, state=state, zip=zip)

        a = Cart.objects.filter(user=request.user)
        a.delete()
        return redirect('/')

    prod = Cart.objects.filter(user=request.user)
    totalPrice = 0
    for i in prod:
        new = i.product.price * i.itemLen
        totalPrice = int(totalPrice) + int(new)
    return render(request, 'checkout.html', context={'prod': prod, 'totalPrice': totalPrice})


# My Account Function
def my_account(request):
    return render(request, 'my_account.html')


# Make Changes in My Account Function
def make_changes(request):
    if request.method == "POST":
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']

        u = User.objects.update(email=email, first_name=fname, last_name=lname)
    return redirect('/my_account')


# My Account Function
def my_orders(request):
    orders = Order.objects.filter(user=request.user)
    return render(request, 'my_orders.html', context={'orders': orders})


# View Bill
def view_bill(request, id):
    bill = Order.objects.get(id=id)
    item = []
    for i in bill.order_Items:
        item.append(i)
    itemLen = []
    for i in bill.itemLen:
        itemLen.append(i)
    price = []
    for i in bill.price:
        price.append(i)
    data = zip(item, itemLen, price)
    return render(request, 'view_bill.html', context={'bill': bill, 'data': data})

