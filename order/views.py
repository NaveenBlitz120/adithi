# from django.shortcuts import render

# Create your views here.
from django.shortcuts import render , redirect
from django.http import JsonResponse
import json
import datetime
from .models import *
from .utils import cookieCart, cartData, guestOrder
from .forms import checkoutform,Create
from adminpanel.filters import myFilter

def store(request):

	data = cartData(request)
	cartItems = data['cartItems']
	order = data['order']
	items = data['items']
	products = product.objects.all()
	myfilter = myFilter(request.GET,queryset=products)
	lis = [250,500,750]
	prod_obj= myfilter.qs
	print(prod_obj)
	# test = product.objects.get(id=1)
	# print(test.types,'entered')
	context = {'products':prod_obj,'order':order,'cartItems':cartItems, 'filter':myfilter,'list':lis }
	return render(request, 'order/store.html', context)

def vegetables(request):
	data = cartData(request)
	cartItems = data['cartItems']
	order = data['order']
	items = data['items']
	products = product.objects.filter(category = 'vegetables')
	myfilter = myFilter(request.GET,queryset=products)
	prod_obj= myfilter.qs
	lis = [250,500,750]
	print(prod_obj)
	# test = product.objects.get(id=1)
	# print(test.types,'entered')
	context = {'products':prod_obj , 'filter':myfilter ,'order':order,'cartItems':cartItems,'list':lis }
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
	lis = [250,500,750]
	# test = product.objects.get(id=1)
	# print(test.types,'entered')
	context = {'products':prod_obj,'order':order,'cartItems':cartItems, 'filter':myfilter,'list':lis }
	return render(request, 'order/store.html', context)

def groceries(request):

	data = cartData(request)
	cartItems = data['cartItems']
	order = data['order']
	items = data['items']
	products = product.objects.filter(category = 'groceries' )
	lis = [250,500,750]
	myfilter = myFilter(request.GET,queryset=products)
	prod_obj= myfilter.qs
	# test = product.objects.get(id=1)
	# print(test.types,'entered')
	context = {'products':prod_obj,'order':order,'cartItems':cartItems, 'filter':myfilter ,'list':lis}
	return render(request, 'order/grocery.html', context)

def nuts(request):

	data = cartData(request)
	cartItems = data['cartItems']
	order = data['order']
	items = data['items']
	products = product.objects.filter(category = 'groceries' ,groceries_category='nuts')
	myfilter = myFilter(request.GET,queryset=products)
	prod_obj= myfilter.qs
	lis = [250,500,750]
	# test = product.objects.get(id=1)
	# print(test.types,'entered')
	context = {'products':prod_obj,'order':order,'cartItems':cartItems, 'filter':myfilter,'list':lis }
	return render(request, 'order/grocery.html', context)

def kitchencleaners(request):

	data = cartData(request)
	cartItems = data['cartItems']
	order = data['order']
	items = data['items']
	products = product.objects.filter(category = 'groceries' ,groceries_category='kitchen-cleaners')
	myfilter = myFilter(request.GET,queryset=products)
	prod_obj= myfilter.qs
	lis = [250,500,750]
	# test = product.objects.get(id=1)
	# print(test.types,'entered')
	context = {'products':prod_obj,'order':order,'cartItems':cartItems, 'filter':myfilter ,'list':lis}
	return render(request, 'order/grocery.html', context)

def daals(request):

	data = cartData(request)
	cartItems = data['cartItems']
	order = data['order']
	items = data['items']
	products = product.objects.filter(category = 'groceries',groceries_category='dhaals' )
	myfilter = myFilter(request.GET,queryset=products)
	prod_obj= myfilter.qs
	lis = [250,500,750]
	# test = product.objects.get(id=1)
	# print(test.types,'entered')
	context = {'products':prod_obj,'order':order,'cartItems':cartItems, 'filter':myfilter ,'list':lis}
	return render(request, 'order/grocery.html', context)

