
from rest_framework import serializers
from core.models import BaseModel


class BaseUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = BaseModel
        exclude = (
            'CreatedBy',
            'CreationTime',
            'UpdatedOn',
            'AccountId',
        )

    def create(self, validated_data):
        return super().create(validated_data)

    def update(self, instance, validated_data):
        return super().update(instance, validated_data)


