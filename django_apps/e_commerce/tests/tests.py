from django.test import TestCase
from ..models import Product, ShoppingCart

# Create your tests here.

class TestModels(TestCase):
    def setUp(self) -> None:
        Product.objects.create(
            name="Test Product", 
            description="Testing product",
            price=10,
            stock=5
        )
    
    def test_model_creation(self):
        obj = Product.objects.get(name="Test Product")
        self.assertEqual(obj.price, 20)
