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
	cartItems = order['get_cart_items']

	for i in cart:
		#We use try block to prevent items in cart that may have been removed from causing error
		try:
			# print(i)
			cartItems += cart[i]['quantity']
			products = product.objects.get(id=i)
			print(i)
			total = (products.price * cart[i]['quantity'])
			print(product)
			order['get_cart_total'] += total
			order['get_cart_items'] += cart[i]['quantity']

			item = {
				'id':products.id,
				'product':{
					'id':products.id,
					'name':products.name,
					'price':products.price,
				        'imageURL':products.image.url
					},
				'quantity':cart[i]['quantity'],
				# 'digital':product.digital,
				'get_total':total,
				}
			print(item)
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
	name = data['form']['name']
	orderid = data['form']['email']

	cookieData = cookieCart(request)
	items = cookieData['items']

	orders = orders.objects.create(
			orderid=orderid,
			)
	orders.name = name
	orders.save()

	# order = Order.objects.create(
	# 	customer=customer,
	# 	complete=False,
	# 	)

	for item in items:
		product = Product.objects.get(id=item['id'])
		ordercart = orderedcart.objects.create(
			product=product,
			orderedid=orderid,
			quantity=item['quantity'],
			pidtotal=item['get_total'],
		)
	return orders, order
