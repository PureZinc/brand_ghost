from django.urls import path
from . import views

urlpatterns = [
    path('subs/', views.SubscribersView.as_view(), name='subscribers_api'),
    path('all/', views.NewslettersView.as_view(), name='all_newsletters_api'),
    path('send/<int:id>/', views.SendNewsletterView.as_view(), name='send_newsletter_api')
]