from django.contrib.auth.backends import BaseBackend
from rest_framework.exceptions import ValidationError as DRFValidationError
from django.contrib.auth.models import User, Group

from users.models import User as iam_user
from django.contrib import admin


class CustomAuthBackend(BaseBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = iam_user.objects.get(username=username)
        except iam_user.DoesNotExist:
            return None

        if user.check_password(password):
            return user

    def get_user(self, user_id):
        try:
            return iam_user.objects.get(pk=user_id)
        except iam_user.DoesNotExist:
            return None
