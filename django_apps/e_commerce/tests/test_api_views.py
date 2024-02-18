from django.contrib.auth.models import User
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient
from ..models import Product, ShoppingCart
from ..api.serializers import ProductSer, ShoppingCartSer

class ViewSetTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.product = Product.objects.create(name='Test Product', description='Description', price=10.0, stock=100)
        self.shopping_cart = ShoppingCart.objects.create(user=self.user)

    def test_products_viewset(self):
        response = self.client.get('/api/products/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['name'], 'Test Product')

    def test_add_to_cart_view(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.post(f'/api/add_to_cart/{self.shopping_cart.id}/', data={'product_id': self.product.id})
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        updated_cart = ShoppingCart.objects.get(id=self.shopping_cart.id)
        self.assertEqual(updated_cart.products.count(), 1)
        self.assertEqual(updated_cart.products.first().name, 'Test Product')
        