from django.db import models
from django.contrib.auth.models import User


class Subscriber(models.Model):
    email = models.EmailField(null=False, unique=True)
    subscribed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email


class Newsletter(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.CharField(max_length=255)
    html_message = models.TextField()
    sent_date = models.DateTimeField(auto_now_add=True)
    recipients = models.ManyToManyField('Subscriber', related_name='received_newsletters')

    def __str__(self):
        return self.subject
