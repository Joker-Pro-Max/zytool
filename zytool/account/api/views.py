from common.LocalApiView import *
from serializers.account_serializers import *


# Create your views here.

class FrontendRegisterView(CommonCreateAPIView):
    serializer_class = CreateFrontendUserSerializer
