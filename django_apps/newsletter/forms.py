from typing import Any
from django import forms
from .models import Subscriber, Newsletter


class SubscribeForm(forms.ModelForm):
    class Meta:
        model = Subscriber
        fields = ['email']


class CreateNewsletterForm(forms.ModelForm):
    class Meta:
        model = Newsletter
        fields = ['subject', 'html_message']
