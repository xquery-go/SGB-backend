
from django_base import core_serializers
from models import BaseModel


class BaseUserSerializer(core_serializers.ModelSerializer):

    class Meta:
        model = BaseModel
        fields = (
            'CreatedBy',
            'CreationTime',
            'UpdatedOn',
            'AccountId',
        )

    def create(self, validated_data):
        return super().create(validated_data)

    def update(self, instance, validated_data):
        return super().update(instance, validated_data)


