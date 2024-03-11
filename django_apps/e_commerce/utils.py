from .models import ShoppingCartItem
from django.db import transaction
from django.contrib import messages
from payment_processing.utils import payment_process
from django_apps.utils import get_session
from payment_processing.models import Order, OrderProduct


@transaction.atomic
def add_to_cart(request, product, quantity):
    session = get_session(request)
    item, created_item = ShoppingCartItem.objects.get_or_create(product=product, cart=session)
    
    if product.stock < item.quantity + quantity:
        messages.error(request, "Product out of stock!")
        if product.stock == 0:
            item.delete()
        return None
    
    item.quantity += quantity
    item.save()
    
    messages.success(request, f"Successfully added product! You have {item.quantity} {item.product.name}'s in your cart!")


@transaction.atomic
def remove_from_cart(request, product, quantity):
    session = get_session(request)
    item, created_item = ShoppingCartItem.objects.get_or_create(product=product, cart=session)
    
    item.quantity -= quantity
    item.save()
    if item.quantity <= 0:
        item.delete()

    messages.success(request, f"Successfully removed product! You have {item.quantity} {item.product.name}'s in your cart!")


@transaction.atomic
@payment_process
def submit_payment(request, total_price, cart):
    items = ShoppingCartItem.objects.filter(cart=cart)
    order = Order.objects.create(session=session, amount=total_price)
    
    if not items:
        messages.error(request, f"You have no products in your cart")
        return None
    
    for item in items:
        if item.product.stock < item.quantity:
            messages.error(request, f"One of your products is out of stock: {item.product}")
            return None
        
        item.product.stock -= item.quantity

        session = get_session(request)

        OrderProduct.objects.create(order=order, item=item, quantity=item.quantity)
        
        item.delete()
        item.product.save()

    messages.success(request, "Payment successful! Your order has been placed.")
