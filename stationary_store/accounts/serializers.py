from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import CustomUser, Adress


class UserSignUpSerializer(ModelSerializer):
    confirm_password = serializers.CharField()
    class Meta:
        model = CustomUser
        fiels = ['id', 'username', 'email', 'password']


class UserLoginSerializer(ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username', 'password']


class AdressSerializer(ModelSerializer):
    class Meta:
        model = Adress
        fields = ['customer_id', 'adress', 'city', 'postal_code']


class OtpSerializer(serializers.Serializer):
    oto_code = serializers.IntegerField()


