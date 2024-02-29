from django.contrib import messages
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings

from ..models import Subscriber


def send_email(success_message=None, error_message=None):

    def decorator(func):
        def wrapper(request, my_form,*args, **kwargs):

            if request.method != 'POST':
                form = my_form()
            else:
                form = my_form(request.POST)

                if not form.is_valid():
                    messages.error(request, error_message)

                else:

                    func(request, form, *args, **kwargs)

                    form.save()
                    messages.success(request, success_message)

            return my_form
        
        return wrapper
    return decorator


@send_email(
    success_message="Congrats! You're now part of our newsletter!",
    error_message= "This form isn't valid. Are you sure you typed in the right email?"
)
def sub_to_newsletter(request, form):
    send_mail(
        subject='Welcome to Our Newsletter!',
        message='Thank you for subscribing to our newsletter.',
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[form.cleaned_data['email']],
        html_message=render_to_string('newsletter/welcome_newsletter.html', {}),
    )


@send_email(
    success_message="Message successfully sent to all subscribers",
    error_message= "Email couldn't be sent."
)
def send_newsletter_to_all(request, form):
    subscribers = Subscriber.objects.all()

    template = form.cleaned_data['html_message']
    subject = form.cleaned_data['subject']
    message = form.cleaned_data['message']

    send_mail(
        subject=subject,
        message=message,
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[sub.email for sub in subscribers],
        html_message=render_to_string(template, {}),
    )
