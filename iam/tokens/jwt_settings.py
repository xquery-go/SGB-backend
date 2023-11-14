from datetime import timedelta

from django.conf import settings
from rest_framework_simplejwt.settings import APISettings

SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=5),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=1),
    "ROTATE_REFRESH_TOKENS": False,
    "BLACKLIST_AFTER_ROTATION": False,
    "UPDATE_LAST_LOGIN": False,
    "ALGORITHM": "HS256",
    "SIGNING_KEY": settings.SECRET_KEY,
    "VERIFYING_KEY": "",
    "AUDIENCE": None,
    "ISSUER": None,
    "JSON_ENCODER": None,
    "JWK_URL": None,
    "LEEWAY": 0,
    "AUTH_HEADER_TYPES": ("Bearer",),
    "AUTH_HEADER_NAME": "HTTP_AUTHORIZATION",
    "USER_ID_FIELD": "id",
    "USER_ID_CLAIM": "user_id",
    "USER_AUTHENTICATION_RULE": "rest_framework_simplejwt.authentication.default_user_authentication_rule",
    "AUTH_TOKEN_CLASSES": ("tokens.base_tokens.BaseAccessToken",),
    "TOKEN_TYPE_CLAIM": "access",
    "JTI_CLAIM": "jti",
}

IMPORT_STRINGS = (
    "AUTH_TOKEN_CLASSES",
    "JSON_ENCODER",
    "TOKEN_USER_CLASS",
    "USER_AUTHENTICATION_RULE",
)

api_settings = APISettings(SIMPLE_JWT, SIMPLE_JWT, IMPORT_STRINGS)
