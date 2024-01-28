from rest_framework import status as rest_status, permissions
from rest_framework.decorators import action

from core.generics import GenericModelMixin, BaseGenericViewSet
from users import serializers
from users.models import User


class UserView(GenericModelMixin):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer

    @action(methods=['post'], url_path='logout',
            detail=False,)
    def logout(self, request, *args, **kwargs):

        return self.response({'message': 'You have logged out successfully.'})
