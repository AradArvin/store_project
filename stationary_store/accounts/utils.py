import jwt
from uuid import uuid4
from django.core.validators import RegexValidator
from datetime import datetime, timedelta
from django.conf import settings


_REGEX = r'^(\+989|09)+\d{9}$'
phone_validator = RegexValidator(regex=_REGEX, message="Invalid Phone Number!")


def access_token_gen(user_id: int):
    """Generate access token based on usser id."""

    access_token = token_encode({
        'token_type':'access',
        'user_id':user_id,
        'exp': datetime.utcnow() + timedelta(minutes=1),
        'iat': datetime.utcnow(),
        'jti':gen_jti()
    })

    return access_token

