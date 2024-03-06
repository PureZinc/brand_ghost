import stripe
from django.conf import settings
from django.contrib import messages


def payment_process(func):
    def wrapper(request, total_price, *args, **kwargs):
        stripe.api_key = settings.STRIPE_SECRET_KEY
        token = request.POST.get('stripeToken', None)

        # Debugging print
        print("POST Data:", request.POST)
        print("Token:", token)
        
        if token is None:
            messages.error(request, "Token not provided")
            return None
        
        amount = int(total_price * 100)

        try:
            charge = stripe.Charge.create(
                amount=amount,
                description='Payment for products',
                source=token,
            )

            func(request, *args, **kwargs)

        except stripe.error.CardError as e:
            messages.error(request, f"Payment failed: {e.error.message}")

    return wrapper
