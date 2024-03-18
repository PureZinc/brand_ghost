from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test
from .utils.utils import save_and_send_newsletter, save_newsletter
from .utils.formats import create_template
from .forms import CreateNewsletterForm
from .models import Newsletter, Subscriber
from django.contrib import messages
from main.auth.utils import client_check


def common_context(request, id=None):
    context_data = {}

    context_data["newsletters"] = Newsletter.objects.filter(user=request.user)
    context_data["subscriber_count"] = len(Subscriber.objects.filter(subbed_to=request.user))

    if id:
        context_data["newsletter"] = Newsletter.objects.get(id=id)

    return context_data


@user_passes_test(client_check, login_url='login')
def my_newsletters(request):
    return render(request, 'newsletter/client/my_newsletters.html', common_context(request))


@user_passes_test(client_check, login_url='login')
def newsletter_details(request, id):
    newsletter = Newsletter.objects.get(id=id)
    message = create_template(newsletter.message)

    context = {
        "newsletter": newsletter,
        "message": message
    }
    return render(request, 'newsletter/client/newsletter_details.html', context)


@user_passes_test(client_check, login_url='login')
def newsletter_sender_view(request):
    form = CreateNewsletterForm

    if request.method == 'POST':
        action = request.POST.get('action')
        form = form(request.POST)

        if not form.is_valid():
            messages.error(request, "Email couldn't be sent.")

        else:
            if action == 'save':
                save_newsletter(request, form)
                messages.success(request, "Message successfully saved!")

            elif action == 'save_and_send':
                save_and_send_newsletter(request, form)
                messages.success(request, "Message successfully saved and sent to all subscribers")

    context= {
        "form": form,
    }
    return render(request, 'newsletter/client/create_newsletter.html', context)
