from rest_framework import serializers
from .models import Employee




class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ["first_name", "last_name", "adress", "email", "phone_number", "date_joined"]