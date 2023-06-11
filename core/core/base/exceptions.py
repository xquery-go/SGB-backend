from rest_framework.exceptions import *
from django.utils.translation import gettext_lazy as _


class TokenExpired(NotAuthenticated):
    default_detail = _('Token Expired')
    default_code = 'token_expired'
