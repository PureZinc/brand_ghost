from django.urls import path
from . import views

urlpatterns = [
    path('products/', views.ProductsView.as_view(), name='products'),
    path('products/<slug:slug>', views.ProductDetailView.as_view(), name='product_detail'),
    path('products/create/', views.CreateProductView.as_view(), name='create_product'),
    path('products/add_to_cart/<slug:slug>', views.add_to_cart_view, name='add_to_cart'),
    path('shopingcart/remove/<slug:slug>', views.remove_from_cart_view, name='remove_from_cart'),
]
