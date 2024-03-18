from django.db import models
from django.contrib.auth.models import User


class UserData(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    special_key = models.CharField(max_length=60, unique=True) # Allows user to use the APIs
    is_premium = models.BooleanField(default=False) # Checks if the user is a premium member or not
    payment_key = models.CharField(max_length=100, blank=True, null=True) # Allows Stripe to handle payments

    def __str__(self):
        return f"{self.user.username}'s Data"


class Brand(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    website = models.URLField(null=True) # Brand's website (for the frontend to use)
    newsletter_email = models.EmailField() # The email used for the newsletters

