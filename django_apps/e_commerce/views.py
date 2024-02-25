from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, ShoppingCart, ShoppingCartItem
from .utils import add_to_cart, remove_from_cart, submit_payment
from django.conf import settings
from .forms import PaymentForm
from frontend.ecom.designs import choose_template


template = choose_template("ecom_style1")


def home_view(request):
    return render(request, template['home'])


def products_view(request):

    context = {
        "products": Product.objects.all(),
    }
    return render(request, template['products'], context)


def product_view(request, slug):
    product = get_object_or_404(Product, slug=slug)

    context = {
        "product": product
    }
    return render(request, template['product'], context)


def my_shopping_cart(request):
    cart = ShoppingCart.get_or_create_cart(request.session.session_key)
    items = ShoppingCartItem.objects.filter(cart=cart)
    price = sum(item.quantity * item.product.price for item in items)

    context = {
        "products": items,
        "price": price,
    }
    return render(request, template['cart'], context)


def checkout(request):
    form = PaymentForm()
    cart = ShoppingCart.get_or_create_cart(request.session.session_key)
    items = ShoppingCartItem.objects.filter(cart=cart)
    price = sum(item.quantity * item.product.price for item in items)

    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            submit_payment(request, cart, price)

    context = {
        "public_key": settings.STRIPE_PUBLIC_KEY,
        "form": form,
        "price": price
    }
    return render(request, template['checkout'], context)


#  Utility views
def add_to_cart_view(request, slug):
    product = get_object_or_404(Product, slug=slug)
    add_to_cart(request, product, 1)
    return redirect('product', product.slug)


def remove_from_cart_view(request, slug):
    product = get_object_or_404(Product, slug=slug)
    remove_from_cart(request, product, 1)
    return redirect('cart')
