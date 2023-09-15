from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser
from .utils import phone_validator
from .managers import CustomUserManager
# Create your models here.


class CustomUser(AbstractBaseUser):
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(validators=phone_validator)

    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'email']

    objects = CustomUserManager()

    def __str__(self) -> str:
        return f"{self.username}"
    



class Adress(models.Model):
    customer_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    adress = models.CharField(max_length=256)
    city = models.CharField(max_length=50)
    postal_code = models.CharField(max_length=100)


    def __str__(self) -> str:
        return self.adress[:15]