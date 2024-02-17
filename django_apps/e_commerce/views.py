from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, ShoppingCart
from .utils import add_to_cart, remove_from_cart, submit_payment
from django.conf import settings
from .forms import PaymentForm


def products_view(request):
    context = {
        "products": Product.objects.all(),
    }
    return render(request, "e_commerce/products.html", context)


def product_view(request, slug):
    product = get_object_or_404(Product, slug=slug)

    context = {
        "product": product
    }
    return render(request, "e_commerce/productDetails.html", context)


def my_shopping_cart(request):
    cart = ShoppingCart.objects.get(user=request.user)
    products = cart.products.all()
    price = sum(product.price for product in products)

    context = {
        "products": products,
        "price": price
    }
    return render(request, "e_commerce/shoppingcart.html", context)


def checkout(request):
    form = PaymentForm()
    cart = ShoppingCart.objects.get(user=request.user)
    products = cart.products.all()
    price = sum(product.price for product in products)

    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            submit_payment(request, cart, price)

    context = {
        "public_key": settings.STRIPE_PUBLIC_KEY,
        "form": form,
        "price": price
    }
    return render(request, "e_commerce/checkout.html", context)


def add_to_cart_view(request, slug):
    product = get_object_or_404(Product, slug=slug)
    add_to_cart(request, product)
    return redirect('product', product.slug)


def remove_from_cart_view(request, slug):
    product = get_object_or_404(Product, slug=slug)
    remove_from_cart(request, product)
    return redirect('cart')
