from django.db import models
from e_commerce.models import ShoppingCartItem
from django.contrib.sessions.models import Session


class Order(models.Model):
    session = models.ForeignKey(Session, on_delete=models.SET_NULL, null=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    ordered_on = models.DateTimeField(auto_now_add=True)


class OrderProduct(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    item = models.ForeignKey(ShoppingCartItem, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)


