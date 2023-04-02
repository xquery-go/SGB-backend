from customers import models
from core.base import serializers


class CustomerCreditRiskParameterSerializer(serializers.BaseUserSerializer):

    class Meta(serializers.BaseUserSerializer.Meta):

        model = models.CustomerCreditRiskParameter
        exclude = serializers.BaseUserSerializer.Meta.exclude


class CustomerSerializer(serializers.BaseUserSerializer):
    CustomerCreditRiskParameters = CustomerCreditRiskParameterSerializer(many=True, required=False)

    class Meta(serializers.BaseUserSerializer.Meta):
        model = models.Customer
