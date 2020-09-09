import json
import urllib.request
import urllib.parse
from .models import *

def cookieCart(request):

	#Create empty cart for now for non-logged in user
	try:
		cart = json.loads(request.COOKIES['cart'])
		flo = json.loads(request.COOKIES['flower'])
	except:
		cart = {}
		flo = {}
		print('CART:', cart)

	items = []
	floitems = []
	order = {'get_cart_total':0, 'get_cart_items':0}
	order['get_cart_items'] += len(cart)+len(flo)
	cartItems = order['get_cart_items']

	for i in flo:
		try:
			flowers = flower.objects.get(id=i)
			# print(flowers.our_price,'entered')
			total = round((flowers.our_price * flo[i]['quantity']),2)
			order['get_cart_total'] += total
			if flowers.image:
				image_check = flowers.image.url
			else:
				image_check = None
			floitem = {
				'id':flowers.id,
				'product':{
					'id':flowers.id,
					'name':flowers.name,
					'price':flowers.our_price,
					'imageURL':image_check,
					'category':flowers.category,
					},
				'quantity':flo[i]['quantity'],
				# 'digital':product.digital,
				'get_total':round(total,2),
			}
			# print(floitem['product']['type'],floitem['quantity'])
			if floitem['product']['category'] != 'count':
				if floitem['product']['category'] != 'maalai':
					if floitem['product']['category'] != 'mulam':
						if floitem['product']['category'] != 'bunch':
							if floitem['quantity']!=0:
								if(floitem['quantity']>=1 ):
									floitem['product']['category'] = 'kg'
								elif (floitem['quantity']<1):
									# print('enterd')
									floitem['product']['category'] = 'grams'

			if floitem['product']['category'] == 'grams':
				# print('entered')
				floitem['quantity'] = floitem['quantity'] * 1000

			# print(floitem)
			floitems.append(floitem)
			print(floitem)

		except:
			print('escaped')
			pass

	for i in cart:
		#We use try block to prevent items in cart that may have been removed from causing error
		try:
			# print(i)
			# cartItems += cart[i]['quantity']
			products = product.objects.get(id=i)
			total = round((products.our_price * cart[i]['quantity']),2)
			print('i')
			# print(products)
			if products.image:
				image_check = products.image.url
			else:
				image_check = None
			order['get_cart_total'] += total
			item = {
				'id':products.id,
				'product':{
					'id':products.id,
					'name':products.name,
					'price':products.our_price,

				    'imageURL':image_check,
					'type':products.types
					},
				'quantity':cart[i]['quantity'],
				# 'digital':product.digital,
				'get_total':round(total,2),
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

	return {'cartItems':cartItems ,'order':order, 'items':items , 'floweritems' : floitems}

def cartData(request):
	cookieData = cookieCart(request)
	cartItems = cookieData['cartItems']
	order = cookieData['order']
	items = cookieData['items']
	floweritems = cookieData['floweritems']
	return {'cartItems':cartItems ,'order':order, 'items':items , 'floweritems':floweritems}


def guestOrder(request, data):
	cust_name = data.cleaned_data['name']#changed
	phonenum = data.cleaned_data['phoneno']
	add = data.cleaned_data['address']
	area_selected = data.cleaned_data['area']
	# orderid = '#ae'+str(int(old_orderid.orderid[2:])+1)
	cookieData = cookieCart(request)
	items = cookieData['items']
	floweritems = cookieData['floweritems']
	order_total_calculated = 0
	for item in items:
		order_total_calculated = order_total_calculated+item['get_total']

	for item in floweritems:
		order_total_calculated = order_total_calculated+item['get_total']

	requirement = setcart.objects.get(id = 1)
	if order_total_calculated < requirement.minimum_cart_value:
		return False

	old_orderid_object = orders.objects.last()
	old_orderid = old_orderid_object.id
	new_orderid = '#aecid'+str(old_orderid)

	# cookieData = cookieCart(request)
	# items = cookieData['items']

	new_order = orders.objects.create(orderid = new_orderid,name = cust_name,phoneno = phonenum,ordertotal=0 ,address = add,area=area_selected)
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
			quantity_type = item['product']['type']
		)
		ordercart.save()
	for item in floweritems:
		order_total_calculated = order_total_calculated+item['get_total']
		products = flower.objects.get(id=item['id'])
		ordercart = orderedcart.objects.create(
			pfid=products,
			orderedid=new_order,
			quantity=item['quantity'],
			pidtotal=item['get_total'],
			quantity_type = item['product']['category']
		)
		ordercart.save()

	offerpercenttage = 0
	service_charge = service.objects.get(area = area_selected)
	update_order = orders.objects.get(orderid=new_orderid)
	order_total_calculated = order_total_calculated + service_charge.rate

	update_order.ordertotal =  round(order_total_calculated,2)
	if requirement.offer_on_or_off == 'on':
		if order_total_calculated >= requirement.silveroff_value:
			offerpercenttage = requirement.silveroff_percentage
			if order_total_calculated >= requirement.goldenoff_value:
				offerpercenttage = requirement.goldenoff_percentage
				if order_total_calculated >= requirement.platinumoff_value:
					offerpercenttage = requirement.platinumoff_percentage


	if offerpercenttage:
		update_order.offer = offerpercenttage
		offerpercenttage = offerpercenttage/100
		amount_reduction = order_total_calculated * offerpercenttage
		order_total_calculated = order_total_calculated - amount_reduction

	update_order.orderfinaltotal =  round(order_total_calculated,2)

	resp =  sendSMS('tjscNy0t/Wc-uAvFTKR7036IdflMIH71wcCasC1DPf', '91'+phonenum,'TXTLCL', 'HI !!!'+cust_name+' your order has been placed Successfully You can track order with order ID :'+update_order.orderid+' Someone from our side will contact you soon and confirm the order. Please ,visit us again at adithiecart.herokuapp.com')
	print (resp)
	update_order.save()
	return new_orderid


def sendSMS(apikey, numbers, sender, message):
    data =  urllib.parse.urlencode({'apikey': apikey, 'numbers': numbers,'message' : message, 'sender': sender})
    data = data.encode('utf-8')
    request = urllib.request.Request("https://api.textlocal.in/send/?")
    f = urllib.request.urlopen(request, data)
    fr = f.read()
    return(fr)
