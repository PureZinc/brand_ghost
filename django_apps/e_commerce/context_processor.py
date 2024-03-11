from newsletter.forms import SubscribeForm
from .models import Product, ShoppingCartItem
from django.contrib.sessions.models import Session
from django.conf import settings
from newsletter.utils.utils import sub_to_newsletter
from django.shortcuts import get_object_or_404


def ecom_context(request, slug=None):
    session_key = request.session.session_key
    if not session_key:
        request.session.save()
        session_key = request.session.session_key

    context_data = {}

    context_data["cart"] = Session.objects.get(session_key=session_key)
    context_data["items"] = ShoppingCartItem.objects.filter(cart=context_data["cart"])
    context_data["price"] = sum(item.quantity * item.product.price for item in context_data["items"])
    context_data["public_key"] = str(settings.STRIPE_PUBLIC_KEY)
    context_data["products"] = Product.objects.all()
    context_data["subscribe_form"] = sub_to_newsletter(request, SubscribeForm)

    if slug:
        context_data["product"] = get_object_or_404(Product, slug=slug)

    return context_data