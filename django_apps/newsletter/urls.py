from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.newsletter_sender_view, name='create_newsletter'),
    path('all/', views.my_newsletters, name='newsletters'),
    path('all/<int:id>/', views.newsletter_details, name='newsletter_details')
]