from django.contrib.auth import authenticate
from rest_framework import serializers
from rest_framework.response import Response

from account.models import FrontendUser, BackendUser
from common.function import CommonFunction


class CreateFrontendUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = FrontendUser
        fields = ('mobile', 'nickname', "password")


class CreateBackendUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = BackendUser
        fields = ('username', "password")