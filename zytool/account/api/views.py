from rest_framework import generics
from serializers.account_serializers import *


# Create your views here.

class CreateUserView(generics.CreateAPIView):
    serializer_class = CreateAccountSerializer


class LoginUserView(generics.ListAPIView):
    serializer_class = LoginUserSerializer

    def get_queryset(self):
        query = self.request.query_params
        queryset = Account.objects.filter(iphone=query.get('iphone'), password=query.get('password')).order_by(
            '-add_time')[:1]
        if not queryset:
            return None
        return queryset
