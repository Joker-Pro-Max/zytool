from django.urls import path, re_path
from account.admin_api import views

urlpatterns = [
     re_path(r'^register-backend/$', views.BackendUserRegisterView.as_view()),  # 注册
]
