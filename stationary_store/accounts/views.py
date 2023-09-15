from django.shortcuts import render
from rest_framework import viewsets
from .models import CustomUser
from .serializers import AdressSerializer, UserSignUpSerializer, UserLoginSerializer, OtpSerializer
# Create your views here.


