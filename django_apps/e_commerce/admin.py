from django.contrib import admin
from .models import Product, ShoppingCartItem, ProductImage
from django.contrib.sessions.models import Session

# Register your models here.
admin.site.register(Product)
admin.site.register(ShoppingCartItem)
admin.site.register(Session)
admin.site.register(ProductImage)
