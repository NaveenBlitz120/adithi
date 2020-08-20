from django import forms

class checkoutform(forms.Form):
    name = forms.CharField(max_length=20)
    number = forms.CharField(max_length=10)
