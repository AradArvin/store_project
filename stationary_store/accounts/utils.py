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



def refresh_token_gen(user_id: int):
    """Generate refresh token based on usser id."""

    refresh_token = token_encode({
        'token_type':'refresh',
        'user_id':user_id,
        'exp': datetime.utcnow() + timedelta(days=1),
        'iat': datetime.utcnow(),
        'jti':gen_jti()
    })
    
    return refresh_token



def gen_jti():
    """Generate hexed unique id for user"""
    return str(uuid4().hex)



def token_encode(payload):
    """Encode tokens based on HS256 algorithm"""

    token = jwt.encode(payload=payload, key=settings.SECRET_KEY, algorithm='HS256').decode('utf-8')
    return token



def token_decode(token):
    """Dencode tokens based on HS256 algorithm"""

    payload = jwt.decode(jwt=token, key=settings.SECRET_KEY, algorithms=['HS256'])
    return payload