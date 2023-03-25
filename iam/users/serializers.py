from users import models
from core.base import serializers


class UserSerializer(serializers.BaseUserSerializer):

    class Meta(serializers.BaseUserSerializer.Meta):
        model = models.User
        exclude = serializers.BaseUserSerializer.Meta.exclude + (
            'password',
        )
