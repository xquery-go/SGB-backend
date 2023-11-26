# from django.middleware
from django.core.exceptions import PermissionDenied
from django.utils.deprecation import MiddlewareMixin

GRPC_REFLECTION_INVOCATION_STRING = 'TokenVerificationRequest'


class IAMTokenAuthenticate(MiddlewareMixin):

    async_capable = False

    def process_request(self, request):
        print('Processing request for token authentication')
        is_valid_token = self.validate_token(request)
        if is_valid_token is True:
            return request
        else:
            raise PermissionDenied('Token authentication failure')

    def validate_token(self, request):
        grpc_response = 'f'
        if grpc_response:
            return True
        else:
            return False
