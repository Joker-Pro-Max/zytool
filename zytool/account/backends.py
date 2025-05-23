from django.contrib.auth.backends import BaseBackend
from .models import FrontendUser, BackendUser

from django.contrib.auth.backends import BaseBackend
from .models import FrontendUser, BackendUser


class FrontendAuthBackend(BaseBackend):
    def authenticate(self, request, mobile=None, password=None, **kwargs):
        if mobile is None:
            return None
        try:
            user = FrontendUser.objects.get(mobile=mobile)
        except FrontendUser.DoesNotExist:
            return None
        if user.check_password(password):
            return user
        return None

    def get_user(self, user_id):
        try:
            return FrontendUser.objects.get(pk=user_id)
        except FrontendUser.DoesNotExist:
            return None


class BackendAuthBackend(BaseBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = BackendUser.objects.get(username=username)
            if user.check_password(password):
                # 添加管理员权限验证
                if not user.is_staff:
                    return None  # 阻止非管理员登录Admin
                return user
        except BackendUser.DoesNotExist:
            return None
        return None

    def get_user(self, user_id):
        try:
            return BackendUser.objects.get(pk=user_id)
        except BackendUser.DoesNotExist:
            return None
