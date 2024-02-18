from rest_framework import viewsets
from rest_framework import generics
from rest_framework.response import Response
from ..models import Product, ShoppingCart
from .serializers import ProductSer, ShoppingCartSer
from ..utils import add_to_cart, remove_from_cart, submit_payment

# This is an unfinished file! Do not use yet!


class ProductsViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSer


class AddToCartView(generics.RetrieveUpdateAPIView):
    serializer_class = ShoppingCartSer
    
    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            queryset = ShoppingCart.objects.filter(user=user)
        else:
            queryset = ShoppingCart.objects.none()
        return queryset

    def post(self, serializer):
        instance = serializer.instance
        products = instance.products.all()

        for product in products:
            add_to_cart(self.request, product)

        serializer.save()

