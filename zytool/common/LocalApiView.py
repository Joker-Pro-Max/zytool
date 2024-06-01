from common.function import CommonFunction
from rest_framework.generics import GenericAPIView, CreateAPIView, ListAPIView, ListCreateAPIView, RetrieveAPIView, \
    RetrieveUpdateDestroyAPIView, RetrieveDestroyAPIView, RetrieveUpdateAPIView, DestroyAPIView, UpdateAPIView


class CommonGenericAPIView(GenericAPIView, CommonFunction):
    pass


class CommonCreateAPIView(CreateAPIView, CommonFunction):
    pass


class CommonListAPIView(ListAPIView, CommonFunction):
    pass


class CommonListCreateAPIView(ListCreateAPIView, CommonFunction):
    pass


class CommonRetrieveAPIView(RetrieveAPIView, CommonFunction):
    pass


class CommonRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView, CommonFunction):
    pass


class CommonRetrieveDestroyAPIView(RetrieveDestroyAPIView, CommonFunction):
    pass


class CommonRetrieveUpdateAPIView(RetrieveUpdateAPIView, CommonFunction):
    pass


class CommonDestroyAPIView(DestroyAPIView, CommonFunction):
    pass


class CommonUpdateAPIView(UpdateAPIView, CommonFunction):
    pass
