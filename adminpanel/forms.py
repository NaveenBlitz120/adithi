from django.forms import ModelForm
from order.models import product,orders,setcart,flower,service


class Create(ModelForm):
	class Meta:
		model = product
		fields = '__all__'

class CreateFlo(ModelForm):
	class Meta:
		model = flower
		fields = '__all__'
		exclude = ['types']

class CreateSer(ModelForm):
	class Meta:
		model = service
		fields = '__all__'

class Update(ModelForm):
	class Meta:
		model = product
		fields = [ 'our_price','market_price' , 'types' , 'name','image','product_avail' ]

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
		fields = [ 'our_price','market_price' , 'name','product_avail' ]

class Update_service(ModelForm):
	class Meta:
		model = service
		fields = '__all__'
