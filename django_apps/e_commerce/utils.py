from .models import ShoppingCart
from django.db import transaction
from django.contrib import messages

import stripe
from django.conf import settings


@transaction.atomic
def add_to_cart(request, product):
    if product.stock <= 0:
        messages.error(request, "Product out of stock!")
        return None
    
    cart, created = ShoppingCart.objects.get_or_create(user=request.user)

    if cart.products.filter(id=product.id).exists():
        messages.error(request, "Product already added to your cart!")
        return None
    
    cart.products.add(product)
    product.stock -= 1
    cart.save()
    product.save()
    messages.success(request, "Product successfully added to your cart!")


@transaction.atomic
def remove_from_cart(request, product):
    cart = ShoppingCart.objects.get(user=request.user)

    cart.products.remove(product)
    product.stock += 1
    cart.save()
    product.save()
    return "Product removed!"


@transaction.atomic
def submit_payment(request, cart, total_price):
    stripe.api_key = settings.STRIPE_SECRET_KEY
    token = request.POST.get('stripeToken', None)
    if token is None:
        messages.error(request, "Token not provided")
        return None
    
    amount = int(total_price * 100)

    try:
        charge = stripe.Charge.create(
            amount=amount,
            currency='usd',
            description='Payment for products',
            source=token,
        )

            # Payment successful
        cart.delete()
        messages.success(request, "Payment successful! Your order has been placed.")

    except stripe.error.CardError as e:
        messages.error(request, f"Payment failed: {e.error.message}")
