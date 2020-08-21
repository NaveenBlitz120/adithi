import json
from .models import *

def cookieCart(request):

	#Create empty cart for now for non-logged in user
	try:
		cart = json.loads(request.COOKIES['cart'])
	except:
		cart = {}
		print('CART:', cart)

	items = []
	order = {'get_cart_total':0, 'get_cart_items':0, 'shipping':False}
	order['get_cart_items'] += len(cart)
	cartItems = order['get_cart_items']
	for i in cart:
		#We use try block to prevent items in cart that may have been removed from causing error
		try:
			# print(i)
			# cartItems += cart[i]['quantity']
			products = product.objects.get(id=i)
			total = (products.price * cart[i]['quantity'])
			# print(products)
			order['get_cart_total'] += total
			item = {
				'id':products.id,
				'product':{
					'id':products.id,
					'name':products.name,
					'price':products.price,
				    'imageURL':products.image.url,
					'type':products.type
					},
				'quantity':cart[i]['quantity'],
				# 'digital':product.digital,
				'get_total':total,
				}
			# print(i,'entered')
			print(item['product']['type'],item['quantity'])
			if item['product']['type'] != 'count':
				if item['quantity']!=0:
					if(item['quantity']>=1 ):
						item['product']['type'] = 'kg'
					elif (item['quantity']<1):
						# print('enterd')
						item['product']['type'] = 'grams'

			if item['product']['type'] == 'grams':
				# print('entered')
				item['quantity'] = item['quantity'] * 1000

			print(item['product']['type'],item['quantity'])
			items.append(item)


		except:
			print('escaped')
			pass

	return {'cartItems':cartItems ,'order':order, 'items':items}

def cartData(request):
	cookieData = cookieCart(request)
	cartItems = cookieData['cartItems']
	order = cookieData['order']
	items = cookieData['items']

	return {'cartItems':cartItems ,'order':order, 'items':items}


def guestOrder(request, data):
	# cust_name = data['form']['name']
	# phonenum = data['form']['phonenumber']
	cust_name = data.cleaned_data['name']#changed
	phonenum = data.cleaned_data['number']#changed
	old_orderid_object = orders.objects.last()
	# orderid = '#ae'+str(int(old_orderid.orderid[2:])+1)
	old_orderid = old_orderid_object.id
	new_orderid = '#aecid'+str(old_orderid)

	cookieData = cookieCart(request)
	items = cookieData['items']

	new_order = orders.objects.create(orderid = new_orderid,name = cust_name,phoneno = phonenum,ordertotal=0)
	# new_order.orderid = new_orderid
	# new_order.name = name
	# new_order.phoneno = phonenum
	# new_order.save()


	# order = Order.objects.create(
	# 	customer=customer,
	# 	complete=False,
	# 	)
	order_total_calculated = 0

	for item in items:
		order_total_calculated = order_total_calculated+item['get_total']
		products = product.objects.get(id=item['id'])
		ordercart = orderedcart.objects.create(
			pid=products,
			orderedid=new_order,
			quantity=item['quantity'],
			pidtotal=item['get_total'],
		)
		ordercart.save()
	update_order = orders.objects.get(orderid=new_orderid)
	# update_order.phoneno = data['form']['phonenumber']
	update_order.ordertotal =  order_total_calculated
	update_order.save()
	# return orders, order
