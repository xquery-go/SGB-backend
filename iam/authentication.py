
from django.contrib.auth import get_user_model
from tokens import jwt_settings as api_settings
from django.utils.translation import gettext_lazy as _
from rest_framework_simplejwt.exceptions import InvalidToken
from rest_framework_simplejwt.exceptions import AuthenticationFailed
from rest_framework_simplejwt.authentication import JWTAuthentication


class IAMJWTAuthentication(JWTAuthentication):

    def __get_token_claim_user(self, validated_token):
        UserModel = get_user_model()
        try:
            user_id = validated_token[api_settings.USER_ID_CLAIM]
        except KeyError:
            raise InvalidToken(
                _('Token Invalid as no user claim found'))
        try:
            query = {
                'UserId': user_id
            }
            user = UserModel.objects.get(
                **query
            )
        except UserModel.DoesNotExist:
            raise AuthenticationFailed(_('User does not exist'), code='user_not_found')
        return user

    def get_user(self, validated_token):
        return self.__get_token_claim_user(validated_token)
