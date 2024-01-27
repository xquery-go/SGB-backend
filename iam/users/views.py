from djangorestframework_camel_case.parser import CamelCaseFormParser, CamelCaseMultiPartParser, \
    CamelCaseJSONParser
from rest_framework import status as rest_status, permissions
from rest_framework.decorators import action

from core.generics import GenericModelMixin
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
    def refresh_token(self, request):
        return self.response({'message': 'You have logged out successfully.'})


class AuthView(GenericModelMixin):
    permission_classes = (permissions.AllowAny,)
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer

    def get_authenticate_header(self, request):
        ret = super().get_authenticate_header(request)
        return ret

    @action(methods=['POST'], url_path='login',
            detail=False,
            )
    def authenticate(self, request, *args, **kwargs):
        data = request.data
        username = str(data['username'])
        password = str(data['password'])

        data = User.authenticate(username, password)
        serializer = self.get_serializer(data['user'])
        response_data = serializer.data
        response_data['refresh'] = data['refresh_token']
        response_data['access'] = data['access_token']
        return self.response(data=response_data, status=rest_status.HTTP_200_OK)

    @action(methods=['POST'], url_path='logout',
            detail=False, permission_classes=())
    def login(self, request):
        return self.response({'message': 'You have logged out successfully.'})
