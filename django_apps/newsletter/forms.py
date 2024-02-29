from django import forms
from .models import Subscriber


class SubscribeForm(forms.ModelForm):
    class Meta:
        model = Subscriber
        fields = ['email']


class CreateNewsletterForm(forms.Form):
    subject = forms.CharField(max_length=150)
    message = forms.CharField(widget=forms.Textarea)
    html_message = forms.CharField(widget=forms.Textarea)
