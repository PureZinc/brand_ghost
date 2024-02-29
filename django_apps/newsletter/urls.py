from django.urls import path
from . import views

urlpatterns = [
    path('', views.newsletter_sender_view, name='email_sender'),
]