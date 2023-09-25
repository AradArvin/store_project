from typing import Any
from django.contrib.auth.models import BaseUserManager
from rest_framework.exceptions import APIException



class UnmatchedException(APIException):
    status_code = 401
    default_detail = 'Not Acceptable'
    default_code = '403'



class CustomUserManager(BaseUserManager):

    def create_user(self, phone_number, email, password=None, **kwargs):
        
        if phone_number is None:
            raise TypeError("User must have a username!")
        
        if email is None:
            raise TypeError("User must have an email!")
        
        if password != kwargs["confirm_password"]:
            raise UnmatchedException("Passwords doesn't match")
        
       
        user = self.model(phone_number=phone_number, email=email)
        user.set_password(password)
        user.save()
        
        return user
    

    def create_superuser(self, phone_number, email, password, **kwargs):
        if password is None:
            raise TypeError("User must have a password!")
        

        user = self.create_user(phone_number=phone_number, email=email, password=password)
        user.is_staff = True
        user.is_superuser = True
        user.save()

        return user