from django import forms
from django.forms import ModelForm
from order.models import feedback,orders

class checkoutform(ModelForm):
    class Meta:
        model = orders
        fields = ['name','phoneno','address','area']
        # widget={'area':forms.TextInput(attrs={'placeholder':'search'})}

class Create(ModelForm):
	class Meta:
		model = feedback
		fields = '__all__'
