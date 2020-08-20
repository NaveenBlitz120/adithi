# from django.shortcuts import render

# Create your views here.
from django.shortcuts import render , redirect
from django.http import JsonResponse
import json
import datetime
from .models import *
from .utils import cookieCart, cartData, guestOrder
from .forms import checkoutform

def store(request):

	data = cartData(request) 
	cartItems = data['cartItems']
	order = data['order']
	items = data['items']
	products = product.objects.all()
	test = product.objects.get(id=1)
	print(test.types,'entered')
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
		print(request)	
		if request.method == 'GET':
			print('hiii')
			form = checkoutform(request.GET)
			if form.is_valid():
				print('hiii')
				guestOrder(request,form) 
				return redirect('store')
			# return render(request, 'order/store.html', context)
		data = cartData(request)
		checkout_data_form = checkoutform()
		checkout_data_form.fields['name'].widget.attrs = {'class' : 'form-control' ,'placeholder' : 'Name','id':'name'}
		checkout_data_form.fields['number'].widget.attrs = {'class' : 'form-control' ,'placeholder' : 'your phone number','pattern':"[0-9]{10}"}
		cartItems = data['cartItems']
		order = data['order']
		items = data['items']
		context = {'items':items, 'order':order, 'cartItems':cartItems,'checkout_data_form':checkout_data_form}
		print('hii')
		return render(request, 'order/checkout.html', context)
#
def updateItem(request):
# 	data = json.loads(request.body)
# 	productId = data['productId']
# 	action = data['action']
# 	print('Action:', action)
# 	print('Product:', productId)
#
# 	# customer = request.user.customer
# 	products = product.objects.get(id=productId)
# 	# order, created = orderedcart.objects.get_or_create(customer=customer, complete=False)
#
# 	# orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)
#
# 	if action == 'add':
# 		products.quantity = (products.quantity + 1)
# 	elif action == 'remove':
# 		products.quantity = (products.quantity - 1)
#
# 	# orderedcart.save()
#
# 	if orderItem.quantity <= 0:
# 		products.delete()
#
	return JsonResponse('Item was added', safe=False)

def processOrder(request):
	# transaction_id = datetime.datetime.now().timestamp()
	data = json.loads(request.body)
	print(data)
	#
	guestOrder(request, data)
	#
	# total = float(data['form']['total'])
	# # order.transaction_id = transaction_id
	#
	# if total == order.get_cart_total:
	# 	order.complete = True


	return JsonResponse(safe=False)
