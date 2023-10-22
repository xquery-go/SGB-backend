from users import models
from core.base import serializers
from rest_framework.exceptions import ValidationError as DRFValidationError


class UserSerializer(serializers.BaseUserSerializer):

    class Meta(serializers.BaseUserSerializer.Meta):
        model = models.User
        exclude = serializers.BaseUserSerializer.Meta.exclude
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        if 'password' not in validated_data:
            raise DRFValidationError('Invalid data')
        password = validated_data.pop('password')
        instance = self.Meta.model(**validated_data)
        instance.set_password(password)
        instance.save()
        return instance


