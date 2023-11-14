from rest_framework import status
from rest_framework.viewsets import GenericViewSet

from core.base.responses import response


class GenericModelMixin(GenericViewSet):
    def response(self, data=None, exception=None, status=None,
                 template_name=None, headers=None, content_type=None
                 ):
        response_instance = response(data=data, exception=exception, status=status,
                                     template_name=template_name, headers=headers, content_type=content_type)
        return response_instance
