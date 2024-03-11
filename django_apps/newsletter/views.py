from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test
from .utils.utils import send_newsletter_to_all
from .utils.formats import create_template
from .forms import CreateNewsletterForm
from .models import Newsletter, Subscriber


def client_check(user):
    return user.is_superuser


def common_context(request, id=None):
    context_data = {}

    context_data["newsletters"] = Newsletter.objects.all()
    context_data["subscriber_count"] = len(Subscriber.objects.all())

    if id:
        context_data["newsletter"] = Newsletter.objects.get(id=id)

    return context_data


@user_passes_test(client_check, login_url='home')
def newsletter_sender_view(request):
    form = CreateNewsletterForm
    send_newsletter_to_all(request, form)

    context= {
        "form": form,
    }
    return render(request, 'newsletter/client/create_newsletter.html', context)


@user_passes_test(client_check, login_url='home')
def my_newsletters(request):
    return render(request, 'newsletter/client/my_newsletters.html', common_context(request))


@user_passes_test(client_check, login_url='home')
def newsletter_details(request, id):
    newsletter = Newsletter.objects.get(id=id)
    html = create_template(newsletter.html_message)

    context = {
        "newsletter": newsletter,
        "html_message": html
    }
    return render(request, 'newsletter/client/newsletter_details.html', context)
