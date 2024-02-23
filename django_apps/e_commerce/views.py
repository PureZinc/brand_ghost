from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, ShoppingCart, ShoppingCartItem
from .utils import add_to_cart, remove_from_cart, submit_payment
from django.conf import settings
from .forms import PaymentForm

design = "e_commerce"  # You can make a design of your own

template = {
    'home': f"{design}/home.html",
    'products': f"{design}/products.html",
    'product': f"{design}/productDetails.html",
    'cart': f"{design}/shoppingcart.html",
    'checkout' : f"{design}/checkout.html",
}


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
    cart, created = ShoppingCart.objects.get_or_create(user=request.user)
    items = ShoppingCartItem.objects.filter(cart=cart)
    price = sum(item.quantity * item.product.price for item in items)

    context = {
        "products": items,
        "price": price,
    }
    return render(request, template['cart'], context)


def checkout(request):
    form = PaymentForm()
    cart, created = ShoppingCart.objects.get_or_create(user=request.user)
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


def add_to_cart_view(request, slug):
    product = get_object_or_404(Product, slug=slug)
    add_to_cart(request, product, 1)
    return redirect('product', product.slug)


def remove_from_cart_view(request, slug):
    product = get_object_or_404(Product, slug=slug)
    remove_from_cart(request, product, 1)
    return redirect('cart')
