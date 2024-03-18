from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings
from ..models import Subscriber, Newsletter
from django.contrib import messages
from ..forms import SubscribeForm


def send_newsletter(subject, message, recipients=[]):
    send_mail(
        subject=subject,
        message="HTML failed to render.",
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=recipients,
        html_message=message,
    )


def save_newsletter(request, form):
    template = form.cleaned_data['message']
    subject = form.cleaned_data['subject']

    newsletter = Newsletter.objects.create(user=request.user, subject=subject, message=template)
    return newsletter


def save_and_send_newsletter(request, form):
    subs = Subscriber.objects.filter(subbed_to=request.user)
    newsletter = Newsletter.objects.create(user=request.user, subject=subject, message=template)

    if not subs.exists:
        messages.error(request, "You don't have any subs!")
        return newsletter

    subject = form.cleaned_data['subject']
    template = form.cleaned_data['message']

    send_newsletter(subject, template, recipients=[sub.email for sub in subs])

    newsletter.recipients.add(*subs)
    newsletter.save()


def sub_to_newsletter(request):
    form = SubscribeForm(request.POST)
    name = form.cleaned_data['name']
    email = form.cleaned_data['email']
    template = render_to_string('newsletter/welcome_newsletter.html', {"name": name})

    subject ='Welcome to Our Newsletter!'
    html = render_to_string('newsletter/newsletter_formatter.html', {"details": template})

    send_newsletter(subject, html, recipients=[email])

    form.save()
