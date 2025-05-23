# Register your models here.
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import FrontendUser, BackendUser

admin.site.register(FrontendUser)
admin.site.register(BackendUser)
