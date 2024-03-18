from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User


class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField(default=0)

    is_featured = models.BooleanField(default=False)
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
            base_slug = self.slug
            if Product.objects.filter(slug=base_slug).exists:
                self.slug = f"{base_slug}-{self.pk}"
        super().save(*args, **kwargs)
    
    def __str__(self) -> str:
        return self.name
    

class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=f'product_imgs/')

    def __str__(self):
        return f"{self.product.name} Image"


class ShoppingCartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    cart = models.CharField(max_length=40)
    quantity = models.PositiveIntegerField(default=0)

    class Meta:
        unique_together = ('product', 'cart')
    
    def save(self, *args, **kwargs):
        request = kwargs.pop('request', None)
        if request and not self.cart:
            self.cart = request.session.session_key
        
        return super().save(*args, **kwargs)