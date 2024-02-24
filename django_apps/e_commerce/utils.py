from .models import ShoppingCart, ShoppingCartItem
from django.db import transaction
from django.contrib import messages

import stripe
from django.conf import settings


@transaction.atomic
def add_to_cart(request, product, quantity):
    session_key = request.session.session_key

    if not session_key:
        request.session.create()
        session_key = request.session.session_key
    
    cart = ShoppingCart.get_or_create_cart(session_key=session_key)
    item, created_item = ShoppingCartItem.objects.get_or_create(product=product, cart=cart)
    
    if product.stock < item.quantity + quantity:
        messages.error(request, "Product out of stock!")
        if product.stock == 0:
            item.delete()
        return None
    
    item.quantity += quantity
    item.save()
    cart.save()
    
    messages.success(request, f"Successfully added product! You have {item.quantity} {item.product.name}'s in your cart!")


@transaction.atomic
def remove_from_cart(request, product, quantity):
    session_key = request.session.session_key

    if not session_key:
        messages.error(request, "Session error: Your session doesn't exist. It must've expired. Try again")
        return None
    
    cart = ShoppingCart.get_or_create_cart(session_key=session_key)
    item = ShoppingCartItem.objects.get(product=product, cart=cart)
    
    item.quantity -= quantity
    item.save()
    if item.quantity <= 0:
        item.delete()
    cart.save()

    messages.success(request, f"Successfully removed product! You have {item.quantity} {item.product.name}'s in your cart!")


#  Payment processing will be added after completing the main backends
@transaction.atomic
def submit_payment(request, cart, total_price):
    stripe.api_key = settings.STRIPE_SECRET_KEY
    token = request.POST.get('stripeToken', None)
    # if token is None:
    #     messages.error(request, "Token not provided")
    #    return None
    
    amount = int(total_price * 100)

    # try:
    #    charge = stripe.Charge.create(
    #        amount=amount,
    #        description='Payment for products',
    #        source=token,
    #    )

    # Removes all the products from the cart. Subtracts quantity from each product's stock.
    items = ShoppingCartItem.objects.filter(cart=cart)
    
    if not items:
        messages.error(request, f"You have no products in your cart")
        return None
    
    for item in items:
        if item.product.stock < item.quantity:
            messages.error(request, f"One of your products is out of stock: {item.product}")
            return None
        
        item.product.stock -= item.quantity
        item.delete()
        item.product.save()
    cart.delete()

    messages.success(request, "Payment successful! Your order has been placed.")

    # except stripe.error.CardError as e:
    #     messages.error(request, f"Payment failed: {e.error.message}")
