from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test
from .utils.utils import send_newsletter_to_all
from .forms import CreateNewsletterForm


def client_check(user):
    return user.is_superuser


@user_passes_test(client_check, login_url='home')
def newsletter_sender_view(request):
    form = CreateNewsletterForm
    send_newsletter_to_all(request, form)

    context= {
        "form": form,
    }
    return render(request, 'newsletter/client_page.html', context)
