import django_filters
from order.models import product
from django_filters import CharFilter

class myFilter(django_filters.FilterSet):
    productname=CharFilter(field_name='name',lookup_expr='contains')

    class meta:
        model = product
        fields = ['name']
