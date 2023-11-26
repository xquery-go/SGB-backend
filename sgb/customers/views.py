from rest_framework.decorators import action
from core.generics import GenericModelMixin
from customers import serializers as customer_serializers
from customers import models as customer_models


# Create your views here.
class CustomerViewSet(GenericModelMixin):
    """
    Automatically creates four methods of CRUD operations for customer's personal information as well as
    their credit risk parameters.
    """
    queryset = customer_models.Customer.objects.all()
    serializer_class = customer_serializers.CustomerSerializer

    @action(
        methods=('get', 'post',),
        detail=True,
        serializer_class=customer_serializers.CustomerSerializer,
        url_path='customer_analysis',
    )
    def analysis(self, request):
        """
        This method is used to get the analysis report of each customer if it exists.


        If it does not exist, we pass the credit risk parameters in order to get the report.
        This method will save the report.
        """
        if request.method == 'POST':
            pass
        elif request.method == 'GET':
            pass
