from django import forms
from django.forms import ModelForm
from order.models import feedback

class checkoutform(forms.Form):
    name = forms.CharField(max_length=20)
    number = forms.CharField(max_length=10)
    address = forms.CharField(max_length=200)

class Create(ModelForm):
	class Meta:
		model = feedback
		fields = '__all__'
