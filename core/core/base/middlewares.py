class IAMTokenAuthenticate:
    def __init__(self, get_response):
        self.get_response = get_response
        print('IAM Authentication enabled')

    def __call__(self, request):
        print('Authenticating request via IAM')
        response = self.get_response(request)
        print('Authentication complete')
        return response
