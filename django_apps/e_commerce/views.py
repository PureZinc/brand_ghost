from django.shortcuts import render, get_object_or_404, redirect
from .utils.cart_functions import add_to_cart, remove_from_cart
from .models import Product
from .context_processor import ecom_context


def choose_template(design):
    return {
        'products': f"{design}/products.html",
        'product': f"{design}/productDetails.html",
        'cart': f"{design}/shoppingcart.html",
        'checkout' : f"{design}/checkout.html",
    }


template = choose_template("e_commerce")


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
