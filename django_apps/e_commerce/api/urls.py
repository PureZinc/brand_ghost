from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductsViewSet, AddToCartView

router = DefaultRouter()
router.register(r'products', ProductsViewSet)

urlpatterns = [
    path('ecom/', include(router.urls)),
    path('ecom/add-to-cart/', AddToCartView.as_view(), name='add_to_cart_api'),
]