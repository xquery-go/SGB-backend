from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status as rest_status, permissions
from rest_framework.decorators import action
from rest_framework.exceptions import AuthenticationFailed

from core.generics import GenericModelMixin
from tokens.base_tokens import BaseRefreshToken
from users import serializers
from users.models import User


# Create your views here.


class UserView(GenericModelMixin):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer

    @action(methods=['POST'], url_path='logout',
            detail=False, permission_classes=())
    def login(self, request):
        return self.response({'message': 'You have logged out successfully.'})

    @action(methods=['post'], url_path='refresh',
            detail=False, permission_classes=())
    def login(self, request):
        return self.response({'message': 'You have logged out successfully.'})


class AuthView(GenericModelMixin):
    permission_classes = (permissions.AllowAny,)

    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer

    @action(methods=['POST'], url_path='login',
            detail=False,)
    def login(self, request, *args, **kwargs):
        data = request.data
        username = str(data['username'])
        password = str(data['password'])

        try:
            USER = User.objects.get(username=username)
        except User.DoesNotExist:
            raise AuthenticationFailed('Incorrect Credentials.')
        if not USER.check_password(password):
            raise AuthenticationFailed(' Please check your password')

        refresh = BaseRefreshToken()

        serializer = self.get_serializer(USER)
        data = serializer.data
        data['refresh_token'] = refresh.for_user(USER)  # Query is run to create a new refresh token
        data['access_token'] = data['refresh_token'].access_token  # Query is run to create a new refresh token
        return self.response(data=data, status=rest_status.HTTP_200_OK)

    @action(methods=['POST'], url_path='logout',
            detail=False, permission_classes=())
    def login(self, request):
        return self.response({'message': 'You have logged out successfully.'})