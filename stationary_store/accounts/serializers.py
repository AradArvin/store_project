from rest_framework import serializers
from .models import CustomUser, Adress
from django.contrib.auth import authenticate
from .utils import access_token_gen, refresh_token_gen


class SignUpSerializer(serializers.ModelSerializer):

    password = serializers.CharField(max_length=128, min_length=8, write_only=True)
    confirm_password = serializers.CharField(max_length=128, min_length=8, write_only=True)
    access_token = serializers.CharField(max_length=255, read_only=True)

    class Meta:
        model = CustomUser
        fields = ['email', 'username', 'password', 'confirm_password', 'access_token']

    def create(self, validated_data):
        
        return CustomUser.objects.create_user(**validated_data)


    class Meta:
        model = CustomUser
        fields = ['username', 'password']


class AdressSerializer(ModelSerializer):
    class Meta:
        model = Adress
        fields = ['customer_id', 'adress', 'city', 'postal_code']


class OtpSerializer(serializers.Serializer):
    oto_code = serializers.IntegerField()


