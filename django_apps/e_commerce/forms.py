from django import forms

class PaymentForm(forms.Form):
    card_number = forms.CharField(label="Card Number", required=True)
    card_expiry = forms.CharField(label="Expiration Date", required=True)
    card_cvc = forms.CharField(label="CVC", required=True)