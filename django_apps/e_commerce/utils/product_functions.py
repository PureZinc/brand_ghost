from ..models import Product, ProductImage
from django.contrib import messages


def add_product(request):
    user = request.user
    product_name = request.POST.get('product_name')
    description = request.POST.get('description')
    price = request.POST.get('price')
    stock = request.POST.get('stock')

    Product.objects.create(
        user=user,
        name=product_name,
        description=description,
        price=price,
        stock=stock
    )
    
    messages.success(request, f"Successfully added product!")


def remove_product(request, id):
    product = Product.objects.get(id=id)
    product.objects.delete()
    messages.success(request, f"Successfully removed product!")
