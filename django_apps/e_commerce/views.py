from django.shortcuts import get_object_or_404, redirect
from django.views import generic
from .utils.cart_functions import add_to_cart, remove_from_cart
from .models import Product
from .forms import CreateProductForm
from main.auth.utils import ClientCheckMixin
from django.urls import reverse_lazy


def choose_template(design):
    return {
        'products': f"{design}/products.html",
        'product': f"{design}/productDetails.html",
        'create': f"{design}/createProduct.html",
        'cart': f"{design}/shoppingcart.html",
        'checkout' : f"{design}/checkout.html",
    }


template = choose_template("e_commerce")


class ProductsView(ClientCheckMixin, generic.ListView):
    model = Product
    template_name = template["products"]
    context_object_name =  'products'

    def get_queryset(self):
        user_products = Product.objects.filter(user=self.request.user)
        return user_products


class ProductDetailView(ClientCheckMixin, generic.DetailView):
    model = Product
    template_name = template["product"]
    context_object_name = 'product'
    slug_field = 'slug'


class CreateProductView(ClientCheckMixin, generic.CreateView):
    model = Product
    form_class = CreateProductForm
    template_name = template["create"]
    success_url = reverse_lazy('products')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


#  Utility views
def add_to_cart_view(request, slug, quantity=1):
    product = get_object_or_404(Product, slug=slug)
    add_to_cart(request, product, quantity)
    return redirect('product', product.slug)

def remove_from_cart_view(request, slug, quantity=1):
    product = get_object_or_404(Product, slug=slug)
    remove_from_cart(request, product, quantity)
    return redirect('cart')
