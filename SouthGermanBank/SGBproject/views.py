from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from rest_framework.decorators import action

from .forms import StaffSignupClass
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from core.generics import GenericModelMixin
from django.contrib.auth import get_user_model
from SGBproject import serializers


class SGBView(GenericModelMixin):

    queryset = get_user_model().objects.all()
    serializer_class = serializers.UserSerializer

    @action(methods=['get', 'post'],
            url_path='welcome',
            detail=False)
    def welcome(self, request):
        return render(request, 'welcome login.html')

    @action(methods=['get', 'post'],
            url_path='employee_signup',
            detail=False)
    def employee_signup(self, request):
        if request.method == 'POST':
            signup_form = StaffSignupClass(request.POST)
            if signup_form.is_valid():
                messages.success(
                    request, 'Account created successfully!! '
                             'Contact administrator/reporting manager for account privileges.'
                )
                signup_form.save()
                return HttpResponse('OK', status=200)
        else:
            signup_form = StaffSignupClass()

        return render(request, 'signup.html', {'form': signup_form})





