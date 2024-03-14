from django.urls import path
from . import views

urlpatterns = [
    path('', views.welcome, name='main'),
    path('home/', views.dashboard_view, name='home'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]
