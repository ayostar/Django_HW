import products as products
from rest_framework.filters import SearchFilter
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.viewsets import ModelViewSet

from logistic.models import Product, Stock
from logistic.serializers import ProductSerializer, StockSerializer


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [SearchFilter]
    search_fields = ['title', 'description']
    pagination_class = LimitOffsetPagination


class ProductSearchFilter(SearchFilter):
    search_param = 'products'

class StockViewSet(ModelViewSet):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer
    filter_backends = [ProductSearchFilter]
    pagination_class = LimitOffsetPagination
    search_fields = [
        # products.id, products.title, products.description
        'products__id', 'products__title', 'products__description'
    ]
