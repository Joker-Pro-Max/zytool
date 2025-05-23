from rest_framework import serializers
from account.models import Account
from rest_framework_jwt.settings import api_settings


class CreateAccountSerializer(serializers.ModelSerializer):
    token = serializers.SerializerMethodField()

    class Meta:
        model = Account
        fields = ('username', 'iphone', 'password', 'token')

    def get_token(self, obj):
        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
        payload = jwt_payload_handler(obj)
        return jwt_encode_handler(payload)


class LoginUserSerializer(serializers.ModelSerializer):
    token = serializers.SerializerMethodField()

    class Meta:
        model = Account
        fields = ('username', 'iphone', 'password', 'token')

    def get_token(self, obj):
        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
        payload = jwt_payload_handler(obj)
        return jwt_encode_handler(payload)
