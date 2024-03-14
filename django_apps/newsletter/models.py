from django.db import models
from django.contrib.auth.models import User


class Subscriber(models.Model):
    subbed_to = models.ForeignKey(User, on_delete=models.CASCADE)

    name = models.CharField(max_length=25)
    email = models.EmailField(blank=False)
    subscribed_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email
    

class Newsletter(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)

    subject = models.CharField(max_length=120)
    message = models.TextField(blank=False)
    recipients = models.ManyToManyField('Subscriber', blank=True)

    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.subject
