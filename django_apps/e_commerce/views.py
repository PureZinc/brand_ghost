from django.shortcuts import render, get_object_or_404, redirect
from .utils import add_to_cart, remove_from_cart
from .designs import choose_template
from newsletter.utils.utils import sub_to_newsletter
from newsletter.forms import SubscribeForm
from .models import Product, ShoppingCartItem
from django.contrib.sessions.models import Session
from django.conf import settings
from .models import Product

template = choose_template("ecom_style1")

def ecom_context(request, slug=None):
    context_data = {}

    session_key = request.session.session_key

    if not session_key:
        request.session.save()
        session_key = request.session.session_key

    context_data["cart"] = Session.objects.get(session_key=session_key)
    context_data["items"] = ShoppingCartItem.objects.filter(cart=context_data["cart"])
    context_data["price"] = sum(item.quantity * item.product.price for item in context_data["items"])
    context_data["public_key"] = str(settings.STRIPE_PUBLIC_KEY)
    context_data["products"] = Product.objects.all()

    context_data["product"] = None
    if slug:
        context_data["product"] = get_object_or_404(Product, slug=slug)

    return context_data


def home_view(request):
    form = sub_to_newsletter(request, SubscribeForm)

    context = {
        "subscribe_form": form
    }
    return render(request, template['home'], context)


def products_view(request):
    context = ecom_context(request)
    return render(request, template['products'], context)


def product_view(request, slug):
    context = ecom_context(request, slug=slug)
    return render(request, template['product'], context)


def my_shopping_cart(request):
    context = ecom_context(request)
    return render(request, template['cart'], context)


def checkout(request):
    context = ecom_context(request)
    return render(request, template['checkout'], context)


#  Utility views
def add_to_cart_view(request, slug, quantity=1):
    product = get_object_or_404(Product, slug=slug)
    add_to_cart(request, product, quantity)
    return redirect('product', product.slug)


def remove_from_cart_view(request, slug, quantity=1):
    product = get_object_or_404(Product, slug=slug)
    remove_from_cart(request, product, quantity)
    return redirect('cart')
