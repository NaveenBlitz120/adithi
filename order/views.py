# from django.shortcuts import render

# Create your views here.
from django.shortcuts import render , redirect
from django.http import JsonResponse
import json
import datetime
from .models import *
from .utils import cookieCart, cartData, guestOrder
from .forms import checkoutform
from adminpanel.filters import myFilter

def store(request):

	data = cartData(request)
	cartItems = data['cartItems']
	order = data['order']
	items = data['items']
	products = product.objects.all()
	myfilter = myFilter(request.GET,queryset=products)
	prod_obj= myfilter.qs
	# test = product.objects.get(id=1)
	# print(test.types,'entered')
	context = {'products':prod_obj,'order':order,'cartItems':cartItems, 'filter':myfilter }
	return render(request, 'order/store.html', context)

def vegetables(request):
	data = cartData(request)
	cartItems = data['cartItems']
	order = data['order']
	items = data['items']
	products = product.objects.filter(category = 'vegetables')
	myfilter = myFilter(request.GET,queryset=products)
	prod_obj= myfilter.qs
	print(prod_obj)
	# test = product.objects.get(id=1)
	# print(test.types,'entered')
	context = {'products':prod_obj , 'filter':myfilter ,'order':order,'cartItems':cartItems }
	return render(request, 'order/store.html', context)


def fruits(request):

	data = cartData(request)
	cartItems = data['cartItems']
	order = data['order']
	items = data['items']
	products = product.objects.filter(category = 'fruits')
	myfilter = myFilter(request.GET,queryset=products)
	prod_obj= myfilter.qs
	print(prod_obj)
	# test = product.objects.get(id=1)
	# print(test.types,'entered')
	context = {'products':prod_obj,'order':order,'cartItems':cartItems, 'filter':myfilter }
	return render(request, 'order/store.html', context)

def groceries(request):

	data = cartData(request)
	cartItems = data['cartItems']
	order = data['order']
	items = data['items']
	products = product.objects.filter(category = 'groceries' )
	myfilter = myFilter(request.GET,queryset=products)
	prod_obj= myfilter.qs
	# test = product.objects.get(id=1)
	# print(test.types,'entered')
	context = {'products':prod_obj,'order':order,'cartItems':cartItems, 'filter':myfilter }
	return render(request, 'order/store.html', context)

def cart(request):

	data = cartData(request)
	cartItems = data['cartItems']
	order = data['order']
	items = data['items']
	context = {'items':items, 'order':order, 'cartItems':cartItems}
	return render(request, 'order/cart.html', context)

def checkout(request):
		# print(request)
		warning = ''
		data = cartData(request)
		checkout_data_form = checkoutform()
		checkout_data_form.fields['name'].widget.attrs = {'class' : 'form-control' ,'placeholder' : 'Name','id':'name'}
		checkout_data_form.fields['number'].widget.attrs = {'class' : 'form-control' ,'placeholder' : 'your phone number','pattern':"[0-9]{10}"}
		cartItems = data['cartItems']
		order = data['order']
		items = data['items']
		context = {'items':items, 'order':order, 'cartItems':cartItems,'checkout_data_form':checkout_data_form,'warning':warning}
		# print('hii')

		if request.method == 'POST':
			print('hiii')
			form = checkoutform(request.POST)
			if form.is_valid():
				print('hiii')
				where = guestOrder(request,form)
				if where:
					# response = redirect('store')
					# # response = request
					# print('here')
					# response.delete_cookie('cart')
					# print('inside1')

					return deletecookie(request,where)
				else:
					# response = redirect(where)
					warning ='minimum cart value is 200'
					print('inside2')
					context = {'items':items, 'order':order, 'cartItems':cartItems,'checkout_data_form':checkout_data_form,'warning':warning}
					return render(request, 'order/checkout.html', context)
			# return render(request, 'order/store.html', context)

		return render(request, 'order/checkout.html', context)


def htmlbill(request):
	# user = request.user
	ordered_id = request.COOKIES['orderid']
	print(ordered_id)
	bill = orders.objects.get(orderid = ordered_id)
	# order = Order.objects.get(complete=False,invoice_id=bill)
	bill_total = bill.orderfinaltotal
	# order_item = []
	order_item = orderedcart.objects.filter(orderedid = bill)
	context = {'order_item' : order_item, 'bill' : bill , 'bill_total':bill_total}
	return render(request, 'order/index.html',context)

def deletecookie(request,ordered_id):
	response = redirect('bill')
	response.delete_cookie('cart')
	response.set_cookie('orderid',ordered_id)
	return response

def deletecartcookie(request):
	response = redirect('store')
	response.delete_cookie('orderid')
	# response.set_cookie('orderid',ordered_id)
	return response
