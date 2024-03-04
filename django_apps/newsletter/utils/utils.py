from django.contrib import messages
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings
from ..models import Subscriber, Newsletter


def send_email_form(success_message=None, error_message=None):

    def decorator(func):
        def wrapper(request, my_form, *args, **kwargs):

            if request.method != 'POST':
                form = my_form()
            else:
                form = my_form(request.POST)

                if not form.is_valid():
                    messages.error(request, error_message)

                else:
                    func(request, form, *args, **kwargs)
                    messages.success(request, success_message)
            return my_form
        
        return wrapper
    return decorator


def save_newsletter(request, form):
    template = form.cleaned_data['html_message']
    subject = form.cleaned_data['subject']

    Newsletter.objects.create(user=request.user, subject=subject, html_message=template)


def send_newsletter(subject, html, recipients=list):
        send_mail(
        subject=subject,
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=recipients,
        html_message=html,
    )


@send_email_form(
    success_message="Congrats! You're now part of our newsletter!",
    error_message= "This form isn't valid. Are you sure you typed in the right email?"
)
def sub_to_newsletter(request, form):
    subject ='Welcome to Our Newsletter!'
    html = render_to_string('newsletter/welcome_newsletter.html', {})
    email = form.cleaned_data['email']

    send_newsletter(subject, html, recipients=[email])

    form.save()


@send_email_form(
    success_message="Message successfully sent to all subscribers",
    error_message= "Email couldn't be sent."
)
def send_newsletter_to_all(request, form):
    subs = Subscriber.objects.all()

    template = form.cleaned_data['html_message']
    subject = form.cleaned_data['subject']

    send_newsletter(subject, template, recipients=[sub.email for sub in subs])

    newsletter_instance = Newsletter.objects.create(user=request.user, subject=subject, html_message=template)
    newsletter_instance.recipients.add(*subs)
