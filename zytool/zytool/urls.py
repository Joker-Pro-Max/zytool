"""
URL configuration for zytool project.

The `urlpatterns` list routes URLs to views.py. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views.py
    1. Add an import:  from my_app import views.py
    2. Add a URL to urlpatterns:  path('', views.py.home, name='home')
Class-based views.py
    1. Add an import:  from other_app.views.py import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

api_urls = [
    path('account/', include('account.api.urls')),
]

admin_api_urls = [
    path('account/', include('account.admin_api.urls')),
]
urlpatterns = [
    path('admin_api/', include(admin_api_urls)),
    path("api/", include(api_urls)),
    path('admin', admin.site.urls),
]
