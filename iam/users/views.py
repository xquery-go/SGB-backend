from django.shortcuts import render
from users import serializers
from users import models

from core.generics import GenericModelMixin
# Create your views here.


class UserView(GenericModelMixin):

    queryset = models.User.objects.all()
    serializer_class = serializers.UserSerializer


