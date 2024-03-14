from rest_framework import serializers as ser
from e_commerce.models import Product, ShoppingCartItem
from  django.contrib.sessions.models import Session


class ProductSer(ser.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'price', 'stock']


class ShoppingCartSer(ser.ModelSerializer):
    total_price = ser.SerializerMethodField()
    items = ser.SerializerMethodField()

    class Meta:
        model = Session
        fields = ['id', 'session_key', 'items', 'total_price']
            
    def get_items(self, obj):
        items = ShoppingCartItem.objects.filter(cart=obj)
        return items
    
    def get_total_price(self, obj):
        items = ShoppingCartItem.objects.filter(cart=obj)
        total_price = sum(item.quantity * item.product.price for item in items)
        return total_price


class ShoppingCartItemSer(ser.ModelSerializer):
    class Meta:
        model = ShoppingCartItem
        fields = ['id', 'product', 'quantity']


class PaymentSer(ser.Serializer):
    card_number = ser.CharField(max_length=16)
    card_expiry = ser.CharField(max_length=4)
    card_cvc = ser.CharField(max_length=3)