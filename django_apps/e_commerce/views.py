from django.shortcuts import render, get_object_or_404, redirect
from .utils import add_to_cart, remove_from_cart
from .designs import choose_template
from .models import Product
from .context_processor import ecom_context

template = choose_template("ecom_style1")


def home_view(request):
    return render(request, template['home'], ecom_context(request))

def products_view(request):
    return render(request, template['products'], ecom_context(request))

def product_view(request, slug):
    return render(request, template['product'], ecom_context(request, slug=slug))

def my_shopping_cart(request):
    return render(request, template['cart'], ecom_context(request))

def checkout(request):
    return render(request, template['checkout'], ecom_context(request))


#  Utility views
def add_to_cart_view(request, slug, quantity=1):
    product = get_object_or_404(Product, slug=slug)
    add_to_cart(request, product, quantity)
    return redirect('product', product.slug)

def remove_from_cart_view(request, slug, quantity=1):
    product = get_object_or_404(Product, slug=slug)
    remove_from_cart(request, product, quantity)
    return redirect('cart')
