from django.urls import path, re_path
from account.api import views

urlpatterns = [
    re_path(r'^register-account/$', views.CreateUserView.as_view()),  # 注册
    re_path(r'^login/', views.LoginUserView.as_view())  # 登录
]
