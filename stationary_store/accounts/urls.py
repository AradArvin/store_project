from django.urls import path
from .views import *



urlpatterns = [
    path('api/signup', RegistrationAPIView.as_view(), name='signup'),
    path('api/login', LoginAPIView.as_view(), name='login'),
    path('api/user', UserProfileAPIView.as_view(), name='user'),
]