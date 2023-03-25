
from core.django_base import core_serializers
from core.models import BaseModel


class BaseUserSerializer(core_serializers.ModelSerializer):

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


