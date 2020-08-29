import django_filters
from order.models import product,orders,flower
from django_filters import CharFilter , ChoiceFilter
from django import forms

class myFilter(django_filters.FilterSet):
    productname=CharFilter(field_name='name',lookup_expr='contains',widget=forms.TextInput(attrs={'placeholder':'what are you looking for?'}))

    class meta:
        model = product
        fields = ['name']

class floFilter(django_filters.FilterSet):
    productname=CharFilter(field_name='name',lookup_expr='contains',widget=forms.TextInput(attrs={'placeholder':'what are you looking for?'}))

    class meta:
        model = flower
        fields = ['name']

Status_Choices = (
        ('pending' , 'pending'),
        ('orderconfirmed' , 'orderconfirmed'),
        ('cancelled' , 'cancelled'),
        ('completed' , 'completed'),
    )

class orderFilter(django_filters.FilterSet):
    status = ChoiceFilter(choices=Status_Choices)
    class meta:
        model = orders
        fields = [ 'status']
