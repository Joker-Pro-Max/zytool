# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class FrontendUserManager(BaseUserManager):
    def create_user(self, mobile, password=None, **extra_fields):
        if not mobile:
            raise ValueError('必须填写手机号')
        user = self.model(mobile=mobile, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, mobile, password=None, **extra_fields):
        extra_fields.setdefault('is_admin', True)
        return self.create_user(mobile, password, **extra_fields)


class FrontendUser(AbstractBaseUser):
    mobile = models.CharField(max_length=15, unique=True)
    nickname = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = FrontendUserManager()

    USERNAME_FIELD = 'mobile'

    def __str__(self):
        return self.mobile

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin


class BackendUserManager(BaseUserManager):
    def create_user(self, username, password=None, **extra_fields):
        if not username:
            raise ValueError('必须填写用户名')
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password=None, **extra_fields):
        extra_fields.setdefault('is_admin', True)
        return self.create_user(username, password, **extra_fields)


class BackendUser(AbstractBaseUser):
    username = models.CharField(max_length=30, unique=True)
    employee_id = models.CharField(max_length=20)
    department = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField('管理权限', default=False)
    is_superuser = models.BooleanField('超级用户', default=False)

    objects = BackendUserManager()

    USERNAME_FIELD = 'username'

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return self.is_staff  # 必须返回布尔值

    def has_module_perms(self, app_label):
        return self.is_staff  # 必须返回布尔值

    @property
    def is_staff(self):
        return self.is_admin
