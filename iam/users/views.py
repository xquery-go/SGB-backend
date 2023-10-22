from django.shortcuts import render

from django.conf import settings
from rest_framework import status as rest_status

from users import serializers
from users import models

from core.generics import GenericModelMixin
from rest_framework.decorators import action
from rest_framework.exceptions import AuthenticationFailed
import datetime
import jwt
from django.utils import timezone

# Create your views here.


class UserView(GenericModelMixin):
    queryset = models.User.objects.all()
    serializer_class = serializers.UserSerializer

    token_timeout = settings.TOKEN_EXPIRATION_TIMEOUT

    @action(methods=['post'], url_path='login',
            detail=False, permission_classes=())
    def login(self, request):
        data = request.data
        username = data['username']
        password = data['password']

        USER = models.User.objects.get(username=username)
        if USER is None:
            raise AuthenticationFailed('Username not found')
        if not USER.check_password(password):
            raise AuthenticationFailed('Incorrect Credentials Please check your password')

        token = models.User.generate_token(USER)
        serializer = self.get_serializer(USER)
        data = serializer.data
        data['token'] = token
        return self.response(data=data, status=rest_status.HTTP_200_OK)
