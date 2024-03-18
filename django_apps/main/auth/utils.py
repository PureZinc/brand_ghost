from django.contrib.auth.mixins import UserPassesTestMixin
from django.urls import reverse_lazy


def client_check(user):
    return user.is_authenticated


class ClientCheckMixin(UserPassesTestMixin):
    def test_func(self):
        return client_check(self.request.user)

    def get_redirect_url(self):
        return reverse_lazy('login')