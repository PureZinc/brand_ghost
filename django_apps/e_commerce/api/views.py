from rest_framework import viewsets
from ..models import Product, ShoppingCart
from .serializers import ProductSer, ShoppingCartSer


class ProductsViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSer


class CartViewSet(viewsets.ModelViewSet):
    queryset = ShoppingCart.objects.all()
    serializer_class = ShoppingCartSer
