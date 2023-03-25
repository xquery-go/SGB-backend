from django.shortcuts import render
from users import serializers
from users import models

from core.generics import GenericModelMixin
from rest_framework.decorators import action
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.response import Response

# Create your views here.


class UserView(GenericModelMixin):
    queryset = models.User.objects.all()
    serializer_class = serializers.UserSerializer

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
            return Response({
                'message': 'Login successful'
            })
        else:
            return Response({
                'message': 'Invalid Request method, ensure it is a POST request.'
            })
