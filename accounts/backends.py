# accounts/backends.py
from django.contrib.auth.backends import ModelBackend
from .models import User  # import your custom user model

class EmailOrUsernameModelBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        user = None
        if username:
            try:
                user = User.objects.get(username=username)
            except User.DoesNotExist:
                try:
                    user = User.objects.get(email=username)
                except User.DoesNotExist:
                    return None

        if user and user.check_password(password):
            return user
        return None
