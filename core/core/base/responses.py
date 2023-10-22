from rest_framework.response import Response
from django.http import HttpResponse
from django.http import Http404


class BaseResponse(Response):
    def __init__(self, data=None, status=None,
                 template_name=None, headers=None,
                 exception=False, content_type=None):
        super().__init__(data, status,
                         template_name, headers,
                         exception, content_type)
        response_data = {
            'statusCode': status,
            'error': None,
            'data': data,
        }
        if exception:
            response_data['error'] = self.data.get('error')
            response_data['data'] = None
        if status:
            response_data['status'] = status


def response(data=None, status=None, template_name=None, headers=None, exception=None, content_type=None):
    return BaseResponse(data, status, template_name, headers, exception, content_type)
