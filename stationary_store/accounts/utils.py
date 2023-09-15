from django.core.validators import RegexValidator


_REGEX = r'^(\+989|09)+\d{9}$'
phone_validator = RegexValidator(regex=_REGEX, message="Invalid Phone Number!")