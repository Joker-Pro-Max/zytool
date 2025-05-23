from django.urls import path, re_path
from account.api import views

urlpatterns = [
     re_path(r'^register-frontend/$', views.FrontendRegisterView.as_view()),  # 前端用户注册
]
