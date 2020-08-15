# from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import JsonResponse
import json
import datetime
from .models import *
from .utils import cookieCart, cartData, guestOrder

def store(request):
	data = cartData(request)

	cartItems = data['cartItems']
	order = data['order']
	items = data['items']

	products = product.objects.all()
	test = product.objects.get(id=1)
	print(test)
	context = {'products':products, 'cartItems':cartItems}
	return render(request, 'order/store.html', context)


def cart(request):
	data = cartData(request)

	cartItems = data['cartItems']
	order = data['order']
	items = data['items']

	context = {'items':items, 'order':order, 'cartItems':cartItems}
	return render(request, 'order/cart.html', context)

def checkout(request):
	data = cartData(request)

	cartItems = data['cartItems']
	order = data['order']
	items = data['items']

	context = {'items':items, 'order':order, 'cartItems':cartItems}
	return render(request, 'order/checkout.html', context)

def updateItem(request):
	data = json.loads(request.body)
	productId = data['productId']
	action = data['action']
	print('Action:', action)
	print('Product:', productId)

	# customer = request.user.customer
	product = product.objects.get(id=productId)
	order, created = orderedcart.objects.get_or_create(customer=customer, complete=False)

	# orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

	if action == 'add':
		orderedcart.quantity = (orderItem.quantity + 1)
	elif action == 'remove':
		orderedcart.quantity = (orderItem.quantity - 1)

	orderItem.save()

	if orderItem.quantity <= 0:
		orderItem.delete()

	return JsonResponse('Item was added', safe=False)

def processOrder(request):
	# transaction_id = datetime.datetime.now().timestamp()
	# data = json.loads(request.body)
	#
	#
	# customer, order = guestOrder(request, data)
	#
	# total = float(data['form']['total'])
	# # order.transaction_id = transaction_id
	#
	# if total == order.get_cart_total:
	# 	order.complete = True
	# order.save()


	return JsonResponse('Payment submitted..', safe=False)
