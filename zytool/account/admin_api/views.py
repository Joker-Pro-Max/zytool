from common.LocalApiView import *
from serializers.account_serializers import *


class BackendUserRegisterView(CommonCreateAPIView):
    serializer_class = CreateBackendUserSerializer
