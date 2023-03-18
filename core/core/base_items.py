
# from django.db import models
from django.urls import re_path
# from django.utils.translation import gettext_lazy as _
from rest_framework import permissions

from drf_yasg.views import get_schema_view
from drf_yasg import openapi


class BaseSwagger:
    """
    Swagger base class
    """
    schema_view = get_schema_view(
        openapi.Info(
            title="Snippets API",
            default_version='v1',
            description="Test description",
            terms_of_service="https://www.google.com/policies/terms/",
            contact=openapi.Contact(email="contact@snippets.local"),
            license=openapi.License(name="BSD License"),
        ),
        public=True,
        permission_classes=[permissions.AllowAny],
    )

    urlpatterns = [
        re_path(r'^swagger(?P<format>\.json|\.yaml)$',
                schema_view.without_ui(cache_timeout=0), name='schema-json'),
        re_path(r'^swagger/$',
                schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
        re_path(r'^redoc/$',
                schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    ]


