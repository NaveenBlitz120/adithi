from django.forms import ModelForm
from order.models import product,orders,setcart,flower


class Create(ModelForm):
	class Meta:
		model = product
		fields = '__all__'

class Update(ModelForm):
	class Meta:
		model = product
		fields = [ 'our_price','market_price' , 'types' , 'name' ]

class Update_order(ModelForm):
	class Meta:
		model = orders
		fields = [ 'status' ]

class Update_offer(ModelForm):
	class Meta:
		model = setcart
		fields = '__all__'

class Update_flower(ModelForm):
	class Meta:
		model = flower
		fields = [ 'our_price','market_price' , 'name' ]
