
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.settings import api_settings
from django.utils.translation import gettext_lazy as _
from rest_framework_simplejwt.exceptions import InvalidToken
from rest_framework_simplejwt.exceptions import AuthenticationFailed
from rest_framework_simplejwt.authentication import JWTAuthentication


UserModel = get_user_model()


def get_token_claim_user(validated_token):
    UserModel = get_user_model()
    try:
        user_id = validated_token[api_settings.USER_ID_CLAIM]
    except KeyError:
        raise InvalidToken(
            _('Token Invalid as no user claim found'))
    try:
        query = {
            api_settings.USER_ID_CLAIM: user_id
        }
        user = UserModel.objects.get(
            **query
        )
    except UserModel.DoesNotExist:
        raise AuthenticationFailed(_('User does not exist'), code='user_not_found')
    return user


class IAMJWTAuthentication(JWTAuthentication):
    def get_user(self, validated_token):
        return get_token_claim_user(validated_token)
