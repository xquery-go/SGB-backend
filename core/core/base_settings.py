

# Creating Rest framework dict for specifying parameters related to authentication.
# Adding Permission and Authorization classes so that this can be used by every microservice
# to authenticate requests.

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ),
}


IAM_SERVER_ADDRESS_FOR_GRPC = '0.0.0.0:8000'
SOUTH_GERMAN_BANK_SERVER_ADDRESS_FOR_GRPC = '0.0.0.0:8001'

MESSAGE_BUS_SETTINGS = {
    "SERVERS": {
        "iam": {
            "address": "[::]:50051"
        },
        "sgb": {
            "address": "[::]:50052"
        }
    }
}
