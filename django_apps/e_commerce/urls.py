from django.urls import path
from . import views

urlpatterns = [
    path('products/', views.products_view, name='products'),
    path('products/<slug:slug>/', views.product_view, name='product'),
    path('products/<slug:slug>/add_to_cart/', views.add_to_cart_view, name='add_to_cart'),
    path('shoppingcart/', views.my_shopping_cart, name='cart'),
    path('shopingcart/remove/<slug:slug>/', views.remove_from_cart_view, name='remove_from_cart'),
    path('checkout/', views.checkout, name='checkout')
]