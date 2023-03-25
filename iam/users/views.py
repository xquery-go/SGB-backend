from django.shortcuts import render

import settings
from users import serializers
from users import models

from core.generics import GenericModelMixin
from rest_framework.decorators import action
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.response import Response
import datetime
import jwt
from django.utils import timezone

# Create your views here.


class UserView(GenericModelMixin):
    queryset = models.User.objects.all()
    serializer_class = serializers.UserSerializer

    token_timeout = settings.TOKEN_EXPIRATION_TIMEOUT

    @action(methods=['post'], url_path='login',
            detail=False,)
    def login(self, request):
        if request.method == 'POST':
            data = request.data
            username = data['username']
            password = data['password']

            USER = models.User.objects.get(username=username)
            if USER is None:
                raise AuthenticationFailed('Username not found')
            if not USER.check_password(password):
                raise AuthenticationFailed('Incorrect Credentials Please check your password')

            payload = {
                'pk': USER.pk,
                'exp': timezone.now() + datetime.timedelta(settings.TOKEN_EXPIRATION_TIMEOUT),
                'iat': timezone.now()
            }

            web_token = jwt.PyJWT()
            token = web_token.encode(payload=payload, key='secret', algorithm='HS256')
            response = Response({
                'message': 'Login successful',
                'token': token,
            })

            response.set_cookie(key='jwt', value=token, httponly=True, expires=settings.COOKIE_EXPIRATION_TIMEOUT)

            return response
        else:
            return Response({
                'message': 'Invalid Request method, ensure it is a POST request.'
            })
