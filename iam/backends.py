from django.contrib.auth.backends import BaseBackend

from users.models import User as iam_user


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
