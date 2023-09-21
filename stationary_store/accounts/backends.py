from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q


class EmailOrPhoneNumberBackend(ModelBackend):
    """
    Authentication backend which allows users to authenticate using either their
    phone_number or email address
    """

    def authenticate(self, request, phone_number=None, email=None, password=None, **kwargs):

        user_model = get_user_model()

        if phone_number is None:
            phone_number = kwargs.get(user_model.USERNAME_FIELD)

        # The `phone_number` field allows to contain `@` characters so
        # technically a given email address could be present in either field,
        # possibly even for different users, so we'll query for all matching
        # records and test each one.
        users = user_model._default_manager.filter(
            Q(**{user_model.USERNAME_FIELD: phone_number}) | Q(email__iexact=phone_number)
        )

        # Test whether any matched user has the provided password:
        for user in users:
            if user.check_password(password):
                return user
        if not users:
            # Run the default password hasher once to reduce the timing
            # difference between an existing and a non-existing user
            user_model().set_password(password)