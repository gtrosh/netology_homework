from django_filters import rest_framework as filters

from .models import Stock, Product

class StockFilter(filters.FilterSet):
    products = filters.NumberFilter(field_name='products__id')

    class Meta:
        model = Stock
        fields = ('products',)