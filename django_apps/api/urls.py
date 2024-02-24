from django.urls import path, include
from . import views

urlpatterns = [
    path('ecom/products/', views.ProductsView.as_view(), name='products_api'),
    path('ecom/products/<int:id>/<int:quantity>', views.ProductDetailView.as_view(), name='product_detail_api'),
    path('ecom/my-cart/', views.MyCartView.as_view(), name='my_cart_api')
]