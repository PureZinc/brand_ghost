from rest_framework import serializers as ser
from ..models import Product, ShoppingCart


class ProductSer(ser.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'price', 'stock']


class ShoppingCartSer(ser.ModelSerializer):
    total_price = ser.SerializerMethodField()

    class Meta:
        model = ShoppingCart
        fields = ['id', 'user', 'products']
    
    def get_total_price(self, obj):
        products = obj.products.all()
        total_price = sum(product.price for product in products)
        return total_price