def oils(request):

	data = cartData(request)
	cartItems = data['cartItems']
	order = data['order']
	items = data['items']
	products = product.objects.filter(category = 'groceries',groceries_category='oils' )
	myfilter = myFilter(request.GET,queryset=products)
	prod_obj= myfilter.qs
	lis = [250,500,750]
	# test = product.objects.get(id=1)
	# print(test.types,'entered')
	context = {'products':prod_obj,'order':order,'cartItems':cartItems, 'filter':myfilter,'list':lis }
	return render(request, 'order/grocery.html', context)

def flowers(request):

	data = cartData(request)
	cartItems = data['cartItems']
	order = data['order']
	items = data['items']
	floweritems = data['floweritems']

	flowers = flower.objects.all()
	myfilter = myFilter(request.GET,queryset=flowers)
	flow_obj= myfilter.qs
	# test = product.objects.get(id=1)
	# print(test.types,'entered')
	context = {'flowers':flow_obj,'order':order,'cartItems':cartItems, 'filter':myfilter ,'list':lis}
	return render(request, 'order/store.html', context)

def cart(request):

	data = cartData(request)
	print(data,'here')
	cartItems = data['cartItems']
	order = data['order']
	items = data['items']
	floweritems = data['floweritems']
	context = {'items':items, 'floweritems':floweritems, 'order':order, 'cartItems':cartItems}
	return render(request, 'order/cart.html', context)

def checkout(request):
		# print(request)
		warning = ''
		data = cartData(request)
		checkout_data_form = checkoutform()
		checkout_data_form.fields['name'].widget.attrs = {'placeholder' : 'Name','id':'name'}
		checkout_data_form.fields['number'].widget.attrs = {'placeholder' : 'your phone number','pattern':"[0-9]{10}"}
		checkout_data_form.fields['address'].widget.attrs = {'id' : 'autocomplete' ,'placeholder' : 'your Address Here or locate yourself ---->'}
		cartItems = data['cartItems']
		order = data['order']
		items = data['items']
		floweritems = data['floweritems']
		context = {'items':items, 'order':order, 'floweritems':floweritems,'cartItems':cartItems,'checkout_data_form':checkout_data_form,'warning':warning}
		# print('hii')

		if request.method == 'POST':
			print('hiii')
			form = checkoutform(request.POST)
			if form.is_valid():
				print('hiii')
				where = guestOrder(request,form)
				if where:
					return deletecookie(request,where)
				else:
					# response = redirect(where)
					warning ='minimum cart value is 200'
					print('inside2')
					context = {'items':items, 'order':order, 'floweritems':floweritems,'cartItems':cartItems,'checkout_data_form':checkout_data_form,'warning':warning}
					return render(request, 'order/checkout.html', context)
			# return render(request, 'order/store.html', context)

		return render(request, 'order/checkout.html', context)


def htmlbill(request):
	ordered_id = request.COOKIES['orderid']
	print(ordered_id)
	print('hiiiis')
	fbform = Create()
	print(fbform,'hereiiii')
	fbform.fields['name'].widget.attrs = {'placeholder' : 'Your Name goes here','id':'name'}
	fbform.fields['feedbackdata'].widget.attrs = {'placeholder' : 'Your Message will be placed here,,,,,','id':'message'}
	bill = orders.objects.get(orderid = ordered_id)
	bill_total = bill.orderfinaltotal
	order_item = orderedcart.objects.filter(orderedid = bill)
	context = {'order_item' : order_item, 'bill' : bill , 'bill_total':bill_total ,'form':fbform}
	if request.method == 'POST':
		form = Create(request.POST)
		print(form)
		if form.is_valid():
			print('hiii')
			form.save()
			return redirect('deletecartcookie')
	return render(request, 'order/index.html',context)

def deletecookie(request,ordered_id):
	response = redirect('bill')
	response.delete_cookie('cart')
	response.delete_cookie('flower')
	response.set_cookie('orderid',ordered_id)
	return response

def deletecartcookie(request):
	response = redirect('store')
	response.delete_cookie('orderid')
	# response.set_cookie('orderid',ordered_id)
	return response
