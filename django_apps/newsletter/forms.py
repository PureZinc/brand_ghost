from django import forms
from .models import Subscriber, Newsletter


class SubscribeForm(forms.ModelForm):
    class Meta:
        model = Subscriber
        fields = ['name', 'email']


class CreateNewsletterForm(forms.ModelForm):
    class Meta:
        model = Newsletter
        fields = ['subject', 'message']
