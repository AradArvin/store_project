from django.db import models
from accounts.utils import phone_validator
# Create your models here.


class Employee(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    adress = models.CharField(max_length=200)
    email = models.EmailField()
    phone_number = models.CharField(max_length=14, validators=[phone_validator,])
    date_joined = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"