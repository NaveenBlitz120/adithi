from django.forms import ModelForm
from order.models import product


class Create(ModelForm):
	class Meta:
		model = product
		fields = '__all__'

class Update(ModelForm):
	class Meta:
		model = product
		fields = [ 'price' , 'types' ]