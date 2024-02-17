from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductsViewSet, CartViewSet

router = DefaultRouter()
router.register(r'products', ProductsViewSet)
router.register(r'carts', CartViewSet)

urlpatterns = [
    path('ecom/', include(router.urls)),
]