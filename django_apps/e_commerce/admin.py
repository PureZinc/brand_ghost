from django.contrib import admin
from .models import Product, ShoppingCart

# Register your models here.
admin.site.register(Product)
admin.site.register(ShoppingCart)
