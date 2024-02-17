from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.urls import reverse

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField(default=0)

    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
            base_slug = self.slug
            counter = 1
            while Product.objects.filter(slug=base_slug).exists:
                self.slug = f"{base_slug}-{counter}"
                counter += 1
        super().save(*args, **kwargs)
    
    def get_absolute_url(self):
        return reverse('product', kwargs={'slug': self.slug})


class ShoppingCart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
