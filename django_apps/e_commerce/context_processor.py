from newsletter.forms import SubscribeForm
from newsletter.utils.utils import sub_to_newsletter
from .models import Product, ShoppingCartItem
from django.conf import settings
from .utils.cart_functions import get_cart
from django.shortcuts import get_object_or_404


def ecom_context(request, slug=None):
    session_key = get_cart(request)

    context_data = {}

    context_data["cart"] = session_key
    context_data["items"] = ShoppingCartItem.objects.filter(cart=context_data["cart"])
    context_data["price"] = sum(item.quantity * item.product.price for item in context_data["items"])
    context_data["public_key"] = str(settings.STRIPE_PUBLIC_KEY)
    context_data["products"] = Product.objects.filter(user=request.user)

    if slug:
        context_data["product"] = get_object_or_404(Product, slug=slug)

    return context_data