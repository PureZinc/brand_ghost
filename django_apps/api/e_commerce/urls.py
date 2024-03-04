from django.urls import path
from . import views

urlpatterns = [
    path('products/', views.ProductsView.as_view(), name='products_api'),
    path('products/<int:id>/<int:quantity>', views.ProductDetailView.as_view(), name='product_detail_api'),
    path('my-cart/', views.MyCartView.as_view(), name='my_cart_api')
]