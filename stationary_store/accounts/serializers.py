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
        fields = ['email', 'phone_number', 'password', 'confirm_password', 'access_token']

    def create(self, validated_data):
        
        return CustomUser.objects.create_user(**validated_data)



class UserLoginSerializer(serializers.ModelSerializer):
    phone_number = serializers.EmailField()
    password = serializers.CharField(max_length=128, write_only=True)
    access_token = serializers.CharField(max_length=255, read_only=True)
    refresh_token = serializers.CharField(max_length=255, read_only=True)


    def validate(self, attrs):
        
        phone_number = attrs.get('phone_number', None)
        password = attrs.get('password', None)

        if phone_number is None:
            raise serializers.ValidationError("A phone number is required to login")
       
        if password is None:
            raise serializers.ValidationError("A password is required to login")
        
        user = authenticate(username=phone_number, password=password)
        

        if user is None:
            raise serializers.ValidationError("User not found!")
        

        if not user.is_active:
            raise serializers.ValidationError("This user has been deavtivated")
        
        access_token = access_token_gen(user.pk)
        refresh_token = refresh_token_gen(user.pk)


        validated_data = {
            'email': user.email,
            'phone_number': user.phone_number,
            'access_token': access_token,
            'refresh_token': refresh_token
        }
    
        return validated_data
    


class UserRUSerializer(serializers.ModelSerializer):

    password = serializers.CharField(max_length=128, min_length=8, write_only=True)
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = CustomUser
        fields = ['id', 'email', 'phone_number', 'password']
        # read_only_fields = ('token',)


    def update(self, instance, validated_data):

        password = validated_data.pop('password', None)

        for key, value in validated_data.items():
            setattr(instance, key, value)

        if password is not None:
            instance.set_password(password)

        instance.save()

        return instance
    


class AdressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Adress
        fields = ['customer_id', 'adress', 'city', 'postal_code']



class OtpSerializer(serializers.Serializer):
    oto_code = serializers.IntegerField()


