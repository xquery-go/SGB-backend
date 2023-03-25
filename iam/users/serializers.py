from users import models
from core.base import serializers


class UserSerializer(serializers.BaseUserSerializer):

    class Meta(serializers.BaseUserSerializer.Meta):
        model = models.User
        exclude = serializers.BaseUserSerializer.Meta.exclude
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        password = validated_data.pop('password')
        instance = self.Meta.model(**validated_data)
        assert password is not None
        instance.set_password(password)
        instance.save()
        return instance


