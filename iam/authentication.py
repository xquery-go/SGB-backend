from django.utils.translation import gettext_lazy as _
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.exceptions import AuthenticationFailed
from rest_framework_simplejwt.exceptions import InvalidToken
from rest_framework_simplejwt.tokens import AccessToken


class IAMJWTAuthentication(JWTAuthentication):

    def __get_token_claim_user(self, validated_token):
        try:
            user_id = validated_token.payload['UserId']
        except KeyError:
            raise InvalidToken(
                _('Token Invalid as no user claim found'))
        try:
            user = self.user_model.objects.get(UserId=user_id)
        except self.user_model.DoesNotExist:
            raise AuthenticationFailed(_('User does not exist'), code='user_not_found')
        return user

    def get_user(self, validated_token):
        return self.__get_token_claim_user(validated_token)

    def has_permission(self, request, view):
        return True


class GRPCAuthentication(AccessToken):
    def __init__(self, token):
        super().__init__(token=token)
