from django import forms
from django.forms import ModelForm
from order.models import feedback,orders

class checkoutform(ModelForm):
    class Meta:
        model = orders
        fields = ['name','phoneno','address','area']


class Create(ModelForm):
	class Meta:
		model = feedback
		fields = '__all__'
