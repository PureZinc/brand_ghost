from django.urls import path, include

urlpatterns = [
    path('ecom/', include('api.e_commerce.urls')),
    path('newsletter/', include('api.newsletter.urls'))
]