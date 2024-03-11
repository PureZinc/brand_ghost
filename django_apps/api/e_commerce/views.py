from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from e_commerce.models import Product, ShoppingCartItem
from .serializers import ProductSer, ShoppingCartItemSer
from e_commerce.utils import add_to_cart, remove_from_cart


# View all products
class ProductsView(APIView):
    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSer(products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


# Receives product, adds to cart or removes from cart
class ProductDetailView(APIView):
    def get(self, request, id, quantity):
        try:
            product = Product.objects.get(id=id)
        except Product.DoesNotExist:
            raise Http404("Product not found")
        
        serializer = ProductSer(product)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request, id, quantity):
        try:
            product = Product.objects.get(id=id)
        except Product.DoesNotExist:
            raise Http404("Product not found")

        try:
            add_to_cart(request, product, quantity)
            item = ShoppingCartItem.objects.get(product=product)
        except Exception as e:
            return Response({'error': f"Error adding product to cart: {str(e)}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        message = f"Successfully added product! You have {item.quantity} {item.product.name}'s in your cart!"
        return Response({'message': message}, status=status.HTTP_202_ACCEPTED)
    
    def delete(self, request, id, quantity):
        try:
            product = Product.objects.get(id=id)
        except Product.DoesNotExist:
            raise Http404("Product not found")

        try:
            remove_from_cart(request, product, quantity)
            item = ShoppingCartItem.objects.get(product=product)
        except Exception as e:
            return Response({'error': f"Error removing product from cart: {str(e)}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        message = f"Successfully removed product! You have {item.quantity} {item.product.name}'s in your cart!"
        return Response({'message': message}, status=status.HTTP_202_ACCEPTED)


# Views from my cart
class MyCartView(APIView):
    def get(self, request, *args, **kwargs):
        cart = request.session
        my_items = ShoppingCartItem.objects.filter(cart=cart)
        serializer = ShoppingCartItemSer(my_items, many=True)
        total_price = sum(item.product.price * item.quantity for item in my_items)
        return Response({"products": serializer.data, "price": total_price}, status=status.HTTP_200_OK)


class CheckoutView(APIView):
    pass 
