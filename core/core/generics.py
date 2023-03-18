from rest_framework import generics, status
from rest_framework.viewsets import ViewSetMixin
from rest_framework.viewsets import ModelViewSet
from django.core.exceptions import FieldDoesNotExist
from rest_framework.settings import api_settings


class GenericModelMixin(ModelViewSet):
    pass
